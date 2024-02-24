import ctypes
import time
from base64 import b85decode
from contextlib import suppress
from ctypes import wintypes
from io import BytesIO

import cv2  # noqa: F401
import pyscreeze
from PIL import Image
from rich.console import Console

_images = {
    "ko-1080": "iBL{Q4GJ0x0000DNk~Le0000?0000T2nGNE002dbc>n+a0drDELIAGL9O(c600d`2O+f$vv5yP<VFdsH010qNS#tmY4#NNd4#NS*Z>VGd02lO0L_t(&Lw#CjS5?Wj<uAPPKD@r&CSY*LIp;7yFtu4RqZklT$vGS(ib~E|kQ@Y?BpCrgMMM$WHet7^&Dw2i_kDNV`DX0{w)e~XFvqH0wW?~ZxmMMw+WRPJ?>T{`Tf(5SH3CaE24m5NAS~MwiY0{lt{5!c8YV$`YbchvheLT=I8=8=L2Yjw5f8O}ghxDdJQAR>>jczy#zJdP0(AB#K$p<k%kkMq%OjT0ajcJnwr4!FM4M*<WFCnU#2D&(#j`?ccqUTD^EpnEOWmWOvHJw{JyT$C@Dz~()m?Hd+7belZIMvsyfU^6sM9C4-Eu759*HGvTjCypMf7jc7W%j?iqEXutnhKsrXVP9kHBK#?;bfc_r*!jqK%rITi7q#6$cfLud-7PCEbI`EW}7gX?Z45nU3r~DH*JNC<WRFlA%t=G!C%sKq9m#HTKh){Yg-xjw+os^h(3V=rU}I5h#c0;S9+3C1V*$m9eiT^|ifHpu@TJD0RI~L;LU<=o~r?9q-f7@;U=8meomw#-UTtB-9Vl2F|bP#X3>H|1?a!)3Gw75UxS_SQ%ObBd=7*_9jZ>%V>)P$+kq=%X-=_ph3U14xEJUfm6`uJo<;uK<}VJ>K>pytW(_;EA^9nCUiKjHf_*7B>JBu2ZDzrC>b10hZ+?%g#$;@=|~z3k7UB^Xco+m<-p=tE=+u~VBnnz1D_1&`J_VsSUU9CPtPZfj;6xYCmWsPQ+V^?B}&>yV16{4PM?7a2{JsM0b}1x=u_9|XeKO==fc7_7v_{E?5E|O2A!iBL?(2O31msoJ)RA9&Y^iU4ceSn`%pT}eR6Q)?tQ#^_Y%I@%`m2&8YEl)IPICYN#7@(b}FPE$JRfbPWv(?n;ZfPusWg?t0GFUDYil?uM97NwQn9wsAu3U{38e6snDfOdW6Ao`p7_Ok{400WE7YW4Hh)0Y)FDE{qnIcrUKFB9XMIrixeWPs0|xq&(YC57|{`JI;QWRBSDkdWJc$kE=}N{|NMZe-f@Xw^&^}xAP1(Qg)j*&fSw@#cpm(6Taej2B#mnwP)K6(p%+9MOwbkqoq&88uuhMeq#slOT{^0BR1jT&8}}Ya^Bl`+f+6S8@y&rjU@i=U^I^!ohN4X9`erjwIk582$JV$iq%{qoYy2kWo;}8sm(TG2_t$v-`Z>mK-$BFRHN=#)V@+h4G=~BG(PKXY&TqtVb^K_*e;&uog_2oB1vKf1;qd}k2NuIOr}c|bU*orrZy-P0MFWapOy~y}LqDVx+J1$wAgW1}(5vaY0#jd35?BOtc@@lKt0k!)R08vWB54evcbSIT2bYrcV(5ib!X&1KdUY_0u7yzy5nTg=sA?Ef>W5cC&#wel0VQ8-JD$@*!g3)a%wwn*Q3<1{bJVA9NEu8x-}mx!h^e?plAhq>A8+yd$G7<L(Husn@1XnYEnFm?ym*E`|9mfvIW#p({chOOFT)@rybOArTQ{r{`eA3G6I=!*^VkOH1y{l<s0{MT9;u^1$CX=*$|a=K4WRY%lvMY}r}xM_KMd>Oau|iuz(_h1S^>+zQdIX}m2_$cuEB}}8-<^PWqc#7lA2(d%xs9Lf+hRKSNBSK<1=^Rz`pvybW+|3<GAxMO=y7`VG@5H7Kwa5LByVCJNpM!z$U1iggun{`{uR5G_V{p{}SkvY)L<^NrFj4HLOC)kwN=~t{|$YeGHzd%~&h1W@3~w$R%)~&W5;J1QxX8hq0TI?(^5bBD|~%Hlb%>8d(kfSk8TdV-g0mQ^`n75L$(OY3K3ow^vf9sy;d$z$p2a!iaET^pZ)OXcO3%)&eUUWf0Q<!^k>VGDB+EN3_)qO~NXy3WjvlGL_NF=!H#YFO1?8eG+Q=CB5;PdvK;fMo|qgKG_MAGrh1(?~!17rVp0vXL`B^7JN2L>V!dL1FS>O;l_OhVSaSdJd6&>&%+>rq$ah(CcTgIT!2+%Ej%+?@t8|btc<j#VK^~>hJnnKdFTcZ{tTF3IgAOX@Cp=mj7ekPdGs^Z#Wlbpf(ao4medB5<TlE7C>bZT!aAxJN%e!0^0l8HVCN}rsNuEHiEM;!R1>qQ8sDF&#~7UyI>nviu!*XJd3-Cg;R4J<&Y@=Ty3|&8>4u^$xeNArW3VqAhh5PaEK)AQCb}L8b&7e$XYa!~rk;_z0JH2-SQcD`UCCA0mnvXab`{n|oTqpk7P%uZiTeSz9Czx$oYddHxC@rdJmXW{u+ATaNm>ug(gt94vIln24Rl_yMRZ-8fi>+j3U7d}ycGs<9TJR_x?mXB4t<WR9nr|WsuJ!g&A9*MvD7cAehAjlb<mCPfLZ1c%rl700VtV}Jx6&xx+Z2M#nNsX8c_?wgib0B(~uz!-U-X7dc@WZDV+WBK9(~@txjHqUP1?~VwzA(qC{K$@Dyxgn_-$U0=x2?a5y&u`*X9L>@sXmv>>rwu}lPEF4VI~W@Z&l!>ar)oa*kuvGyJuY97G8Y7P#yb8xJigLT;*n4TPhoxJ65!b*BzMQ2SiMy2uX&fbDi))<Uvw<C$1d;Uz)i>?}kmB_-BewgJj0A)8}dv+SO6}MqcX;pL`#%Bg$6x&9>>rgqM2z*)hHP~<*0|vk}|0->~2J7N0P_jJLiyay5c*?aa8B*2@t9Tlc%P3d>1c$o&Fw5f-P3(YAkz)UO^WinNq;<e1bpS@`Bd}##{pc;Jt$ySt9FsbjUE^?I);JYjgHy=_EQ_zhfmxQ+bXn3Hzw;2TCpkv`6}YrLgY(6=u<Lk>m3?opqW2Bldfvdb`>iA$TAwk?uEK#!V(Q@|seeGl0PNEGVO4X7eO|NAE7&#v%xt}km8UvzYwl-BFT839Hk{YI>^7WQpAygDbpA1%sOv~Lw>*Yr)g2gTj>DFIm-i_MYZ<={`x9J2+01aZTQQJMb$6j;MRs>&UBu@<-${yl^BB3zQP?y-#`3<8SU&Ix)=f`YH-=3aJ$U}+g`^i$JqoKdMz87~>{I*EFs8`RhRe6%QG5xzOGe;XJ__HOakyj;!Lno$_H;10MX^-If11Mz?o;-4GjO~18S7?&6*qx3w}J18m7;u$atd%A{{-8bSvaNjVrrg<pqgPga;ZD?JjZ(W6@A<;e}rw-ESyt&(0fy{eVqB>Dx5P0;n?s9uKk~}V)S2FG5i<YhW>)<ppgHB?S<Fe25w_(?f_<gRxHVuE3>dq<|-@WlD@!Tbi9LY`)erK<&MK6U$GGj>?!DnZOIMTb-$w{bYcQ<9QXjcid)!}+lNOlpG$h7b)#@78-ru_BRJ*{qMi{E^`Ab!!|&oJocO>Ex9|2ntYT(bSC7HDxF0F)3c{}3o5SkDUbuA4;QPm)vH2~q@eQ!$9kBHSC9(B4*714m(@$95I|~=;-{giY`iC?Q!?k7%D<+>~6Z^Uoo1gpzmyuuKSU7~(`M}(L@&rCLBXFykfLq5stQ>iPRX09j)zlwYF-{*ZKIS&?BbFD8Af*1XlsJFThamQ`$r^!K(-XLi{ToiB!0NGoLCL0i0>^4DNoNs(?Ir!Nzc3A#*$-IrD<k)s5x)N$9DcZo4JCaf;k9Il*SSF~Zybl~HAb%TZ^CXc1BUNBzzETM`z|U*Z(>VnAJcgpE6e(EdVVv$O2Rgk^uoPo21kDV3||ry@DcDONg;m#;Y0)x`3X4o;uG~|v5v$~&l48GU%vJAW7s+U9KP&#lsNS9-`M)#HC&snV0CU6I&a>QbjLYYeCJhcV^*$dzKT^X6IgX&5^K)0Ts4aAwWB!0rTFoaVwIJ09~S+s8?M84g4@GmX8SV*lx*uJ;mQ5rcV>eiY)|<BoSG)!eCHk3Flyfut`7uZQ`khu7YIAdy}_kn9Bvcygk4b(Rx>^gr>u6^6OP&KT#oH<Bhk)uVpTZ_<1ehx6NIfVC1K1QpBJAINQZ+-P!MGpNfLw!vZ6n;?$sxFT$;s361+fII5TW*-5A_&J;xFD@sS8)rv35(Zo?0xY(82u_=U9RZ(m???h*1YO(CUc0<m3Jkx7zTC+}e97sWCZr~m4)TUeWakv}9nZ(e4$-v0zQCeA8iEumytK84M>y_ow|@vGupc?tIXDYqMVftB~EI0rc0_`uD75=W{OnfTXV@3}wq!}{DcI1fL<@-mTO(^7vS-O2}H*D?v~^HU`H7M6E%Ikin=W%&?JeZ3?Lda;^q?vFlW_X}X(D`4+S;2?u^kV|ntrNGAfAF;A)7Ax|5aciEi(1u~G;xb>)CFw~WPcCN<_Sy36U))Mwz^(U3ZWTRPm)C`p9aqqO>n?ugcCv7)U%)3mzkL4+jaO#i$Cb7`y%RP?!?10hg~RxJIRE%>xc<oHNVsudRWi?J`kwCMCagFRR$byzfSa>5f6ko-xakl73A-llQ#^~5^eayM&$#isb3d~s*|u!6<)&ZD&0e%MjL*O+djR$wk6}OX3busf$XnQUK7v!hB_v-^5H@~y4sLn9aBR5^*U9%-b^9YX{r7O2e8)ZJ4VH5$xJ<r<%itrdyz~ez?K5yC!CyB0Ivz&L$KW*l9IF{vml^K0H<$%?>D=`H!eQ_we*ox9HaGlJo!roSaG-P$iLF<V*>xR-y*CiwJdUV_G59c$+p>9nOX=ppc?8zwGq7oS0sFo`h)=ZPPdN8~;*Z83P%=mz;(4YOsq>Cpx%&{?GWm0#eF;|8w_(%p6U)PJIoXEJ>px05X9xJBzyqsA&KN9tuCY()LhbPUv0`+Z#|Pdy`BUuF`4TG!f5(bJ{(99ufCEqPN$2MYV}MrhCg70EAC7`6aO5#Wz(IgNL@otmaOHvZ``k;+l1o^d%PrvaMNBX=MgPFcA=vYrXj**_wq0*XDzk9lcewSxhil(^9z~wQHs>;S<@KSIfiCX7jvd+Eu!wJiC2s?kJTjQ`TxXTg2Cw2?R1DrgN#7*gQaWM91Gin{1K6Gag+~=G%a$i_U|AeRlyrIhFy_H?Z&n*Oy|<DvsVzJV#<##$oRgS+_VLY#u2!7T#jl?i)7*lS8K=`=9#Cz0eW)2y99-+TVcPHxXu(OPqd*g{K+X4HQNVLf!UZHYjY@jc%#@hA5kzn!7KmoX2sH3K*EBXw+(P@rEc$Q$gx;w;IFR2Bm&8^QrdSC9<$bW>mC87u<hJsF+r)r0^5EOZJ8HvS9)xeeisvtntWHT^z=Qj$1&;~_DZS85x(FS@hG)jmiax3R;j^c3=7HRdXH)ai37DOof_3FI?5cS9u4dMqn}(7;C)JB?ggNhNsm&u_2G4C9LqugC2kS+7?^V3zVO7+h;;)kfFWm+t*^rrJl-wa*A^yG^O~O*#5l>y@$(R|)>y1U>Wl7hXH;TCVtI_`laU2nN^Wha<zI!3PZP=Ib1DxayxcSx9$c$GlLk85kc$By-!A78Hl(&?ASn%S!C$06%xE|@PFq1dawr=Q=OfzP<B~SAqW!+NyL(bzQuj6&E1%|1-|8i?FBP?<Td2k+pX?8!9v|}5f&P%Lb@L9OUR3Wyi4?q9<^vfg*5I?!68i(K{UZVt8Kqsb=*QXX<etAU-t3>sH;__WHI01{W3f|jzsXxO^%%o9SJ<#Rl+nks0@Uz_#sp67e`xX3(IwklQcOsS-bUE$tq=ScZe!%kR8aPK+!=8bfo!|8Ri#lKuUIlgDgU!=ArMDF30w)-JN;68+$SUkU)AYrMJ*m91@j`7BLsI08+=`lD!7+nN6j}K2=@U3dRl%5dRzn8YgoK-kj3bQViR2b2>BZDQE3^XYz9rE0Eryw2F?OXiqOkok>PW)*(Hl73I0(<wCRq9x!+`DT0cE_Di#G+e&?Y$+LI3%B$0E24dL+j*fd+CCljK%tN7h3>r~+mIr7-0<#(pI*=9~-C(7#lIiGSIAxdcX(y5jXsKsk&8%VAGDXC5i8Mt=EiTotrCxE#iu%O<=M8x!lX;VZ09s6}95`xnBF=3Kz~_*$$ZHnDwULLJtgs6oQ~E2q1^{EQtb4b-W_y0}_wpcG@SimibK=Q4<@;gXCfhfY`tRDBDe?41kQ;auqW<iq%A0SvseVSFr)D1hP7d}tiWgUXS7Xa*ERKdc-EgtlK1Ec}b4H?3a?W4m?`Nr*lNgXk)v8akn8p-!?@eF`As*lIq7Q0KTB3-B$1CW+Kw&@@PrCZR!nF^)7=U@@#Hzr5bbyFl_wAY)%mpIkVGl%Z$hHXb~E{2!Pj76|*g{^2}k=H{fAiVHg8m5|s17W71WVH=k?ebhXj4<((T0%!%~K_eg+>c?}S>Yan7UYSrilnLd7=~%WuRg#N^Je)yCGodS9AB$JYlp5llKXI;So-k&bnJ>vbo(J8KV(12!z#xPOWd;WpLdQR!SyMpCc?k_a1vJHL=%6AAdco{RX&782jiDXLItI?lukgzoSKpi#m@>#3Buo29HXLb7|KyDHdgf~g=M~`d<9U45evert;qfoh+gAahzo2)M0ZOUw<6L==9m#@{#<5K4V}r6!DxJ?{^wS~p$$*M?I+l2z#3GMG35)k8k+_psx<8RJ8Jg5n^E!=X`%+-&m5!=;!lYN!M{^)!o#wGDXdTOzK4|FsWkJvPZ>i_UdP)JIqr+!C{~QTAet$z(NRFfJEk2;+k+A#HJjb(|VeG?s4yHnvfiyat3G3szu=UHAV8>vHXKVJcp|dtDFThT;Gf4K-5fHiyWzpBhFOPMKG1f$sVMRE%2cIk~*_TYh4xfV7;nPqTpR-7SOnm0@IwMIH&m^cHJ|jWYi7!i<)KwLq*Y?HZyKPZex;qi39IX0l!j6#m102Vj`rfHr;^HfeLTVE_ENdT8JZrIC^RS{$=NR>lvre?LEFkJMkDP%v=eIbf_-Z8P@y{V)45~Wkk?l{BKEtW+qs_Y+*j<TIS;O-*v<|R8p}wDfc+xM{t9qnBZQmKTvu@vMXh@*F)R)F!yU>yCJq2|_$R)etv1sQB5+**xN*_)Wqz|*I9tj*Yfs@KfN`gd;iihH(tqRNHyPpK=FY^%kB+NSlC2hl!BMk#rVC<DfeL-phv=1gi$4h+gOOl{@kU==0fcU(pA+l9Kv=LffiZ<E)B(}}#i_d_}c2n=HFNFDJ^H{@qWcxTibyR4#uw~iq1T5W2yY?hNg%DCv7l*|=VzFe$2`t(!=kp0Dvwqp`cqmIcLdHvS(T+HL=N^M^x5@DjcR9Wxz9p1*#X?C&VpMj>p-!o`lX5pDv3PSZly^iiVnQ(nYHU~DDP$~EL?2?=ju<T49t%T8FS4i=@{%^lOWXK-8jH5XN@Hp6l|y5X99oo`9tx?#F~l4yyM+{AsZT(4mqIR-mFbWwp+W}*)ajfV36ht!BOtpOJK`!h53_)Fh;fB|ntK)FsuCI=v5@VFm83c$)ze-X<<e~tv^$FJa>#_9q(k2cVXu&?d+00M#Yb-0y#K-vB{la*C~uCCAj-1skyx}j4BxHyBWXb-h0D%83~HQU@zzi*-5NfRFsN>$?xqN+Y>S2Vo+Rk(VW#Y2=ImgkwnRXE$5+@H0U4!?Qk0jvhhs5ymbphkSwb|&iGk|&zoEuJ3W)NutufHxQq$%fT7<4gGL$**(yfssg4iy`S4aW%U7{Q*{f$8Qq(-QcC>74TXhR_V3zD8iA2s5OeS`+f8apGQA?m+^7(+>IO9)gqhd_l8a@nR}EaqU}uJXY*u7|LAoj;av0@Y2SSiCV1OG)CAO(c?1nOV4aV+j7SJ_P^0Itbsa4aI-04#xki4Tj2=V94Bqp}tK48KK5!)vW}jGUr{w`4(*o!M7Y^$>wm9!oax;rx-jsEg;(-PGi}|_C*^QNP&&vlmemBIEy*XQrf*_Lok+Y<lKB-ynf-Ceo;q_!B(cuw`-2!o0UiK-S>WcCTUVz2xPQNMw``y-Sbi^vrR}9`l`Am1pfy<)}6w=-m!rI0000<MNUMnLSTX",
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
# msdn.microsoft.com/en-us/library/dd375731
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


def found_any_image(images: dict[str, Image.Image]) -> bool:
    for image in images.values():
        try:
            result = pyscreeze.locateCenterOnScreen(
                image, grayscale=False, confidence=0.95
            )  # pyright: ignore [reportCallIssue]
        except pyscreeze.ImageNotFoundException:
            continue
        return result is not None
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
                con.log("[green]Restart![/green]")

            time.sleep(3)


def main():
    with suppress(Exception, KeyboardInterrupt):
        run()


if __name__ == "__main__":
    main()
