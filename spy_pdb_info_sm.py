# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : spy_pdb_info_sm.py
# Time       ：2022/6/13 10:04
# Author     ：Jago
# Email      ：18146856052@163.com
# version    ：python 3.7
# Description：
"""
import gzip
import os.path
import random
import time
from io import BytesIO
from urllib.request import ProxyHandler, build_opener, Request, urlopen

import lxml.html
from bs4 import BeautifulSoup as bs

import pandas as pd


# 动态ip每过两分钟会变，该方法重新设置代理并返回opener
def get_opener(url):
    request = urlopen(url)
    address = request.read().decode('utf-8')

    proxy = {
        'http': 'http://{}'.format(address),
        'https': 'https://{}'.format(address)
    }
    proxy_handler = ProxyHandler(proxy, )
    opener = build_opener(proxy_handler)

    print("update proxy to", address)
    return opener


# 爬取validation信息
def crawl_validation(validate_url, opener):
    print("crawling", validate_url)

    request = Request(validate_url, headers=header)
    response = opener.open(request, timeout=10)
    response = response.read()
    # response经过gzip压缩，需要解压
    buffer = BytesIO(response)
    unzip_response = gzip.GzipFile(fileobj=buffer)
    decode_response = unzip_response.read().decode('utf-8')
    obj = bs(decode_response, 'xml')
    entry = obj.find('Entry')

    data = []
    data.append(entry.attrs['PDB-Rfree'] if entry.has_attr('PDB-Rfree') else "")
    data.append(entry.attrs['absolute-percentile-DCC_Rfree'] if entry.has_attr('absolute-percentile-DCC_Rfree') else "")
    data.append(entry.attrs['relative-percentile-DCC_Rfree'] if entry.has_attr('relative-percentile-DCC_Rfree') else "")
    data.append(entry.attrs['clashscore'] if entry.has_attr('clashscore') else "")
    data.append(entry.attrs['absolute-percentile-clashscore'] if entry.has_attr('absolute-percentile-clashscore') else "")
    data.append(entry.attrs['relative-percentile-clashscore'] if entry.has_attr('relative-percentile-clashscore') else "")
    data.append(entry.attrs['percent-rama-outliers'] if entry.has_attr('percent-rama-outliers') else "")
    data.append(entry.attrs['absolute-percentile-percent-rama-outliers'] if entry.has_attr('absolute-percentile-percent-rama-outliers') else "")
    data.append(entry.attrs['relative-percentile-percent-rama-outliers'] if entry.has_attr('relative-percentile-percent-rama-outliers') else "")
    data.append(entry.attrs['percent-rota-outliers'] if entry.has_attr('percent-rota-outliers') else "")
    data.append(entry.attrs['absolute-percentile-percent-rota-outliers'] if entry.has_attr('absolute-percentile-percent-rota-outliers') else "")
    data.append(entry.attrs['relative-percentile-percent-rota-outliers'] if entry.has_attr('relative-percentile-percent-rota-outliers') else "")
    data.append(entry.attrs['percent-RSRZ-outliers'] if entry.has_attr('percent-RSRZ-outliers') else "")
    data.append(entry.attrs['absolute-percentile-percent-RSRZ-outliers'] if entry.has_attr('absolute-percentile-percent-RSRZ-outliers') else "")
    data.append(entry.attrs['relative-percentile-percent-RSRZ-outliers'] if entry.has_attr('relative-percentile-percent-RSRZ-outliers') else "")
    return data


# 尽量使爬取的表格信息具有可读性
def get_content(td):
    if (td.a and td.a.img) or td.find('a', class_="btn btn-primary btn-sm"):  # 多层级查找一定要确保中间没有NoneType
        return td.a.attrs['href']

    if td.find('a', class_="hidden-print querySearchLink") or td.find('a', class_="btn btn-default btn-xs hidden-print"):
        return td.a.text

    if td.find('br'):
        s = str(td).replace("<br/>", "\n")
        h = lxml.html.fromstring(s)
        return h.text_content()

    return td.text


# 爬取summary信息
def crawl_summary(href_url, opener):
    print("crawling", href_url)

    request = Request(href_url, headers=header)
    response = opener.open(request, timeout=10)
    response = response.read().decode('utf-8')
    obj = bs(response, 'html.parser')

    # 有的网页中会重复一遍前两个信息，有的网页不会重复！！！所以使用字典而非列表
    carousel_data = {"Global Symmetry": "", "Global Stoichiometry": "", "Pseudo Symmetry": "", "Pseudo Stoichiometry": ""}
    symmetry_spans = obj.find_all('span', class_="glyphicon glyphicon-info-sign hidden-xs hidden-sm hidden-md", limit=4)
    for sym in symmetry_spans:
        sb_up1 = sym.previous_sibling                                                        # 前一个兄弟节点
        sb_up2 = sym.previous_sibling.previous_sibling if sb_up1 else None                   # 上数第2个strong标签
        sb_up3 = sym.previous_sibling.previous_sibling.previous_sibling if sb_up2 else None  # 上数第3个strong标签

        if sb_up2:
            if sb_up2.text == "Global Symmetry":
                global_symmetry = sb_up1.text
                global_symmetry = global_symmetry[1:].strip()
                carousel_data['Global Symmetry'] = global_symmetry
            elif sb_up2.text == "Pseudo Symmetry":
                pseudo_symmetry = sb_up1.text
                pseudo_symmetry = pseudo_symmetry[1:].strip()
                carousel_data['Pseudo Symmetry'] = pseudo_symmetry
            elif sb_up3:
                if sb_up3.text == "Global Stoichiometry":
                    global_stoichiometry = sb_up2.text + sb_up1.text
                    global_stoichiometry = global_stoichiometry[1:].strip()
                    carousel_data['Global Stoichiometry'] = global_stoichiometry
                elif sb_up3.text == "Pseudo Stoichiometry":
                    pseudo_stoichiometry = sb_up2.text + sb_up1.text
                    pseudo_stoichiometry = pseudo_stoichiometry[1:].strip()
                    carousel_data['Pseudo Stoichiometry'] = pseudo_stoichiometry
                else:
                    break
            else:
                break
        else:
            break

    upper_data = []
    if obj.find('li', id="contentStructureWeight"):  # Total Structure Weight
        c = obj.find('li', id="contentStructureWeight").text
        colon_index = c.find(':')
        upper_data.append(c[colon_index+1:].strip())
    else:
        upper_data.append("")
    if obj.find('li', id="contentAtomSiteCount"):  # Atom Count
        c = obj.find('li', id="contentAtomSiteCount").text
        colon_index = c.find(':')
        upper_data.append(c[colon_index+1:].strip())
    else:
        upper_data.append("")
    if obj.find('li', id="contentResidueCount"):  # 2个Residue Count的id一样
        rc_model = obj.find('li', id="contentResidueCount")
        rc_deposit = rc_model.next_sibling
        if "Modelled" in rc_model.text and "Deposited" in rc_deposit.text:
            t1 = rc_model.text
            colon_index = t1.find(':')
            upper_data.append(t1[colon_index + 1:].strip())
            t2 = rc_deposit.text
            colon_index = t2.find(':')
            upper_data.append(t2[colon_index + 1:].strip())
        elif "Modelled" in rc_model.text and "Deposited" not in rc_deposit.text:
            t1 = rc_model.text
            colon_index = t1.find(':')
            upper_data.append(t1[colon_index + 1:].strip())
            upper_data.append("")  # Modelled Residue Count
        elif "Modelled" not in rc_model.text and "Deposited" in rc_deposit.text:
            upper_data.append("")  # Modelled Residue Count
            t2 = rc_deposit.text
            colon_index = t2.find(':')
            upper_data.append(t2[colon_index + 1:].strip())
    else:
        upper_data.append("")  # Modelled Residue Count
        upper_data.append("")  # Deposited Residue Count
    if obj.find('li', id="contentProteinChainCount"):  # Unique protein chains
        c = obj.find('li', id="contentProteinChainCount").text
        colon_index = c.find(':')
        upper_data.append(c[colon_index+1:].strip())
    else:
        upper_data.append("")
    if obj.find('li', id="contentNucleicAcidChainCount"):  # Unique nucleic acid chains
        c = obj.find('li', id="contentNucleicAcidChainCount").text
        colon_index = c.find(':')
        upper_data.append(c[colon_index+1:].strip())
    else:
        upper_data.append("")
    upper_data.append(obj.find('li', id="header_classification").strong.a.text if obj.find('li', id="header_classification") else "")
    upper_data.append(obj.find('li', id="header_organism").a.text if obj.find('li', id="header_organism") else "")
    upper_data.append(obj.find('li', id="header_expression-system").a.text if obj.find('li', id="header_expression-system") else "")
    upper_data.append(obj.find('li', id="header_mutation").strong.next_sibling.text.replace(u'\xa0', ' ').strip() if obj.find('li', id="header_mutation") else "")
    upper_data.append(obj.find('li', id="exp_header_0_method").strong.next_sibling.text if obj.find('li', id="exp_header_0_method") else "")
    upper_data.append(obj.find('li', id="exp_header_0_diffraction_resolution").strong.next_sibling.text.replace(u'\xa0', ' ').strip() if obj.find('li', id="exp_header_0_diffraction_resolution") else "")
    upper_data.append(obj.find('li', id="exp_header_0_diffraction_rvalueFree").strong.next_sibling.text.replace(u'\xa0', ' ').strip() if obj.find('li', id="exp_header_0_diffraction_rvalueFree") else "")
    upper_data.append(obj.find('li', id="exp_header_0_diffraction_rvalueWork").strong.next_sibling.text.replace(u'\xa0', ' ').strip() if obj.find('li', id="exp_header_0_diffraction_rvalueWork") else "")
    upper_data.append(obj.find('li', id="exp_header_0_diffraction_rvalueObserved").strong.next_sibling.text if obj.find('li', id="exp_header_0_diffraction_rvalueObserved") else "")
    upper_data.append(obj.find('li', id="pubmedDOI").a.attrs['href'] if obj.find('li', id="pubmedDOI") else "")

    macromolecule_data = {}
    oligosaccharide_data = {}
    entity_infos = obj.find_all('tr', class_="info")
    for e in entity_infos:
        e_id = e.th.h5.text
        colon_index = e_id.find(':')
        mm_id = e_id[colon_index + 1:].strip()
        mm_headers = [e_header.text for e_header in e.next_sibling.find_all('th')]
        mm_tds = e.next_sibling.next_sibling.contents

        e_grandfather = e.parent.parent
        e_gf_class = ' '.join(e_grandfather.attrs['class'])  # 跟网页html显示的不一样，它的class返回值为列表
        if e_gf_class == "table table-bordered table-condensed tableEntity":  # 大分子
            macromolecule_data[mm_id] = {}
            i = 0
            for i in range(len(mm_headers)):
                header_name = mm_headers[i]
                macromolecule_data[mm_id][header_name] = get_content(mm_tds[i])
        elif e_gf_class == "table table-bordered table-condensed":            # 寡聚糖
            oligosaccharide_data[mm_id] = {}
            i = 0
            for i in range(len(mm_headers)):
                header_name = mm_headers[i]
                oligosaccharide_data[mm_id][header_name] = get_content(mm_tds[i])
        else:
            print("Unknown situation", e_gf_class)

    ligand_data = {}
    ligand_actives = obj.find_all('tr', class_="active")
    for l in ligand_actives:
        if (not l.parent.has_attr('id')) or l.parent.attrs['id'] != "LigandsMainTable":  # 跟网页html显示的不一样，tr的parent是id为LigandsMainTable的table而非tbody
            continue

        aa_headers = [l_header.text for l_header in l.next_sibling.find_all('th')]
        ligand_trs = l.next_sibling.next_sibling.find_all('tr')  # tbody只是唬人的，忽视它，不要作为父节点或子节点
        i = 0
        for i in range(len(ligand_trs)):
            ligand_data[str(i+1)] = {}           # 下标从1开始
            ligand_tds = ligand_trs[i].contents
            j = 0
            for j in range(len(aa_headers)):
                header_name = aa_headers[j]
                ligand_data[str(i+1)][header_name] = get_content(ligand_tds[j])

    below_data = [macromolecule_data, oligosaccharide_data, ligand_data]
    return carousel_data, upper_data, below_data


# 下载pdb文件
def crawl_file(download_url, filepath, opener):
    print("downloading", download_url)

    request = Request(download_url, headers=header)
    response = opener.open(request, timeout=10)

    data = response.read()
    with open(filepath, "wb") as f:
        f.write(data)


# 改变数据格式
def transfer_data(old_list, new_dict, old_list_length, start_dict_key):
    index = 0
    start_flag = False
    for key in new_dict.keys():
        if not start_flag and key != start_dict_key:  # 在没有遍历到Rfree Value之前，前者永真，后者永真；遍历到时，后者为假
            continue
        start_flag = True
        if index == old_list_length:
            break
        new_dict[key].append(old_list[index])
        index += 1


# 爬取信息总的过程
def crawl_process():
    df = pd.read_csv(csv_path)
    lost_pdb = []
    table_format = {"ID": [], "Rfree Value": [], "Rfree Absolute(%)": [], "Rfree Relative(%)": [],
                    "Clashscore Value": [], "Clashscore Absolute(%)": [], "Clashscore Relative(%)": [],
                    "Ramachandran Value(%)": [], "Ramachandran Absolute(%)": [], "Ramachandran Relative(%)": [],
                    "Sidechain Value(%)": [], "Sidechain Absolute(%)": [], "Sidechain Relative(%)": [],
                    "RSRZ Value(%)": [], "RSRZ Absolute(%)": [], "RSRZ Relative(%)": [],
                    "Global Symmetry": [], "Global Stoichiometry": [], "Pseudo Symmetry": [], "Pseudo Stoichiometry": [],
                    "Total Structure Weight": [], "Atom Count": [], "Modelled Residue Count": [],
                    "Deposited Residue Count": [], "Unique protein chains": [], "Unique nucleic acid chains": [],
                    "classification": [], "organism": [], "expression system": [], "mutation": [], "method": [],
                    "resolution": [], "rvalueFree": [], "rvalueWork": [], "rvalueObserved": [], "pubmedDOI": [],
                    "macromolecule": [], "oligosaccharide": [], "ligand": []}

    i = 0
    header['User-Agent'] = random.choice(USER_AGENTS_LIST)
    opener = get_opener(proxy_url)
    error_times = 0
    start_time = time.time()

    for index, row in df.iterrows():
        id = str(row['ID'])

        end_time = time.time()
        if error_times == 3 or end_time - start_time == 120:
            header['User-Agent'] = random.choice(USER_AGENTS_LIST)  # 更新header
            opener = get_opener(proxy_url)                          # 更新代理设置
            error_times = 0                                         # 重置异常次数
            start_time = time.time()                                # 更新时间起点

        # if id not in lost_pdb:
        #     continue

        id_lower = id.lower()
        # https://files.rcsb.org/pub/pdb/validation_reports/a7/1a7c/1a7c_validation.xml.gz
        validate_url = init_validate_url + id_lower[1:3] + '/' + id_lower + '/' + id_lower + '_validation.xml.gz'
        href_url = row['href']
        filename = id_lower + ".pdb"
        filepath = pdb_path + filename
        # https://files.rcsb.org/download/1a7c.pdb
        download_url = init_download_url + filename

        try:
            validation_data = crawl_validation(validate_url, opener)
            carousel_data, upper_data, below_data = crawl_summary(href_url, opener)
            if not os.path.exists(filepath):
                crawl_file(download_url, filepath, opener)

            # 提取数据
            table_format['ID'].append(id)
            transfer_data(validation_data, table_format, 15, "Rfree Value")
            transfer_data(upper_data, table_format, 16, "Total Structure Weight")
            transfer_data(below_data, table_format, 3, "macromolecule")
            for key in carousel_data.keys():
                table_format[key].append(carousel_data[key])

            i += 1
            if i == 50:
                i = 0
                table_copy = table_format.copy()
                table_format = {"ID": [], "Rfree Value": [], "Rfree Absolute(%)": [], "Rfree Relative(%)": [],
                                "Clashscore Value": [], "Clashscore Absolute(%)": [], "Clashscore Relative(%)": [],
                                "Ramachandran Value(%)": [], "Ramachandran Absolute(%)": [],
                                "Ramachandran Relative(%)": [],
                                "Sidechain Value(%)": [], "Sidechain Absolute(%)": [], "Sidechain Relative(%)": [],
                                "RSRZ Value(%)": [], "RSRZ Absolute(%)": [], "RSRZ Relative(%)": [],
                                "Global Symmetry": [], "Global Stoichiometry": [], "Pseudo Symmetry": [],
                                "Pseudo Stoichiometry": [],
                                "Total Structure Weight": [], "Atom Count": [], "Modelled Residue Count": [],
                                "Deposited Residue Count": [], "Unique protein chains": [],
                                "Unique nucleic acid chains": [],
                                "classification": [], "organism": [], "expression system": [], "mutation": [],
                                "method": [],
                                "resolution": [], "rvalueFree": [], "rvalueWork": [], "rvalueObserved": [],
                                "pubmedDOI": [],
                                "macromolecule": [], "oligosaccharide": [], "ligand": []}
                wdf = pd.DataFrame(data=table_copy)
                wdf[['ID']] = wdf[['ID']].astype(str)
                wdf.to_csv(save_path, header=False, index=False, mode='a')
                print("+ 50 rows, has reached", str(index+1))

        except Exception as e:
            error_times += 1
            lost_pdb.append(id)
            print("ERROR", id, e)

        # time.sleep(random.random())  # 担心被封

    # 最后一次不足50条的数据加入
    wdf = pd.DataFrame(data=table_format)
    wdf[['ID']] = df[['ID']].astype(str)
    wdf.to_csv(save_path, header=False, index=False, mode='a')
    print(lost_pdb)


csv_path = "data/all_(0-2]_legal_ligands.csv"
pdb_path = "D:/code/SuLab/data/pdb/"
save_path = "data/all_(0-2]_sm.csv"
proxy_url = "https://api.xiaoxiangdaili.com/ip/get?appKey=853530275123449856&appSecret=SoXMwiEv&cnt=&wt=text"
init_validate_url = "https://files.rcsb.org/pub/pdb/validation_reports/"
init_download_url = "https://files.rcsb.org/download/"
USER_AGENTS_LIST = [
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; AcooBrowser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Acoo Browser; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.0.04506)",
    "Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.5; AOLBuild 4337.35; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
    "Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US)",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0)",
    "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 1.0.3705; .NET CLR 1.1.4322)",
    "Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 3.0.04506.30)",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/523.15 (KHTML, like Gecko, Safari/419.3) Arora/0.3 (Change: 287 c9dfb30)",
    "Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527+ (KHTML, like Gecko, Safari/419.3) Arora/0.6",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.2pre) Gecko/20070215 K-Ninja/2.1.1",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9) Gecko/20080705 Firefox/3.0 Kapiko/3.0",
    "Mozilla/5.0 (X11; Linux i686; U;) Gecko/20070322 Kazehakase/0.4.5",
    "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.8) Gecko Fedora/1.9.0.8-1.fc10 Kazehakase/0.5.6",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/535.20 (KHTML, like Gecko) Chrome/19.0.1036.7 Safari/535.20",
    "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; fr) Presto/2.9.168 Version/11.52",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.11 TaoBrowser/2.0 Safari/536.11",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.71 Safari/537.1 LBBROWSER",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; LBBROWSER)",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E; LBBROWSER)",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.84 Safari/535.11 LBBROWSER",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E)",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; QQBrowser/7.0.3698.400)",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SV1; QQDownload 732; .NET4.0C; .NET4.0E; 360SE)",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E)",
    "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.89 Safari/537.1",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.89 Safari/537.1",
    "Mozilla/5.0 (iPad; U; CPU OS 4_2_1 like Mac OS X; zh-cn) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8C148 Safari/6533.18.5",
    "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:2.0b13pre) Gecko/20110307 Firefox/4.0b13pre",
    "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:16.0) Gecko/20100101 Firefox/16.0",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11",
    "Mozilla/5.0 (X11; U; Linux x86_64; zh-CN; rv:1.9.2.10) Gecko/20100922 Ubuntu/10.10 (maverick) Firefox/3.6.10"
]
# header会在循环中更改
header = {'User-Agent': "",
          'Cache-Control': "max-age=0",
          'sec-ch-ua': "\" Not A;Brand\";v=\"99\", \"Chromium\";v=\"99\", \"Google Chrome\";v=\"99\"",
          'sec-ch-ua-mobile': "?0",
          'sec-ch-ua-platform': "Windows",
          'Sec-Fetch-Dest': "document",
          'Sec-Fetch-Mode': "navigate",
          'Sec-Fetch-Site': "same-site",
          'Sec-Fetch-User': "?1",
          'Upgrade-Insecure-Requests': "1"
          }

print("***start process***")
crawl_process()
print("***finish process***")
