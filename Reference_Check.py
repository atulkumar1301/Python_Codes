from multiprocessing import Pool
def Ref_Check (i):
    path_out = "/Users/at5381ku/Desktop/1_Test/Out_Files/"
    file_out_1 = path_out + "Match_" + str (i) + ".txt"
    f_m = open(file_out_1, 'w')
    f_m.write ("HRC_Chrom" + "\t" + "HRC_Pos" + "\t" + "HRC_REF_Allele" + "\t" + "HRC_Alt_Allele" + "\t" + "Data_Chrom" + "\t" + "Data_Pos" + "\t" + "Data_REF_Allele" + "\t" + "Data_Alt_Allele" + "\n")
    file_out_2 = path_out + "Mismatch_" + str (i) + ".txt"
    f_m_1 = open(file_out_2, 'w')
    f_m_1.write ("HRC_Chrom" + "\t" + "HRC_Pos" + "\t" + "HRC_REF_Allele" + "\t" + "HRC_Alt_Allele" + "\t" + "Data_Chrom" + "\t" + "Data_Pos" + "\t" + "Data_REF_Allele" + "\t" + "Data_Alt_Allele" + "\n")
    file_out_3 = path_out + "Not_Found_" + str (i) + ".txt"
    f_m_2 = open(file_out_3, 'w')
    f_m_2.write ("Data_Chrom" + "\t" + "Data_Pos" + "\t" + "Data_REF_Allele" + "\t" + "Data_Alt_Allele" + "\n")
    file_out_4 = path_out + "Stats_" + str (i) + ".txt"
    f_m_3 = open(file_out_4, 'w')
    lines = []
    match_count = 0
    mismatch_count = 0
    notfound_count = 0
    num_lines = sum(1 for line in open("/Users/at5381ku/Desktop/1_Test/Bim_Files/chr_" + str (i) + ".bim"))
    with open ("/Users/at5381ku/Desktop/1_Test/Bim_Files/chr_" + str (i) + ".bim", 'r') as myFile:
        next (myFile, None)
        for line in myFile:
            line_list = line.split ()
            lines.append (line_list)
    with open ("/Users/at5381ku/Desktop/1_Test/Tab_Files/chr_" + str (i) + ".tab", 'r') as myFile_1:
        for line_1 in myFile_1:
            k = line_1.split ()
            c = 0
            d = 0
            for i in range (0, len (lines)):
                line_list_1 = lines [i]
                if ((line_list_1 [0] == k [0]) and (line_list_1 [3] == k [1]) and (line_list_1 [4] == k [3]) and (line_list_1 [5] == k [4])):
                    match_count = match_count + 1
                    c = c + 1
                    f_m.write (str (k [0]) + "\t" + str (k [1]) + "\t" + str (k [3]) + "\t" + str (k [4]) + "\t" + str (line_list_1 [0]) + "\t" + str (line_list_1 [3]) + "\t" + str (line_list_1 [4]) + "\t" + str (line_list_1 [5]) + "\n")
                elif (((line_list_1 [0] == k [0]) and (line_list_1 [3] == k [1])) and ((line_list_1 [4] != k [3]) or (line_list_1 [5] != k [4]))):
                    mismatch_count = mismatch_count + 1
                    d = d + 1
                    f_m_1.write (str (k [0]) + "\t" + str (k [1]) + "\t" + str (k [3]) + "\t" + str (k [4]) + "\t" + str (line_list_1 [0]) + "\t" + str (line_list_1 [3]) + "\t" + str (line_list_1 [4]) + "\t" + str (line_list_1 [5]) + "\n")
            if (c == 0) and (d == 0):
                notfound_count = notfound_count + 1
                f_m_2.write (str (line_list_1 [0]) + "\t" + str (line_list_1 [3]) + "\t" + str (line_list_1 [4]) + "\t" + str (line_list_1 [5]) + "\n")
    f_m_3.write ("Match Percetange" + str ((float (match_count)/float (num_lines)) * 100))
    f_m_3.write ("Mismatch Percetange" + str ((float (mismatch_count)/ float (num_lines)) * 100))
    f_m_3.write ("Notfound Percetange" + str ((float (notfound_count)/ float (num_lines)) * 100))
    f_m_3.write ("Total Number of Matches" + str (match_count))
    f_m_3.write ("Total Number of Mismatches" + str (mismatch_count))
    f_m_3.write ("Total Number of Not found" + str (notfound_count))
    f_m_3.write ("Total Number of lines" + str (num_lines))
    f_m_3.write ("Total Number of Data" + str (match_count + mismatch_count + notfound_count))
p = Pool ()
p.map (Ref_Check, range (1, 23))
