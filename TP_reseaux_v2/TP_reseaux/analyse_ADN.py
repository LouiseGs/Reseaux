#!/usr/bin/python3
# -*- coding: utf-8 -*-

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
#                                                                     Projet Réseau 4BIM 
#                                                                  Analyse de sequence nucleique
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------#


def composition(seq): # Donne la composition de la sequence en nucleotides. (Fonctionne pour les sequence proteique ou nucleotidique)
    "Cette fonction calcule la composition d'une sequence (argument) sous forme de chaine de caractére."
    seq=seq.strip()
    dico={}
    for ele in seq:
        if ele in dico: # Si la cle "ele" existe deja on rajoute 1 a sa valeur.
            dico[ele]+=1
        else: # Si la cle "ele" n'existe pas on la cree et on lui associe la valeur 1.
            dico[ele]=1    
    return(dico)

def contenu_C_et_G(seq, con, taille=-1): # Renvoie le poucentage de C+G contenue dans la sequence "seq" (par defaut) ou dans toutes les fenetres glissante de longueurs donnees.
    "Cette fonction calcule le pourcentage de C+G contenue dans une sequence (premier argument) (par defaut) ou dans toutes les fenetres glissante de longueurs donnees (deuxieme argument)."
    if taille==-1:
        taille=len(seq)
    seq=seq.upper()
    longueur=len(seq)
    contenu=[]
    if taille<=longueur: # Permet de verifier que la sequence est suffisamant longue pour creer des fenetres glissante de la taille demandee.
        for i,element in enumerate(seq[:longueur-(taille-1)]): # Permet de parcourie l'ensemble de la ou des fenetre(s) glissante(s).
            fenetre=seq[i:i+taille]
            dico=composition(fenetre, con)
            if "C" in dico.keys() and "G" in dico.keys():
                    contenu.append((dico['C']+dico['G'])/taille*100) # Calcule le pourcentage de C+G dans la fenetre et de l'ajouter a la liste "contenu".
            elif "C" in dico.keys():
                contenu.append(dico['C']/taille*100) # Calcule le poucentage de C dans la fenetre quand la fenetre ne contient pas de "G".
            elif "G" in dico.keys():
                contenu.append(dico['G']/taille*100)
            else:
                contenu.append(0)
        return(contenu)
    else:
        con.sendall("---------------\nAttention : Arret du programme.\n\nCe programme ne fonctionne que pour des sequence de longueur minimum "+str(taille)+",\n ou de taille de fenetre maximale "+str(longueur)+"\n".encode())
        con.sendall("Changez de sequence ou de taille de fenetre.\n---------------\n".encode())
        return('')


def nb_CpG(seq,con, taille=-1): # Renvoie le nombre de couple CG presents dans la sequence (par defaut) ou dans toutes les fenetres glissante de longueurs donnees.
    "Cette fonction calcule le nombre de couple CG presents dans une sequence donnee en premier argument (par defaut) ou dans toutes les fenetres glissante de longueurs donnees en deuxieme argument."
    if taille==-1:
        taille=len(seq)
    seq=seq.upper()
    seq=seq.strip()
    longueur=len(seq)
    contenu_CpG=[]
    if taille<=longueur:
        for i,ele in enumerate(seq[:longueur-(taille-1)]):
            fenetre=seq[i:i+taille]
            CpG=0
            for j,ele in enumerate(fenetre[:-1]):
                couple=fenetre[j]+fenetre[j+1]
                if couple == 'CG':
                    CpG+=1
            contenu_CpG.append(CpG)
        return(contenu_CpG)
    else:
        con.sendall("---------------\nAttention : Arret du programme.\n\nCe programme ne fonctionne que pour des sequence de longueur minimum "+str(taille)+",\n ou de taille de fenetre maximale "+str(longueur)+"\n".encode())
        con.sendall("Changez de sequence ou de taille de fenetre.\n---------------\n".encode())
        return('')

def contenu_C_et_G_et_nb_CpG(seq,con,taille=-1,comp=-1): # Renvoie le poucentage de C+G et le nombre de couple CG contenue dans la sequence (par defaut) ou dans toutes les fenetres glissante de longueurs donnees.
    "Cette fonction calcule le pourcentage de C+G (premiere liste retournee) le nombre de couple CG (deuxieme liste retournee) presents dans une sequence donnee en premier argument (par defaut) ou dans toutes les fenetres glissante de longueurs donnees en deuxieme argument."
    if taille==-1:
        taille=len(seq)
    seq=seq.upper()
    longueur=len(seq)
    contenu=[]
    contenu_CpG=[]
    if taille<=longueur: # Permet de verifier que la sequence est suffisamant longue pour creer des fenetres glissante de la taille demandee.
        for i,element in enumerate(seq[:longueur-(taille-1)]): # Permet de parcourie l'ensemble de la ou des fenetre(s) glissante(s).
            fenetre=seq[i:i+taille]
            CpG=0
            for j,ele in enumerate(fenetre[:-1]):
                couple=fenetre[j]+fenetre[j+1]
                if couple == 'CG':
                    CpG+=1
            contenu_CpG.append(CpG)
            if taille==-1: # Permet de ne pas calculer inutilement la composition de la sequence si elle est donnee en entree et que l'analyse se fait sur la sequence entiere.
                if comp==-1:
                    dico=composition(fenetre, con)
                else:
                    dico=comp
            else:
                dico=composition(fenetre, con) # Permet de ne pas calculer inutilement la composition de la sequence si elle est donnee en entree et que l'analyse se fait sur la sequence entiere.
            if "C" in dico.keys() and "G" in dico.keys():
                    contenu.append((dico['C']+dico['G'])/taille*100) # Calcule le pourcentage de C+G dans la fenetre et de l'ajouter a la liste "contenu".
            elif "C" in dico.keys():
                contenu.append(dico['C']/taille*100) # Calcule le poucentage de C dans la fenetre quand la fenetre ne contient pas de "G".
            elif "G" in dico.keys():
                contenu.append(dico['G']/taille*100)
            else:
                contenu.append(0)
        return(contenu,contenu_CpG)
    else:
        con.sendall("---------------\nAttention : Arret du programme.\n\nCe programme ne fonctionne que pour des sequence de longueur minimum "+str(taille)+",\n ou de taille de fenetre maximale "+str(longueur)+"\n".encode())
        con.sendall("Changez de sequence ou de taille de fenetre.\n---------------\n".encode())
        return('','')

