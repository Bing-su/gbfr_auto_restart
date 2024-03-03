import time
from base64 import b85decode
from contextlib import suppress
from io import BytesIO

import cv2  # noqa: F401
import pydirectinput
import pyscreeze
from PIL import Image
from rich.console import Console

_images = {
    "en-1080": "iBL{Q4GJ0x0000DNk~Le0000d0000R2nGNE0RJ17;{X5v0drDELIAGL9O(c600d`2O+f$vv5yP<VFdsH010qNS#tmY4#NNd4#NS*Z>VGd01CKCL_t(oM{QU6SCiKk%|F!Ef+2*Efh<A@la^qex@ujoPb;7xV?jlbNdaXZ!VqS{kPzlD1Q5bl2PSdCk*e>tbgr+pU8`%q{e@*9wm<CkCHJ21+<nfy-?{sUqzSbU$JJmjAx*4-B(4e`F=hDRR3XGM6_6#>!YAGUU*XAl?}Tc2$5%rfTLtl113dZkA|z)y9%rCUEq_<RhkieZEW&$V6vFdN8N4{Q{Z1u3=~o<E4hhG-&y>RBivozF3gH!90&#Q^$4WR?3XxArBcy~Rp^gq};d#0OdkJYg$#4PRFO5*1Z+1ErlcWHjWFyBL;C+^4V{5oL1Bxah%NU#iiqt0B)I&zUKD2wEBqfP;5GNSn#dRbM(u;n)<EyYYrWEg;yvo2T;Kjsv#a3`#&hfWMp56utoq5I8;&f>*qDy-Cv?8j+3Q3Fs@{}fcC)Ywsl78v!P^FuQHb|4|5lqrirGkC06CoFx@If@4pKFBjVjE<f_r1`9J+Wo*;cxHMW=Otl;y4qMYJ{BdJX?;vXZcPNGtb@eCUKwSI{L4LNPXD?UoPs!sB+ru`18-7op|%+C&X6tGZTE_%X+9YJE6+5K%QxaGRF*YVgrJ?@LPKU`iwSs#u?#3=L*^>vd!>eFp~34P-dAS<vIf7mrRglv_h8Nf)AN7IiHdgBLiq;0L=IWX8c?OMB1W3_|lOip#j;Zaks^m9zB7I+ahdxKmjvTG7RmtA^2Y%ptDwlGK0JA^_SYQH@=<(I-t()r`;eVB&W{ngWr`t_~!ILkz<7_x0|rgj=PrD3?+k*WtbRvCw%Eck<|ftMmt1772{Cm_Hx@=k<&imwwQoC^E9N%&2(x(h~YYP<r4@l8)tM~B-i0)8<EuoaZ)o$jY3;&hyS$^_-0$7Eg6UU+9(uPN1!MehU)4t{H_j>c&GEJxY7$bp|~srV1@j0kMk)CH7>xvXq+kSAh}7m#oi)Z*q)1B2&$feu4bOkIc`Ze!Y*~W*+pbqAWk(QpnMv^v{MVDN*GMd0<@J5s4E=MRyhz*ISpmWB+1&KDVu<%bR7OAcBj2x(b)Fy;xT5<xQIZ*JY;DWWOq!tE%p|*!;6rTd;k{;ZCl1Z(+Z;;!v36YH#_}henb~72x`2IFw+_W8*d?~c?H2OD+sJzK!8AwP#2CdQ-e;Dn#vgj)GQ*PngI|2m2(VW9$Ld3MEg4KBBXJdhqNC#T@JU!b|c3;16BSgbd5_0w?2j6wMl%$t=MgIpkM&fY#Ty5A0fPV6WZ2wgmpcEreYqdD>kUI`}tAzAuO*SLBjdV>SvHPW@-k3b+;MBI<bb3);kC$M2E+}Ly+k%7q%nUGV5CC=hxrEe*2#5|JD!RLSM|YRJ{m&?{nvZ;XE&I=LH-p;+ZO(hJN@v9Gv_GA(m&*8CRgn8%288941#E;@AKEfZyNzh|O<aVQOsyX&tjX^EPhh6oNZ85XPYP^?vPy=(FX&5ZcehN*&1UUT`h+2a(?Hp2_;jWvI&>2(dC7^|ugCvb*OGm)jB0a2xvBU-8Kb5Zrkmdczckmmj*>y^HbH4d^Q-p=(-!-oAxH^S?PEI`tBWnB8Jp9k|@*PVQj&Fsepxy2f7r_5+UAPa>@QCW6hkaKP{mxoSJKT}$}n@f+ypUqRPAgT|Q^HyZ(hpLfS>OAnx_x{m#}M>zfzIQ|3>#r+O^dVh-t*MYo2cXFW>LpV?|h^PO3<r;tZ@&zIq?1-=|;1i=ex#Ju^Vq3!b*KcrWXa#W=_sk1hdW1d?mk%Pobpi_;Pu%7cd9L^O-a_<`e<Au8l1l<`a&wCZ(1H9RcXD9{8v@IRkka8^VzT<@ain7!$Lrn6ebHz~)YuZv-Fb=Q)&&#~@AwlC*)WQb8awnI4wjcOMDqPV{`ko?pKhInzGo3J-@QiSpCp&?7jWYFHo3oLj^x5jGtd<GV`A-rYfkuBPMW6h={uSGoSFL<$(@*cf&<Oh(K)}fr89RoSd0g8baVxg5B`HAW2*=%9l+wQ?DgGZ<!GA3i3i_6*iljB_rS4rp1H=qpSi$t8$PnFLfbft6Lll5IRR~Rt2kKWPVUosJNEZ2;lShubhUO|-xW~V$Rae=*KzFjCQiM2gTr%A;a@%i>sNPNHnaC0L1P%l(Zv^tA}`UgyZj&~x1cU}Am^R0Rm}<>Hn4#J(;diIbn7N=yXJqRFo<Gy-u@SG#9)V}WeGvu>+mZc!N!XhuDPPYMW|R{56*v!V;eyD<SVFH)GhOCE}NT=p0XND;iIt^IChWZjyitE{vH<9s}soCRp$h9e%S-u?z;%GK7+j2LG@zA^5bVNo0;{;uHOO<m5xEh`loGLgPgVN-t$e@T!}!AwQT>uOB`MJ9s9bUL6J8G^X#h2=H>=@6pSOx{1``PUPBZy_#7c^YrNP8k!{}jx&(5{jBaRo?Sv0Jg_4<-X7nPZ$z8eZMg(sNMIrA>)<B<(9*piP;<g*>P-gbBmM!7qk(bcX#`jVW9CvnV;PB0L$a#wd3pTb*h{C(p5kvy=3@dUvckWh!obUN|ZqEclOv~JoDadmA;gw=Srs<yrf^fGg^T*)FLM`Q8-7~+FmCbKoVPCElnnF8*DIC-Vqxg&;$nN*!YpG(=c{kV0L2u^u723dqS~>wAN}%kHoiikm^Py%_<lA`P2^aVc$O?uarT{pcXTjqA4L8RE^wel_9tCCbb$DMeBbB9N_k0ZnL{#+%blKhbH%rv?>V3EQ&x`vgPA$Cjr?Ic;D~Lj>rr=*-gHLKZvUf=)ft-xmOrB|lj#&$(1PY)=^QLqXCp06ecG%6afCy?nIgf&d(npp?#Y{<l^MU)hT;`$w{--Vc!g92Ge1zNX72ik&ZH2%otY!wHz>+a2De@%AEx6L@{`Cc>wennaBaoU)TQZ8kk`V?%b(=y3d)A2io6p_s4^i^V(mJ<ACiR{qu?cDKWbdD_u>KH1l>8D3UPX2fbY)`*DzlRurL-T@EXefqrcq2T-^I-8J&fL1LomttoTqp!=!cdNYy&9Kr56M_-T-xSgVV8N<-YU1!#Q1$QEcjHr^)Ss>|7i6L{{QpRy*1!Zv2hZ*o`~LHBCSoTg%o|=pEYOPgSnFHi)3YA&3GfiItbkOldtlq72w`suFunR^a^;rR*=+`kiZm|CMg|<(lEg#>Su7k!N(mE4c|Cr)!*xJKrHZPggVgW~ljLX!Gfpc6(yjtJ2Shv{NS<p-wX5<4k^N{Ou9N_oCPylAL!6dx?w==<=-y%-e=YOWp6!L1|JW8)WvaggCYi9%l@Urq0>YsWaKIu<6ibQS%GGFLm%sZetHy&$doz?`R*x=;PVXUTB4m0R&&MAb_^ARQ9(?4eU>=8B8?;FgSZ$ArQ|qY~tDVNx1{cv^E6NzmD10F$sZe4MZAtM*>vbb6=sSOlEt=hT0>V4Kf>JWm*e+&=#l&rO+u|Y=w%B1o+Ti$_z@lxHp57vBy=Xx5A(PbeU~Xu-%igK~|m<{2FOf4@rC-{TrQ6DYK_YZG?&m(D1!&v~44!4gUuU@a`h@<;F|^0000<MNUMnLSTX",
    "ja-1080": "iBL{Q4GJ0x0000DNk~Le0000`0000S2nGNE0QQSGx&QzG0drDELIAGL9O(c600d`2O+f$vv5yP<VFdsH010qNS#tmY4#NNd4#NS*Z>VGd02Q}ML_t(&L!DapTa{P3<zJb(PZA?=dM~sGFq%Fon#nl#CX;9SBu*3+RH`6NtQ4st^#F(7IrKvZrKl(tP*fDf7Gj&kb=UqVa-7Wl;r_6m{gu7nwfEchyU%yrJigC^C*kq^DPrkbww>*ce8_ed5QUKKT86kLJOzT5!RPKl`B?XTE<AX>Zbt#{i|{tztqUsP`y#9l%EMdRvhnMGWMDn}DRvjbgJTrI#nN~o&x3u}llSfI`4ZNXUpyCc5dA&bU&;2(Z!_^<e;0C2O1$pu=T7<Sw{!kMxt#k+$iC0Py1%Ev{ksf!lGkHfCgk5|OV1TMP7-W`av<N%cDr~^u=ON7*vI{!*;vnUVy^C#>n`*|9*-T=i=>-n@VT4kE*lq7!o}MNw!3-1y9Bb}Qpop~Ns#SfOUT5vbZ=jUC+`J*wJnFO9qU3$;2vCt^~5^L@Zh^QxX?EQG2eUgy=RCGihXvx$;pX#Z&G>g!8UU7z2MnbhPOD6H+NBC+i95KBB;Xb(p(gwc4_RdzRQA##6^x^$`r=fEeuUVP)Wc3dpfVlNdtIL!Ja$wprX<>L8pjZsM)I63P|_l(QurW2GH?ZzeC)gl8ouGQ^*z^)QhAW8^M<Pa+8NvLO>Q;0a;iT<lzF<Qmc%pCTf-t=?Vp(3CJU>p@^!*n^cNNcm+H-#*<hdPPq}akngYN^K!hsw-n0#LRKZz?7x1G4esJuR1NR>T(tY^po<Zx=XEVq?585vTS7Tu<$OlI2+oU~Z%`>R%JLx3dd^)QQO^0>p$exFchQTfI5{~y_msk&hEVOyhj(xuK8h^Chmke}?kkY+PG})Mh_K<4{U!J!){gH|>kyvrK$5)+8^emJXhsnoMNSSym_Q|zghJ?wa8vAWgd(~TvdDTUsWde$tO+fLfmYTFYlm}j2b!UZZGmzbs#tN~L^MiJ9B7af@YbFZDB>NE@x6q&CddvnK_1r(cPd0i9u@Cplq;iBG;H<c5u8HVGRl_4I-p5(K$YNtB91NP$zvMvrkD$5D)-k@aWoJWsfurbM@)kR<pDmA5eBQl8}vkFbPe38P@&|vm`04j`ADnn#iiNnxODwGCTC_OT)8oeg@^OF|M)Jh-?@bsFCML8S5_l*G=%#;DlMA&iEe<3Yf$bdAFq|Xc2gyELK)vdtyaOjuN0ppRO5?-HQ1foia#bdKu@j9xhVCaE~t|Px}{dL3?a}+&$H0-YFb<nsgF3JJj{1&)kph?UMQ0~;7LX5qw8P^Eybq^mH2H^4MOtT@Tb&9=&2A{d^@zq`k-Nd#i3rQ75APAZE&Zzo9KB~DnvzZSCdzL*a_LeF31mZ4V14=YJ&%jxt_*S(g?EH1{$<k@=#rHAwo~J;LPQ#`0?oj7e)Oiw2Yj`yHRCOi)f5*gNi)rWoV?f3vQaDgY=MYXz6KR9j(Wmg*&SPqKZ3Vq5@^{-O!|*CPt)In=%Y-@(?HP<f3Zu^|1zIG!A1&P8$_YPoYs1$%9a*jY555398i7Sa+ZmI)>%f#~WOEY+W#Ol8Qt9P^FEr?*t5)<1iBXj4`|&+YS@M`|IP463_Qp4p>Eq)9{MqVJMCdK}D#O2P6&^TlwK0$OzG{i=x*vziPNCZ3wsFi-Zb<=C>idpdGaX6L6fK#3Ge?_ra?<tso?~4JM`uh0wuqu3zBT5Zhr1ZrY3q$ddYDj;cefy~kzn?o(~hMbtrgYy^g!i_ov&<RtGWp-Ae5iQ%*-uS4oTJ$H*^I$#tYOCs&bOVH(Bh9U1N^m&)zafCd~Z*k?lt~`14yr>4qlSkSAD$E5}U?R+gSD-(2nM&z^iHhHozr=HuJRt>L<Y|HY2#tC2A~ZP{AWJ_7&*TxPGbf-*ABXD17?hlc;!q!*q=Wgnk-3a1i6N;8DT9F<ft6{;FRTo|V>EnC2l`uD6M}MD5na-S=+bU{!zdKaC3K|AnuIo+$U0Amb`ownE>4k3Ycsb*mAWeMFDF`IWLT*)FTiBG0i%Rj7>j3NAe8BoP{*~y$`Gy_IxmeGnwrMvM_ORuq!pQ5Sm|vT%kRNpzYBTxMVOfb_uKnic>bK;1_Q%EN#&U;@4{GlPlCC60osyVcsqHV;o@ZYR+DFPm1oQGR_G7)K%FxM9s7A?U1a|oP!-G&*XWreFebFa!W?d4J~cB8O@uM76@~*X&@=z*X*gY^P*N@Q+&l#ggpm;;;1yW~9oMKzn}CjT^@Z1<7p;V8xasY8ASbaYt_9(xuRP=7;sU-(bwJAy*Ha0W+8<V7CQO9Bd;yB=E6^S6!S9n>@t9-8SbP6D_$PHT{LaHz_an@W&tYwT0r{zGFfpG++WTF2{^vv+w5g-eS3ZQb^(R<beul;I64o}r)ch0VCHFXX7W%{e`0}`84bOS_9U@OAJ)-hH6s32dt9cAf`9r8|^URThRB{`NofF7u8%K8gI5OMDu(zZiA;kiH2(k5HcTq2P7xp5zeM~||>nIYd2a(=#25HTw@$TU^Xi~?ZqZ1g(W2m4*RNRH3{4U&#&Cj4Nx(+ipgoxJ`_Q8>M80e;^#wYOVgaoTV*Agte*4Ho6L(jsJ(1OI;;nnfMrTy?u>nG6-So+zw571QHhWSVjqACVld5)7Oe-h@dC-4~rd`6bwJ;avKbpXcJMTY8G$<S+gLduqS)I~R7asmc1CqiBSBQ)s~_+47Zs>1(2xPAW)K1=R^HixN*j$m&68RnK3#J?oCS^8c=T`>pi@g7tzhljwO`}5e6&fH_Wz{Nj>?>HB;g0o!Q3MO7c(=-QjdLOnGI#<U}&d%bux!tgojI+;E_)NWoscR12nLVf)apl>Z&AeH~G;#JRyspwXglJ7ufd4ge@Y;OwCA1uG$|jF(4G+tZFY>yXR>onS<oL@Rdx>L5pF(e+#Alfu=$^cSeujMG*c4J*&mh%t2644R5)$i%kiz@Kx?yB?jIPREfqmdS-eamT=AVPP|2e#9Q0o9Wmf_}gjuvj2gVzZs4%7~=4!kx$hflJ&`_)as`{FbB&vG%#@VmwKHe15~4h2pzoNLChIkz1n)7MsIWOa|iV(W+X>>PX-NqBJ%K1JkdSi^I74xe&2wDeEG=OKCiMVT*vfS)M;8I{Lz)*ooJC-koCKfuT^+)_xMnKe94@-QsDFU`U4DaZfFad)4=*f|ArZYQ0i0ajKDmSc^urZ688W~L`|iUXEp2R_Vb#lhxRUM=vHyK;QP5PXg{!f>(=y5<>pU3d;(8pxN1U4feqm7pKF18YGK(z?#93Rrl24_jHrSi3I3ci|ZVxu`%cN-S){OW+-_B}5ze^f@dOGw?0!Kx)_NRT;z6)A)?Lna|KA1pfF80n>L7z@0wb>B{p}Nhdb+U%-cp&+rN534FQ?as3-&GqH(0f#eDN1)k5z6G)y-<av*M-zB`R--T&liXqLiNWjTl+0TuJ&=FouBlv*xNm(-=fq^U2h^X&}e^xV$HAB#kUWaA+Ap&U302(vkF^%+y?L#WimsU2;+=EwTKXzBY+C=U?x{Lp|b-=raiF)xV0y!a}FbOYy!ls{JViT{$WCeU?@4=^L03lVbJ9%`|00Qa;5itJ<e(dv36_fXCJl~M#ee!H3&sNI%{W7+a=PUAjBd(X9eNGvh$g}S?o&)50mpt#0M=1QGWo*3v12)`#xCFlQU-$vOcOJsO>nz?cb0Uv*;95E3Jf-}(l#U~m*D?z8)J<vqV%<UqufxrUnlxOb0-5x8Rl3$^LV;e~g;oUkJ$(WH(^nA4ohs0I4uQ1r#+OTq^uPBQevKpe1HI|dnxs8??HV=|bs%u`DmHNO8)>Mu3KaMQdEOz<Z^*NSvOXuz$K?5lJRgx~GkHEG&zIsIc{Y;gkFW8Jk!K@$Hj(FJ_7hl9;)lx+h7O?e0))5QohTeU>oO0=`AhgRzZG6ZoiNf{E!XbCe|haI5K$;a<8y+}=jMBb33r&~L;e8%T+rzvaC@l}Ugf9ZJ-sNotJm->{JG^vGhh6Jitwu#hWGeQ1TsJQEj)p>dlDbB!avP3=8BAa^swKTc5(OSPJNj<ir({AT6itbjtVDyslb4Ti%W~VFpGEWy@+WY#&@;-2xu6F&!wA^5;iVAfnV<=J}GF!nP1@Xp=Sj?`VpI$W<(f^b`uvZ5OC`O{M#q+0Sn}u-Z7UsoM8I;EZYGSHzY&nC0Hi!A>j541TIif_c->hP(C5@{!O+w2)1rs!}P$mM?5wSV@rnXmY>x*2Hz~6Hk|ii8D4~!Z46)MIk~~y#>C8Ze3Zr0K-H9#Tz#(o41M!7yts3xzqXqlU^4c$4MEp;6PB`J{FbK`7oP4h_!sxWa^XI_XBOdIH%3oh=DBtqADrS*uYC#u3(pyXKf}~N4WC@{bp1PzPw5cM=N?m8OAD32#d;0S!>3{ln_2G_vrb(ZBQ^^g@4v`sgEhkmLk&+r{SV<g$xVXrySUW)a<lb2Pgw%2J_G^?H&NS}o4DokX!hRWR$RDoV^w&5_XPZpaq{J?6YVqDl;*?<$I_$=Se#mTc-I$ShQ;|D-mKsB_46<%_ppy^Qchs0;FHk{LoH7+C6jocMYjtNWd)>>r=C1@<jEvY+cHnj1k8tcdZ@e%@6qS*<3bE=^IR-9z1Ml_$&=m-bMriWN4el-csJdKZ~iE@=Jud%;*!gl-V4*X#dEo1{1Uz`>Vr?_2n+uO_^@^r@MWpu%hsFao_FuR`0Qu+@!p?xtzRz{XlZy1Q`G`=JU?1vn^4KRXGQqso44?J3Tw3VQFtf!V;@U}m3QBs?Ba3F3AJqw7IAtYv}Jc-KGu%}?p!PV1RBq9$2;PLCVv_Ro^ibrTTwOmsusL_>lQXsftHi!;F~^#eJqYw-u>fbH%}nF&{ogG(oIk5p`ohpu@o6VT-B?BT%c)`(Qw#Fqt3#sg9{c#e=)0rv?2T@uODX_HEa974(GWm_*~3G{E)!|g2nNI>v}=`Jb*Qq)kxY1tl8&aseS;T7DipmGb+%|u(I>~$b+{vz6A*tuO=^WjNap)=)l(0Hq0%|OV8|mXR$G^9_ph5&=<|X!t<+umS;oL!A|`1<kF#E;5zHcQ|+VhqHHzE<vfgA659~Z9J<m+;HdD@gl2r1()x;rp%oZg2X)FQbTp2s?gv;2J<q)+o}9M1@Z3gT#~67W&}E-z#N32Aa}>UZJF&Oei3=?3SNaMxpT3CTf^O6dzH%6WG?q5jM4pWDF2iV_gZ|`2SdaGNLq=yfPikMJcEFlE0CVXqe5!erGv!}`fF|_}^wACYAhrtE?##Iet)^FAxpi~(K8l-*N&Mz^e3(bD%P<vRg{kN&k2~jhP;bVzEC(i7P)9P4eVkAOV^}#<`x~TRNfcRUp^a_E`|-6>vF^gd#jNEK;|)>d;X&S5audcfD#d;a`ur=<#x!DEP8)fyBa-tGJm&C9=wcm^A7>t9#Q4THA*Q@fGU8gEL)HD*5LF@llJsq+!{yz~?OW1s0K&-D!`+m@^)T9+PhXJUC$m)Y<{C}(Qty%(xS6>qvv66ur!t0Hc$gg#+{V`mU5ipCe7|rzv{CdxhN~%u<9S9E(4`JT9m7gL)Q$}ib{Im-p^X&3L^s1j{HB+~J{jYX@!Aqzj)>y!U*r%FJig&&&_*{wn|2x&VdzslR_0xRQOJm>gO!Ha5K&H^3TPv!=x7I22YX>W*a6>|I)oPeyZne^Rs>w5hV#<KG?BxOuGjM7#PkgQM#cU!r(ODq@7(gKXO6itvAhRf5mnF~bizCLJlu@TCB_sU`Uyo`D>R&x*IpZHU#pP>7Fa5LeWVsTDn_=y89KVMK6MC&G<qT-?&Yx^kcZVskVT4Lggc-)(hFH4bLoi@Xj2BEAh{;Inmi@{ndfL7^x;*IA83OieS}rQD6KvQOZGT92k~}91C-&lP=wV&&TCbCC-g`Ap*_T7S5ytQ9IQdpuxogxuq4_@!>Yu0paTx+S7z~R`d?EUu=wQv{+0S1BWhcEBg}hjoO>m-NuBV{7-0w>VJUKS2|6Zs@ohpIQi|UtRwAEu*g0Bb@yUG*PhG`dj@Q8$Tnq&#ppI>U@dyv`0!N)h57A4@bU_o_DtV%gxx{>&<q4rnVqQ7a0R#J~86KYG(d;SvWuBA<nD&%FMK9A*@g|0&2uTZ#?48;V4d-b(+yyQ3or*kK@|cdX+!Fi=G#C|c3bA1;WvA6G<=Rr#dGAJ)LeI5{bYftx)^nUTtP++z#W+;ag9kiTzOK0W2lGg@cVkOjIb{|@y^jXqc%e6IN*@(?&_S19f`QP))WegVlsgMy3d+N~Va3vyEbFd37<T1DzS{;xWDWEQEiMpa4F_9cWNBlhvR*;lv)thZp^9ccJlw$ri-k8}{a!odK?N}GBu}^vA4QdtCm+U;A}FX_@!>`&U7tknWotgd1b(yw%BU)qHk2*qokUK-y8<d#!Q3VfE`yH7-Vj=hBr4$3Xz>el5tQWA#Wivha=^^7N`|9`US$q0z}5t&mBKbe5;4Uc2szn;P2t5b?=FCPSD`dkd^t2QFPaav!ou>(&BR=>gnH@ccG2o6R31_W*$xico)5(`Ja<xgBCl}+F&wCuU_8(u!6YUX*9226Tf#yT7YIeiF#O{hxQWzD5Q>n#6;p}w9r;iOkxzWA=i*fiaUJCtsd&r5C0LW#CN@z{4ZM<C$j3QLysv@dwBjQb*Pz;20NsvL&`KZXOQrBz>1U2_gn@HXGG{Ay6+y#3hM-fc(Cx^BijW5hgEH@PPUcvymFr$Y9djU)xiO*=#>gsyEw2rPmbp+VeLOBAis^a9Q0*;+jyXfe_xd$3aO?_9QPl+7{cH&{y-wWgn5<>H^Pwi6nu%XP6H&4B!JJ{`NzWD^t>wWCv3-2UFx1hL43uZ29MM{1s-R|mmeWg3`vqSGjFfHQynhKA@mW*+>tRQMv<^*Z8D(*uQCug-37B|o5Od<%6bw-rjVU1g>q7i1LVN*aM2fY&(h+$jRMG>P$W8l7i82XB3Nr9sKp!elB0;y$75Zfu*hfNGDHF1tpqyoxU%S=?)1p+Ob{{9ThYQ+EqwFc<<V*OBJ1!x<MT;+cl3@u0ug#QeA}rhhltH;Lg;6G947CyDU4}FdF?W}1&X*yor{cvtjAEP^zh-W0q37Im0_-o=C)Q(Ne+e|eif#;?vte&3{ujo`;rzqfjFbQX002ovPDHLkV1f",
    "ko-1080": "iBL{Q4GJ0x0000DNk~Le0000?0000T2nGNE002dbc>n+a0drDELIAGL9O(c600d`2O+f$vv5yP<VFdsH010qNS#tmY4#NNd4#NS*Z>VGd02lO0L_t(&Lw#CjS5?Wj<uAPPKD@r&CSY*LIp;7yFtu4RqZklT$vGS(ib~E|kQ@Y?BpCrgMMM$WHet7^&Dw2i_kDNV`DX0{w)e~XFvqH0wW?~ZxmMMw+WRPJ?>T{`Tf(5SH3CaE24m5NAS~MwiY0{lt{5!c8YV$`YbchvheLT=I8=8=L2Yjw5f8O}ghxDdJQAR>>jczy#zJdP0(AB#K$p<k%kkMq%OjT0ajcJnwr4!FM4M*<WFCnU#2D&(#j`?ccqUTD^EpnEOWmWOvHJw{JyT$C@Dz~()m?Hd+7belZIMvsyfU^6sM9C4-Eu759*HGvTjCypMf7jc7W%j?iqEXutnhKsrXVP9kHBK#?;bfc_r*!jqK%rITi7q#6$cfLud-7PCEbI`EW}7gX?Z45nU3r~DH*JNC<WRFlA%t=G!C%sKq9m#HTKh){Yg-xjw+os^h(3V=rU}I5h#c0;S9+3C1V*$m9eiT^|ifHpu@TJD0RI~L;LU<=o~r?9q-f7@;U=8meomw#-UTtB-9Vl2F|bP#X3>H|1?a!)3Gw75UxS_SQ%ObBd=7*_9jZ>%V>)P$+kq=%X-=_ph3U14xEJUfm6`uJo<;uK<}VJ>K>pytW(_;EA^9nCUiKjHf_*7B>JBu2ZDzrC>b10hZ+?%g#$;@=|~z3k7UB^Xco+m<-p=tE=+u~VBnnz1D_1&`J_VsSUU9CPtPZfj;6xYCmWsPQ+V^?B}&>yV16{4PM?7a2{JsM0b}1x=u_9|XeKO==fc7_7v_{E?5E|O2A!iBL?(2O31msoJ)RA9&Y^iU4ceSn`%pT}eR6Q)?tQ#^_Y%I@%`m2&8YEl)IPICYN#7@(b}FPE$JRfbPWv(?n;ZfPusWg?t0GFUDYil?uM97NwQn9wsAu3U{38e6snDfOdW6Ao`p7_Ok{400WE7YW4Hh)0Y)FDE{qnIcrUKFB9XMIrixeWPs0|xq&(YC57|{`JI;QWRBSDkdWJc$kE=}N{|NMZe-f@Xw^&^}xAP1(Qg)j*&fSw@#cpm(6Taej2B#mnwP)K6(p%+9MOwbkqoq&88uuhMeq#slOT{^0BR1jT&8}}Ya^Bl`+f+6S8@y&rjU@i=U^I^!ohN4X9`erjwIk582$JV$iq%{qoYy2kWo;}8sm(TG2_t$v-`Z>mK-$BFRHN=#)V@+h4G=~BG(PKXY&TqtVb^K_*e;&uog_2oB1vKf1;qd}k2NuIOr}c|bU*orrZy-P0MFWapOy~y}LqDVx+J1$wAgW1}(5vaY0#jd35?BOtc@@lKt0k!)R08vWB54evcbSIT2bYrcV(5ib!X&1KdUY_0u7yzy5nTg=sA?Ef>W5cC&#wel0VQ8-JD$@*!g3)a%wwn*Q3<1{bJVA9NEu8x-}mx!h^e?plAhq>A8+yd$G7<L(Husn@1XnYEnFm?ym*E`|9mfvIW#p({chOOFT)@rybOArTQ{r{`eA3G6I=!*^VkOH1y{l<s0{MT9;u^1$CX=*$|a=K4WRY%lvMY}r}xM_KMd>Oau|iuz(_h1S^>+zQdIX}m2_$cuEB}}8-<^PWqc#7lA2(d%xs9Lf+hRKSNBSK<1=^Rz`pvybW+|3<GAxMO=y7`VG@5H7Kwa5LByVCJNpM!z$U1iggun{`{uR5G_V{p{}SkvY)L<^NrFj4HLOC)kwN=~t{|$YeGHzd%~&h1W@3~w$R%)~&W5;J1QxX8hq0TI?(^5bBD|~%Hlb%>8d(kfSk8TdV-g0mQ^`n75L$(OY3K3ow^vf9sy;d$z$p2a!iaET^pZ)OXcO3%)&eUUWf0Q<!^k>VGDB+EN3_)qO~NXy3WjvlGL_NF=!H#YFO1?8eG+Q=CB5;PdvK;fMo|qgKG_MAGrh1(?~!17rVp0vXL`B^7JN2L>V!dL1FS>O;l_OhVSaSdJd6&>&%+>rq$ah(CcTgIT!2+%Ej%+?@t8|btc<j#VK^~>hJnnKdFTcZ{tTF3IgAOX@Cp=mj7ekPdGs^Z#Wlbpf(ao4medB5<TlE7C>bZT!aAxJN%e!0^0l8HVCN}rsNuEHiEM;!R1>qQ8sDF&#~7UyI>nviu!*XJd3-Cg;R4J<&Y@=Ty3|&8>4u^$xeNArW3VqAhh5PaEK)AQCb}L8b&7e$XYa!~rk;_z0JH2-SQcD`UCCA0mnvXab`{n|oTqpk7P%uZiTeSz9Czx$oYddHxC@rdJmXW{u+ATaNm>ug(gt94vIln24Rl_yMRZ-8fi>+j3U7d}ycGs<9TJR_x?mXB4t<WR9nr|WsuJ!g&A9*MvD7cAehAjlb<mCPfLZ1c%rl700VtV}Jx6&xx+Z2M#nNsX8c_?wgib0B(~uz!-U-X7dc@WZDV+WBK9(~@txjHqUP1?~VwzA(qC{K$@Dyxgn_-$U0=x2?a5y&u`*X9L>@sXmv>>rwu}lPEF4VI~W@Z&l!>ar)oa*kuvGyJuY97G8Y7P#yb8xJigLT;*n4TPhoxJ65!b*BzMQ2SiMy2uX&fbDi))<Uvw<C$1d;Uz)i>?}kmB_-BewgJj0A)8}dv+SO6}MqcX;pL`#%Bg$6x&9>>rgqM2z*)hHP~<*0|vk}|0->~2J7N0P_jJLiyay5c*?aa8B*2@t9Tlc%P3d>1c$o&Fw5f-P3(YAkz)UO^WinNq;<e1bpS@`Bd}##{pc;Jt$ySt9FsbjUE^?I);JYjgHy=_EQ_zhfmxQ+bXn3Hzw;2TCpkv`6}YrLgY(6=u<Lk>m3?opqW2Bldfvdb`>iA$TAwk?uEK#!V(Q@|seeGl0PNEGVO4X7eO|NAE7&#v%xt}km8UvzYwl-BFT839Hk{YI>^7WQpAygDbpA1%sOv~Lw>*Yr)g2gTj>DFIm-i_MYZ<={`x9J2+01aZTQQJMb$6j;MRs>&UBu@<-${yl^BB3zQP?y-#`3<8SU&Ix)=f`YH-=3aJ$U}+g`^i$JqoKdMz87~>{I*EFs8`RhRe6%QG5xzOGe;XJ__HOakyj;!Lno$_H;10MX^-If11Mz?o;-4GjO~18S7?&6*qx3w}J18m7;u$atd%A{{-8bSvaNjVrrg<pqgPga;ZD?JjZ(W6@A<;e}rw-ESyt&(0fy{eVqB>Dx5P0;n?s9uKk~}V)S2FG5i<YhW>)<ppgHB?S<Fe25w_(?f_<gRxHVuE3>dq<|-@WlD@!Tbi9LY`)erK<&MK6U$GGj>?!DnZOIMTb-$w{bYcQ<9QXjcid)!}+lNOlpG$h7b)#@78-ru_BRJ*{qMi{E^`Ab!!|&oJocO>Ex9|2ntYT(bSC7HDxF0F)3c{}3o5SkDUbuA4;QPm)vH2~q@eQ!$9kBHSC9(B4*714m(@$95I|~=;-{giY`iC?Q!?k7%D<+>~6Z^Uoo1gpzmyuuKSU7~(`M}(L@&rCLBXFykfLq5stQ>iPRX09j)zlwYF-{*ZKIS&?BbFD8Af*1XlsJFThamQ`$r^!K(-XLi{ToiB!0NGoLCL0i0>^4DNoNs(?Ir!Nzc3A#*$-IrD<k)s5x)N$9DcZo4JCaf;k9Il*SSF~Zybl~HAb%TZ^CXc1BUNBzzETM`z|U*Z(>VnAJcgpE6e(EdVVv$O2Rgk^uoPo21kDV3||ry@DcDONg;m#;Y0)x`3X4o;uG~|v5v$~&l48GU%vJAW7s+U9KP&#lsNS9-`M)#HC&snV0CU6I&a>QbjLYYeCJhcV^*$dzKT^X6IgX&5^K)0Ts4aAwWB!0rTFoaVwIJ09~S+s8?M84g4@GmX8SV*lx*uJ;mQ5rcV>eiY)|<BoSG)!eCHk3Flyfut`7uZQ`khu7YIAdy}_kn9Bvcygk4b(Rx>^gr>u6^6OP&KT#oH<Bhk)uVpTZ_<1ehx6NIfVC1K1QpBJAINQZ+-P!MGpNfLw!vZ6n;?$sxFT$;s361+fII5TW*-5A_&J;xFD@sS8)rv35(Zo?0xY(82u_=U9RZ(m???h*1YO(CUc0<m3Jkx7zTC+}e97sWCZr~m4)TUeWakv}9nZ(e4$-v0zQCeA8iEumytK84M>y_ow|@vGupc?tIXDYqMVftB~EI0rc0_`uD75=W{OnfTXV@3}wq!}{DcI1fL<@-mTO(^7vS-O2}H*D?v~^HU`H7M6E%Ikin=W%&?JeZ3?Lda;^q?vFlW_X}X(D`4+S;2?u^kV|ntrNGAfAF;A)7Ax|5aciEi(1u~G;xb>)CFw~WPcCN<_Sy36U))Mwz^(U3ZWTRPm)C`p9aqqO>n?ugcCv7)U%)3mzkL4+jaO#i$Cb7`y%RP?!?10hg~RxJIRE%>xc<oHNVsudRWi?J`kwCMCagFRR$byzfSa>5f6ko-xakl73A-llQ#^~5^eayM&$#isb3d~s*|u!6<)&ZD&0e%MjL*O+djR$wk6}OX3busf$XnQUK7v!hB_v-^5H@~y4sLn9aBR5^*U9%-b^9YX{r7O2e8)ZJ4VH5$xJ<r<%itrdyz~ez?K5yC!CyB0Ivz&L$KW*l9IF{vml^K0H<$%?>D=`H!eQ_we*ox9HaGlJo!roSaG-P$iLF<V*>xR-y*CiwJdUV_G59c$+p>9nOX=ppc?8zwGq7oS0sFo`h)=ZPPdN8~;*Z83P%=mz;(4YOsq>Cpx%&{?GWm0#eF;|8w_(%p6U)PJIoXEJ>px05X9xJBzyqsA&KN9tuCY()LhbPUv0`+Z#|Pdy`BUuF`4TG!f5(bJ{(99ufCEqPN$2MYV}MrhCg70EAC7`6aO5#Wz(IgNL@otmaOHvZ``k;+l1o^d%PrvaMNBX=MgPFcA=vYrXj**_wq0*XDzk9lcewSxhil(^9z~wQHs>;S<@KSIfiCX7jvd+Eu!wJiC2s?kJTjQ`TxXTg2Cw2?R1DrgN#7*gQaWM91Gin{1K6Gag+~=G%a$i_U|AeRlyrIhFy_H?Z&n*Oy|<DvsVzJV#<##$oRgS+_VLY#u2!7T#jl?i)7*lS8K=`=9#Cz0eW)2y99-+TVcPHxXu(OPqd*g{K+X4HQNVLf!UZHYjY@jc%#@hA5kzn!7KmoX2sH3K*EBXw+(P@rEc$Q$gx;w;IFR2Bm&8^QrdSC9<$bW>mC87u<hJsF+r)r0^5EOZJ8HvS9)xeeisvtntWHT^z=Qj$1&;~_DZS85x(FS@hG)jmiax3R;j^c3=7HRdXH)ai37DOof_3FI?5cS9u4dMqn}(7;C)JB?ggNhNsm&u_2G4C9LqugC2kS+7?^V3zVO7+h;;)kfFWm+t*^rrJl-wa*A^yG^O~O*#5l>y@$(R|)>y1U>Wl7hXH;TCVtI_`laU2nN^Wha<zI!3PZP=Ib1DxayxcSx9$c$GlLk85kc$By-!A78Hl(&?ASn%S!C$06%xE|@PFq1dawr=Q=OfzP<B~SAqW!+NyL(bzQuj6&E1%|1-|8i?FBP?<Td2k+pX?8!9v|}5f&P%Lb@L9OUR3Wyi4?q9<^vfg*5I?!68i(K{UZVt8Kqsb=*QXX<etAU-t3>sH;__WHI01{W3f|jzsXxO^%%o9SJ<#Rl+nks0@Uz_#sp67e`xX3(IwklQcOsS-bUE$tq=ScZe!%kR8aPK+!=8bfo!|8Ri#lKuUIlgDgU!=ArMDF30w)-JN;68+$SUkU)AYrMJ*m91@j`7BLsI08+=`lD!7+nN6j}K2=@U3dRl%5dRzn8YgoK-kj3bQViR2b2>BZDQE3^XYz9rE0Eryw2F?OXiqOkok>PW)*(Hl73I0(<wCRq9x!+`DT0cE_Di#G+e&?Y$+LI3%B$0E24dL+j*fd+CCljK%tN7h3>r~+mIr7-0<#(pI*=9~-C(7#lIiGSIAxdcX(y5jXsKsk&8%VAGDXC5i8Mt=EiTotrCxE#iu%O<=M8x!lX;VZ09s6}95`xnBF=3Kz~_*$$ZHnDwULLJtgs6oQ~E2q1^{EQtb4b-W_y0}_wpcG@SimibK=Q4<@;gXCfhfY`tRDBDe?41kQ;auqW<iq%A0SvseVSFr)D1hP7d}tiWgUXS7Xa*ERKdc-EgtlK1Ec}b4H?3a?W4m?`Nr*lNgXk)v8akn8p-!?@eF`As*lIq7Q0KTB3-B$1CW+Kw&@@PrCZR!nF^)7=U@@#Hzr5bbyFl_wAY)%mpIkVGl%Z$hHXb~E{2!Pj76|*g{^2}k=H{fAiVHg8m5|s17W71WVH=k?ebhXj4<((T0%!%~K_eg+>c?}S>Yan7UYSrilnLd7=~%WuRg#N^Je)yCGodS9AB$JYlp5llKXI;So-k&bnJ>vbo(J8KV(12!z#xPOWd;WpLdQR!SyMpCc?k_a1vJHL=%6AAdco{RX&782jiDXLItI?lukgzoSKpi#m@>#3Buo29HXLb7|KyDHdgf~g=M~`d<9U45evert;qfoh+gAahzo2)M0ZOUw<6L==9m#@{#<5K4V}r6!DxJ?{^wS~p$$*M?I+l2z#3GMG35)k8k+_psx<8RJ8Jg5n^E!=X`%+-&m5!=;!lYN!M{^)!o#wGDXdTOzK4|FsWkJvPZ>i_UdP)JIqr+!C{~QTAet$z(NRFfJEk2;+k+A#HJjb(|VeG?s4yHnvfiyat3G3szu=UHAV8>vHXKVJcp|dtDFThT;Gf4K-5fHiyWzpBhFOPMKG1f$sVMRE%2cIk~*_TYh4xfV7;nPqTpR-7SOnm0@IwMIH&m^cHJ|jWYi7!i<)KwLq*Y?HZyKPZex;qi39IX0l!j6#m102Vj`rfHr;^HfeLTVE_ENdT8JZrIC^RS{$=NR>lvre?LEFkJMkDP%v=eIbf_-Z8P@y{V)45~Wkk?l{BKEtW+qs_Y+*j<TIS;O-*v<|R8p}wDfc+xM{t9qnBZQmKTvu@vMXh@*F)R)F!yU>yCJq2|_$R)etv1sQB5+**xN*_)Wqz|*I9tj*Yfs@KfN`gd;iihH(tqRNHyPpK=FY^%kB+NSlC2hl!BMk#rVC<DfeL-phv=1gi$4h+gOOl{@kU==0fcU(pA+l9Kv=LffiZ<E)B(}}#i_d_}c2n=HFNFDJ^H{@qWcxTibyR4#uw~iq1T5W2yY?hNg%DCv7l*|=VzFe$2`t(!=kp0Dvwqp`cqmIcLdHvS(T+HL=N^M^x5@DjcR9Wxz9p1*#X?C&VpMj>p-!o`lX5pDv3PSZly^iiVnQ(nYHU~DDP$~EL?2?=ju<T49t%T8FS4i=@{%^lOWXK-8jH5XN@Hp6l|y5X99oo`9tx?#F~l4yyM+{AsZT(4mqIR-mFbWwp+W}*)ajfV36ht!BOtpOJK`!h53_)Fh;fB|ntK)FsuCI=v5@VFm83c$)ze-X<<e~tv^$FJa>#_9q(k2cVXu&?d+00M#Yb-0y#K-vB{la*C~uCCAj-1skyx}j4BxHyBWXb-h0D%83~HQU@zzi*-5NfRFsN>$?xqN+Y>S2Vo+Rk(VW#Y2=ImgkwnRXE$5+@H0U4!?Qk0jvhhs5ymbphkSwb|&iGk|&zoEuJ3W)NutufHxQq$%fT7<4gGL$**(yfssg4iy`S4aW%U7{Q*{f$8Qq(-QcC>74TXhR_V3zD8iA2s5OeS`+f8apGQA?m+^7(+>IO9)gqhd_l8a@nR}EaqU}uJXY*u7|LAoj;av0@Y2SSiCV1OG)CAO(c?1nOV4aV+j7SJ_P^0Itbsa4aI-04#xki4Tj2=V94Bqp}tK48KK5!)vW}jGUr{w`4(*o!M7Y^$>wm9!oax;rx-jsEg;(-PGi}|_C*^QNP&&vlmemBIEy*XQrf*_Lok+Y<lKB-ynf-Ceo;q_!B(cuw`-2!o0UiK-S>WcCTUVz2xPQNMw``y-Sbi^vrR}9`l`Am1pfy<)}6w=-m!rI0000<MNUMnLSTX",
    "zh-cn-1080": "iBL{Q4GJ0x0000DNk~Le0000W0000R2nGNE03FATng9R*0drDELIAGL9O(c600d`2O+f$vv5yP<VFdsH010qNS#tmY4#NNd4#NS*Z>VGd00~S<L_t(YOO==TQ<O&<$LAl}txC2MVeb2aB)YX8Ww}@4MiY}tRkBGoTSnu7qDVB#WmFWo6hv+q7>0p4IA#DD5E$-j20=MQG?HkPE5W38^WE<|Akl1o$q%3Ee*5iyo~NJge)?&V>}WY;M=V%(paARk=0bd+2+AYnkVch26~i*x5<+sQ6yk%W2zv%eR2ig)EKo#SSuYKhFYd|33%heDuMpxxB?x1?_+T;C?JGd|zI@2oE~BoOKh1{tv#Ss(PS_ziT88lG5~yj2CaMU!s6yxt6+^i%7xMjiP!Q$80;q&G{#P9;f`mdO`|}~$n*;fQe5emU{kKwzcV|OEW%B(6P==rk%9C+S80#<Wz5*G?h!hDmP@Hn&CC*aIhSyJ(<C9buK2E8|N93I|cKjpJ7Gg(YC3YlL;>{!*UQbwIJ9#6noMi>x6#DU7==;}`7X0m$74Iik<HHmO_FQuFy9{b77reCYa4BTRtPrWsHbHm38DXE>p{2_XWY=MF>0A8x<9vw4rAK(Y@ZdS-79V1PeFVN+p2PB!$Dw}0_tQR)1m+*C$q|URTnl;S_j~gpkFP=4@hXTk>7CGJb|E~jj&3Z)!5q(Xg9MhAALIKcb8Fu}kY%<BJlpTPUwr?P__AimxgTDPu7LdPHAs>?5b3Utz>s?b(&RR%j#{zlgca|ecVZV^x9gmPbr;@AcH-@G0uJmvE0iwm&+(#vVrorzp0@{oPqgDNaW-r_S%K}RtMS1_cZl~cxUut0HD2cuh8--!O9@Sor1&8wB2Dpa7%Vf8Uk)Pti+Zk$9jec(Aw6n?<cN*mRglHlA&zxHe#`-7EceBQ8g!0L{H(m87ZJxQpc48XspPmy$YY%lAFV>zkt#@Hsvss|(Uo}N^IC+ZbVGJ!gajed+8)E~ScIYS5fr(TkYo%&nKgp&)PDRSxeM#kh9G5KeZdbyf(P$iYJz`ka!vX0)HJpwI-oyQi(TnWcrBq8x}+wkk~<(h*NN~8J$U)z0A5b%!|xK?5S}#(Y2h8niob%i=pIA{FJNi}j17RgW*G|m9E|QI$SWQ|T6Q1W{7D#7yYWUwE8^^3nEv|ynsR}j@!QzIle9CVnTAcFqCJ49k`8Q3X@>s1ANtIGX!55Zx6C4}@GeyD@1dw#g0hOGeF-8{7hvutEKPnud+k4nxHb=c`4sdygD|JIVrNz}id%=*ls;N`i1yJHFZ52_#=rAg;2F5N_FrJ^?p>sM`|;=WW*E~upt?K^mE#*Iy~|LyaI!u?MMQ>Mz$;ULp_j|hI1Ph+6p_W<FlSuD+XXE+@9DwR>{n}oYx+mA*V2koe<1YTJ9!(st~6kGu@9G;`Y`ni4+%#$o$cGWbf!Xj#1??2;~@mS`kOSsyug_c%)sR8#d_;??6S5Zs=6I{9YfCvdh){@^4bTm`BDuc(_P5#7!0)!-MNDem+GL(_ClND!ma`@(wcj5@7u4R8{aWLg_s&YwiaH4!8;7y^a3K5Xn^U_B8<LaY%XX-DhH0<n|W@aK<&^dKC5WKYiTa%EiH)5^`c<afMFW2C8r*d^?lIP^uS03rZgwsD{MfCe;9Mm1U292I6f}r|B5yk$L?Z1XuzxA%tPA}fIh1Z`)#cumpvWe4c^2)D&D{uM=(OZTGEV-b@WtT0}7upU>gnild}_>8|Weaf6dkwGBPsNi4Th#F*rSqsc-Hh*3k}gW)1W-)HMDTHvRV}h$5DMfN_Gmy_N$r+=#FBqr5wSJysvKQ}8E@Ui<9Vae#xPoE<ns4zup)zY#KEWM&4(*mm&gKNm|9?eZg<{WfOR;;lR{C)WaVx*JAYJB-0Qc=h1|HVGauKLH{iEkPZ)16_#^uh4ywbhSF$gRL~6vNyQqk>AS5-5G45=M06sZy4hBbiKOk7R<AA*g)lf6b#Tz01>l1et~(&8pa_n^+QqK1-Wey`jlGOx_{jO;Xe4a_Gg)#y~kr*53Qpg(#G)+x*Kzdq`t`eD~NPF|At-~5%>xEjzy^J??clt3sp%FhO=HcdRAQR8=1hn*^LZH9&AtdU`M7m#Li1zyqUgQW_s|}<p%g~uG|p~L$|Oc#RIJ+z<u@@hR!AGp{^k+A0#YAx@JIG|09fTG^CXQ={log6NAOoAawB_RClc!5S+mJ({)guZ6Q9$zg$6*=z}!L2L;;{XPRM%uU#{s&^H7_Qaz7o06OpYFbT4$!^l8nB4*Y_rkVw4><=K62KQs=+;h-WJ%r+7H?$|5sP0@@g682{h&btl>|8r<vTi6d2BGE!CQ0dmGBXH8W&ldo4ZIWDMpmL^QOh8Vr)r=|?}Og{5Jne|yn7KQ_X6Y2Jk0KSMnc;?Xe_s(ES`YTJ`0VN@w#LR3L%c4aG-iM;x!G9Ve6M}nB&}tNUWn^?&wo4nBr;>kx<Vz4@?Pl*qGo#dD}|ZwzLkxNEs^1QWr6_TkpXjP(i5INJPdWZjAgfD6`qQc#;>#E!G2&Cp1DIYo`G#!p3;qT=a&3vnvoXY=z(&UWVxb<_I%9^C1HS55(G_N@|8SI|yUJ_zFdwEGKL#nSe;2)eqg}KFBV#L6<cERc0^L8GXzX>!4$HT-EXOCG=ad_~?4dP@eQaoz~4@$CE`2+2jf*oHIlZr1=>-{m>@2FgI+4?xG*6bKGdLRWLBawOt<w2@Bqy#@@?y_=pMXhpBG7pW?&^t30j$^CFX3{_9>%RvP<mVB>KsRL7mreAxmcWeXStQdv*y<Q_=&K|pu55lY_chLlz)nX4&dY=}5qg!-N!zGZURG;jm!V@e?1R|qNJ4$}Qh%|jGJOr%84c4Jflx)}2X1Nv@F;*EGN!7&@u+$V-)o|0Ac=c$*7%x4-9f(GblfcA7flyNS|_~6hmh29iXOp352wgfun^zvvcQ!S=zM9h>;OhaW{X8{%87ka)Qw#SuW2h;SOiB@PiM#W{&oOHo>+Vg*iOjK&5LLDC{vLmHXe^Cv^aT~&;EPS~XK)UBD$%W)ozMA$HBAiL3k~yP*nmb%ebYD22VX2HRgM_al@xLxZ&M}Hlukta%2Mk|F+7nz-zCWJFiT?o|Te|ag^bw-~0000<MNUMnLSTX",
    "zh-tw-1080": "iBL{Q4GJ0x0000DNk~Le0000W0000R2nGNE03FATng9R*0drDELIAGL9O(c600d`2O+f$vv5yP<VFdsH010qNS#tmY4#NNd4#NS*Z>VGd00~J+L_t(YORbmrTa#B7$MgSmsuc)?Ed(Ay47-RGTb=53vvyGtK?Ma|kVO#?WDQ{p7%)JPB?*XGSc0r7;8GT)t+-L4wQ4(^`Of!!!=&Rg^HZPs;gfT7?|siX_q_L>_gsm0N)0>@RbkVCQoQ@sMMx7X;G3d_PqGHSM{3}mQVs9J)sQAtyXGZU!DAhvPnx8Gj5@qHCQGiNj$*vCuZa4};K4p|?x70)uYhM_Ii&2D($>a(1@QR#A|!q%8sSM}UWcpTbF3b|Nm^2kfaF?8_m{)#U?n^cRKh2b4kgvV=a3dM&hb2`fyV(l^mQquoa1}A1~PHXB{%FVVZVmZ$padAbB;?_1w0Ox;+-!F;hj_gNx;b~@JVliG_{titw-QtE%p|+BQ8USxXea;R?r4@T7yW$2^}H@(sgVL{~Hi~yaB4CHQ1b1hX}US$LmQ0LKrz!YCXcZsGT`2_$app{)~tawG9W$vFQ*Obwmq^Ji8t893%WswLp5b0rHeu*r)E`x8K%8R@R=nS$nzS=BNKa?ECqTF`+HYe=e{}UOYwr#0)}@*2064`U_vPU#1>jbWjpp*at;HF9LF|!t0n0p{Y8|fB&7^f&T|@-mJnjdK)T6@jbrUO=*qrKidx3sVk6#RSZK}J_JRv71H!(gm7?gaVPd(?7-(m9msC6A+gegJ^Ag}b*>FN^V&teD(%AL+=AOk-W5A`pXXR^D?ZFIU{{_nmu<3}&kAF*<a)fDtb^}4GyKk(C{2*4Y9^qnokEy)3|`qLI&lTQCtBcrv<Y5Eble-wkREG>cWMh{X?%}q&De3y2;0qjZsYle0Vt2_ImXwR(g^91CU_sa0<WXZ@F1Qddc2ovz{X4?<d+;|K$Mbj{e47TnMbr?9tzDQJBJZ?aTv0E8$7am;ZraGzYBH*U9du#-GzM>7A!pa!EM}mcOIc9nxW1z;()dvarxa)WOYJup&$PFR`?bULPmTpIIt<(0(sRaf@^LfSWBv>Ac^UEf~c#H5!>|?s@CtIYMw__+Y*8s?m*57%F1zs(D>#&Gg2EJc<}g<+ql5M%pBBbjL2;r#=`Os&{-#u)8@p^l3s-5SrA$>giy^C_1%TMb{Z<fLn!qN2-7b@d3gbnIL8}oalFP>${6b_M4DFU%oC{UXQ3>0BBIcWeOfyV&RMt7m9=N+8g-qN!Py0TQPmH}%)EPCU~1tZN-Y!ERnEv24<MMj!de!fHoqWiP@7goB=NU^_ox4X82gVj{v9GO-$sPSiKt69q#2y3x8HnAvB5cw!%Yrc>YWh(58he8_F@Y@r4#9fA&lH#d~5zZUsrz57~;#UP}hziy!Ad}ZoEO<O<>CuAW2vT;^$u?(macJhWN|oLFDw@fb;$WUcFv*D_VT=2*rJ4P!)9{wA75U>n;Zd?lGK~EC{N)4ta?Mab+fC8i#Q6!9(}60+w6%k<sCVy3UTMfknK(^eaAiN(VmvCq0>ejOcbJKG*d#c|3dT!6!^24TDoiY~~6|IuXTp9ou9>rOoBQ^wJXIYkHAz{T5>TZ*wybLtSOTwu&A)IgUpwPsDk@yncZU;~*kyuOW8mE_VO)3ZMQ?2fhUG;qnW_SSF#?SWw)1W8Lr*)YEW!+W<bR?ZsA(CFt$g$uK9>_d~PpzziMOQ`d*TwhrN=wqbnKGJqYI?bu#-4SVR=!KUjlj?bX1e+-eO-Pm$<1iR)Q;j6#@j{USP`ItX@)?On1?)Ql89>uouZd6*w@kL`l!kLh=dz|Q-z7O-QduSb-abv$TCpxh7Y#HtRZ@4jy_VHPCOw7Va+Gtc*Kvbm}F*F>`=*2L43AYyUIqiK-y8@CASAf601`?KDBFc6Tn{^H-OS%!FwIRIbI?i@EMMHlEtz#0KE3ZLq9Kq&}aYT<S;)4fk_~aMhlUFVzu{;Ia7kCopfQX@|2<e`KqICwr?Q;mN9zwF-Au1C-I@Pu*5shsUMdneFOMT<eSY7=Wd&iK|>BP!Uu6?ArK8cW08zP4vK|RQQHnEEB4`^=@*g+C#R}$@b#ZB=m;>UokB*y*=qOCt8)VPe`;$b8+B7(A~+>BfD%?Lc(gMh3a$eFfX^uX_Q4+7Z^Vmq$Dj31sq7N7Y>Yen$I0c`GE#@3PFv5oq-jq=ouxY$M{5oTsU;}W8;tsv6!95Iwzh>}SoFxP@3byiW?%Gz_LSrZf`gOHbvBA~=6A}bn#A03sKk0G$ofr#8LEU)kUZ>stboZpY&%imHjH@ZOIkBI4gj#%1??OlN+s%;)B{VXCWBMjd{ZJ0xN8;xtm;D6ePl$vX92V!$rJ7ir&P_7A~=X(*xd>@p<HjM}bGxbJhceowcU)c)<Bc{+!GQBUjiKeaSwmA`ry6HBQbrbwJ+(1P048n9b5!QGM0Zg3%r;JFhwyZnw422y-C}ff;>==HFqN`4ka?>bkn5@=bK3{i$3F=e_6lKE*Z=5E#MIr=Ay8;q54Xdi0P%!nX`AJq*jv%DM$!~QZ0y0{WqA`og{tWw>73Jv$$j|XeYi|63c9bV<6cM$fkc5`l5W-@_Kd+m|&jv*i!^v;8FGK5>dKt-8CQ+FX0gcHi79Qsfc3fz6{1>?_Ub6I7tp4nZz;Pz9fK)v<Z8uaUb~j<A0uHFkSPz7;91{r2?c_V`;-;}c!QC#)Y={3*9a6Qf2)y}q6}wpx`5dl;PtqUAl4>bk2<^C2&6xOhUOcv!_{suV=J{u~anG2cywLj=VFi7x3G)QQojgJ`c#<XA`EC}e9q?w6A=LTXPwSCzMxa@&h^5I5@JQ3M(rJVTs~-<mKbumTL@A@g>f<`>EnpdT&VU_!&Yv})538ln+^cRv@&r0XB%x=G5KwaW2C+yC%4&uDjDe+CBi>_u@5S2QlXbnwLEZ;w)Gwn2fhP?J$TWyD=rlQHfQ+k^Ch`LFO{FNk_OlE>R15!fI*`REkdSrxZzLf!8l2gTK(5X^xr&pU;Ge<Ou!8ksiN1jjY~bZ$W1<!wLa4dQKspe>0#=YgnJoxD>5>7w4{Y3D!JAPDZ&S6r?C>IUq>lZKP-N);2YUPqxp=ZnXl;*#00000NkvXXu0mjf",
}

images = {
    k: Image.open(BytesIO(b85decode(v.encode("utf-8")))) for k, v in _images.items()
}


def found_any_image(images: dict[str, Image.Image]) -> bool:
    for image in images.values():
        try:
            result = pyscreeze.locateCenterOnScreen(
                image, grayscale=False, confidence=0.95
            )  # pyright: ignore [reportCallIssue]
        except pyscreeze.ImageNotFoundException:
            continue

        if result is None:
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
                pydirectinput.press(["w", "enter"], duration=0.1, delay=0.5)
                con.log("[green]Restart![/green]")

            time.sleep(3)


def main():
    with suppress(KeyboardInterrupt):
        run()


if __name__ == "__main__":
    main()
