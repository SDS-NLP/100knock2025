file = "daiki/chapter02/popular-names.txt"
with open(file, 'r') as r:
    lines = r.readlines()
    names = []
    for line in lines:
        first_column = line.split()[0]
        names.append(first_column)
    dct = {}
    for name in names:
        if name in dct:
            dct[name] += 1
        else:
            dct[name] = 1 
    sorted_dct = dict(sorted(dct.items(), key = lambda item: item[1], reverse = True))
    for key, value in sorted_dct.items():
        print(key, value)
#awk '{print $1}' daiki/chapter02/popular-names.txt | sort | uniq -c | sort -nr | awk '{print $2, $1}'

"""James 118
William 111
John 108
Robert 108
Mary 92
Charles 75
Michael 74
Elizabeth 73
Joseph 70
Margaret 60
George 58
Thomas 58
David 57
Richard 51
Helen 45
Frank 43
Christopher 43
Anna 41
Edward 40
Ruth 39
Patricia 38
Matthew 37
Dorothy 36
Emma 35
Barbara 32
Daniel 31
Joshua 31
Sarah 26
Linda 26
Jennifer 26
Emily 26
Jessica 25
Jacob 25
Mildred 24
Betty 24
Susan 24
Henry 23
Ashley 23
Nancy 22
Andrew 21
Florence 20
Marie 20
Donald 20
Amanda 20
Samantha 19
Karen 18
Lisa 18
Melissa 18
Madison 18
Olivia 18
Stephanie 17
Abigail 17
Ethel 16
Sandra 16
Mark 16
Frances 15
Carol 15
Angela 15
Michelle 15
Heather 15
Ethan 15
Isabella 15
Shirley 14
Kimberly 14
Amy 14
Ava 14
Virginia 13
Deborah 13
Brian 13
Jason 13
Nicole 13
Hannah 13
Sophia 13
Minnie 12
Bertha 12
Donna 12
Cynthia 11
Alice 10
Doris 10
Ronald 10
Brittany 10
Nicholas 10
Mia 10
Noah 10
Joan 9
Debra 9
Tyler 9
Ida 8
Clara 8
Judith 8
Taylor 8
Alexis 8
Alexander 8
Mason 8
Harry 7
Sharon 7
Steven 7
Tammy 7
Brandon 7
Liam 7
Anthony 6
Annie 5
Gary 5
Jeffrey 5
Jayden 5
Charlotte 5
Lillian 4
Kathleen 4
Justin 4
Austin 4
Chloe 4
Benjamin 4
Evelyn 3
Megan 3
Aiden 3
Harper 3
Elijah 3
Bessie 2
Larry 2
Rebecca 2
Lauren 2
Amelia 2
Logan 2
Oliver 2
Walter 1
Carolyn 1
Pamela 1
Lori 1
Laura 1
Tracy 1
Julie 1
Scott 1
Kelly 1
Crystal 1
Rachel 1
Lucas 1"""