def rapport_CpG(seq,con,taille=-1): # Renvoie le rapport CpG de la sequence (par defaut) ou dans toutes les fenetres glissante de longueurs donnees.
    "Cette fonction calcule le rapport CpG d'une sequence donnee en premier argument (par defaut) ou dans toutes les fenetres glissante de longueurs donnees en deuxieme argument."
    if taille==-1:
        taille=len(seq)
    seq=seq.upper()
    longueur=len(seq)
    rapports=[]
    if taille<=longueur:
        for i,ele in enumerate(seq[:longueur-(taille-1)]):
            fenetre=seq[i:i+taille]
            nb_observe=nb_CpG(fenetre, con)[0]
            contenu=composition(fenetre, con)
            if "C" in contenu.keys() and "G" in contenu.keys():
                nb_attendu=(contenu["C"]*contenu["G"])/taille
                rapports.append(nb_observe/nb_attendu)
            else:
                rapports.append("NA")
        return(rapports)
    else:
        con.sendall("---------------\nAttention : Arret du programme.\n\nCe programme ne fonctionne que pour des sequence de longueur minimum "+str(taille)+",\n ou de taille de fenetre maximale "+str(longueur)+"\n".encode())
        con.sendall("Changez de sequence ou de taille de fenetre.\n---------------\n".encode())
        return('')

def rapport_CpG_nb_CpG_contenu_C_et_G(seq,con, taille=-1,comp=-1): # Renvoie le rapportCpG, le nombre observe CpG et le pourcentage de C+G de de la sequence (par defaut) ou dans toutes les fenetres glissante de longueurs donnees.
    "Cette fonction calcule le rapport CpG (premiere liste retournee) le nombre de couple CG (deuxieme liste retournee) le pourcentage de C+G (troisieme liste retournee) presents dans une sequence donnee en premier argument (par defaut) ou dans toutes les fenetres glissante de longueurs donnees en deuxieme argument."
    if taille==-1:
        taille=len(seq)
    seq=seq.upper()
    longueur=len(seq)
    nb_observe=[]
    contenu=[]
    rapports=[]
    if taille<=longueur:
        for i,ele in enumerate(seq[:longueur-(taille-1)]):
            fenetre=seq[i:i+taille]
            nb_observe.append(nb_CpG(fenetre, con)[0])
            if taille==-1: # Permet de ne pas calculer inutilement la composition de la sequence si elle est donnee en entree et que l'analyse se fait sur la sequence entiere.
                if comp==-1:
                    dico=composition(fenetre, con)
                else:
                    dico=comp
            else: # Si l'analyse se fait par fentre la composition donnee en entree ne permet pas de calculer la composition par sequence. 
                dico=composition(fenetre, con)
            if "C" in dico.keys() and "G" in dico.keys():
                nb_attendu=(dico["C"]*dico["G"])/taille
                rapports.append(nb_observe[i]/nb_attendu)
                contenu.append((dico['C']+dico['G'])/taille*100) # Calcule le pourcentage de C+G dans la fenetre et de l'ajouter a la liste "contenu".
            elif "C" in dico.keys():
                contenu.append(dico['C']/taille*100) # Calcule le poucentage de C dans la fenetre quand la fenetre ne contient pas de "G".
                rapports.append("NA")
            elif "G" in dico.keys():
                contenu.append(dico['G']/taille*100)
                rapports.append("NA")
            else:
                contenu.append(0)
                rapports.append("NA")
        return(rapports,nb_observe,contenu)
    else:
        con.sendall("---------------\nAttention : Arret du programme.\n\nCe programme ne fonctionne que pour des sequence de longueur minimum "+str(taille)+",\n ou de taille de fenetre maximale "+str(longueur)+"\n".encode())
        con.sendall("Changez de sequence ou de taille de fenetre.\n---------------\n".encode())
        return('','','')

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
#                                                                     Fonctions suplementaires
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

def fenetre_seq(seq,taille, con):# Fonction tres generale mais qui est trop gourmande en memoire pour etre utilisee sur de longues sequences
    "Cette fonction prend en argument une sequence et une taille de fenetre inferieure a la longueur de la sequence et renvoie une liste de fenetres glissantes." 
    seq=seq.upper()
    fenetres=[]
    longueur=len(seq)
    if longueur>=taille:
        for i,element in enumerate(seq[:longueur-(taille-1)]):
            fenetre=seq[i:i+taille]
            fenetres.append(fenetre)
    else:
        con.sendall("---------------\nAttention : Arret du programme.\n\nCe programme ne fonctionne que pour des sequence de longueur minimum "+str(taille)+".\n---------------\n".encode())
        fenetres=''
    return(fenetres)

def temperature_fusion(seq): # Permet de calculer la temperature de fusion d'une sequence.
    "Cette fonction calcule la temperature de fusion d'une sequence donnee entree."
    T=70+0.44*contenu_C_et_G(seq, con)[0]
    return T


