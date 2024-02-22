import ctypes
import time
from base64 import b85decode
from contextlib import suppress
from ctypes import wintypes
from io import BytesIO

import cv2  # noqa: F401
import pyautogui
from PIL import Image
from rich.console import Console

_images = {
    "ko-1080": "iBL{Q4GJ0x0000DNk~Le0001v0000d2nGNE0NL(vE&u=k0drDELIAGL9O(c600d`2O+f$vv5yP<VFdsH010qNS#tmY4#NNd4#NS*Z>VGd048xsL_t(|UZtFQbe7e*_W7quR_46xeKQiK1xSD}WF`YiR)7Fuo`)a;B8UnIGRPpv3|bTv5mW@~P#I(pP!WgPT5FwJJyv_Po>q^wgH~JHo_^n1-~C<JeeeCePeQ0Y>-=%8{mjGOzkS{J-p`w~OY2lENm)gb5bGz&*+sgXmRlkzIVBR!FPF5uGRf>%A?Y2;Q4Yj<xkNftV1JpULW$X>IHyb!GE1QnX&)=WwMyj5jQ*0GTd7LQ85k^6DO6sSq^hbVwSy^5RTC&ZpBg0T9cv|n>O|G)as<mMnRo_VD;3udg!MFD7t87S)i{0-u2m_SR}GQqRYN7#vr%FN!z8oUaLMX3Lb3{*B(LvC$?Z2%IzstSW{<%rn<S@4gX9!6N_Nj7k_BaklvOZPa(WJy4uvD6L!V)i+Z)Ff4#TyFNKT)jxEIdtHCQsb*W%ndN$)yHqTTQ;ovS4sO6`c}hLZD9H>l4RLLH~%v))QkkA<k?VoA(I8)XiFiX<@$>lC&pu<a;rZ!NzarJf%fAnhZ4QTJ%qPN<`fd=67Gp9M<k$n8}qQIFW(rofDXLue9WXlOi065vsAplE(s8{m{lMi`u|Qk6kdELTR0<O)EOlsnLrQ=v-6vMCOZmj@>hU<x4e@OS|lmV_t?fTjSDlx$RVHlB%c@NhXbuTsHD!F^*rhDdsM2xXM;^ctq%WCNTIfTcsfQPOF^C<P`PP$)Q84F)(v0nSj#0(gW^<>1K%93A@pFTepDmw=P!%W~{T{bi#QqOm<REfj)=^02fCj&3(_2qd4wpdlnCzs%AUf~A$(CFjB|qJ8zk3J%IRIL>i888|TjM90bC%e4Zhy$1(ML_;O!R-i|eOCq45JV53?29QFeuH)pO38e5qfX5UEC;$h5B*S@<SvnD(<Sf91>qolQ<64zyv<ArlG!eK?Iz@N@PEKDq4#DXk2d4wnvHwT|r&ru@Vpxv>9F_q%>Nt&(18}nbWpLOit-xWOs>(w`9TOh7f1BV0;=Z^H8n}@wTL}9Jk2zi(n%0U#)DoC9Y*TO&vv4Do0|!dWD@Cs@y%d~$f@6+DaOgS;4x!1U+Z4+caGWGGRC{iB&?KTE2~6NZ3QicFxC6x@q8vN{I3^$B64D0%kTL*Ns-Oh$;9iN?&TFUQc!tu9t_>2U+o0hIP9_{D)*Imp4WC1B08PiD(Fj{3u&+__0S<v7I2xux(5Mi`V%=&b4{nnOXmWcYbQLyA)PWPZsvhSyNF)HK2H@cN;qU~9p@2}Nw00aX4-Yyv8~KX#J{Fo34ueI*57!ZbJT$i6-z~QS2j?fk!4e|<&_-}HJj=Ji<3kyj4Vo%+T7bhF5EjBiaFRiH3vfEL1Sgf?@P)$QWEnUNQ3-IFglxDNM8`>B{zK;pi_YWW0W?$!Kv5AO2NU<R^q_c%H0SADr^gWrDjC;J0yK#LC<#h{3lW|aoRa{c2~b9NG$i1OA@mqH5L_n@kmLazI!zX~Q5~=?3pq><fXJf5KvBY?&=^GAmsdDkLsbrd$)?lvY>@2UgK?ia1t;z}00;7+%7fz}VMEeks3gGR9f$dd?q|LOr!d!G*dY{gXHi%Jd5AnX@ne0yM1Wd?gF1%;2Bj(tPRMbPAHi|p5DLzvjuY`Y4!|KmEx{=TILK`P4Z*o0(qF?<0)<9Ycyd@FXk0Wrl?*VF(U8epR~HHaq#{IkSUL-nT7)Ai-IZw_2Pr&>2vLb}8I}nVR02!DL0AZnUYpKC0C9XO&*S;s*r3dDhDs`2Cjxjf;W$|cS4@s`v7Ai@VSWQ3av7!w1j7`diFB_Il-^|!9H$P6G(r*p(;TPoFp2g8P=y9it^-KH=~AuWq@vQ*anLZS$Qd<cFi~wKIuW7qvXJGHWd{%8@Gu0+3XuoLB8kD{We{;+vOWXu=S7g96n%y`Ft*>ybd>3I9NzR2Z~#q8$Z<5cLCJN3lkUKw5*VTgO&-DnKp-^j6&fy=DNt8L2B@x76{!>$x(Z#UBP!GjBcTL9p&&T5_a)9_X<>*Jix*<(Qn5D>vU)&<hU$#6izyv>P6narZs0IMj$pJD0T|If!vlB-44o!_0CS!u$>%ogV>rrz3uVG#7{+2qm@}a)<S_&%vwNL}ttiA$6eA!VkdSu<7#vh|!{`pq6YGKe4Er*;AC17C8xKDa8$2XJ6?YwmEOsu|xrHf(fTdrCi-fn?asJpaJP@`g!R-_jJPRRWzQt{pcX1i*9fHQ^Wh~)1ypUZu4vr<q-f?0b4WOuVoB$jQ#pyW7goaK7hsp0<FZsRdboo2!eHEDE>Jh5^tEx2*(vep>Msa|KN%fUc1B;>ViVP%g1O*|`kH$275ilmjZde}SupA;J3W}}+l918>Plkfiph^We$pDBsP6m?WC}4;Xh>+`KLrj+Qk?RneT!2+OYP!^ooF<ixQ{X_2NQ{y9aF`B=m;>b@Ip#<#yEokoAR$Dh0hG+{1gHWzA)OE@K#sY4e$OiT;GOTuZ$A9KY}&jmG%|7kQ3yHdc_lLQ+BvfGj$38X(uJrCm+z$YcAY&g4ND3L<o9`K!uxc)EAdP|pDAq^D+7m&lfudohz=DRIvFxE5LVMVVQ3EdV*_yXAt2^A3JyY5+u*cv9Du_{PXUn$$alI87$PrTyiZ<z`G8Dqp00`V6|o|D@wvV7=ii-@jhmMnC>VKtC%vD1C!-&hQDJbVB*1451iBHXRDeXo41l4Vc<DA(E$+?rIvh`71Vv!H)O7$1;K}GZSW+>vN&!4+bRC4N3^aNsz#u#^gr+RO(zSH7bSi@5sM8Err#W`)yYkC_dsNOowFgc^aE8Kl2o4frm4&n%fRkM?Sn~TYnXU&&9LXV66##CyOtcGoY=!jbUngIDdP3x{PXnA=3>-Ej>NF8;V2xU=;GBQzE<JAN9jnoK&~b4-0lG3`^E;Nucrb7tR8U+mJ&WpP+SSccKB!6hmJhXK0;v44h%#`OJb?cCs}IVD?>!>haUZ&kAK@j!;Rp{yrMZ)ZH<#nsMa^+A9CzT9*N%`8V<$>o;~1$PGFobfvb5!a4Wpz2`v(plD;4#lr3~s`)F^-Y?UVYV)32H3ASsg9UU@*b-M(>|t|!8cQaV|9Nkz$gX6)3Nvh&V$vU2TGS-GYStz8yqRZ!ld<(+rkrs|3YCoJim(c@XdWd_tukOL2HmD8to%PHvGxqF~{<@|Zm(@#@-<r#?OsndI8^winvG`R>-Oq5TZyj!1N!C_*}oQEY{2I7c{Bd;9fHynmXdm;}4FnIuH&W#J?rdw{58<yQ5i?qB^ZbbRJ-yGL#-o1OB%)jY6nSbLvnZIzZ%)5S$%v(4|N~(uzCqDD!clEd(cLE%AS}!^nht(byYUG5;vU|^3`SB0-$sa#GF2DQrG5P4dN9FLtn`GVko7L$&FdiVfN(ba(|M~Gzz0Y>In}WlT1tsxb&Uq~Fq2mx7wKFIT4ntK=u`FJ?Kri;s^xuCuFMt2jQ}W0o+ZCKIKeL`RZPrZr4)dF6{{Wm#TUP=Y&Qd}yYxlYd6&t?p|3v@qoAdJ4YY)R_$4V-I2?VF<Q#DRL`}mlA_4!HF*G~T2Z@xGqU;hr<pszkZB_DtAeVH=%I?1AoKr!gV3G4M2p4|&5Y)H;hXOIaD+$IwVa;yN*z-gjLh9f;VR39uaT->Mk|NPf%$m3|BC$y3N@1M`<H9z_23Hj}R*#6Ja&<tNxan&${?EV2bTemGo2eZ7$REfstEIrx|?KX4HEP3~hhxOQB<NTMNyH}on_8$4=yWf+qKC{kz@S)q`L=6UxYjc(a{F9G7IB*>1IGX36gFAQ<7;0NMjt2+QPY$7(<K-)Fkdw#nkaMT+lC!6F$!Yfz)VVWv$+0JP%JHK+<n)O<WzD)p(xrEe{2o2&|9pK`nh~3mIxsF)%a4C}K+oB-eKl_CM@$SqgCxRG1J_xya<Lxs?+6KZ>{=&#_uVcJ9o%|}4r;j#WnA|k*dqHM*dhgGqcM6xc!1Mnu;ip4R6b-fG)c-EQ9{$_&6h7+Wv;n>rBpRdmGTi&rLt+7)Q+AZ1BXq~2|b1)I?Ra^yY$$L7w&`85F9#=jkX95!&D65Wc31204L)rgeD})*>Ij4;V^5~FOyquTPkbUFO^%dyb8-J*WE0)+`1TABCFP6JG2^Fx%OsNdBZq#s7g75de^$!x*XxDua2sy_R)SCw&*&|aQAl{G*6$sOGb{LB)L5*CEBr6dKEVSx)t)pe_Dq=ba0~q1Lxr=jUg_#SFL>Nz}fj-g2P1F<uuyCEA`%-N+38aTY-a%;i9R|aUvZ`HEc1*Nk@*u2l^bngEzPageP<E2XT-WCZSiAG|KNk0XTm?D>LWK1vsD<H-F{j{d&&kZL1WV6ojZ`xJ(kDN~HThOI9q>V+c<1ps{#BjywPvk9VLYBPrHzPbi~Y?rifpR65HpHk#6em?cJ298sm|s0zdBZX8NC$n?4M0&r$6TwpE&Wk8(3qjHg}aG1?GoF`9Mhq?IdeL9Nbd=8}}Du|=2Xb<ExbR2}J7#zpX-(++fgnS1hD!?>s{8U-LX}KIbx>L@b-6KDEVV@jF$GmUf2D$cz1=6i(s5K58MTf*#e)6~vRcny&bL41wQW6@T@Fd3i$^QG->oM=Vc}Qx9ja3+Y-fAJKSRISU{1py6Y5Ft+2QI?>IX$Z7(_eXT)@W4F$iQ6Ig{)wj0QYBmx9K<v4irz0kq`r-n!%$0j>YEbb7rH#I48kzJuZri^(+}0fHQ0UJTx4V+0Hfc>W|EEHf>vp<1r+K(xB8XTt?$}sg<Rxmgq4AC#O3bA8<f~A){*@mLUL;3Gp+6E(3-bfq=tg1Bgr{zEqZ$XwV)gIa%lBW`0LbnHA(>i&ri|IN~rH`%o6wj+5aNnq}BTXu=FE&yZ73TBv&dx%&VEVInLjIfCMZ9~9%z9N@&@GC95Qd;loBfF(v(J!@q#I>y_tn=AYgy`SOg<M$uau*49>aDU;Mdu7b@X3Zu1=;g%mJM|pqIE02`eKY4^-IvymmS4W}h#s?R*R9r;8iE`=>Mli6STb1N|M_7(ZZi^c&2=19*<C6$Wa@p8<8V|J<T*^n0Z@<_<KEmB|Kxxh5*psj9H#`sNKOQnNUUq6M7mT-RpSH=MZCf2X*1ENZm0%;2uMNMupm^;ymq$r9^5P*s&3T>V605jq?li?G1`EZ2BGQ^+>g#;+apjqu1%-O0Bo61mMgPyTnun!q2zKDfW@3LyK!y>;v9>rUdt%T5tEwbO9#%{+n4JIh>AhmcC6OK^$(w%P<yAC$MM+bFYE=30D>bWItztsW};*=Ojn`P5EKs#*PG{E3s8>9H-9)SM~~hi^A|6a>fsZlcEluU95+>N+qhibed~zc<5A>_bZLsYgm=5|-n~w`^&cvo3mc?Up9Y18ngwU)e(JiL7NCA@?neQ_ke=<yC_;yN>EgY5-1i^fX5grbB!}R9=)k!X$+7=#MsOT7>NpN&Za2qqg!*|LhN)D9sA$(}R8B1{o0UGO1vq1;U#;6B7-mMgFr*BWf^vZ49B0n;*Wvs@l8?CW9cTN_)d~eC%S-?O7S9Q^6{~O7V?M+vpfk?NLnG#(C+GOm^=!&|JbE|6M272q5!{Ov$;44BmA#Ye>?O2XRAw5=bX4rNJJ#sEsD}=1Rd>kXJK#DSk-)$G(}(5fZyb_$Vg2u-{F4i7&m%dG;du!RpWB|P9ytP@4{no#Br^*xliRyq!&DxeCktU}&%G8(&Yrm&$$AqU6dgx99U4NPnW6e7J?2Z?i*qVIG@L$dZbwIW<JE@{jt=9Q4r3&?KpSwulIwMF@HaSCGa%x3BwmkUEd`??&IhrLX#mfhv(e$>k8L%e-1JLMkE+0N7^>{v21^R+OWg*gg()}@VAA2ZlBe?k2v_{nfR`c=1S11ZlLdI9SZ)|KDHxGVnKet&^O5`TOE2;tI#0jKCbeDeXC*N{pG0E$>wkY-w{6>Tt3pPgytqy+TWJ;dON;_i5h6LCVLgRV+k{vGVmg%=QWExYmYbEN0w5+E5fB>vJc1Dd^9@$g$>TfqUKAT@+RSEk%?RExx1d&YjouZ*WkAhHDT0`X@YoB_+yh7vD%{UZ2qQnu_~{Fq;pLo{_0%+H^Ska^tLHy|;U4MK7kL-zl;EU0SSfZi9>Y#ouHYcYAULNC9J(Hz@Xx<L1)apOexc6$jGQ!0os7p^4~Pg28=T;18UgXSdLvZ*_~rZcxb?R$4WMCyoYNiPAY^i%g2T>6P!yoJT7aX|(r6s6@I`ndLc?B6SR&nO(7QMZS0>{Sp8o#j8NI=c%WhJ8kHU(*N@~XhIZ#`o<3v#LY5bHy=l~qWieKV}{tQ*QxL+pjo7KGrxeG!P)^pHvvvEK6a21wgxMwQdF{9H!$v`7z!1YvkX*vtVhE5|iD4Bm8cxbcy7kcN9kg)GNuu<>H;p^24u0v=+B8|%7JM-Q7HJkEz#zo{HF|6~GLJXkMiB)i!Y&Z;ECKJj=h~npk%pP|BsL9jiSHE~n{)WW#fd@87^XyqtJ#@6xK*PsPmW7KK1XC7I9^Zv)VpN9u=SRh-PMJ&GyLY|RH%*p72ys-;lHr;>^Yg{~F2_0g#2wPVdQ{*ze(26NUB7XK{O!x9bRu@{{MiN#l4Am-;CRQ`<sHW*=ng~`!Ev3U9Vd7A0HjH+6GWx6S7A8<OHDxo$IyU;DLmIg`=v86&!NpzB{ic1aCY6jR)?4CZ(k<=_SPZYwt34f)-xf7LKT)dE4_5-d_CqvfYYyXgaQ_IiU15PLn15$BMGkKdp@0q*9=dTrQq7Eq*T1ehRrK9A*Hp?nm<>1A}4$FvF&=_H(xs_H^cQ<DeP@@P+p(q@nhyV&(U$PuJ`u!0{4h@LuW%7<u@tR8B5k3x9d8z5N`1P&yVQ*&3}FUl+NjJ6vPn2YyagBr{wq(JEUR6ICTNdFVF^0oi=d%sLDc-Z%8YdGyT!cL_hKP4ykM$uiFVskK#sIwrY{Q_1Z(a|HzST3MFTsnfI`6axtp9G*n%x6m(8=oHA+WKb3Qcr4NK<qZKa>DA>C)p{(xJat`5#7pH!Lyk$VmDDCwc($JW_%P^{9atyn@8pCzY2N8-_e`prT`Gho%)aWvhhB}B1v0{}$`89gPxih;pEWC8_zHikF&)y?1Ja?~Z@W}BR9@6+xR?C69Tv9zk?z!hS9nJg$jm8m96b=?eGFwp5B;P|q%6qdn-o58G88v0PHoOXTaKeQuf)j<)L;(rm&B6K10W%?nIZpa98Me~g+JDqc$F&;pd^g{+Q1<WNpx2`~G-v3TJ#UWm7|;+OLQ{wYegbgY_7xg(6lm9Bqv)(rKtL_Jd7;h}^H_G&XV34EXP;)>><yqg^zas)5@7q<po2s1GRf&y83G5RH*nxXo`;mBPSxQ4be(po`Pk^dq3dws$CGW9R1I*dWgcQMW9dJ>IxBC!`k>x~jm?BQg+j<EC~AmL00JC30bRhyR&^X47l`fytK@MvEuN=C(yu>%QuWnuPij*7tpW^R;dmypjiV<xM>F^7Tv#is)-00O06FI`*sIrXxH)JT&W2K*`qW|jGWpr-2j#B_#hhQ6F$beU08Je~W;xLXG(<XJq!?-$w%CXSj3vKErEwYZCE?MqgZ)`(pv<lVrMRXk7-VcgXCm;m!^X(?Y13u&q^Z(8cb3e#ZVpD3<#OhvO#p7&zA}Kx@=?qESpOMtfe0FQ&ir}WxfvG!f?Vh?XfKB4pS}LD&L8zI8(~18y?r>#z=*YD@4*2$J9cu)#Ec^l*BxXU-f+)$oVZKmm>s2tD_k_f3qo`o(wq%TKCs_L2FIS*7Ptdlhu^Mz&Qee^BygOWbFZ-wg3#f?*|KH1Ff@f_VXI8CI+e<xVdG^udIU9e%w(w_IZ-tl4xmD=;P($3H$@u9;+V!!Qa608)D0Ue`30yH4S~2X@|upl>*VDZ??Y@qqch#}7S7X`x2beaZb3|7T{&UKOnLC&CJa}1pz>(-=tL-ea;%|B!z8u?9(7uP!JmZES<?B_Q0Fp)XzR{f<!SVMe)xU)#rpvy91_m>;>Eq%NqEgSfAWxq5e^^-?Pnh!m2bW{t;fW=42*-bW2NRJ{^u;ZO!#B{q<y3igND93{Lb!HC4&&ECeCP<@za}S?35Xji=4}b?+zAM`fUWqPXH1eoiD<^_^%V0^z)}IxHn2VAHYEdO#%_JSZ1KqIErO90H?HXTW^zdoYNRPX}VO^H|Zw`ZhPkJZX|kRw1@XB8XPzd!O<Jx1p~*~e2Y#p+OVIcjhc8&0;jYYUfR%YaDzR2*2(5=D-~i3L4>>l=M~~UR*AfhR}$|HRSg*}i<ez59eNG2FVA6Ne<I#75%FGy3SmWcDr`Vq@JCjru;ch=BAEJ%J~#>Um{b6kisi5lJg`aYjP7aQ$mpaHN`BL0p7ZeskL!oX_ue{;kiK7@2b|1PHg8=n5!~B<a@Y=VJTwZ9zAuFO<H$0`5gMM~egTLPC*4RJy+T78I|kdBb7O>s%O0YRy&Hm04tF3qW~b7T6$OB_9%wAMhITmAS-UiXgN^BGUpNTMIu(rv>e{<TlO+!Sc+ndcU#|%#r@1TYN6O3SLEQe_Gker|3W}ZMC^)mU0r_&T{2&ZYyn!vVw{`ZIG~Am|@ELU3Y4g?<dj2af-LE4ogN7QY=NX_JS~_qXG=xXL?m8(Xfy&{u6_SMOvs9rj5^-H7#f;@%J~?LIrQ7rw(I6VC+z+z|i<Xcpo6yOo&6y(;X3moFGp?2~Q>Mw-sncZK^ch+<O_-u8t!<J4RT%zP50@@|>(CbE+6L^|+jp#z!-u!XqNUg4-R!*rY5gH&p*>g^bipatTq6t6PV*LCYf}~gh;>W|G$-QoqMa!Ns7msC#lf-U81F(697unSi24Zw)sDpRB54R$!H<amO+nER*}Z$U4&ivgLx(oQwg<|U>3xDmZyGmIUVh%-dGjX^%7R7L#lb<2V_*~o;P6LFd=WzFp`lm_bR3<ia}Vgn^=+s;p8pnXJsTqcHkuc0n!xDnH?9>3*NnRhmf<J~(0%*X%eklSmZca$aXo>()C+Zxh)N<DDNgD*E>!V7JTz=njx-tjncwKh)Rnp%D*4@~u(C-i(Yb1n%hZk-FV&4>WZ>XYQUTR8jzyR@Rl*^8982zJ-ZOsM3_Yd=G<bG(Yb?`oD1HJujCSI){^UpdCA+KDrNV<_85J_n=)TQ4J5PA(MoiQZ9?v`Q;HDtAQF!<sx=iN*G=vE6-;Nc~p0H@b#Y(rz<`0Z`Ats<pZn?p1ij~VrH`lwVDKnd4;d|t#KYjpt$;1Gh=Gik9ibMrxpI%GB(N7!(j!*X3y9j`vunU7jd2pByWMgy}2P_1Rzn&Li35$@Rya0FPwYDJHRB!@#5ccRkZjhjYyRhU`KEGryTDH)7AL|0orQiUTFgOZIYoX%jEWA$Md;75b;S+w&@ISFQsz0+}o%!uv{FwYH_J8&tM|F9_#$^T!+>+4fGTxIgsN14m>6Ay{PJF+&kvC;^wkZkUIoaV^H>r4E1IWOs1vq!@UMKtRzg<851dc;kyj+LU5^6_x;k<!{Ck;_n@hN#F^3VetbVif=*+^HU_f|*pPNBy`UHjFcw~UeQ{p(wR<Fo$&oK18bjs|QyrGGIBC(Fn!lB}*(7<q6M$Il21Q+z=>&dLCs{#8wqS74KZJU%_ANJk&h{8EW_EOSCH!?hD=;~pG{kUR^>c`fEk?cFwm2jI|k35IhT9eNTHw=IAMCBNld;y9NR8i8NG`TLmn-#H>5K)$@3-u~%9`QeNEf_bs+J69PrUI4+59yJ0uS2=QIYXDAmCj-Yqn!%&%tPgI(yU;}lkBYzBMj5zGAO{bQ^=fC04+z+pEFCxmgrDsR40|-^58AswM^$$U9qX?V24}`K1`e;|!Py9Kd?=(2?BAf_=M99p*I#`=-o(qkq3bQhO62+cqV2cou@KMW`ER^x`YCks_??<3B=A}B>~tCx06Blw=At(6XRKInpF?oWaoRh0bcE?-qb>(eXq^*<n%e*j!b3okTML!0KTm-23x^;<uhk)W_Ej|yMym+B**&V@q7X~&<1)&;o;A|BuufjMU>_zG96WCzyiaR*2uRp*a=YQVxsO5{X{pDWbZCus;JeUW`Jvi_6IR@L01ai}gc=_gAq;dF{cAr~6bSY3a9i*jSDq7qW9r_&F620~-1Xv)vynf{R+vl#hd)5#sN$pd9+6+Y|5%&)_=CsfHy?dp%hvmN-bcT{`4q0hnP(2c{}pi5WfT^MDRc}vjswTu-9bV*Xv}d8oWOA)0z_EC01+B59>=_kzb&?8-TszJmkENaV@>EO*U-<L+il=*RK-RQiQndek|3Z{9y++mz(Hs0SWt^?MH-qsXbKpYRa~}wmEwEp<R6~3ZEzesVQ}aK9vuE70shL2ISuLNey*!qgpQ+Y*!kXZLf{}d_WR?>F@FbQZbKE<43n}!BcxC15b0CWApNRFNWaSAmx|jjqu#}}(zjx$6qXHvhDxuJA<_%iQ)pBMj)kgHdD=Auzk;WBMkPQVo<zVw5gKzBS7M)c923C_g(@fvPFvFbIFHZ7KRXFS6F|g9#B*xN<M8aKPuk2eM^^@nhs8OKFL6BO!TH6{j!6H3!xSb9PX>vHM%~8UL(33AeE&<~q3Ae(N5LT|gn&RO049!}m;mx3`sb%~37sQ=upEah4o*dVle)s+zd9=uXUwpDIL3p+sdc~2<lP4^7wXAg1eb0{@i|Pk?2o4lvWEuG9z2r=2g?Kp6;5!TId3@*e>(9ZMuctYrB-_WxxG&JO7pd|abJU}H8^bn<K;tI7#6;xxsQopX+tVNXk=__364S2S}nn`54UvV7cSf*FXEYBy14gS#bcjC{`dH!TM;h#n;w3%^T0TGTz<p%H^&JY(!_@JziH(Q7%Xs`0GxQ9VvS_r@R#{3R^KG6*DjWZrt!h{7U1YT+<7b=kO~SK!$V{1w#~!RT5LRm!wS~x;aTl@ys)m&#N~gA`9Be7!YO`onR)Hp037Bx{5ghA(N|sGaZu?L;UP49CZ2CUm~sHI@d*^3TY=zq9LG5_KEs{6)?5mUD-9f*SUvpkW_5f%FF&ZZewWMXzrQ&z|G;^#ytGepk$?H;P+0KX-f0LwoyUP=4d|h{GQtU^O0E1LM0sf11P5ZHUD9wSg0y<wVrd#T$sOaw^LZUy(*xoiCU6^WYYQAV>e2t}LvV0ibsow;OCYx$*Bm){x{RCNEaPTSGi6+}*VQr>VmSfp;~|zR97j!r3Q8Mwi2g5w<DiLygXh4z8!&JXNF4~<Jrvex<}NE%FGAfdk=gU-*nYf^KaTPMaR!;-G>#lE<0ns(ag(OVWWLKZyzkVhT8^K}Iibsl`=(BlF*w(*&G3d2()#A}Lws&R6n7j44%Z2emK;T~VOxXa;R((`<KSi<6qRc<R*1>Dg2KYmmRU)>p1Dd09IrOPVG?Ix^BR0ne;>Us%hn=Xc<Ds+^7u@#&D(e}L1xK&1o;ey;k4&gA~@`U`f(HRd>c4g@mN=gJveL}!lRHlah(n3*LB$xK;o9|$7@(8OsoedPH}J>C;oI9^^~gD;&vYIuH%<O_qaqjSI@(9DL8m<Mxh|b@!)7fy6~afxU7&kDKyy5Msp1p^lHD2;<oU*7ms(7fI5qeZ59>{iU1Z@dY}Sm=rmel6vQy)D;u)>0RXvW`vzsu@Nc3G9Q)Leh%guj$I1j;Q^6q|DBA+Y!^8^YJA2ppm%&lDMPuN6du|6%NIu8Wq}DfJUZ^o4?(?H6ZCnRU93E`vb+Bw7o87S<6fb|xU>(Qlv0-65VaGD-hPnhCHfR7zcsV2mK*4apP+B2j;TXza-(5Q>-F}}#=>ri62g+r`lY&#B;lYO~eK9rwU}ynRAWK3G8UshaQ7JS|xW77%tC%*S@xr;9=iqw!B^>TYcrFW$D+6%w&I(S@NUp(r8E(*T6OTnbhN0298E(`4<}w=kSx3RSykAS%Pj7h~OI!D!D>$U*HnttFX}>vUBRX(wl;d?NG?bm=;P3#s3JI1WLg7nWHdw;aIio25LzDp#2c;D_*l%CO2Lc-Ymj^yCUc&c8yp-O@E$cd7JnTT;bqGxo03akua0-?RPDfj2?$iPluIn}f#*5eIb16KR1INp`j(=|jJy5s--Sf8rPv9`Yy4%LYm~{cMk^L;P0u#QjFL`afKGyZ#SazjBW03Ltp#lhTnbC;*4IDPIcL4{CFXOq)rQq0ngDDIOhm%@4ye3P(4-eJixUg`X&Jp}Gmx1)lIpjl~zHAG*3ZVFtQMikj#%5eU4i2v4KnWb@pMj&x4jNzbI(UD&BS#x;0z=Vtoa1=l0$^B%8`d|dUk^7b*5l%SYiRE{9vCet0Og%Suj8*Blng(%tgx`86JkGqb-;D~6#|}FkHdYqo$VD&0J0$hr_p6VLU7uEN5R2G6$EW~gC!1)xmQa-2$>zr8>_HR2z0)PP~ZVulp*O0paJ=lNrou?mRMh=1uVWXOy)A!hK5bXHRv*4{5`LC8<t6Q1AxPQybnQ9fbc8|4a-YpA(a(R*SW0YcyOEuOG|hlu4^M&Lt5juRNyczwqc!h83raKpPLvYJlCDi_P{yudpmgO%4l;Q&pKy_@*kDiE<7$NyIB4|41&)`@`Zs>00000NkvXXu0mjf",
}

