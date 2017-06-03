import pymorphy2
import os
import time
import json

start_time = time.time()

morph = pymorphy2.MorphAnalyzer()


def getlist():
    directory = '/Users/sea_fog/Documents/github/homework/pymorphy_bot/chapters_clean'
    files = os.listdir(directory)
    done = []
    words_morphs = []
    allwords = []
    for file in files:
        f = open(directory + '/' + file, 'r', encoding='utf-8')
        words = f.read().split()
        for word in words:
            if word not in done:
                words_morphs.append(morph.parse(word)[0])
                done.append(word)
            else:
                continue
        for el in words_morphs:
            if 'PRTF' in el.tag:
                allwords.append(el.word)
            else:
                allwords.append(el.normal_form)
    allwords = list(set(allwords))
    return allwords


def makejson(allwords):
    nounsmasc = []
    nounsfemn = []
    nounsneut = []
    adjfs = []
    verbs_perf_intr = []
    verbs_perf_tran = []
    verbs_impf_intr = []
    verbs_impf_tran = []
    prtfs_pssv = []
    prtfs_actv_intr = []
    prtfs_actv_tran = []
    numrs = []
    advbs = []
    npros = []
    preds = []
    conjs = []
    prcls = []
    intjs = []
    for word in allwords:
        if {'NOUN', 'masc'} in (morph.parse(word)[0]).tag:
            nounsmasc.append(word)
        elif {'NOUN', 'femn'} in (morph.parse(word)[0]).tag:
            nounsfemn.append(word)
        elif {'NOUN', 'neut'} in (morph.parse(word)[0]).tag:
            nounsneut.append(word)
        elif {'ADJF'} in (morph.parse(word)[0]).tag:
            adjfs.append(word)
        elif {'INFN', 'perf', 'intr'} in (morph.parse(word)[0]).tag:
            verbs_perf_intr.append(word)
        elif {'INFN', 'perf', 'tran'} in (morph.parse(word)[0]).tag:
            verbs_perf_tran.append(word)
        elif {'INFN', 'impf', 'intr'} in (morph.parse(word)[0]).tag:
            verbs_impf_intr.append(word)
        elif {'INFN', 'impf', 'tran'} in (morph.parse(word)[0]).tag:
            verbs_impf_tran.append(word)
        elif {'PRTF', 'pssv'} in (morph.parse(word)[0]).tag:
            prtfs_pssv.append(word)
        elif {'PRTF', 'actv', 'intr'} in (morph.parse(word)[0]).tag:
            prtfs_actv_intr.append(word)
        elif {'PRTF', 'actv', 'tran'} in (morph.parse(word)[0]).tag:
            prtfs_actv_tran.append(word)
        elif {'NUMR'} in (morph.parse(word)[0]).tag:
            numrs.append(word)
        elif {'ADVB'} in (morph.parse(word)[0]).tag:
            advbs.append(word)
        elif {'NPRO'} in (morph.parse(word)[0]).tag:
            npros.append(word)
        elif {'PRED'} in (morph.parse(word)[0]).tag:
            preds.append(word)
        elif {'CONJ'} in (morph.parse(word)[0]).tag:
            conjs.append(word)
        elif {'PRCL'} in (morph.parse(word)[0]).tag:
            prcls.append(word)
        elif {'INTJ'} in (morph.parse(word)[0]).tag:
            intjs.append(word)
        else:
            continue
    allwords_sorted = [nounsmasc, nounsfemn, nounsneut, adjfs, verbs_perf_intr, verbs_perf_tran, verbs_impf_intr,
                       verbs_impf_tran, prtfs_pssv, prtfs_actv_intr, prtfs_actv_tran, numrs, advbs, npros, preds, conjs, prcls, intjs]
    a = open('words.json', 'w', encoding='utf-8')
    json.dump(allwords_sorted, a, ensure_ascii=False)
    a.close()

def makejson1(allwords):
    a = open('words1.json', 'w', encoding='utf-8')
    allwords_morph = []
    for word in allwords:
        allwords_morph.append(morph.parse(word)[0])
    json.dump(allwords_morph, a, ensure_ascii=False)
    a.close()

def main():
    makejson(getlist())
    makejson1(getlist())
    print("--- %s seconds ---" % (time.time() - start_time))


if __name__ == "__main__":
    main()
