#Olá Engenheiro
#aqui você encontra a corrente do seu circuito de forma bem rápida
#Defina a dimensão da sua matriz de impedancias
dimensaomatrix=int(input('Quantas malhas tem seu circuito?\n2, 3, ...\n'))
#para malha 2x2
if dimensaomatrix == 2:
    confirm='n'
#defina os valores das impedancias a+bj ou a-bj
    while confirm=='n' or confirm=='N':
        a=complex(input('informe matrix a11\na11: '))
        b=complex(input('informe matrix a12\na12: '))
        c=complex(input('informe matrix a21\na21: '))
        d=complex(input('informe matrix a22\na22: '))
        m2x2=[[a,b],[c,d]]
        print('Sua matrix é\n{}'.format(m2x2))
        confirm=input('continuar [S/N]?\n')
        if confirm=='s' or confirm=='S':
#defina os valores das tensões
            confirm1='n'
            while confirm1=='n' or confirm1=='N':
                t1=complex(input('informe a tensão na malha 1\n'))
                t2=complex(input('informe a tensão na malha 2\n'))
                v2x1=[t1,t2]
                print('Suas tensões são\n{}'.format(v2x1))
                confirm1=input('continuar [S/N]?\n')
                if confirm1=='s' or confirm1=='S':
                    import numpy as np
                    m2x2i=np.linalg.inv(m2x2)
                    c=np.dot(m2x2i,v2x1)
                    Ia=c[0]
                    Ib=c[1]
                    print('Ia: {}\nIb: {}'.format(Ia,Ib))

#para malha 3x3
elif dimensaomatrix == 3:    
    
    confirm='n'
#defina os valores das impedancias a+bj ou a-bj
    while confirm=='n' or confirm=='N':
        a=complex(input('informe matrix a11\na11: '))
        b=complex(input('informe matrix a12\na12: '))
        c=complex(input('informe matrix a21\na13: '))
        d=complex(input('informe matrix a22\na21: '))
        e=complex(input('informe matrix a22\na22: '))
        f=complex(input('informe matrix a22\na23: '))
        g=complex(input('informe matrix a22\na31: '))
        h=complex(input('informe matrix a22\na32: '))
        i=complex(input('informe matrix a22\na33: '))
        m3x3=[[a,b,c],[d,e,f],[g,h,i]]
        print('Sua matrix é\n{}'.format(m3x3))
        confirm=input('continuar [S/N]?\n')
        if confirm=='s' or confirm=='S':
#defina os valores das tensões
            confirm1='n'
            while confirm1=='n' or confirm1=='N':
                t1=complex(input('informe a tensão na malha 1\n'))
                t2=complex(input('informe a tensão na malha 2\n'))
                t3=complex(input('informe a tensão na malha 3\n'))
                v3x1=[t1,t2,t3]
                print('Suas tensões são\n{}'.format(v3x1))
                confirm1=input('continuar [S/N]?\n')
                if confirm1=='s' or confirm1=='S':
                    import numpy as np
                    m3x3i=np.linalg.inv(m3x3)
                    c=np.dot(m3x3i,v3x1)
                    Ia=c[0]
                    Ib=c[1]
                    Ic=c[2]
                    print('Ia: {}\nIb: {}\nIc: {}'.format(Ia,Ib,Ic))

#para   malha 4x4
elif dimensaomatrix == 4:    
    
    confirm='n'
#defina os valores das impedancias a+bj ou a-bj
    while confirm=='n' or confirm=='N':
        a=complex(input('informe matrix a11\na11: '))
        b=complex(input('informe matrix a12\na12: '))
        c=complex(input('informe matrix a21\na13: '))
        d=complex(input('informe matrix a22\na14: '))
        e=complex(input('informe matrix a22\na21: '))
        f=complex(input('informe matrix a22\na22: '))
        g=complex(input('informe matrix a22\na23: '))
        h=complex(input('informe matrix a22\na24: '))
        i=complex(input('informe matrix a22\na31: '))
        j=complex(input('informe matrix a22\na32: '))
        l=complex(input('informe matrix a22\na33: '))
        m=complex(input('informe matrix a22\na34: '))
        n=complex(input('informe matrix a22\na41: '))
        o=complex(input('informe matrix a22\na42: '))
        p=complex(input('informe matrix a22\na43: '))
        q=complex(input('informe matrix a22\na44: '))
        m4x4=[[a,b,c,d],[e,f,g,h],[i,j,l,m],[n,o,p,q]]
        print('Sua matrix é\n{}'.format(m4x4))
        confirm=input('continuar [S/N]?\n')
        if confirm=='s' or confirm=='S':
#defina os valores das tensões
            confirm2='n'
            while confirm2=='n' or confirm2=='N':
                t1=complex(input('informe a tensão na malha 1\n'))
                t2=complex(input('informe a tensão na malha 2\n'))
                t3=complex(input('informe a tensão na malha 3\n'))
                t4=complex(input('informe a tensão na malha 4\n'))
                v4x1=[t1,t2,t3,t4]
                print('Suas tensões são\n{}'.format(v4x1))
                confirm2=input('continuar [S/N]?\n')
                if confirm2=='s' or confirm2=='S':
                    import numpy as np
                    m4x4i=np.linalg.inv(m4x4)
                    c=np.dot(m4x4i,v4x1)
                    Ia=c[0]
                    Ib=c[1]
                    Ic=c[2]
                    Id=c[3]
                    print('Ia: {}\nIb: {}\nIc: {}\nId: {}'.format(Ia,Ib,Ic,Id))