images = {
    k: Image.open(BytesIO(b85decode(v.encode("utf-8")))) for k, v in _images.items()
}

# https://stackoverflow.com/questions/54624221/simulate-physical-keypress-in-python-without-raising-lowlevelkeyhookinjected-0/54638435#54638435
user32 = ctypes.WinDLL("user32", use_last_error=True)
INPUT_KEYBOARD = 1
KEYEVENTF_EXTENDEDKEY = 0x0001
KEYEVENTF_KEYUP = 0x0002
KEYEVENTF_UNICODE = 0x0004
MAPVK_VK_TO_VSC = 0
wintypes.ULONG_PTR = wintypes.WPARAM


class MOUSEINPUT(ctypes.Structure):
    _fields_ = (
        ("dx", wintypes.LONG),
        ("dy", wintypes.LONG),
        ("mouseData", wintypes.DWORD),
        ("dwFlags", wintypes.DWORD),
        ("time", wintypes.DWORD),
        ("dwExtraInfo", wintypes.ULONG_PTR),
    )


class KEYBDINPUT(ctypes.Structure):
    _fields_ = (
        ("wVk", wintypes.WORD),
        ("wScan", wintypes.WORD),
        ("dwFlags", wintypes.DWORD),
        ("time", wintypes.DWORD),
        ("dwExtraInfo", wintypes.ULONG_PTR),
    )

    def __init__(self, *args, **kwds):
        super().__init__(*args, **kwds)
        if not self.dwFlags & KEYEVENTF_UNICODE:
            self.wScan = user32.MapVirtualKeyExW(self.wVk, MAPVK_VK_TO_VSC, 0)


