from ...libs.md5lines import md5lines

import re


transcriptome_filename_re = re.compile("""
    (?P<id>\d{4,6})_
    (?P<library>PE|MP)_
    (?P<insert_size>\d*bp)_
    (?P<project>\w+)_
    (?P<vendor>AGRF|UNSW)_
    (?P<flow_id>\w{9})_
    (?P<index>[G|A|T|C|-]*)_
    (?P<lane>L\d{3})_
    (?P<read>[R|I][1|2])\.fastq\.gz
""", re.VERBOSE)


# FIXME: we need the full convention from BPA / MA
metabolomics_filename_re = re.compile("""
    (?P<id>\d{4,6})_
    SC_
    (?P<vendor>MA)_
    (?P<analytical_platform>GCMS|LCMS)_
    .*
    (\.tar\.gz|\.mzML)$
""", re.VERBOSE)


proteomics_filename_re = re.compile("""
    (?P<id>\d{4,6})_
    SC_
    (?P<vendor>APAF|MBPF)_
    .*
    (\.wiff|\.wiff\.scan|\.txt|\.raw)$
""", re.VERBOSE)


proteomics_pool_filename_re = re.compile("""
    (?P<pool_id>P\d+_\d+_Exp\d+_Pool\d+)_
    .*
    (\.raw)$
""", re.VERBOSE)


proteomics_analysed_filename_re = re.compile("""
    (?P<zip_file_name>.*)
    (\.zip)$
""", re.VERBOSE)


singlecell_filename_re = re.compile("""
    (?P<id>\d{4,6}-\d{4,6})_
    (?P<library>PE|MP)_
    (?P<insert_size>\d*bp)_
    (?P<project>\w+)_
    (?P<vendor>WEHI|UNSW)_
    (?P<flow_id>\w{9})_
    (?P<index>[G|A|T|C|-]*|NoIndex)_
    (?P<lane>L\d{3})_
    (?P<read>[R|I][1|2])\.fastq\.gz
""", re.VERBOSE)


singlecell_index_info_filename_re = re.compile("""
    Stemcells_
    (?P<vendor>WEHI|UNSW)_
    (?P<flow_id>\w{9})_
    index_info_
    BPA(?P<id>\d{4,6}-\d{4,6})\.xlsx$
""", re.VERBOSE)


smallrna_filename_re = re.compile("""
    (?P<id>\d{4,6})_
    (?P<insert_size>[\d-]+nt)_
    smRNA_
    (?P<project>\w+)_
    (?P<vendor>AGRF|UNSW)_
    (?P<flow_id>\w{9})_
    (?P<index>[G|A|T|C|-]*)_
    (?P<lane>L\d{3})_
    (?P<read>[R|I][1|2])\.fastq\.gz
""", re.VERBOSE)


xlsx_filename_re = re.compile(r'^.*\.xlsx')
pdf_filename_re = re.compile(r'^.*\.pdf')


def parse_md5_file(md5_file, regexps):
    with open(md5_file) as f:
        for md5, path in md5lines(f):
            matches = [_f for _f in (regexp.match(path.split('/')[-1]) for regexp in regexps) if _f]
            m = None
            if matches:
                m = matches[0]
            if m:
                yield path, md5, m.groupdict()
            else:
                if path.endswith('_metadata.xlsx'):
                    continue
                if path.endswith('_Report.pdf'):
                    continue
                yield path, md5, None


def proteomics_raw_extract_pool_id(v):
    if v is None:
        return
    m = proteomics_pool_filename_re.match(v)
    if m is None:
        return
    return m.groupdict()['pool_id']
