# -*- coding: utf-8 -*-
import os
import time
import sys

def sprint(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.1 / 100)

logo1 = """

███████╗██╗         ███╗   ███╗███████╗██████╗ ██╗ █████╗ 
██╔════╝██║         ████╗ ████║██╔════╝██╔══██╗██║██╔══██╗
███████╗██║         ██╔████╔██║█████╗  ██║  ██║██║███████║
╚════██║██║         ██║╚██╔╝██║██╔══╝  ██║  ██║██║██╔══██║
███████║███████╗    ██║ ╚═╝ ██║███████╗██████╔╝██║██║  ██║
╚══════╝╚══════╝    ╚═╝     ╚═╝╚══════╝╚═════╝ ╚═╝╚═╝  ╚═╝
                                                          
"""
logo2 = """
            ______________
      ,===:'.,            `-._
           `:.`---.__         `-._
             `:.     `--.         `.
               \.        `.         `.
       (,,(,    \.         `.   ____,-`.,
    (,'     `/   \.   ,--.___`.'
,  ,'  ,--.  `,   \.;'         `
 `{D, {    \  :    \;
   V,,'    /  /    //
   j;;    /  ,' ,-//.    ,---.      ,
   \;'   /  ,' /  _  \  /  _  \   ,'/
         \   `'  / \  `'  / \  `.' /
          `.___,'   `.__,'   `.__,'
"""
logo3 = """
$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
$$$$$$$$$$$$$$$$Y/'$$$$P'a$$$$$$$$$$$$$$$$
$$$$$$$$$",` /,/,mT$$$$ d$$$$$$$$$$$$$$$$$
$$$$$l',` , '/d$$$$P^$a `^a`W$$$$$$$$$$$$$
$$l', ` ,   |d$$$P^$'   _  _ ==~a$$$$$$$$$
$l.`  .      'i$^4'   _eP$$$$$$$$$$$$$$$$$
l '  .         /   ,  $$$$' `$~$$$$$$$$$$$
; ' ,              l /^' .,$oa$$$$$$$$$$$$
b ' ,        .     (_ ,1$$$$$$'$$$$$$$$$$$
$ , ,      .;       _$$$$$$$P $a$$$$$$$$$$
$, ,`    .$Ly        lM"^ ,  ,$$$$$$$'$$$$
$$, ,`   d$Liy      /'   edb $$$$$$$'$$$$$
$$$$,,'. $$$Li     (    d$$$$$$$$$$'$$$$$$
$$$$$$,' v$$$Li4.   `  `Q$$$$$$$P',$$$$$$$
$$$$$$$$,$$$$$$$L44., . .     ,,;d$$$$$$$$
$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
"""
logo4 = """
                            ,--.
                           {    }
                           K,   }
                          /  ~Y`
                     ,   /   /
                    {_'-K.__/
                      `/-.__L._
                      /  ' /`\_}
                     /  ' /
             ____   /  ' /
      ,-'~~~~    ~~/  ' /_
    ,'             ``~~~  ',
   (                        Y
  {                         I
 {      -                    `,
 |       ',                   )
 |        |   ,..__      __. Y
 |    .,_./  Y ' / ^Y   J   )|
 \           |' /   |   |   ||
  \          L_/    . _ (_,.'(
   \,   ,      ^^""' / |      )
     \_  \          /,L]     /
       '-_~-,       ` `   ./`
          `'{_            )
              ^^\..___,.--`
"""
logo5 = """
      NO!                          MNO!
     MNO!!         [NBK]          MNNOO!
   MMNO!                           MNNOO!!
 MNOONNOO!   MMMMMMMMMMPPPOII!   MNNO!!!!
 !O! NNO! MMMMMMMMMMMMMPPPOOOII!! NO!
       ! MMMMMMMMMMMMMPPPPOOOOIII! !
        MMMMMMMMMMMMPPPPPOOOOOOII!!
        MMMMMOOOOOOPPPPPPPPOOOOMII!
        MMMMM..    OPPMMP    .,OMI!
        MMMM::   o.,OPMP,.o   ::I!!
          NNM:::.,,OOPM!P,.::::!!
         MMNNNNNOOOOPMO!!IIPPO!!O!
         MMMMMNNNNOO:!!:!!IPPPPOO!
          MMMMMNNOOMMNNIIIPPPOO!!
             MMMONNMMNNNIIIOO!
           MN MOMMMNNNIIIIIO! OO
          MNO! IiivvvvvvvviI OOOO
     NNN.MNO!   O!''''''''!O   OONO NO!
    MNNNNNO!    OOOOOOOOOOO    MMNNON!
      MNNNNO!    PPPPPPPPP    MMNON!
         OO!                   ON!
"""
sprint ("----------------------------------------")
sprint ("\033[41m                 LOGO 1                 \033[00m")
sprint ("----------------------------------------")
sprint (logo1)
sprint ("----------------------------------------")
sprint ("\033[41m                 LOGO 2                 \033[00m")
sprint ("----------------------------------------")
sprint (logo2)
sprint ("----------------------------------------")
sprint ("\033[41m                 LOGO 3                 \033[00m")
sprint ("----------------------------------------")
sprint (logo3)
sprint ("----------------------------------------")
sprint ("\033[41m                 LOGO 4                 \033[00m")
sprint ("----------------------------------------")
sprint (logo4)
sprint ("----------------------------------------")
sprint ("\033[41m                 LOGO 5                 \033[00m")
sprint ("----------------------------------------")
sprint (logo5)