class HARDWAREINPUT(ctypes.Structure):
    _fields_ = (
        ("uMsg", wintypes.DWORD),
        ("wParamL", wintypes.WORD),
        ("wParamH", wintypes.WORD),
    )


class INPUT(ctypes.Structure):
    class _INPUT(ctypes.Union):
        _fields_ = (("ki", KEYBDINPUT), ("mi", MOUSEINPUT), ("hi", HARDWAREINPUT))

    _anonymous_ = ("_input",)
    _fields_ = (("type", wintypes.DWORD), ("_input", _INPUT))


LPINPUT = ctypes.POINTER(INPUT)
W = 0x57
ENTER = 0x0D


def press_key(key: int):
    x = INPUT(type=INPUT_KEYBOARD, ki=KEYBDINPUT(wVk=key))
    user32.SendInput(1, ctypes.byref(x), ctypes.sizeof(x))


def release_key(key: int):
    x = INPUT(type=INPUT_KEYBOARD, ki=KEYBDINPUT(wVk=key, dwFlags=KEYEVENTF_KEYUP))
    user32.SendInput(1, ctypes.byref(x), ctypes.sizeof(x))


def press(key: int, interval: float = 0.1):
    press_key(key)
    time.sleep(interval)
    release_key(key)


def found_any_image(images: dict[str, Image.Image]) -> bool:  # noqa: FA102
    for image in images.values():
        try:
            pyautogui.locateCenterOnScreen(
                image, grayscale=True, confidence=0.5
            )  # pyright: ignore [reportCallIssue]
        except pyautogui.ImageNotFoundException:
            continue
        return True
    return False


def run():
    con = Console()
    with con.status(
        "[bold green]Running...[/bold green]  Press [u]Ctrl + C[/u] to stop"
    ):
        while True:
            if found_any_image(images):
                press(W)
                time.sleep(0.5)
                press(ENTER)
                con.log("[green]Restarted![/green]")

            time.sleep(1)


def main():
    with suppress(Exception, KeyboardInterrupt):
        run()


if __name__ == "__main__":
    main()
