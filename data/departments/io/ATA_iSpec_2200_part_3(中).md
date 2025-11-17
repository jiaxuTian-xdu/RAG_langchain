# 航空维修资料标准

# ATA iSpec 2200

（三）

![](images/f5e7f9addb38d3b5f2d5dfb9d714a5e87e247ba9c9da70bd6fad9317b8bb9fa0.jpg)

中国航空综合技术研究所

2005年12月

```txt
<!-- This is the DTD for the Fault Reporting Manual --  
<!-- and Fault Isolation Manual --  
<!--这是故障报告手册和故障隔离手册的 DTD --  
<!-- --  
<!-- DTD Reference : -//ATA-TEXT//DTD FRMFIM-VER5-LEVEL2//EN --  
<!-- DTD 参考：ATA-TEXT-DTD-AMM-VER3-LEVEL2 --  
<!-- DTD Level : 2 --  
<!-- DTD 级别 : 2 --  
<!-- Rev Date : 15 July 1998 --  
<!-- 更改日期 : 1998 年 7 月 15 日 --  
<!-- Highlights --  
<!-- 1) Added + to Taskref structure to allow Taskdata and --  
<!-- Refint in Master Fault Table Description column. --  
<!-- 更改摘要: --  
<!-- 1) Taskref 结构中增加了 “+”，使主故障表说明栏中允许(使用)Taskdata 和 Refint --  
<!-- --  
<!-- --  
<!DOCTYPE FRMFIM [  
<!-- The following set of declarations may be referred to using a public entity as follows: --  
<--以下公共实体的使用可参考如下声明的集合： --  
<!DOCTYPE frmfim PUBLIC  
'-//ATA-TEXT//DTD FRMFIM-VER5-LEVEL2//EN'  
[ ]->  
<!-- NOTATIONS --  
<!-- 符号 --  
<!-- NOTATION Cgm PUBLIC  
'-//USA-DOD//NOTATION Computer Graphics Metafile//EN'  
<!NOTATION ccitt4 PUBLIC  
'-//USA-DOD//NOTATION CCITT Group 4 Facsimile//EN'  
<!-- ENTITIES --  
<!-- 实体 --  
<!-- --  
<!ENTITY %g.r ' (graphref*, refext*, refint*)'  
<!ENTITY %w.c ' (warning*, caution*)'
```

<!ATTLIST FRMFIM  
```txt
<!ENTITY %text 'para|table|unlist|numlist|note)  $^+$  >  
<!ENTITY %deleted('deleted,chgdesc?)'  
<!ENTITY %yesorno'NUMBER'  
<!ENTITY %revatt  
'chg (N|R|U|D) #REQUIRED  
key ID #REQUIRED  
revdate NUMBER #REQUIRED'  
<!ENTITY %ISOtech PUBLIC  
'ISO 8879-1986//ENTITIES General Technical//EN'  
<!ENTITY %ISOpub PUBLIC  
'ISO 8879-1986//ENTITIES Publishing//EN'  
<!ENTITY %ISOnum PUBLIC  
'ISO 8879-1986//ENTITIES Numeric and Special Graphic//EN'>  
<!ENTITY %ISOgrk1 PUBLIC  
'ISO 8879-1986//ENTITIES Greek Letters//EN'  
%ISOtech; %ISOpub; %ISOnum; %ISOgrk1;  
<-- FRMFIM TOP LEVEL STRUCTURE  
<-- FRMFIM 顶层结构-->  
<-- ELEMENT FRMFIM ((title,effxref,transltr,frmfmatr,fimfmatr,chapter+,mstfltab,cabinloc)|increv|tr+)  
+(revst|revend|cocst|cocend|docunit|hotlink)>
```

```txt
spl CDATA #REQUIRED  
model CDATA #REQUIRED  
oidate NUMBER #REQUIRED  
revdate NUMBER #REQUIRED  
tsn CDATA #REQUIRED  
cus CDATA #IMPLIED  
cusname CDATA #IMPLIED  
docnbr CDATA #IMPLIED  
lang CDATA #REQUIRED  
chg (N|R|U) 'N'
```

```txt
<!ELEMENT increv -- (transltr?, frmtrlst?, fimtrlst?, (chapter | section | subject | pgblk | task | subtask | sheet | graphic | mstfltab | faultrow | frmintro | fimintro | fimusage | effxref | sblist | cabinloc | acrolist)) +>
```

```txt
<!ELEMENT tr -- (trfmatr, (chapter | section | subject+ | pgblk+ | task+ | subtask+ | sheet+
```

```txt
| graphic+ | frmintro | fimintro | effxref
| sblist | mstfltab | faultrow* | cabinloc
| acrolist) >  
<!ELEMENT trfmatr -- (title, trxref, revhist, trreason,
(%text;?) >  
<!ATTLIST trfmatr
trnbr CDATA #REQUIRED
trdel CDATA #IMPLIED
trepl CDATA #IMPLIED
issdate NUMBER #REQUIRED >  
<!ELEMENT trxref -- (paptnbr+) >  
<!ELEMENT paptnbr -- (#PCDATA) >  
<!ATTLIST paptnbr
issdate NUMBER #REQUIRED >  
<!ELEMENT revhist -- (prclist1) >  
<!ELEMENT treason -- (#PCDATA) >  
<!ELEMENT transltr -- (chgdesc*, title, (prclist1 | %text;)) >  
<!ATTLIST transltr
%revatt; >  
<!ELEMENT effxref -- (chgdesc*, title, (%text);?, effdata+) >  
<!ATTLIST effxref
%revatt; >  
<!ELEMENT effdata -- (cus?, modtype?, cec, linenbr?, venbr?, benbr?, msnbr, acn) >  
<!ELEMENT cus -- (#PCDATA) >  
<!ELEMENT modtype -- (#PCDATA) >  
<!ELEMENT cec -- (#PCDATA) >  
<!ELEMENT linenbr -- (#PCDATA) >  
<!ELEMENT venbr -- (#PCDATA) >  
<!ELEMENT benbr -- (#PCDATA) >  
<!ELEMENT msnbr -- (#PCDATA) >  
<!ELEMENT acn -- (#PCDATA) >  
<!-- FRMFIM FRONT MATTER ->  
<!-- FRMFIM 前页 ->  
<!-- FRMFIM FRFIMFRMFRFIMFRFIMFRFIMFRFIMFRFIMFRFIMFRFIMFRFIMFRFIMFRFIMFRFIMFRFIMFRFIMFRFIMFRFIMFRFIMFRFIMFRFIMFRFIMFRFIMFRFIMFRFIMFRFIMFRFIMFRFIMFRFIMFRFIMFRFIMFRFIMFRFIMFRFIMFRFIMFRFIMFRFIM
```

```txt
%revatt;  
<!ELEMENT trlist -- ((%text);, (trdata+ | isempty))  
<!ELEMENT trdata -- (tmbr, trstatus, trloc+)  
<!ELEMENT tmbr -- (#PCDATA)  
<!ELEMENT trstatus -- (#PCDATA)  
<!ELEMENT trloc -- (#PCDATA)  
<!ELEMENT frmintro -- (chgdesc*, title, (prclist1 | %text);, acrolist)  
<!ATTLIST frmintro %revatt;  
<!ELEMENT frmintro -- (chgdesc*, title, (prclist1 | %text);, acrolist, panloc)  
<!ATTLIST frmintro %revatt;  
<!ELEMENT acrolist -- (chgdesc*, title, acrodata+)  
<!ATTLIST acrolist %revatt;  
<!ELEMENT acrodata -- (acro, acrodef)  
<!ELEMENT acro -- (#PCDATA)  
<!ELEMENT acrodef -- (#PCDATA)  
<!ELEMENT panloc -- (prclist1)  
<!ELEMENT sblist -- (chgdesc*, title, %text; (sbdata+ | isempty))  
<!ATTLIST sblist %revatt;  
<!ELEMENT sbdata -- (sbnbr?, sbtitle?, eonbr?, atanbr*, mdnbr*, cocnbr*, sc?, ics, custeff?)  
<!ELEMENT sbnbr -- (#PCDATA)  
<!ELEMENT sbtitle -- (#PCDATA)  
<!ELEMENT eonbr -- (#PCDATA)  
<!ELEMENT atanbr -- (#PCDATA)  
<!ELEMENT mdnbr -- (#PCDATA)  
<!ELEMENT cocnbr -- (#PCDATA)  
<!ELEMENT sc -- (#PCDATA)  
<!ELEMENT ics -- (#PCDATA)  
<!ELEMENT custeff -- (cus, effrc)+  
<!ELEMENT effrc -- (#PCDATA)  
<!ELEMENT fimusage -- (chgdesc*, title, (prclist1 | %text;))  
<!ATTLIST fimusage %revatt;
```

```sgml
<!-- ->  
<!-- MASTER FAULT TABLE & CABIN LOCATION ->  
<!-- 主故障表和客舱位置 ->
```

```sql
<!ELEMENT mstfltab -- (faultrow+) >  
<!ATTLIST mstfltab %revatt;  
<!ELEMENT faultrow -- ((faultcode, custdata?, faltdesc+, fmsgdesc?, (mmsgtref | taskref | stdref)) | %deleted;)  
<!ATTLIST faultrow %revatt;  
<!ELEMENT mmsgtref -- (taskref?, (maintmsg, taskref) +)  
<!ELEMENT faltcode -- (#PCDATA)  
<!ATTLIST faltcode faultype CDATA #REQUIRED >  
<!ELEMENT custdata -- (#PCDATA)  
<!ELEMENT faltdesc -- (effect?, fltlatch?, fltdata)  
<!ATTLIST faltdesc fmsglvl CDATA #REQUIRED  
fdescver (pri|alt1|alt2|alt3) #IMPLIED >  
<!ELEMENT fltlatch -- (#PCDATA)  
<!ELEMENT fltdata -- (fkeytext, fsubprob?, faultloc?)  
<!ELEMENT fkeytext -- (#PCDATA)  
<!ELEMENT fsubprob -- (#PCDATA)  
<!ELEMENT faultloc -- (#PCDATA)  
<!ELEMENT fmsgdesc -- (fmsgdata | (effect, fmsgdata) +)  
<!ELEMENT fmsgdata -- (#PCDATA)  
<!ELEMENT mainmsg -- (effect?, mmsgdata)  
<!ATTLIST mainmsg mmsgnbr CDATA #IMPLIED >  
<!ELEMENT mmsgdata -- (#PCDATA)  
<!ELEMENT taskref -- (refint | refext | taskdata) +  
<!ELEMENT taskdata -- (#PCDATA)  
<!ELEMENT stdref -- (#PCDATA)  
<!ELEMENT cabinloc -- (%text;)  
<!ATTLIST cabinloc oldkey NAME #IMPLIED  
%revatt;  
<-- CHAPTER ->  
<--章 ->  
<--CHAPTER chapter -- ((effect, chgdesc*, title, section+) | %deleted;)
```

```txt
<!ATTLIST chapter
chapnbr NUMBER #REQUIRED
%revatt;
<--->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->-->
<----SECTION
<----节
<---->---→
<--ELEMENT section -- ((chgdesc*, title, subject+) | %deleted);
<--ATTLIST section
chapnbr NUMBER #REQUIRED
sectnbr NUMBER #REQUIRED
%revatt;
<---->---→
<----SUBJECT
<----标题
<---->---→
<--ELEMENT subject -- ((chgdesc*, title, pgblk+) | %deleted);
<--ATTLIST subject
chapnbr NUMBER #REQUIRED
sectnbr NUMBER #REQUIRED
subjnbr NUMBER #REQUIRED
%revatt;
<----PAGEBLOCK
<----页号组
<---->---→
<--ELEMENT pgblk -- ((effect, chgdesc*, title, pbfmatr?, (task+|prlist1)?, graphic*) | %deleted);
<--ATTLIST pgblk
chapnbr NUMBER #REQUIRED
sectnbr NUMBER #REQUIRED
subjnbr NUMBER #REQUIRED
pgblknbr NUMBER #REQUIRED
confnbr NUMBER #IMPLIED
%revatt;
<--ELEMENT pbfmatr -- (title, %g.r.; (list1 | %text;))
<---->---→
<TASK
<----任务
<---->---→
<--ELEMENT task -- ((effect, chgdesc*, title, %g.r.; %w.c;
```

```txt
note\*, tfmatr?, topic\*, graphic\*)  
|%deleted;）  
<!ATTLIST task  
chapnbr NUMBER #REQUIRED  
sectnbr NUMBER #REQUIRED  
subjnbr NUMBER #REQUIRED  
func CDATA #REQUIRED  
seq CDATA #REQUIRED  
confltr CDATA #IMPLIED  
varnbr NUMBER #IMPLIED  
alunqi CDATA #IMPLIED  
pgblknbr NUMBER #REQUIRED  
confnbr NUMBER #IMPLIED  
%revatt;
```

```txt
<!-- Meanless: <icon/>-->
```

```txt
<!-- TASK ASSOCIATED ELEMENTS -->
```

```txt
<!-- 任务相关的元素 -->
```

```asp
<!-- Meanless: <1-->
```

```batch
<!ELEMENT tfmatr -- (pretopic+)
```

```lisp
<!ELEMENT pretopic -- (title, (%text; | list1)) + (effect)
```

```txt
<!ELEMENT topic -- (effect?, title, %g.r;, %w.c;, note*, subtask*)
```

```txt
<!-- Meanless: <---->
```

```txt
<!-- SUBTASK -->
```

```txt
<!-- 子任务-->
```

```txt
<!-- Meanless: <---->
```

```txt
<!ELEMENT subtask -- ((effect, chgdesc*, %g.r; %w.c; note*, list1) |%deleted;) + (effect)
```

```txt
<!ATTLIST subtask
chapnbr NUMBER #REQUIRED
sectnbr NUMBER #REQUIRED
subjnbr NUMBER #REQUIRED
func CDATA #REQUIRED
seq CDATA #REQUIRED
confltr CDATA #IMPLIED
vambr NUMBER #IMPLIED
alunqi CDATA #IMPLIED
pgblknbr NUMBER #REQUIRED
confnbr NUMBER #IMPLIED
%revatt;
```

```asp
<!-- Meanless: <1-->
```

```txt
<!-- PROCEDURE LIST STRUCTURE
```

# <!-- 程序清单结构-->

<table><tr><td>&lt;!ELEMENT prclist1</td><td>--</td><td>(prcitem1+)</td><td>+(effect)</td><td>&gt;</td></tr><tr><td>&lt;!ELEMENT prclist2</td><td>--</td><td>(prcitem2+)</td><td></td><td>&gt;</td></tr><tr><td>&lt;!ELEMENT prclist3</td><td>--</td><td>(prcitem3+)</td><td></td><td>&gt;</td></tr><tr><td>&lt;!ELEMENT prclist4</td><td>--</td><td>(prcitem4+)</td><td></td><td>&gt;</td></tr><tr><td>&lt;!ELEMENT prclist5</td><td>--</td><td>(prcitem5+)</td><td></td><td>&gt;</td></tr><tr><td>&lt;!ELEMENT prclist6</td><td>--</td><td>(prcitem6+)</td><td></td><td>&gt;</td></tr><tr><td>&lt;!ELEMENT prclist7</td><td>--</td><td>(prcitem7+)</td><td></td><td>&gt;</td></tr><tr><td>&lt;!ELEMENT prclist1</td><td>--</td><td>(prcitem, prclist2?, graphic*)</td><td></td><td>&gt;</td></tr><tr><td>&lt;!ELEMENT prclist2</td><td>--</td><td>(prcitem, prclist3?)</td><td></td><td>&gt;</td></tr><tr><td>&lt;!ELEMENT prclist3</td><td>--</td><td>(prcitem, prclist4?)</td><td></td><td>&gt;</td></tr><tr><td>&lt;!ELEMENT prclist4</td><td>--</td><td>(prcitem, prclist5?)</td><td></td><td>&gt;</td></tr><tr><td>&lt;!ELEMENT prclist5</td><td>--</td><td>(prcitem, prclist6?)</td><td></td><td>&gt;</td></tr><tr><td>&lt;!ELEMENT prclist6</td><td>--</td><td>(prcitem, prclist7?)</td><td></td><td>&gt;</td></tr><tr><td>&lt;!ELEMENT prclist7</td><td>--</td><td>(prcitem)</td><td></td><td>&gt;</td></tr><tr><td>&lt;!ELEMENT prclist</td><td>--</td><td>(title?, %w.c;, (%text;)?)</td><td></td><td>&gt;</td></tr></table>

<table><tr><td>&lt;-- STANDARD Lists</td><td>-&gt;</td></tr></table>

<table><tr><td>标准清单</td><td>→</td></tr></table>

<table><tr><td>&lt;!ELEMENT</td><td>list1</td><td>--</td><td>(11item+)</td><td>&gt;</td></tr><tr><td>&lt;!ELEMENT</td><td>list2</td><td>--</td><td>(ltitle?, l2item+)</td><td></td></tr><tr><td>&lt;!ELEMENT</td><td>list3</td><td>--</td><td>(l3item+)</td><td>&gt;</td></tr><tr><td>&lt;!ELEMENT</td><td>list4</td><td>--</td><td>(l4item+)</td><td>&gt;</td></tr><tr><td>&lt;!ELEMENT</td><td>list5</td><td>--</td><td>(l5item+)</td><td>&gt;</td></tr><tr><td>&lt;!ELEMENT</td><td>list6</td><td>--</td><td>(l6item+)</td><td>&gt;</td></tr><tr><td>&lt;!ELEMENT</td><td>list7</td><td>--</td><td>(l7item+)</td><td>&gt;</td></tr></table>

<table><tr><td>&lt;!ELEMENT 11item</td><td>--</td><td>(%w.c.;, %text;, ((list2 | art), note*) *)&gt;</td></tr><tr><td>&lt;!ELEMENT 12item</td><td>--</td><td>(%w.c.;, %text;,(list3, note*)?)</td></tr><tr><td>&lt;!ELEMENT 13item</td><td>--</td><td>(%w.c.;, %text;,(list4, note*)?)</td></tr><tr><td>&lt;!ELEMENT 14item</td><td>--</td><td>(%w.c.;, %text;,(list5, note*)?)</td></tr><tr><td>&lt;!ELEMENT 15item</td><td>--</td><td>(%w.c.;, %text;,(list6, note*)?)</td></tr><tr><td>&lt;!ELEMENT 16item</td><td>--</td><td>(%w.c.;, %text;,(list7, note*)?)</td></tr><tr><td>&lt;!ELEMENT 17item</td><td>--</td><td>(%w.c.;, %text;)</td></tr></table>

<table><tr><td>&lt;!--ACTION RESULT TABLE--&gt;</td></tr></table>

<table><tr><td>操作结果表 -&gt;</td></tr><tr><td>-&gt;</td></tr></table>

<table><tr><td>&lt;!ELEMENT art</td><td>--</td><td>((%w.c; note*, action)+)</td></tr><tr><td>&lt;!ELEMENT action</td><td>--</td><td>(%text:, result*)</td></tr></table>

<table><tr><td>&lt;!ELEMENT result</td><td>--</td><td>(%text;)</td></tr></table>

<table><tr><td>&lt;--</td><td>TABLE (CELLULAR, CALS BASED)</td><td>-&gt;</td></tr></table>

表（单元，基于CALS）->

```txt
<!-- --->  
<!ELEMENT table -- ((title?, tgroup, ftnote*) | graphic+)  
-(table) >
```

```batch
<!ATTLIST table
tabstyle NMTOKEN #IMPLIED
frame (top|bottom|topbot|all|sides|none) #IMPLIED
colsep %yesorno; #IMPLIED
rowsep %yesorno; #IMPLIED
orient (port|land) #IMPLIED
pgwide %yesorno; #IMPLIED
id ID #IMPLIED
```

```txt
<!ELEMENT tgroup -o (colspec*, spanspec*, thread?, tfoot?, tbody)
```

```txt
<!ATTLIST tgroup  
cols NUMBER #REQUIRED  
colsep %esorno; #IMPLIED  
rowsep %esorno; #IMPLIED  
align (left|right|center|justify|char) 'left'  
charoff NUTOKEN '50'  
char CDATA "
```

```batch
<!ELEMENT colspec -o EMPTY >  
<!ATTLIST colspec
```

```batch
colnum NUMBER #IMPLIED
colname NMTOKEN #IMPLIED
align (left|right|center|justify|char) #IMPLIED
charoff NUTOKEN #IMPLIED
char CDATA #IMPLIED
colwidth CDATA #IMPLIED
colsep %yesorno; #IMPLIED
rowsep %yesorno; #IMPLIED
```

```txt
<!ELEMENT spanspec - o EMPTY >  
<!ATTLIST spanspec
```

```csv
nastest NMTOKEN #REQUIRED
nameend NMTOKEN #REQUIRED
spanname NMTOKEN #IMPLIED
align (left|right|center|justify|char) 'center'
charoff NUTOKEN #IMPLIED
char CDATA #IMPLIED
colsep %esorno; #IMPLIED
rowsep %esorno; #IMPLIED
<!ELEMENT thad -o (colspec*, row+) >>
<!ATTLIST thad
valign (top|m middle|bottom) 'bottom'
```

<!ELEMENT tfoot -o (colspec*, row+) >  
<!ATTLIST tfoot valign (top|middle|bottom) 'top'  
<!ELEMENT tbody -o (row+)  
<!ATTLIST tbody  
valign (top|middle|bottom) 'top'  
<!ELEMENT row -o (entry+)  
<!ATTLIST row
rowsep %yesorno; #IMPLIED  
<!ELEMENT entry -o (%text; |%w.c;|graphic)*  
<!ATTLIST entry

colname NMTOKEN #IMPLIED

namest NMTOKEN #IMPLIED

nameend NMTOKEN #IMPLIED

spanname NMTOKEN #IMPLIED

morerows NUMBER '0'

colsep %yesorno; #IMPLIED

rowsep %yesorno; #IMPLIED

rotate %yesorno; '0'

valign (top|middle|bottom) 'top'

align (left|right|center|justify|char) #IMPLIED

charoff NUTOKEN #IMPLIED

char CDATA #IMPLIED

<!ELEMENT fnote -- %text;  
<!ATTLIST ftnote

ftnoteid ID #REQUIRED

<!-- Meanless:  $\rightarrow$ -->  
<!-- GRAPHIC REFERENCING MECHANISM -->  
<!-- 图形参考机制-->  
<!-- Meanless:-->  
<!ELEMENT graphhref -- (effect?, #PCDATA)  
<!ATTLIST graphcoef

refid IDREF #IMPLIED

sheetnbr CDATA #IMPLIED

structid CDATA #IMPLIED

shownow %yesorno '0'

<!ELEMENT graphic -- ((effect, chgdesc*, title?, sheet+)

|%deleted;)

<!ATTLIST graphic

chapnbr NUMBER #IMPLIED

sectnbr NUMBER #IMPLIED

subjnbr NUMBER #IMPLIED

func CDATA #IMPLIED

seq CDATA #IMPLIED

```txt
conflr CDATA #IMPLIED
varnbr NUMBER #IMPLIED
alunqi CDATA #IMPLIED
pgblknbr NUMBER #IMPLIED
confnbr NUMBER #IMPLIED
%revatt;
<!ELEMENT sheet -- ((effect, chgdesc*, title?, gdesc?)
| %deleted;)
<!ATTLIST sheet
gnbr ENTITY #REQUIRED
sheetnbr CDATA #REQUIRED
%revatt;
<!ELEMENT gdesc -- (unlist | numlist)
<!-- ->->>
<!NUMBERED & UN-NUMBERED LIST ->>
<!-- 有编号和无编号的清单 ->>
<!-- ->-><ELEMENT unlist -- (unltem+) ><ATTLIST unlist
bulltype (NONE|BULLET|NDASH|MDASH|DIAMOND|ASTERISK
|DELTA|SQUARE|SYSTEM)
'SYSTEM' ><ELEMENT unltem -- (para+) ><ELEMENT numlist -- (numltem+) ><ATTLIST numlist
numtype (NNP|AUP|NNB|ALB|NNS|RUP|RLP|RUR|RLR|NNR
|AUR|ALR)
'NNP' ><ELEMENT numltem -- (para+) ><-- PARAGRAPH
段 -><--PARAGRAPH CONTENTS -><-- 段内容 -><--
```

<!ELEMENT conname -- (#PCDATA)  
<!ELEMENT csn -- (#PCDATA)  
<!ELEMENT ein -- (#PCDATA)  
<!ELEMENT equ -- (#PCDATA)  
<!ELEMENT ncon -- (#PCDATA)  
<!ELEMENT pan -- (#PCDATA)  
<!ELEMENTrefext -- (#PCDATA)  
<!ATTLISTrefext

refman CDATA #IMPLIED

refspl CDATA #IMPLIED

refmodel CDATA #IMPLIED

docnbr CDATA #IMPLIED

refloc CDATA #IMPLIED

<!ELEMENT refint -- (#PCDATA)

<!ATTLIST refint

retypeof CDATA #IMPLIED

refid IDREF #IMPLIED

<!ELEMENT std -- (stdinbr, stdname)

<!ELEMENT stdnbr -- (#PCDATA)

<!ELEMENT stdname -- (#PCDATA)

<!ELEMENTTed -- (toolnbr, toolname)

<!ELEMENT toolnbr -- (#PCDATA)

<!ELEMENT toolname -- (#PCDATA)

<!ELEMENT txtgraphc -- (txtline+)

<!ELEMENT txtline -- (#PCDATA)

<!ELEMENT zone -- (#PCDATA)

<!-- ---->

<!-- TITLE, etc.

<!-- 标题等-->

<!-- Meanless:-->

<!ELEMENT title -- (#PCDATA | ein | sbnbr) +

<!ELEMENT ltitle -- (#PCDATA)

<!ELEMENT warning -- %text; - (note)

<!ELEMENT note -- %text; - (note)

<!ELEMENT caution -- %text; - (note)

<!-- Meanless:  $\rightarrow$ -->

<!-- EFFECTIVITY -->

<!-- 有效性-->

<!-- Meanless:  $\rightarrow$ -->

<!ELEMENT effect -- ((sbeff | coceff) *) >

<!ATTLIST effect

efrg CDATA #IMPLIED efftext CDATA #IMPLIED

```txt
<!ELEMENT sbeff -O EMPTY  
<!ATTLIST sbeff  
effrg CDATA #IMPLIED  
efftext CDATA #IMPLIED  
sbnbr CDATA #REQUIRED  
sbcond CDATA #REQUIRED  
sbrev CDATA #IMPLIED  
<!ELEMENT coceff -O EMPTY  
<!ATTLIST coceff  
effrg CDATA #IMPLIED  
efftext CDATA #IMPLIED  
cocnbr CDATA #REQUIRED  
<!--  
->  
<!-- MISCELLANEOUS CONSTRUCTIONS TO:  
->  
MARK DOCUMENT UNITS  
->  
MARK DELETED AND REVISED ELEMENTS  
->  
SUPPORT CROSS-REFERENCING MECHANISMS  
->  
其它用途的结构：->  
标记文档单元->  
标记删除和修改元素 ->  
支持对照机制->  
<!--  
->  
<!ELEMENT deleted -O EMPTY  
<!ELEMENT isempty -O EMPTY  
<!ELEMENT revst -O EMPTY  
<!ELEMENT revend -O EMPTY  
<!ELEMENT cocst -O EMPTY  
<!ELEMENT cocend -O EMPTY  
<!ELEMENT chgdesc -- (#PCDATA)  
<!ELEMENT hotlink -O EMPTY  
<!ATTLIST hotlink  
targetid CDATA #IMPLIED  
targetrefid CDATA #IMPLIED  
<!ELEMENT docunit -O EMPTY  
<!ATTLIST docunit  
docunbr CDATA #IMPLIED
```

# 2 结构图表

结构图的可关键组成部分参见 DTD 技术要求（参见[4-2-3.22.4]）。为利用采用交互式阅读器的 DTD 的图形进行工作，使用 DTD 结构树阅读器。

![](images/dc37dc4ffdc8719aebf2b41c8b83d08db4c874b898f0ade7ae8282808a5a3af1.jpg)  
图4-2-26.1 FRM FIM DTD结构一前页

![](images/96ff2b3fd5253814b44d025444e85efcba8dd4f70cd5b093594cac10f22a621d.jpg)  
图4-2-26.2 FRMFIM DTD结构一概述

![](images/01b42c259725cf0bb2f30d5b8229e5ddaa97d4515d00e62503290e609d103bc7.jpg)  
图4-2-26.3 EM DTD结构-Increv和TR

# 4-2-27 飞行机组操作手册(FCOM) DTD

# 1 结构图表

飞行机组操作手册(FCOM)DTD是在DTD技术要求中定义的3级DTD(参见[4-2-1.2.1.4])。按照这个定义，ATAFCOM仅仅是数据生产者主题文档的特定结构框架。不存在一个(标准的)ATAFCOMDTD，因为每个数据生产者的主题是唯一的，因此在下列结构图中仅示出了适用于一个FCOMDTD的ATA框架。

![](images/fd903e16ab88ceaddf64e9d3d61a4ccb350904612ff86b92ac9ffebb8343a615.jpg)  
图4-2-27.1 FCOM DTD纲要结构

![](images/0225831a5a3a68d1cd33f08c51bc9360b4f96f010f04ecf10acc78f1d09cd0e3.jpg)  
图4-2-27.2 FCOM DTD结构一前页

![](images/41d62f93da6e397a18690969b8d27da240b2c911591409fbd0c21f286ac89414.jpg)  
图4-2-27.3 FCOM DTD结构一前言

![](images/e017244e9b9d8444c523a91d1608c3f027bdb6689d9eef2a27f80ad2f1f3ec01.jpg)  
图4-2-27.4 FCOM DTD结构一节和程序

# 2 ATA FCOM 级别，三种结构图表的术语表

元素：abnemer

识别FCOM异常的，非正常的，以及紧急情况的程序和检查清单。

元素：fcom

这个标记标识一个飞机机组操作手册(最初版本、再版，部分更改的集合，临时更改，或通告)。元素：manufacturer defined（由制造商定义）

每个制造商定义他们自己的结构。

元素：normal（正常）

标识FCOM正常程序。

元素：proc

标识支持飞机操作要求规定步骤的一张有序步骤的列表。

元素：reffmend

标识手册内容结尾的空元素，这个手册内容的结尾可包含在一个边界框架中。

元素：reffmst

标识手册内容开始的空元素，这个手册内容的开始可包含在一个边界框架中。

元素：vol

卷是FCOM章或节的一个逻辑组。FCOM可以有一个或多个卷。

# 4-2-28 有效位置标识清单(LEA)DTD

# 1 LEA(有效位置标识清单)DTD

```txt
<!---->  
<!-- This is the common List of Effective Anchors DTD used by -->  
<!-- all ATA DTDs. -->
```

```txt
<!--这是由所有的ATA DTD均可使用的有效位置标识清单(LEA)DTD-->  
<!---->
```

```txt
<!-- DTD Reference : "/ATA-TEXT//DTD LEA-VER1//EN" ->  
<!-- DTD 参考: "/ATA-TEXT//DTD LEA-VER1//EN" ->  
<!-- Revision Date : 01 March 96
```

```txt
<!--更改日期：1996年3月1日 -->  
<!-- Highlights：Updated LEA per Tech Req 2100 Ver 3.2 -->
```

```txt
<!-- dated March 1996: --  
-- Changed LEA DTD to make it common for --  
all DTDs. --  
-- Add element "anchor" and the following --  
-- attributes: --  
-- chg --  
-- tagname --  
-- treeloc --  
-- Deleted "chg" attribute from LEA element --
```

```txt
<!--更改摘要：按2100技术要求的版本3.2更新了LEA  
<!--更改日期：1996年3月：
```

```txt
$<  ! - -$  改变了LEADTD，以使它成为所有DTD通用的LEADTD->  
 $<  ! - -$  增加了“anchor”元素及以下属性
```

```txt
<!-- chg ->  
<!-- tagname ->
```

<!-- treeloc --

$<  ! - -$  从LEA元素中删除了“chg”属性

<!-- Meanless: ->

<!---->

<!DOCTYPE LEA[

$<  ! - -$  The following set of declarations may be referred to using a public entity as follows:

```txt
<!DOCTYPE LEA PUBLIC
  "/ATA-TEXT//DTD LEA-VER1//EN."[>]
```

<!ELEMENT LEA -- (anchor+)

```shell
<!ATTLIST LEA  
spl CDATA #REQUIRED  
model CDATA #REQUIRED  
oidate NUMBER #REQUIRED  
revdate NUMBER #REQUIRED  
tsn CDATA #REQUIRED  
cus CDATA #IMPLIED  
docnbr CDATA #IMPLIED  
cusname CDATA #IMPLIED  
lang CDATA #REQUIRED
```

<!ELEMENT anchor -o EMPTY

```txt
<!ATTLIST anchor
key ID #REQUIRED
revdate NUMBER #REQUIRED
chg (N|R|U|D) #REQUIRED
tagname NMTOKEN #REQUIRED
treeloc NUMBER #REQUIRED
```

]>

# 4-2-29 主最低设备清单(MMEL)DTD

# 1 MMEL DTD

<!-- Meanless: ->

<!-- DTD header

<!- DTD程序头

<!-- Meanless:-->

<!-- Meanless: ->

<!-- This DTD is for the Master Minimum Equipment List

$<  ! - -$  of the Federal Aviation Administration.

<!--这是联邦航空管理局的主最低设备清单 DTD-->

<!-- Meanless: ->

<!-- DTD Reference: "/ATA-TEXT//DTD FAAMMEL-VER4-

LEVEL2//EN" ->

<!-- DTD 参考："//ATA-TEXT//DTD FAAMMEL-VER4- LEVEL2//EN" -->

<!-- DTD Level : 2

<!--DTD级别：2

<!-- Rev. Date : 22 January 96 -->

<--更改日期：1996年1月22日

<!-- Highlights : Update DTD per Tech Req 2100 Ver3.2: -->

- Remove poschg and poskey from

<!-- entity %revatt

<!----更改摘要：按2100技术要求版本3.2更新了DTD-->

$<  ! - -$  一从实体%revatt中删除poschg和poskey

<!---->

<!DOCTYPE faammel [

$<  ! - >$  The following set of declarations may be referred

to using a public entity as follows:

<!DOCTYPE faammel PUBLIC

"-//ATA-TEXT//DTD FAAMMEL-VER4-LEVEL2//EN"[ ]>

<!-- Meanless:-->

<!-- ENTITIES

<!-- 实体-->

<!-- Meanless:-->

<!ENTITY % ref "refext | refint"

<!ENTITY % text "para | unlist | numlist | txtgrphc) *">

<!ENTITY % revatt

<table><tr><td>&quot;chg</td><td>(N|R|U|D)</td><td>#REQUIRED</td></tr><tr><td>key</td><td>ID</td><td>#REQUIRED</td></tr><tr><td>revdate</td><td>NUMBER</td><td>#REQUIRED</td></tr><tr><td>tsn</td><td>CDATA</td><td>#REQUIRED</td></tr><tr><td>tsntype</td><td>CDATA</td><td>#IMPLIED &quot; &gt;</td></tr></table>

<!ENTITY % yesorno "NUMBER"

<!-- Meanless:-->

FAA MMEL HIGH LEVEL STRUCTURE

<!-- FAAMMEL高层结构-->

<!-- Meanless:-->

<!ELEMENT faammel -- ((mfmatr, chapter+) | increv) + (revst | revend | hotlink | %ref) >

<!ATTLIST faammel

model CDATA #REQUIRED

oidate NUMBER #REQUIRED

revdate NUMBER #REQUIRED

tsn CDATA #REQUIRED

tsntype CDATA #IMPLIED

chg (N|R) #REQUIRED

lang CDATA #REQUIRED

cusname CDATA #IMPLIED

spl CDATA #REQUIRED

farid CDATA #IMPLIED

status (A|P|D) #REQUIRED

<!---->

FAA MMEL INIncrementAL REVISION

<!-- FAAMMEL增加性更改-->

<!---->

```typescript
<!ELEMENT increv -- (meldef | preamble | omsect | chapter | section | item | subitem1 | subitem2 | subitem3) +
```

```txt
<!ATTLIST mfmatar %revatt;
```

<!-- ->  
FAA MMEL FRONT MATTER  
<!-- FAA MMEL 前页-->  
<!---->  
<!ELEMENT mfmatr -- (mmelDefs, preamble, omsect?) >  
FAA MMEL DEFINITIONS  
$<  >$  These definitions each constitute an anchor  
$<  ! - -$  Each definition has its use specified as being  
<-- MMEL or MEL use.  
Each definition has a fleet for which it is  
<!-- effective. The effrg is specified in the -->  
<!-- effxref table. For the MMEL, this table  
$<  ! - -$  is simply the effrg and its corresponding  
$<  ! - >$  fleet.  
<!-- Effect is used to select proper definitions for -->  
$<  >$  
FAA MMEL 说明  
<!-- 按照这些定义的每一个都可形成一个位置标识

在MMEL或MEL使用时，每个定义有它特定的用途。

$<  ! - >$  每个定义都有其有效的机群。

在effxref表中指定effrg。

$<  ! - >$  对于MMEL，这个表仅包含effrg及其相应的机群。

$<  ! - >$  任何特定的MMEL选择这些定义时，利用其作用可选择适当的定义。  $\rightarrow >$

<!-- -- ->

<!ELEMENT mmelrefs -- (effxref, meldef+)

<!ATTLIST mmelDefs %revatt;

<!ELEMENT effxref -- (effrg, fleet) +

<!ELEMENT effrg -- (#PCDATA)

<!ELEMENT fleet -- (#PCDATA)

<!ELEMENT meldef -- (effect, chgdesc*, term, def)

<!ATTLIST meldef mmeluse %yesorno #IMPLIED meluse %yesorno #IMPLIED %revatt;

<!ELEMENT effect -o EMPTY

<!ATTLIST effect effrg CDATA #IMPLIED

<!ELEMENT term -- (#PCDATA)

<!ELEMENT def -- (para|subdef) + +(mmelnote)

<!ELEMENT subdef -- (effect, stern, sdef)

<!ELEMENT stern -- (#PCDATA)

<!ELEMENT sdef -- (para+)

<!---->

<!-- FAA MMEL PREAMBLE -->

FAAMMEL前言

<!---->

<!ELEMENT preamble -- (chgdesc*, para+)

<!ATTLIST preamble %revatt;

<!-- Meanless:  $\rightarrow$ -->

FAA MMEL O&M SECTION

<!-- FAAMMELO和M节 -->

<!-- Meanless: ->

```txt
<!ELEMENTomsect -- (chgdesc\*, (para\*, omproc+)+) > <!ATTLISTomsect %revatt;
```

```txt
<!ELEMENT omproc -- (para|unlist|list1|txtgraphc| mmelnote|notelist) *
```

```tcl
<!ATTLIST omproc  
chapnbr NUMBER #REQUIRED  
sectnbr NUMBER #IMPLIED  
itemnbr NUMBER #REQUIRED  
sitem1nbr NUMBER #IMPLIED  
maint %yesorno; "0"  
ops %yesorno; "0"
```

```txt
<!-- =>  
<!-- CHAPTER ->
```

```javascript
$<  ! - -$  It corresponds to a specific ATA allocated
```

```txt
$<  ! - -$  chapter. The first level of qualification in the  $\rightarrow$ $<  ! - -$  manual.
```

```txt
$<  ! - -$  章
```

```txt
<!-- 它与一个ATA分配的特定章相一致 -->
```

```txt
在手册中限定的第一级别。
```

```txt
<!---->
```

```javascript
<!ELEMENT chapter -- (chgdesc*, title, (section+|item+))>
```

```txt
<!ATTLIST chapter
chapnbr NUMBER #REQUIRED
%revatt;
```

```asp
<!-- Meanless:-->
```

```txt
<!-- SECTION -->
```

```txt
<!-- 节-->
```

```txt
<!-- ---->
```

```txt
<!ELEMENT section -- (chgdesc*, title?, item+) >
```

```txt
<!ATTLIST section
chapnbr NUMBER #REQUIRED
sectnbr NUMBER #REQUIRED
%revatt;
```

```txt
<!---->
```

```txt
<!-- ITEM of the MMEL
```

```txt
<!-- It corresponds to a NUMBERed MMEL item -->
```

```txt
<!--MMEL item NUMBER consists of the ATA section NUMBER-->
```

<!-- followed by the MMEL item sequence NUMBER. -->

<-- MMEL的项目 -->

<!--它相对应于一个有编号的MMEL项目-->

<!--MMEL项目号由ATA节编号在其后加上MMEL项目顺序编号组成-->

<!-- -- -->

<!ELEMENT item -- (chgdesc*, title, (((dispcond, subitem1*) | subitem1*) | deleted)) >

<!ATTLIST item
chapnbr NUMBER #REQUIRED
sectnbr NUMBER #IMPLIED
itemnbr CDATA #REQUIRED
opteqp %yesorno "0"
dup %yesorno "0"
%revatt;

<!---->

<!-- SUB-ITEM of the MMEL -->

$<  ! - -$  Next level of indent, usually 1), 2).

MMEL的分项目

$<  ! - -$  缩进的下一个级别通常为1)，2).

<!--  $\rightarrow$

<!ELEMENT subitem1 -- (chgdesc*, title, ((dispcond, subitem2*) | subitem2+) | deleted))

<!ATTLIST subitem1
chapnbr NUMBER #REQUIRED
sectnbr NUMBER #IMPLIED
itemnbr CDATA #REQUIRED
sitem1nbr CDATA #REQUIRED
opteqp %yesomo "0"
dup %yesomo "0"
%revatt;

<!-- Meanless:-->

SUB/SUB-ITEM of the MMEL

<-- MMEL的分/分项目 -->

<!-- Meanless: ->

<!ELEMENT subitem2 -- (chgdesc*, title, ((dispcond, subitem3*) | subitem3+) | deleted))

<!ATTLIST subitem2

<table><tr><td>chapnbr</td><td>NUMBER</td><td>#REQUIRED</td></tr><tr><td>sectnbr</td><td>NUMBER</td><td>#IMPLIED</td></tr><tr><td>itemnbr</td><td>CDATA</td><td>#REQUIRED</td></tr><tr><td>sitem1nbr</td><td>CDATA</td><td>#REQUIRED</td></tr><tr><td>sitem2nbr</td><td>CDATA</td><td>#REQUIRED</td></tr><tr><td>opteqp</td><td>%yesorno</td><td>&quot;0&quot;</td></tr><tr><td>dup</td><td>%yesorno</td><td>&quot;0&quot;</td></tr><tr><td>%revatt;</td><td></td><td></td></tr></table>

<!-- Meanless:-->

<!-- SUB/SUB/SUB-ITEM of the MMEL

-- MMEL的分/分/分项目 --

<!-- Meanless:-->

<!ELEMENT subitem3 -- (chgdesc*, title, (dispcond | deleted))

<table><tr><td colspan="3">&lt;!ATTLIST subitem3</td></tr><tr><td>chapnbr</td><td>NUMBER</td><td>#REQUIRED</td></tr><tr><td>sectnbr</td><td>NUMBER</td><td>#IMPLIED</td></tr><tr><td>itemnbr</td><td>CDATA</td><td>#REQUIRED</td></tr><tr><td>sitem1nbr</td><td>CDATA</td><td>#REQUIRED</td></tr><tr><td>sitem2nbr</td><td>CDATA</td><td>#REQUIRED</td></tr><tr><td>sitem3nbr</td><td>CDATA</td><td>#REQUIRED</td></tr><tr><td>opteqp</td><td>%yesorno</td><td>&quot;0&quot;</td></tr><tr><td>dup</td><td>%yesorno</td><td>&quot;0&quot;</td></tr><tr><td>%revatt;</td><td></td><td></td></tr></table>

<!-- Meanless:  $\rightarrow$ -->

<!-- DISpatch CONDITIONS

分配条件

<!-- ---->

<!ELEMENT dispcond -- (remark)?

<table><tr><td>@categ</td><td>(A|B|C|D|X)</td><td>#REQUIRED</td></tr><tr><td>nbrins</td><td>CDATA</td><td>#REQUIRED</td></tr><tr><td>nbrreq</td><td>CDATA</td><td>#REQUIRED</td></tr></table>

<!ELEMENT remark -- (para|unlist|list1|txtgraphc| mmelnote|notelist) *

<table><tr><td colspan="3">&lt;!ATTLIST remark</td></tr><tr><td>maint</td><td>%yesorno</td><td>&quot;0&quot;</td></tr><tr><td>ops</td><td>%yesorno</td><td>&quot;0&quot;</td></tr></table>

<!---->  
<!-- TITLE -->  
<!-- 标题-->  
<!---->  
<!ELEMENT title -- (#PCDATA)  
<!---->  
<!-- TXTGRPHC to set simple tables -->  
<!-- 设置简单的表的 TXTGRPHC -->  
<!---->  
<!ELEMENT txtgrphc -- (txtline+)  
<!ELEMENT txtline -- (#PCDATA)  
<!---->  
UNNUMBEREDLISTS  
<!-- 无编号的清单-->  
<!-- ->  
<!ELEMENT unlist -- (unltem+)  
<!ATTLIST unlist  
bulltype (NONE|BULLET|NDASH|MDASH|DIAMOND|ASTERISK|DELTA|SQUARE|SYSTEM) "SYSTEM">  
<!ELEMENTunltem -- (para+)  
<!ELEMENT para -- (#PCDATA)  
<!-- Meanless:-->  
<!--DELETED is a placeholder for deleted material -->  
<!-- 删除是已删除内容的占位符-->  
<!---->  
<!ELEMENT deleted -o empty  
<!ATTLIST deleted deltype (D|M|I) "D"  
<!-- Meanless: ->  
NUMLIST  
$<  ! -$  编号清单  
<!-- Meanless:-->  
<!ELEMENT numlist -- (numltem+)  
<!ATTLIST numlist numtype (NNP|AUP|NNB|ALB|NNS|RUP|RLP|RUR|

# RLR|NNR|AUR|ALR) "NNP"

<!ELEMENT numltem -- (para+)

<!-- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -

<!-- NUMBERED Lists Levels 1-4

有编号的清单 1-4级

<!---->

<!ELEMENT list1 -- (11item+)

<!ELEMENT list2 -- (12item+)

<!ELEMENT list3 -- (13item+)

<!ELEMENT list4 -- (l4item+)

<!-- Meanless:-->

<!-- LIST ITEMS

$<  ! - -$  清单项目

<!-- ---->

<!ELEMENT 11item -- ((mmelnote | notelist | %text;) +, list2?)

<!ELEMENT 12item -- ((mmelnote | notelist | %text;) +, list3?)

<!ELEMENT 13item -- ((mmelnote | notelist | %text;) +, list4?)

<!ELEMENT l4item -- (mmelnote | notelist | %text;) +

<!-- Meanless:  $\rightarrow$ -->

<!-- NOTES (NUMBERED and UNNUMBERED) --

$<  ! - -$  注释（有编号和无编号的）

<!---->

<!ELEMENTnotelist - - (mmelnote)+

<!ELEMENT mmelnote -- (para | numlist | unlist) +

<!-- Meanless: ->

<!-- REVISION MARKING

<!-- 更改标记 -->

<!-- Meanless:-->

<!ELEMENT revst -o EMPTY

<!ELEMENT revend -o EMPTY

![](images/9d23bb0534b20f5f4826fed4a04cea7afc5905ab68296a768b6a49430ce3eb2b.jpg)

# 2 结构图表

结构图的可关键组成部分参见 DTD 技术要求(参见[4-2-3.22.4])。为利用采用交互式阅读器的 DTD 的图形进行工作, 使用 DTD 结构树阅读器。

![](images/d83ec511f4d5edf500d65e0e78372e18badaa3ab5eeb5000833a5aa72df6a20a.jpg)  
图4-2-29.1 MMEL DTD结构一前页(Mfmatr)

# 4-2-30 维修计划文件(MPD)DTD

# 1 MPD DTD

<!-- Meanless:-->

<!-- This is the ATA DTD for the Maintenance Planning Document

<!--这是维修计划文件的ATA DTD-->

<!---->

<!-- DTD Reference : ATA TEXT.MPDDTD V4

<!-- DTD参考：ATA TEXT.MPDDTDV4

<!-- DTD Level : LEVEL2

<!--DTD级别：2级 ->

Rev Date : November 1, 1999

<!--更改日期：1999年11月1日 -->

<-- REVISION HISTORY

<-- November 1999 V4 (according to decisions in MRWG, September 99

$<  ! - >$  element name CHECKCODE to changed to CHECKCOD to avoid

<!-- confusion with attribute CHKCODE -->

<!-- * element CAGECODE in content model of PRODID deleted and ->

<!-- attribute CAGECODE added to PRODID for consistency reasons -->

$<  ! - - ^{*}$  element PROCREF in SMTASK changed from required to optional

$<  ! - -$  to cover SMTASK without references to procedures

<!-- 更改历史记录  $\rightarrow$

<!-- 1999年11月V4（根据99年9月MRWG的决定-->

<!--*将元素名称CHKCODE改为CHECKCOD以避免与属性CHKCODE混淆-->

<!--*在PRODID的内容模型中删除了元素CAGECODE

<!-- 并为保持一致性，在PRODID中增加了CAGECODE属性 -->

<!-- *将SMTASK中的元素PROCREF由必选项改为可选项-->

<!-- 以涵盖没有对程序进行参考的 SMTASK -->

<!-- Meanless:-->

<!DOCTYPE mpd [

$<<$  The following set of declarations may be referred by using a public identifier as follows:

<!DOCTYPE m pd PUBLIC "/ATA-TEXT//DTD MPD-VER4-LEVEL2//EN" []>

$\rightarrow$

<!-- Meanless:-->

<!-- ENTITIES

实体  $\rightarrow$

<!-- Meanless:  $\rightarrow$ -->

<!ENTITY % wcn " (warning | caution | note)"

<!ENTITY % text "(para | table | %wcn; | unlist | numlist

list1|graphic|txtgraphc)+"

<!ENTITY % yesomo "NUMBER"

<!ENTITY % deleted " (deleted, chgdesc*)" >

<!ENTITY % revatt

```txt
"chg (N|R|U|D) #REQUIRED
key ID #REQUIRED
revdate NUMBER #REQUIRED>
<!ENTITY % unitlist
    "unitcode (FH|FC|MO|WK|YR|DY|PC|OC|LD|
    HR|OH|SC|SH)" > <!
ENTITY % coderlist
    "chkcode (A|B|C|D|E|DL|TR|WL|PF|OV|
    ST)" > <!
ENTITY % ISOtech PUBLIC
    "ISO 8879:1986//ENTITIES General Technical//EN"
<!
ENTITY % ISOpub PUBLIC
    "ISO 8879:1986//ENTITIES Publishing//EN"
<!
ENTITY % ISOnum PUBLIC
    "ISO 8879:1986//ENTITIES Numeric and Special Graphic//EN">
<!
ENTITY % ISOgrkl PUBLIC
    "ISO 8879:1986//ENTITIES Greek Letters//EN"
<---> -> <!-- MPD TOP LEVEL STRUCTURE -> <--
MPD顶层结构 -> <--
<!
ELEMENT mpg -- (((title, mfmatr, prodlist, intro, section,
append) | tr++)
+(revst | revend | hotlink)
<!
ATTLIST mpg docnbr CDATA #REQUIRED
spl CDATA #REQUIRED
model CDATA #REQUIRED
oidate NUMBER #REQUIRED
revdate NUMBER #REQUIRED
tsn CDATA #REQUIRED
lang CDATA #REQUIRED
chg (N|R|D|U) #REQUIRED>
<---> TEMPORARY REVISION -> <--->临时更改 -> <--
<!
ELEMENT tr -- (trfmatr, (mfmatr | intro | section|
syspower | structur | zonal | srclist|
smtask+ | graphic+ | sheet+ | append|
acclist | jobcard | reltali |CHKcodli|
refaftli | otherapp+)) -> <!
ELEMENT trfmatr -- (title, trreason, (%text;?) -> <!
ATTLIST trfmatr
```

```txt
trnbr CDATA #REQUIRED   
issdate NUMBER #REQUIRED   
trdel CDATA #IMPLIED   
trrepl CDATA #IMPLIED >   
<!ELEMENT trreason -- (#PCDATA) >   
<!-- MPD FRONT MATTER --   
<!- MPD 前页 ->   
<!--   
<!ELEMENT mfmatr -- (%text;） >   
<!ATTLIST mfmatr %revatt; >   
<!--   
<!PRODUCT LIST --   
<!--产品清单 ->   
<!--   
<!ELEMENT prodlist -- (prodnum)+ >   
<!ATTLIST prodlist cagecode CDATA #REQUIRED>   
<!ELEMENT prodnum -- (prodnum+|msnxref)? >   
<!ATTLIST prodnum CDATA #REQUIRED>   
<!ELEMENT msnxref -- (msnbr, acn?, cusnbr?, venbr?, benbr?, esnbr?, linenbr?, verrank?)+ >   
<!ELEMENT cusnbr -- (cus, cec) >   
<!ELEMENT verrank -- (vers, mk) >   
<!ELEMENT (msnbr|acn|cus|cec|venbr|benbr|esnbr|linenbr|vers|mk) -- (#PCDATA) >   
<!--   
<!-- INTRODUCTION ->   
<!--前言 ->   
<!--   
<!ELEMENT intro -- (chgdesc*, %text; , chkcodli?, refaftli?) >   
<!ATTLIST intro %revatt; >   
<!--   
<!INTRODUCTION: Check Code Reference List ->   
<!-- INTRODUCTION: 检查代码引用清单 ->   
<!--   
<!ELEMENTCHKcodli -- (checkcod+) >   
<!ATTLISTCHKcodli %revatt; >   
<!ELEMENT checkcod -- (unitval+) >   
<!-- chkcode/ key is referenced by chkcodva/refid
```

```txt
<!ATTLIST checkcod %codelist; #REQUIRED key ID #REQUIRED > <!ELEMENT unitval -- (#PCDATA) > <!ATTLIST unitval chg (N|R|U|D) #IMPLIED #unitlist; #REQUIRED >  
<!--INTRODUCTION: Reference Average Flight Time List -- <--INTRODUCTION: 参考平均飞行时间清单 --  
<!--ELEMENT refaftli -- (refaftda+|%deleted;) > <!ATTLIST refaftli %revatt; > <!ELEMENT refaftda -- (refaft, toleranc, modtype) > <!ELEMENT refaft -- (#PCDATA) > <!ELEMENT toleranc -- (#PCDATA) > <!ELEMENT modtype -- (#PCDATA) >  
<!-- SCHEDULED MAINTENANCE TASK SECTION --  
<--预定的维修任务节 --  
<!--ELEMENT section -- (syspower, structur, zonal, srclist) > <!ATTLIST section %revatt; > <!ELEMENT syspower -- (chgdesc*, intro, smtask+) > <!ATTLIST syspower %revatt; > <!ELEMENT structur -- (chgdesc*, intro, smtask+) > <!ATTLIST structur %revatt; > <!ELEMENT zonal -- (chgdesc*, intro, smtask+) > <!ATTLIST zonal %revatt; >  
<!-- SCHEDULED MAINTENANCE TASK --  
<--预定的维修任务 --  
<!--ELEMENT smtask -- ((effect,chgdesc*, title, smdesc, note*, tahour, nbrpers, source+, periobox+, procbox*, primzone+, reltask*) |%deleted;) >  
<!ATTLIST smtask tasknbr CDATA #REQUIRED taskcode (GVI|DVI|SDI|VCK|FNC|OPC|LUB|SVC|
```

```txt
RST|DIS|TPS) #REQUIRED
remorequ %yesorno; #REQUIRED
fatirat NUMBER #IMPLIED
%revatt; > <!
<-- SMTASK : Description / Labour Hours / Number of Persons -> <-- SMTASK : 说明/工时/人数 -> <--
<!ELEMENT smtdesc -- (#PCDATA) > <-- ELEMENT tahour -- (#PCDATA) > <-- ELEMENT nbrpers -- (#PCDATA) > <--
<-- SMTASK : Source -> <-- SMTASK: 源 -> <--
<-- source/refid refers to srcdoc/key -> <-- ELEMENT source -o EMPTY -> <-- ATTLIST source
revdate NUMBER #IMPLIED
tsn CDATA #IMPLIED
refid IDREF #REQUIRED >
<!
<-- SMTASK : Periodicity -> <-- SMTASK: 周期 -> <--
<-- the repetition of periodic indicates a sequence of periodicity statement - all of them have to be done -> <--周期的重复给出了周期指令的顺序-它们必须被全部执行。-> <-- element peribox -- (effect, (limit | periodic+ | specacc)) -> <-- the repetition of (threshold+, interval) indicates a choice of (first of) periodicity statements expressed in different units -> <-- element periodic -- (threshold+, interval)+ -> <-- ELEMENT threshol -- (minthr?, (chkcodva | unitval), sampperc?, note?) -> <-- ELEMENT minthr -- (chkcodva | unitval) -> <-- ELEMENT chkcodva -- (#PCDATA) -> <-- chkcodva/refid refers to chkcode/key -> <-- ATTLIST chkcodva
refid IDREF #IMPLIED
%coderlist; #REQUIRED >
<-- ELEMENT interval -- ((chkcodva|unitval), tolperc?, sampperc?, note?) -> <-- ELEMENT tolperc -- (#PCDATA) -> <-- ELEMENT sampperc -- (#PCDATA, note?) -> <-- ELEMENT limit -- (#PCDATA)
```

```sgml
<!ATTLIST limit %unitlist; #REQUIRED>  
<!ELEMENT specacc -- (#PCDATA) >  
<!-- --->  
<!-- SMTASK: Procedure References ->  
<!--SMTASK: 程序参考 ->  
<!-- --->  
<!ELEMENT procbox -- (effect, procref+) >  
<!ELEMENT procref -- (refext) >  
<!ATTLIST procref procdoc (AMM|EMM|CMM|WM|SB|JC|SRM) #REQUIRED  
proctype (AMTOSS|JEMTOSS|PageBlock) #IMPLIED  
procseq NUMBER #REQUIRED>  
<!-- --->  
<!-- SMTASK: Access/Boundary ->  
<!--SMTASK: 访问/范围 ->  
<!-- --->  
<!ELEMENT primzone -- (#PCDATA, (accbox+ | boundbox+)?) >  
<!ATTLIST primzone  
nbrocc NUMBER #REQUIRED>  
<!ELEMENT accbox -- (effect, accpan+) >  
<!ELEMENT accpan -o EMPTY >  
<!-- accpan/refid refers to acdatakey ->  
<!ATTLIST accpan  
refid IDREF #REQUIRED>  
<!ELEMENT boundbox -- (effect, boundary+) >  
<!ELEMENT boundary -- (#PCDATA) >  
<!-- --->  
<!-- SMTASK: Related Tasks ->  
<!--SMTASK: 相关任务 ->  
<!-- --->  
<!-- reltask/teltaid refers to smtask/key ->  
<!ELEMENT reltask -o EMPTY >  
<!ATTLIST reltask  
relcode (A|P|B|S|W) #REQUIRED  
reltaid IDREF #REQUIRED>  
<!-- Source Documents for Scheduled Maintenance Tasks ->  
<!--适合于预定的维修任务的源文档 ->  
<!-- --->  
<!ELEMENT srclist -- (chgdesc*, intro, srcdoc+) >  
<!ATTLIST srclist  
%revatt; ->  
<!ELEMENT srcdoc -- (refext)
```

```txt
<!-- srcdoc/ key is referenced by source/refid  
<!ATTLIST srcdoc  
srctype (TCDS | MRB | CMR | ALI | ALL | CPCP | AD | NR | SB | SL | MPD | SIL | AOT | AMM05) #REQUIRED  
cmr (NO | ONESTAR | TWOSTAR) #IMPLIED  
fec (5 | 6 | 7 | 8 | 9) #IMPLIED  
key ID #REQUIRED >  
<!--APPENDICES-->  
<!--附录-->  
<!--ELEMENT append -- (acclist, reltali, jobcard?, otherapp*)  
<!ATTLIST append %revatt;  
<!--APPENDICES: Access Data  
<!-- APPENDICES: 访问数据  
<!--ELEMENT acclist -- (chgdesc*, intro, accdata+)  
<!ATTLIST acclist %revatt;  
<!--ELEMENT accdata -- (pan, openhour, closhour, nbrpers, accessto)  
<!-- accdata/ key is referenced by accpan/refid  
<!ATTLIST accdata  
key ID #REQUIRED>  
<!ELEMENT pan -- (#PCDATA)  
<!ELEMENT openhour -- (#PCDATA)  
<!ELEMENT closhour -- (#PCDATA)  
<!ELEMENT accessto -- (#PCDATA)  
<!--APPENDICES: Scheduled Maint Task/Job Card References -->  
<!--content to be generated based on Procedure -->  
<!--References attached to smtask -->  
<!--APPENDICES: 预定的维修任务/工作卡的引用文件内容将基于附属  
<!-- 于 mtask 的程序参考来生成 -->  
<!--ELEMENT jobcard -- ((chgdesc*, intro) | %deleted;))  
<!ATTLIST jobcard %revatt;  
<!--Related Scheduled Maint. Tasks List -->  
<!--content to be generated based on reltask attached to smtask -->  
<!--相关的预定的维修任务清单 -->  
<!-- 内容基于附属于 smtask 的 reltask 生成 -->
```

```txt
<!ELEMENT reltali -- (chgdesc*, intro) >  
<!ATTLIST reltali %revatt; >  
<!--APPENDICES: other Appendices -->  
<!APPENDICES: 其它附录 -->  
<!---- appendices: -- (chgdesc*, title, intro, %text;) | %deleted; >  
<!ATTLIST otherapp %revatt; >  
<!---- EFFECTIVITY -->  
<!-- 有效性 -->  
<!---- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
<!--ELEMENT effect --> 
<!--ELEMENT prodid --> 
<!--ELEMENT prodid --> 
<!--ELEMENT endrange --> 
<!--ELEMENT subeff --> 
<!--ELEMENT subeff --> 
<!--ELEMENT subeff --> 
<!--ELEMENT subeff --> 
<!--ELEMENT subeff --> 
<!--ELEMENT subeff --> 
<!--ELEMENT subeff --> 
<!--ELEMENT subeff --> 
<!--ELEMENT subeff --> 
<!--ELEMENT subeff --> 
<!--ELEMENT subeff --> 
<!--ELEMENT subeff --> 
<!--ELEMENT subeff --> 
<!--ELEMENT subeff --> 
<!--ELEMENT subeff --> 
<!--ELEMENT subeff --> 
<!--ELEMENT subeff --> 
<!--Element condeff --> 
<!--Element condeff --> 
<!--Element opercond --> 
<!--Element opercond --> 
<!--Element opercond --> 
<!--Element opercond --> 
<!--Element opercond --> 
<!--Element opercond --> 
<!--Element opercond --> 
<!--Element opercond --> 
<!--Element opercond --> 
<!--Element opercond --> 
<!--Element opercond --> 
<!--Element opercond --> 
<!--Element opercond --> 
<!--Element opercond --> 
<!--Element opercond --> 
<!--Element opercond --> 
<!--Element opercond --> 
<!--ELEMENT opercond --> 
<!--Element opercond --> 
<!--Element opercond --> 
<!--Element opercond --> 
<!--Element opercond --> 
<!--Element opercond --> 
<!--Element opercond --> 
<!--Element opercond --> 
<!--Element opercond --> 
<!--Element opercond --> 
<!--Element opercond --> 
<!--Element opercond --> 
<!--Element opercond --> 
<!--Element opercond --> 
<!--Element opercond --> 
<!--Element opercond --> 
<!--Element opercond -->
```

```txt
<!ELEMENT eftext -- (efftxtli+) >  
<!ELEMENT eftxtli -- (#PCDATA | refext) + >  
<!--TABLE (CALS) ->  
<!--表 (CALS) ->  
<!--table -- ((title?, tgroup, ftnote*) | graphic+)-(table) ->  
<ATTLIST table  
tabstyle NMTOKEN #IMPLIED  
frame (top|bottom|topbot|all|sides|none) #IMPLIED  
colsep %yesorno; #IMPLIED  
rowsep %yesorno; #IMPLIED  
orient (port | land) #IMPLIED  
pgwide %yesorno; #IMPLIED  
id ID #IMPLIED >  
<!ELEMENT tgroup -o (colspec*, spanspec*, thead?, tfoot?, tbody) ->  
<!ATTLIST tgroup  
cols NUMBER #REQUIRED  
colsep %yesorno; #IMPLIED  
rowsep %yesorno; #IMPLIED  
align (left|right|center|justify|char) "left"  
charoff NUTOKEN "50"  
char CDATA " " >  
<!ELEMENT colspec -o EMPTY ->  
<!ATTLIST colspec  
colnum NUMBER #IMPLIED  
colname NMTOKEN #IMPLIED  
align (left|right|center|justify|char) #IMPLIED  
charoff NUTOKEN #IMPLIED  
char CDATA #IMPLIED  
colwidth CDATA #IMPLIED  
colsep %yesorno; #IMPLIED  
rowsep %yesorno; #IMPLIED >  
<!ELEMENT spanspec -o EMPTY ->  
<!ATTLIST spanspec  
namest NMTOKEN #REQUIRED  
nameend NMTOKEN #REQUIRED  
spanname NMTOKEN #REQUIRED  
align (left|right|center|justify|char) "center"  
charoff NUTOKEN #IMPLIED  
char CDATA #IMPLIED  
colsep %yesorno; #IMPLIED  
rowsep %yesorno; #IMPLIED >
```

```lisp
<!ELEMENT thad -o (colspec\*, row+) >   
<!ATTLIST thad   
valign (top|middle|bottom) "bottom" >   
<!ELEMENT tfoot -o (colspec\*, row+) >   
<!ATTLIST tfoot   
valign (top|middle|bottom) "top" >   
<!ELEMENT tbody -o (row+) >   
<!ATTLIST tbody   
valign (top|middle|bottom) "top" >   
<!ELEMENT row -o (entry+) >   
<!ATTLIST row   
rowsep %yesorno; #IMPLIED >   
<!ELEMENT entry -- ((para | unlist)+) >   
<!ATTLIST entry   
colname NMTOKEN #IMPLIED   
namest NMTOKEN #IMPLIED   
nameend NMTOKEN #IMPLIED   
spanname NMTOKEN #IMPLIED   
morerows NUMBER "0"   
colsep %yesorno; #IMPLIED   
rowsep %yesorno; #IMPLIED   
rotate %yesorno; "0"   
valign (top|middle|bottom) "top"   
align (left|right|center|justify|char) #IMPLIED   
charoff NUTOKEN #IMPLIED   
char CDATA #IMPLIED >   
<!ELEMENT ftnote -- (%text;)   
-(graphic)
```

```txt
<!ATTLIST ftnote
ftnoteid ID #REQUIRED>
<!--->->->--GRAPHIC ->->->图形->->->--ELEMENT graphcref -- (#PCDATA) -><!ATTLIST graphcref
refid .IDREF #IMPLIED
sheetnbr CDATA #IMPLIED
structid CDATA #IMPLIED
shownow %yesorno; "0" ><!ELEMENT graphic -- ((chgdesc*, title?, sheet+) |%deleted;)
<!ATTLIST graphic
%revatt;
```

<!ELEMENT sheet -- ((chgdesc*, title?, gdesc?) | %deleted;)

<!ATTLIST sheet

sheetnbr CDATA

#REQUIRED

gnbr ENTITY

#REQUIRED

%revatt;

<!ELEMENT gdesc --(%text;

-(graphic)

<!-- LISTS

<!--清单

<!ELEMENT list1 -- (title?, 11item+)

-(list1)

<!ELEMENT list2 -- (title?, l2item+)

<!ELEMENT list3 -- (title?, 13item+)

<!ELEMENT list4 -- (title?, l4item+)

<!ELEMENT list5 -- (title?, 15item+)

<!ELEMENT list6 -- (title?, 16item+)

<!ELEMENT list7 -- (title?, 17item+)

<!-- LIST ITEMS

<!--清单项

<!ELEMENT 11item --(%text;, list2?)

<!ATTLIST11item

key ID

<!ELEMENT l2item --(%text;，list3?)

<!ATTLIST l2item

key ID

<!ELEMENT l3item --(%text;, list4?)

<!ATTLIST l3item

key ID

<!ELEMENT l4item --(%text;，list5?)

<!ATTLIST l4item

key ID

<!ELEMENT l5tem --(%text;，list6?)

<!ATTLIST l5item

key ID

<!ELEMENT l6item --(%text;，list7?)

<!ATTLIST l6item

key ID

<!ELEMENT 17item --(%text;

<!ATTLIST 17item

key ID

#IMPLIED >

#IMPLIED

#IMPLIED

#IMPLIED

#IMPLIED

#IMPLIED >

#IMPLIED >

```txt
<!-- NUMBERED & UN-NUMBERED LIST -->
<!-- 有编号和无编号的清单 -->
<!-- -->
<!ELEMENT numlist -- (numltem+) > <!ATTLIST numlist numtype (NNP|AUP|NNB|ALB|NNS|RUP|RLP|RUR|RLR|NNR|AUR|ALR) 'NNP' >
<!ELEMENT numltem -- (para+) > <!ELEMENT unlist -- (unltem+) >
<!ATTLIST unlist bulltype (NONE|BULLET|NDASH|MDASH|DIAMOND|ASTERISK |DELTA|SQUARE|SYSTEM) 'SYSTEM' >
<!ELEMENT unltem -- (%text;) >
<!WARNING, CAUTION, NOTE -->
<!警告，注意，注释 ->>
<!PARAGRAPH -> <!--PARAGRAPH -> <!--段 -> <!--PARAGRAPH -> <!--PARAGRAPH -> <!--PARAGRAPH -> <!--PARAGRAPH -> <!--PARAGRAPH -> <!--PARAGRAPH -> <!--PARAGRAPH -> <!--PARAGRAPH -> <!--PARAGRAPH -> <!--PARAGRAPH -> <!--PARAGRAPH -> <!--PARAGRAPH-> <!--PARAGRAPH-> <!--PARAGRAPH-> <!--PARAGRAPH-> <!--PARAGRAPH-> <!--PARAGRAPH-> <!--PARAGRAPH-> <!--PARAGRAPH-> <!--PARAGRAPH-> <!--PARAGRAPH-> <!--PARAGRAPH-> <!--PARAGRAPH-> <!--PARAGRAPH-> <!--PARAGRAPH-> <!--PARAGRAPH-> <.--(#PCDATA|refext|refint|equi|graphcref |txtgraphc)+ -> <!--PARAGRAPH -> <!--PARAGRAPH-> <!--PARAGRAPH-> <!--PARAGRAPH-> <!--PARAGRAPH-> <!--PARAGRAPH-> <!--PARAGRAPH-> <!--PARAGRAPH-> <!--PARAGRAPH-> <!--PARAGRAPH-> <!--PARAGRAPH-> <!--PARAGRAPH-> <!--PARAGRAPH-> <!--PARAGRAPH-><!--PARAGRAPH-> <!--PARAGRAPH-> <!--PARAGRAPH-> <!--PARAGRAPH-> <!--PARAGRAPH-> <!--PARAGRAPH-> <!--PARAGRAPH-> <!--PARAGRAPH-> <!--PARAGRAPH-> <!--PARAGRAPH-> <!--PARAGRAPH-> <!--PARAGRAPH-> <!--PARAGRAPH-> <!--PARAGRAPH-> <!--PHREF> #IMPLIED #IMPLIED #IMPLIED #IMPLIED #IMPLIED #IMPLIED #IMPLIED #IMPLIED #IMPLIED #IMPLIED #IMPLIED #IMPLIED #IMPLIED #IMPLIED #IMPLIED #IMPLIED #IMPLIED #IMPLIED #IMPLIED #IMPLIED #IMPLIED #IMPLIED #IMPLIED #IMPLIED #IMPLIED #IMPLIED #IMPLIED #IMPLIED #IMPLIED #IMPLIED #IMPLIED #IMPLIED #IMPLIED #IMPLIED #IMPLIED #IMPLIED #IMPLIED #IMPLIED #IMPLIED #IMPLIED #IMPLIED #IMPLIED #IMPLIED #IMPLIED #IMPLIED #IMPLIED #IMPLIED #IMPLIED #IMPLIED #IMPLIED #.-- (#PCDATA) > <!ATTLIST refext CDATA refman CDATA refspl CDATA refmodel CDATA docnbr CDATA refloc CDATA refloc CDATA refloc CDATA refloc CDATA refloc CDATA refloc CDATA refloc CDATA refloc CDATA refloc CDATA refloc CDATA refloc CDATA refloc CDATA refloc CDATA refloc CDATA refloc CDATA refloc CDATA refloc CDATA refloc CDATA refloc CDATA refloc CDATA refloc CDATA refloc CDATA refloc CDATA refloc CDATA refloc CDATA refloCDATA refloc CDATA refloc CDATA refloc CDATA refloc CDATA refloc CDATA refloc CDATA refloc CDATA refloc CDATA refloc CDATA refloc CDATA refloc CDATA refloc CDATA refloc CDATA refloc CDATA refloc CDATA refloc CDATA refloc CDATA refloc CDATA refloc CDATA refloc CDATA refloc CDATA refloc CDATA refloc CDATA refloc CDATA refloc CDA DATA refloc CDA DATA refloc CDA DATA refloc CDA DATA refloc CDA DATA refloc CDA DATA refloc CDA DATA refloc CDA DATA refloc CDA DATA refloc CDA DATA refloc CDA DATA refloc CDA DATA refloc CDA DATA refloc CDA DATA refloc CDA DATA refloc CDA DATA refloc CDA DATA refloc CDA DATA refloc CDA DATA refloc CDA DATA refloc CDA Data refloc CDA Data refloc CDA Data refloc CDA Data refloc CDA Data refloc CDA Data refloc CDA Data refloc CDA Data refloc CDA Data refloc CDA Data refloc CDA Data refloc CDA Data refloc CDA Data refloc CDA Data refloc CDA Data refloc CDA Data refloc CDA Data refloc CDA Data refloc CDA Data refloc CDA Data refloc CDAData refloCDA Data refloCDA Data refloCDA Data refloCDA Data refloCDA Data refloCDA Data refloCDA Data refloCDA Data refloCDA Data refloCDA Data refloCDA Data refloCDA Data refloCDA Data refloCDA Data refloCDA Data refloCDA Data refloCDA Data refloCDA Data refloCDA Data refloCDA Data refloCDAData refloCDA Data refloCDA Data refloCDA Data refloCDA Data refloCDA Data refloCDA Data refloCDA Data refloCDA Data refloCDA Data refloCDA Data refloCDA Data refloCDA Data refloCDA Data refloCDA Data refloCDA Data refloCDA Data refloCDA Data refloCDA Data refloCDA Data reflo
```

```txt
refid IDREF #REQUIRED>  
<!ELEMENT txtgraphc -- (txtline+) >  
<!ELEMENT txtline -- (#PCDATA) >  
<!ELEMENT hotlink -o EMPTY >  
<!ATTLIST hotlink  
targetid CDATA #IMPLIED  
targetrefid CDATA #IMPLIED >  
<!ELEMENT equ -- (#PCDATA) >  
<!ELEMENT revst -o EMPTY >  
<!ELEMENT revend -o EMPTY >  
<!ELEMENT deleted -o EMPTY >  
<!ELEMENT chgdesc -- (#PCDATA) >  
<!ELEMENT title -- (#PCDATA) >
```

# 2 结构图表

结构图的关键组成部分可参见 DTD 技术要求(参见[4-2-3.22.4])。为利用采用交互式阅读器的 DTD 的图形进行工作，使用 DTD 结构树阅读器。

![](images/692dfa7d38062141fad94579cac9c96f9012c45c79b32b1bbafea2df6b245380.jpg)  
图4-2-30.1 MPD DTD结构一产品清单(Prodlist)

![](images/adae4f1489cb14010f5f385062e36e641a88154cffc2b08e299472449133ede0.jpg)  
图4-2-30.2 MPD DTD结构一概述

![](images/653e6c6e41d656834e510434e9bc1d3712bc9ac691af7b988abaf9b024d1ea7a.jpg)  
图4-2-30.3 MPD DTD结构一附录和TR

# 4-2-31 服务通报(SB)DTD

# 1 SB DTD

<!---->

<!-- DTD Header -->

<!-- DTD 程序头 -->

<!---->

<!-- ->

<!-- This is the ATA Service Bulletin DTD -->

<!--这是ATA服务通报的DTD

<!-- Meanless: ->

<!-- DTD Reference : ATA-TEXT-DTD-SB-VER5-LEVEL-->

<!-- DTD参考：ATA-TEXT-DTD-SB-VER5-LEVEL ->

<-- Revision Date : 31 January, 1997 -->

```html
<!--更改日期：1997年1月31日-->  
<!--Highlight：Incorporated modifications-->  
<!----from September meeting in-->  
<!--Toulouse，France.-->  
<!----更改摘要：在法国图卢兹的9月会议上合并修改。-->  
<!------>  
<!----DTD Level：2-->  
<!----DTD级别：2-->  
<!----->  
<!DOCTYPE sb[
```

$<  ! - -$  The following set of declarations may be referred to using a public entity as follows:

<!--以下公共实体的使用可参考如下声明的集合：-->

```txt
<!DOCTYPE sb PUBLIC  
"-//ATA-TEXT//DTD SB-VER5-LEVEL2//EN" []> -->
```

```txt
$<  ! - -$  NOTATIONS  $\rightarrow$ $<  ! - -$  符号  $\rightarrow$ $<  ! - -$
```

```txt
<!NOTATION cgm PUBLIC
  "/ / USA-DOD//NOTATION Computer Graphics Metafile//EN"
<!NOTATION ccitt4 PUBLIC
  "/ / USA-DOD//NOTATION CCITT Group 4 Facsimile//EN"
```

```txt
<!-- ->  
<!-- ENTITIES ->  
<!-- 实体 ->  
<!-- ->
```

```txt
<!ENTITY % wcn " (warning* | caution* | note*)" >
```

```txt
<!ENTITY % text " (para | table | unlist | numlist | %wcn | list1 | graphic | txtgraphc) +"
```

```txt
<!ENTITY % deleted ."(deleted, chgdesc*)")
```

```batch
<!ENTITY % yesorno "NUMBER"
```

```txt
<!ENTITY % revatt
"chg (N|R|U|D) #REQUIRED
key ID #REQUIRED
revdate NUMBER #REQUIRED"
```

<!ENTITY % ISOtech PUBLIC

"ISO 8879-1986//ENTITIES General Technical//EN"

<!ENTITY % ISOpub PUBLIC

"ISO 8879-1986//ENTITIES Publishing//EN"

<!ENTITY % ISOnum PUBLIC

"ISO 8879-1986//ENTITIES Numeric and Special Graphic//EN">

<!ENTITY % ISOgrk1 PUBLIC

"ISO 8879-1986//ENTITIES Greek Letters//EN"

%ISOtech; %ISOpub; %ISOnum; %ISOgrk1;

<!---->

<!-- Service Bulletin HIGH LEVEL STRUCTURE -->

$<  ! - -$  服务通报高级结构  $\rightarrow$

<!---->

<!ELEMENT sb -- ((title, (curadr, oldadr)?, (summary

| (ts?, sbfmatr?, body, append*))))

+ (revst | revend | hotlink | effect) >

<!ATTLIST sb

model CDATA #REQUIRED

docnbr CDATA #IMPLIED

mdnbr NMTOKENS #IMPLIED

spl CDATA #REQUIRED

prevspl CDATA #IMPLIED

tsn CDATA #REQUIRED

oidate NUMBER #REQUIRED

revdate NUMBER #REQUIRED

chapsect NUMBERS #IMPLIED

chapnbr NUMBER #REQUIRED

seqnbr CDATA #REQUIRED

sbtype (Alert | Standard | Other) 'Standard'

chg (N|R|U|S) #REQUIRED

sbebpl CDATA #IMPLIED

lang CDATA #REQUIRED

regact CDATA #IMPLIED

}}}

mfrrec (rec|des|opt) #IMPLIED

<!---->

SUMMARY SECTION

<!--摘要节-->

<!---->

<!ELEMENT summary -- (sbfmatr)

<!---->

<!-- TRANSMITTAL SECTION -->

-- 信息传输节

<<

<!ELEMENT ts --((title,para\*,tssect+) |%deleted;)

<!ATTLIST ts oldkey NAME #IMPLIED %revatt;

<!ELEMENT tssect -- (title, %text;) - (graphic)

<!---->

$<  ! - -$  SB FRONT MATTER

$<  ! - -$  SB前页

<!---->

<!ELEMENT sbfmatr -- ((chgdesc*, title, para?, sbfmsect+, graphic*, effxref?) |%deleted;) >

<!ATTLIST sbfmatr
oldkey NAME #IMPLIED
%revatt;

<!ELEMENT sbebmfsect -- (title, %text;) - (graphic)

<!---->

<!-- EFFECTIVITY CROSS REFERENCE --

<!-- 有效性对照 -->

<!-- Meanless:  $\rightarrow$ -->

<!ELEMENT effxref -- (effdata+)

<!ELEMENT effdata -- (set?, (sunit | (munit, expndrg?)) +) >

<!ELEMENT expndrg -- (sunit+)

<!ELEMENT set -- (#PCDATA)

<!ELEMENT sunit -- (#PCDATA)

<!ATTLIST sunit  
unittype CDATA #IMPLIED

<!ELEMENT munit -- (stunit, endunit)

<!ATTLIST munit  
unittype CDATA #IMPLIED

<!ELEMENT stunit -- (#PCDATA)

<!ELEMENT endunit -- (#PCDATA)

<!---->

$<  ! - -$  SBBODY

$<  ! - -$  SB正文

<!-- ---->

<!ELEMENT body -- (para?, plan, matinfo, instr) >

<!ATTLIST body
oldkey NAME #IMPLIED
%revatt;

<--

$<  ! - -$  SBBODYSECTIONS

$<  -$  SB正文节

<1

<!ELEMENT plan -- (title, plansect+, graphic*)

<!ATTLIST plan
oldkey NAME #IMPLIED
%revatt;

<!ELEMENT matinfo -- (title, (para | matsect+))

<!ATTLIST matinfo oldkey NAME #IMPLIED %revatt;

<!ELEMENT instr -- (title, instsect+, graphic*)

<!ATTLIST instr
oldkey NAME #IMPLIED
%revatt;

←

<!-- SB BODY SUBLECTIONS --

<!-- SB 正文分节 -->

<!---->

<!ELEMENT plansect -- ((chgdesc*, title, %text;)
|%deleted;) + (effxref)

<!ATTLIST plansect  
sectname (EFF | CON | RES | DES | COM | APP  
| MAN | WAB | ELD | SAS | REF | PUB  
| FTC | OTH) #REQUIRED  
%revatt;

<!ELEMENT matsect -- ((chgdesc*, title, %text;)
|%deleted;) - (graphic)

<!ATTLIST matsect sectname (MPA | ISI | MNU | MNS | RIP | TPA

```txt
| OTH) #REQUIRED
%revatt; > <!ELEMENT instsect -- ((chgdesc*, title?, %text; | %deleted;) > <!ATTLIST instsect %revatt; > <-- -> -- <-- APPENDIX -> <-- 附录 -> <-- -- -> <!ELEMENT append -- ((chgdesc*, title, %text; | %deleted;) > <!ATTLIST append %revatt; > <-- - -> <-- TABLE (CALS) -> <-- 表 (CALS) -> <-- - -> <!ELEMENT table -- ((title?, tgroup, ftnote*) | graphic+) - (table) > <!ATTLIST table tabstyle NMTOKEN #IMPLIED frame (top|bottom|topbot |all|sides|none) #IMPLIED colsep %yesorno; #IMPLIED rowsep %yesorno; #IMPLIED orient (port | land) #IMPLIED pgwide %yesorno; #IMPLIED id ID #IMPLIED > <!ELEMENT tgroup -O (colspec*, spanspec*, thead?, tfoot?, tbody) > <!ATTLIST tgroup cols NUMBER #REQUIRED colsep %yesorno; #IMPLIED rowsep %yesorno; #IMPLIED align (left|right|center |justify|char) "left" charoff NUTOKEN "50" char CDATA " "
```

<table><tr><td>&lt;!ELEMENT colspec</td><td>-O EMPTY</td><td></td><td>&gt;</td></tr><tr><td>&lt;!ATTLIST colspec</td><td></td><td></td><td></td></tr><tr><td>colnum</td><td>NUMBER</td><td>#IMPLIED</td><td></td></tr><tr><td>colname</td><td>NMTOKEN</td><td>#IMPLIED</td><td></td></tr><tr><td>align</td><td>(left|right|center</td><td></td><td></td></tr><tr><td></td><td>[justify|char)</td><td>#IMPLIED</td><td></td></tr><tr><td>charoff</td><td>NUTOKEN</td><td>#IMPLIED</td><td></td></tr><tr><td>char</td><td>CDATA</td><td>#IMPLIED</td><td></td></tr><tr><td>colwidth</td><td>CDATA</td><td>#IMPLIED</td><td></td></tr><tr><td>colsep</td><td>%yesorno;</td><td>#IMPLIED</td><td></td></tr><tr><td>rowsep</td><td>%yesorno;</td><td>#IMPLIED</td><td>&gt;</td></tr><tr><td>&lt;!ELEMENT spanspec</td><td>-O EMPTY</td><td></td><td>&gt;</td></tr><tr><td>&lt;!ATTLIST spanspec</td><td></td><td></td><td></td></tr><tr><td>namest</td><td>NMTOKEN</td><td>#REQUIRED</td><td></td></tr><tr><td>nameend</td><td>NMTOKEN</td><td>#REQUIRED</td><td></td></tr><tr><td>spanname</td><td>NMTOKEN</td><td>#REQUIRED</td><td></td></tr><tr><td>align</td><td>(left|right|center</td><td></td><td></td></tr><tr><td></td><td>[justify|char)</td><td>&quot;center&quot;</td><td></td></tr><tr><td>charoff</td><td>NUTOKEN</td><td>#IMPLIED</td><td></td></tr><tr><td>char</td><td>CDATA</td><td>#IMPLIED</td><td></td></tr><tr><td>colsep</td><td>%yesorno;</td><td>#IMPLIED</td><td></td></tr><tr><td>rowsep</td><td>%yesorno;</td><td>#IMPLIED</td><td>&gt;</td></tr><tr><td>&lt;!ELEMENT thread</td><td>-O (colspec*, row+)</td><td></td><td>&gt;</td></tr><tr><td>&lt;!ATTLIST thread</td><td></td><td></td><td></td></tr><tr><td>valign</td><td>(top|middle|bottom) &quot;bottom&quot;</td><td></td><td>&gt;</td></tr><tr><td>&lt;!ELEMENT tfoot</td><td>-O (colspec*, row+)</td><td></td><td>&gt;</td></tr><tr><td>&lt;!ATTLIST tfoot</td><td></td><td></td><td></td></tr><tr><td>valign</td><td>(top|middle|bottom) &quot;top&quot;</td><td></td><td></td></tr><tr><td>&lt;!ELEMENT tbody</td><td>-O (row+)</td><td></td><td>&gt;</td></tr><tr><td>&lt;!ATTLIST tbody</td><td></td><td></td><td></td></tr><tr><td>valign</td><td>(top|middle|bottom) &quot;top&quot;</td><td></td><td></td></tr><tr><td>&lt;!ELEMENT row</td><td>-O (entry+)</td><td></td><td></td></tr><tr><td>&lt;!ATTLIST row</td><td></td><td></td><td></td></tr><tr><td>rowsep</td><td>%yesorno;</td><td>#IMPLIED</td><td>&gt;</td></tr><tr><td>&lt;!ELEMENT entry</td><td>-- (para | unlist | numlist | %wcn</td><td></td><td></td></tr><tr><td></td><td>| list1 | graphic | txtgraphc) +</td><td></td><td>&gt;</td></tr><tr><td>&lt;!ATTLIST entry</td><td></td><td></td><td></td></tr><tr><td>colname</td><td>NMTOKEN</td><td>#IMPLIED</td><td></td></tr><tr><td>namest</td><td>NMTTOKEN</td><td>#IMPLIED</td><td></td></tr><tr><td>nameend</td><td>NMTTOKEN</td><td>#IMPLIED</td><td></td></tr></table>

```csv
spanganese NMTOKEN #IMPLIED  
morerows NUMBER "0"  
colsep %yesorno; #IMPLIED  
rowsep %yesorno; #IMPLIED  
rotate %yesorno; "0"  
align (top|middle|bottom) "top"  
align (left|right|center  
|justify|char) #IMPLIED  
charoff NUTOKEN #IMPLIED  
char CDATA #IMPLIED >  
<!ELEMENT ftnote -- (%text;) - (graphic)  
<!ATTLIST ftnote  
ftnoteid ID #REQUIRED >  
<!-- -- ->  
<!-- GRAPHIC ->  
<!-- 图形 ->  
<!-- -- ->  
<!ELEMENT graphref -- (#PCDATA) ->  
<!ATTLIST graphref  
refid IDREF #IMPLIED  
sheetnbr CDATA #IMPLIED  
structid CDATA #IMPLIED  
shownow %yesorno; "0" >  
<!-- ELEMENT graphic -- ((effect?, chgdesc*, title?, sheet+) | %deleted; >  
<!ATTLIST graphic  
%revatt; ->  
<!ELEMENT sheet -- ((effect?, chgdesc*, title?, gdesc?) | %deleted; >  
<!ATTLIST sheet  
sheetnbr CDATA #REQUIRED  
gnbr ENTITY #REQUIRED  
%revatt; ->  
<!ELEMENT gdesc -- (%text;) - (graphic) >  
<!-- -- ->  
<!-- LISTS ->  
<!-- 清单 ->  
<!-- -- ->  
<!ELEMENT list1 -- (title?, 11item+) - (list1) >  
<!ATTLIST list1
```

<table><tr><td>key</td><td>ID</td><td>#IMPLIED</td><td>&gt;</td></tr><tr><td>&lt;!ELEMENT list2</td><td colspan="2">-- (title?, 12item+)</td><td>* &gt;</td></tr><tr><td>&lt;!ATTLIST list2</td><td></td><td></td><td></td></tr><tr><td>key</td><td>ID</td><td>#IMPLIED</td><td>&gt;</td></tr><tr><td>&lt;!ELEMENT list3</td><td colspan="2">-- (title?, 13item+)</td><td>&gt;</td></tr><tr><td>&lt;!ATTLIST list3</td><td></td><td></td><td></td></tr><tr><td>key</td><td>ID</td><td>#IMPLIED</td><td>&gt;</td></tr><tr><td>&lt;!ELEMENT list4</td><td colspan="2">-- (title?, 14item+)</td><td>&gt;</td></tr><tr><td>&lt;!ATTLIST list4</td><td></td><td></td><td></td></tr><tr><td>key</td><td>ID</td><td>#IMPLIED</td><td>&gt;</td></tr><tr><td>&lt;!ELEMENT list5</td><td colspan="2">-- (title?, 15item+)</td><td>&gt;</td></tr><tr><td>&lt;!ATTLIST list5</td><td></td><td></td><td></td></tr><tr><td>key</td><td>ID</td><td>#IMPLIED</td><td>&gt;</td></tr><tr><td>&lt;!ELEMENT list6</td><td colspan="2">-- (title?, 16item+)</td><td>&gt;</td></tr><tr><td>&lt;!ATTLIST list6</td><td></td><td></td><td></td></tr><tr><td>key</td><td>ID</td><td>#IMPLIED</td><td>&gt;</td></tr><tr><td>&lt;!ELEMENT list7</td><td colspan="2">-- (title?, 17item+)</td><td>&gt;</td></tr><tr><td>&lt;!ATTLIST list7</td><td></td><td></td><td></td></tr><tr><td>key</td><td>ID</td><td>#IMPLIED</td><td>&gt;</td></tr></table>

<table><tr><td>&lt;--</td><td>LIST ITEMS</td><td>-&gt;</td></tr><tr><td>&lt;--</td><td>清单项</td><td>-&gt;</td></tr><tr><td>&lt;--</td><td>--</td><td>-&gt;</td></tr><tr><td>&lt;--ELEMENT 11item</td><td>-- (chgdesc*, effect?, (%text; | list2) +)</td><td>&gt;</td></tr><tr><td>&lt;--ATTLIST 11item</td><td></td><td></td></tr><tr><td>key</td><td>ID #IMPLIED</td><td>&gt;</td></tr><tr><td>&lt;--ELEMENT 12item</td><td>-- (chgdesc*, (%text; | list3)) +</td><td>&gt;</td></tr><tr><td>&lt;--ATTLIST 12item</td><td></td><td></td></tr><tr><td>key</td><td>ID #IMPLIED</td><td>&gt;</td></tr><tr><td>&lt;--ELEMENT 13item</td><td>-- (chgdesc*, (%text; | list4?)) +</td><td></td></tr><tr><td>&lt;--ATTLIST 13item</td><td></td><td></td></tr><tr><td>key</td><td>ID #IMPLIED</td><td>&gt;</td></tr><tr><td>&lt;--ELEMENT 14item</td><td>-- (chgdesc*, (%text; | list5?))</td><td></td></tr><tr><td>&lt;--ATTLIST 14item</td><td></td><td></td></tr><tr><td>key</td><td>ID #IMPLIED</td><td>&gt;</td></tr><tr><td>&lt;--ELEMENT 15item</td><td>-- (chgdesc*, (%text; | list6?))</td><td></td></tr><tr><td>&lt;--ATTLIST 15item</td><td></td><td></td></tr><tr><td>key</td><td>ID #IMPLIED</td><td>&gt;</td></tr><tr><td>&lt;--ELEMENT 16item</td><td>-- (chgdesc*, (%text; | list7?))</td><td></td></tr><tr><td>&lt;--ATTLIST 16item</td><td></td><td></td></tr><tr><td>key</td><td>ID #IMPLIED</td><td>&gt;</td></tr><tr><td>&lt;--ELEMENT 17item</td><td>-- (chgdesc*, (%text;)</td><td>&gt;</td></tr></table>

```txt
<!ATTLIST 17item  
key ID #IMPLIED >  
<!-- -- =>  
<!-- NUMBERED & UN-NUMBERED LIST ->  
<!-- 有编号和无编号的清单 ->  
<!-- -- =>  
<!ELEMENT numlist -- (numltem+) >  
<!ATTLIST numlist numtype (NNP|AUP|NNB|ALB|NNS|RUP|RLP|RUR|RLR|NNR|AUR|ALR) 'NNP' >  
<!ELEMENT numltem -- (para | unlist) + >  
<!ELEMENT unlist -- (unltem+) >  
<!ATTLIST unlist bulltype (NONE|BULLET|NDASH|MDASH|DIAMOND|ASTERISK|DELTA|SQUARE|SYSTEM) 'SYSTEM' >  
<!ELEMENT unltem -- (%text;) >  
<!-- =>  
<!-- WARNING, CAUTION, NOTE ->  
<!-- 警告，注意，注释 ->  
<!-- =>  
<!ELEMENT warning -- (%text;) - (warning | caution | note | graphic) >  
<!ELEMENT note -- (%text;) - (warning | caution | note | graphic) >  
<!ELEMENT caution -- (%text;) - (warning | caution | note | graphic) >  
<!-- =>  
PARAGRAPH ->  
<!-- 段 ->  
<!-- =>  
<!ELEMENT para -- (#PCDATA | cb | con | csn | ein | equ | ncon | pan | refext | refint | std | ted | toolnbr | toolname | price | zone | sbnbr | manhour | elaphour | pnr | kitnbr | weight | moment | custname | set | kwd | dwg | cus | msnbr | compcode | graphcref | txtgrphc | oldpnr
```

| mdnbr | qty | instdisp | revdate

| revnbr | genrange) + >

<!---->

<!-- REFERENCE ELEMENTS CONTENTS -->

<!-- 参考元素内容 -->

<!-- Meanless:-->

<!ELEMENT cb. -- (#PCDATA)

<!ELEMENT con -- (connbr, conname)

<!ELEMENT connbr -- (#PCDATA)

<!ELEMENT conname -- (#PCDATA)

<!ELEMENT csn -- (#PCDATA)

<!ELEMENT ein -- (#PCDATA)

<!ELEMENT equ -- (#PCDATA)

<!ELEMENT ncon -- (#PCDATA)

<!ELEMENT pan -- (#PCDATA)

<!ELEMENTrefext -- (#PCDATA)

<!ATTLISTrefext refman CDATA #IMPLIED refloc CDATA #IMPLIED refmode CDATA #IMPLIED docnbr CDATA #IMPLIED refspl CDATA #IMPLIED

<!ELEMENT refint -- (#PCDATA)

<!ATTLIST refint  
reftype CDATA #IMPLIED  
refid IDREF #REQUIRED

<!ELEMENT std -- (#PCDATA)

<!ELEMENTTed -- (toolnbr, toolname)

<!ELEMENT toolinbr -- (#PCDATA)

<!ELEMENT toolname -- (#PCDATA)

<!ELEMENT zone -- (#PCDATA)

<!ELEMENT price -- (#PCDATA)

<!ATTLIST price currency CDATA #IMPLIED

<!ELEMENT sbnbr -- (#PCDATA)

<!ELEMENT manhour -- (#PCDATA)

<!ELEMENT elaphour -- (#PCDATA)

<!ELEMENT pnr -- (#PCDATA)

<!ELEMENT kitnbr -- (#PCDATA)

<!ELEMENT weight -- (#PCDATA)

<!ELEMENTmoment --(#PCDATA)

<!ELEMENT kwd -- (#PCDATA)

<!ELEMENT dwg -- (#PCDATA)

<!ELEMENT custname -- (#PCDATA)

<!ELEMENTcus -- (#PCDATA)

<!ELEMENT msnbr -- (#PCDATA)

<!ELEMENT compcode- - (#PCDATA)

<!ELEMENT txtgraphc -- (txtline+)

<!ELEMENT txtline -- (#PCDATA)

<!ELEMENT oldpnr -- (#PCDATA)

<!ELEMENT mdnbr -- (#PCDATA)

<!ELEMENT qty -- (#PCDATA)

<!ELEMENT instdisp -- (#PCDATA)

<!ELEMENT revdate -- (#PCDATA)

<!ELEMENT revnbr -- (#PCDATA)

<!ELEMENT genrange -- (stnbr, endnbr)

<!ATTLIST genrange rangtype CDATA #REQUIRED

<!ELEMENT stnbr -- (#PCDATA)

<!ELEMENT endnbr -- (#PCDATA)

<!---->

<-- MISCELLANEOUS CONSTRUCTIONS: ->

<-- REVISION MARKERS, HOTLINK, TITLE -->

<-- DELETE and CHANGE DESCRIPTION -->

其他用途的结构：->

<!-- 更改标记、热链接、标题-->

<!-- 删除和修改说明-->

<!---->

<!ELEMENT revst -O EMPTY

<!ELEMENT revend -O EMPTY

<!ELEMENT hotlink -O EMPTY

<!ATTLIST hotlink

targetid CDATA #IMPLIED

targetrefid CDATA #IMPLIED

<!ELEMENT title -- (#PCDATA)

<!ELEMENT curadr -- (#PCDATA)

<!ELEMENT oldadr -- (#PCDATA)

<!ELEMENT deleted -O EMPTY

<!ELEMENT chgdesc -- (#PCDATA)

![](images/b0361fdfdfff4502a4000cf588df14de73df61d7e0366a0e224d236597966a55.jpg)

# 2 结构图表

结构图的关键组成部分可参见 DTD 技术要求（参见[4-2-3.22.4]）。为利用采用交互式阅读器的 DTD 的图形进行工作，使用 DTD 结构树阅读器。

![](images/0a8c934c0e76bd8e8b95b31162c78d9d4ebfdd128987435c6ecc55dc58575370.jpg)  
图4-2-31.1 SB/ESB DTD结构一概要和前页

![](images/54a2577e7a12a456a3a89f81f0fecd65d4b38fc119cfc057b275f539487b2c03.jpg)  
图4-2-31.2 SB/ESB DTD结构一概要一和传输表，SB前页，正文与附录

# 4-2-32 服务通报索引(SBI)DTD

# 1 SBI(服务通报索引)DTD

```txt
<!---->  
<!-- DTD Header -->  
<!-- DTD 程序头 -->  
<!---->  
<!---->  
This is the ATA Service Bulletin Index DTD -->  
<!-- 这是 ATA 服务通报索引的 DTD -->  
<!---->  
DTD Reference : ATA-TEXT-SB-INDEX-DTD -->  
DTD 参考: ATA-ATA-TEXT-SB-INDEX-DTD -->  
Revision Date : September 15, 1995 -->  
<!-- 更改日期 : 1995 年 9 月 15 日 -->  
<!-- DTD Level : 2 -->  
<!-- DTD 级别 : 2 -->
```

```txt
<!DOCTYPE sbi [
```

```txt
<-- The following set of declarations may be referred
```

to using a public entity as follows:

<!DOCTYPE sbi PUBLIC

"-//ATA-TEXT//DTD SB-2100NEW-VER3-REV1-LEVEL2//EN" []>

<!-- Meanless:-->

$<  -  >$  NOTATIONS  $\rightarrow$

<!-- 符号-->

<!-- ---->

<!NOTATION cgm PUBLIC

"~/USA-DOD//NOTATION Computer Graphics Metafile//EN"

<!NOTATION ccitt4 PUBLIC

"~/USA-DOD//NOTATION CCITT Group 4 Facsimile//EN"

<!-- Meanless:  $\rightarrow$ -->

<! -- ENTITIES

<!-- 实体-->

<!-- ---->

<!ENTITY % text "para | unlist | numlist | list1 | note) +"

<!ENTITY % yesorno "NUMBER"

<!ENTITY % ISOtech PUBLIC "ISO 8879-1986//ENTITIES General Technical//EN" >

<!ENTITY %ISOpub PUBLIC "ISO 8879-1986//ENTITIES Publishing//EN"

<!ENTITY % ISOnum PUBLIC

"ISO 8879-1986//ENTITIES Numeric and Special Graphic//EN"

<!ENTITY % ISOgrk1 PUBLIC "ISO 8879-1986//ENTITIES Greek Letters//EN"

%ISotech; %ISOpub; %ISOnum; %ISOgrk1;

<!-- Meanless:-->

<!-- Service Bulletin Index High Level Structure -->

<!--服务通报索引高级结构

<!-- ---->

<!ELEMENT sbi -- (title, intro?, effxref?, index, vsbindex?)

<!ATTLIST sbi

model CDATA #REQUIRED

spl CDATA #REQUIRED

tsn CDATA #IMPLIED

oidate NUMBER #IMPLIED

revdate NUMBER #REQUIRED

chg (N|R|U) #REQUIRED

lang CDATA #REQUIRED

<!-- Meanless:-->

<!-- TITLE -->

<!-- 标题 -->

```txt
<!-- --->  
<!ELEMENT title -- (#PCDATA)
```

```txt
INTRODUCTION
```

```twig
<!-- 前言 -->
```

```txt
<!---->
```

```batch
<!ELEMENT intro -- (%text;)
```

```asp
<!-- Meanless:-->
```

```txt
<!-- EFFXREF -->
```

```txt
<--
```

```txt
<!ELEMENT effxref -- (title, eqdata+)
```

```txt
<!ELEMENT eqdata -- (cus?, linenbr?, msnbr, venbr?)
```

```txt
<!ELEMENTcus （#PCDATA）
```

```batch
<!ELEMENT linenbr -- (#PCDATA)
```

```txt
<!ELEMENT msnbr -- (#PCDATA)
```

```txt
<!ELEMENT venbr -- (#PCDATA)
```

```asp
<!-- Meanless:-->
```

```txt
<!-- INDEX -->
```

```twig
<!-- 索引 -->
```

```asp
<!-- Meanless: <1-->
```

```txt
<!ELEMENT index -- (idxdata+)
```

```txt
<!ATTLIST index
indertype CDATA #IMPLIED
```

```asp
<!-- Meanless: <1-->
```

```txt
<!-- INDEX DATA -->
```

```txt
<!-- 索引数据 -->
```

```asp
<!-- Meanless:-->
```

```txt
<!ELEMENT idxdata -- (sbnbr, title, chapsect*, kitnbr*, equipid?, mvt?, (asbnbr, title)*, revinfo+)
```

```batch
<!ATTLIST idxdata digsb %yesorno; #REQUIRED
```

```txt
<!ELEMENT revinfo -- (tsn, typecode*, (revdate | oidate), sbtype?, mdnbr*, compcode*) >
```

```txt
<!ELEMENT sbnbr -- (#PCDATA)
```

```batch
<!ATTLIST sbnbr approvsb %yesomo; #IMPLIED > <!ELEMENT tsn -- (#PCDATA)
```

<table><tr><td>&lt;!ELEMENT oidate</td><td>--</td><td>(#PCDATA)</td><td>&gt;</td></tr><tr><td>&lt;!ELEMENT typecode</td><td>--</td><td>(#PCDATA)</td><td>&gt;</td></tr><tr><td>&lt;!ELEMENT mdnbr</td><td>--</td><td>(#PCDATA)</td><td>&gt;</td></tr><tr><td>&lt;!ELEMENT sbtype</td><td>--</td><td>(#PCDATA)</td><td>&gt;</td></tr><tr><td>&lt;!ELEMENT chapsect</td><td>--</td><td>(#PCDATA)</td><td>&gt;</td></tr><tr><td>&lt;!ELEMENT kitnbr</td><td>--</td><td>(#PCDATA)</td><td>&gt;</td></tr><tr><td>&lt;!ELEMENT revdate</td><td>--</td><td>(#PCDATA)</td><td>&gt;</td></tr><tr><td>&lt;!ELEMENT equipid</td><td>--</td><td>(eqentry | (eqrange, expndrg?))+</td><td>&gt;</td></tr><tr><td>&lt;!ELEMENT eqentry</td><td>--</td><td>(#PCDATA)</td><td>&gt;</td></tr><tr><td>&lt;!ELEMENT eqrange</td><td>--</td><td>(eq, eqend)</td><td>&gt;</td></tr><tr><td>&lt;!ELEMENT expndrg</td><td>--</td><td>(eq+))</td><td>&gt;</td></tr><tr><td>&lt;!ELEMENT eqst</td><td>--</td><td>(#PCDATA)</td><td>&gt;</td></tr><tr><td>&lt;!ELEMENT eqend</td><td>--</td><td>(#PCDATA)</td><td>&gt;</td></tr><tr><td>&lt;!ELEMENT mvt</td><td>--</td><td>(#PCDATA)</td><td>&gt;</td></tr><tr><td>&lt;!ELEMENT compcode</td><td>--</td><td>(#PCDATA)</td><td>&gt;</td></tr><tr><td>&lt;!ELEMENT asbnbr</td><td>--</td><td>(#PCDATA)</td><td>&gt;</td></tr><tr><td>&lt;!ATTLIST asbnbr</td><td></td><td></td><td></td></tr><tr><td>spl</td><td>CDATA</td><td># IMPLIED</td><td>&gt;</td></tr></table>

<table><tr><td colspan="3">&lt;-- VSBINDEX DATA</td><td>-&gt;</td></tr><tr><td>&lt;--</td><td></td><td></td><td>-&gt;</td></tr><tr><td>&lt;-- ELEMENT vsbindex</td><td>--</td><td>(vsbxdata+)</td><td>&gt;</td></tr><tr><td>&lt;-- ELEMENT vsbxdata</td><td>--</td><td>(chapnbr, vendname, sbnbr, issdate, title)</td><td>&gt;</td></tr><tr><td>&lt;-- ELEMENT chapnbr</td><td>--</td><td>(#PCDATA)</td><td>&gt;</td></tr><tr><td>&lt;-- ELEMENT issdate</td><td>--</td><td>(#PCDATA)</td><td>&gt;</td></tr><tr><td>&lt;-- ELEMENT vendname</td><td>--</td><td>(#PCDATA)</td><td>&gt;</td></tr></table>

<table><tr><td colspan="3">-&gt;</td></tr><tr><td colspan="3">-&gt;</td></tr><tr><td colspan="3">-&gt;</td></tr><tr><td colspan="3">-&gt;</td></tr><tr><td colspan="3">-&gt;</td></tr><tr><td colspan="3">-&gt;</td></tr><tr><td colspan="3">-&gt;</td></tr><tr><td colspan="3">-&gt;</td></tr><tr><td colspan="3">-&gt;</td></tr><tr><td colspan="3">-&gt;</td></tr><tr><td colspan="3">-&gt;</td></tr><tr><td colspan="3">-&gt;</td></tr><tr><td colspan="3">-&gt;</td></tr><tr><td colspan="3">-&gt;</td></tr><tr><td colspan="3">-&gt;</td></tr><tr><td colspan="3">-&gt;</td></tr><tr><td colspan="3">-&gt;</td></tr><tr><td colspan="2">-&gt;</td><td></td></tr><tr><td colspan="3">-&gt;</td></tr><tr><td colspan="3">-&gt;</td></tr><tr><td colspan="3">-&gt;</td></tr><tr><td colspan="3">-&gt;</td></tr><tr><td colspan="3">-&gt;</td></tr><tr><td colspan="3">-&gt;</td></tr><tr><td colspan="3">-&gt;</td></tr><tr><td colspan="3">-&gt;</td></tr><tr><td colspan="3">-&gt;</td></tr><tr><td colspan="3">-&gt;</td></tr><tr><td colspan="3">-&gt;</td></tr><tr><td colspan="3">-&gt;</td></tr><tr><td colspan="3">-&gt;</td></tr><tr><td colspan="3">-&gt;</td></tr><tr><td colspan="3">-&gt;</td></tr><tr><td colspan="3">-&gt;</td></tr><tr><td colspan="3">-</td></tr></table>

<table><tr><td>&lt;--</td><td>LIST ITEMS</td><td>→</td></tr><tr><td>&lt;--</td><td>清单项</td><td>→</td></tr><tr><td>&lt;--</td><td></td><td>→</td></tr></table>

```batch
<!ELEMENT 11item -- (%text;， list2?) >  
<!ELEMENT 12item -- (%text;， list3?) >  
<!ELEMENT 13item -- (%text;， list4?) >  
<!ELEMENT 14item -- (%text;， list5?) >  
<!ELEMENT 15item -- (%text;， list6?) >  
<!ELEMENT 16item -- (%text;， list7?) >  
<!ELEMENT 17item -- (%text;） >
```

```txt
<!-- NUMBERED & UN-NUMBERED LIST  
<!-- 已编号和未编号的清单-->  
<!--  
<!ELEMENT numlist -- (numltem+)  
<!ATTLIST numlist numtype (NNP|AUP|NNB|ALB|NNS|RUP|RLP|RUR|RLR|NNR|AUR|ALR) 'NNP'>  
<!ELEMENT numltem -- (para+)  
<!ELEMENT unlist -- (unltem+)  
<!ATTLIST unlist  
bulldype (NONE|BULLET|NDASH|MDASH|DIAMOND|ASTERISK|DELTA|SQUAR|SYSTEM)'SYSTEM'  
<!ELEMENT unltem -- (%text;)  
<!-- NOTE  
<!-- 注释  
<!--  
<!ELEMENT note -- (%text;) - (note)  
<!--  
<!-- PARAGRAPH  
<!-- 段 ->  
<!--  
<!ELEMENT para -- (#PCDATA)  
]
```

# 2 结构图表

结构图的关键组成部分可参见 DTD 技术要求（参见[4-2-3.22.4]）。为利用采用交互式阅读器的 DTD 的图形进行工作，使用 DTD 结构树阅读器。

![](images/27cc9fdd30275255ae751bf9c1a03b6fd404d0898003e835ed568b5a8c427ab4.jpg)  
图4-2-32.1 SBI DTD结构一有效性对照、索引和供应商SB索引

# 4-2-33 结构修理手册(SRM)DTD

# 1 SRM(结构修理手册)DTD

<!---->  
$<  ! - -$  This is the ATA DTD for the Structural Repair Manual  
<!--这是结构修理手册的ATA DTD-->  
<!-- Meanless: <1-->  
<!-- DTD Reference : ATA-TEXT-SRM-DTD-2100-002  
<!-- DTD参考：ATA-TEXT-SRM-DTD-2100-002 ->  
<!-- DTD Level : 2  
<!-DTD级别 :2  
Rev Date : August, 1999  
<!--更改日期 : 1999年8月 -->  
←  
<!-- REVISION HISTORY  
<!-- 更改历史 -->  
<!-- Meanless:  $\rightarrow$ -->  
<-- Spec 2200 Rev , August 1999 DTD Ver 2  
<!-- Attribute name SECNBR changed to SECTNBR according to CSDD -->  
<!-- Spec 2100 Rev 5, Jan 1999 DTD Ver 1 -->  
<!-- Corrected %TEXT to include elements DAMAGE and TABNMET as -->  
<!-- choices  $\rightarrow$  
<-- Corrections to published DTD to match electronic DTD (Ed.) -->  
$<  ! - -$  Removed duplicate definitions of sbnbr, mdnbr (Ed.)  
<!-- Status Level to RECOMMENDED FOR USE per the September 1998 -->

```txt
<!-- ATA TEXT Working Group meeting in Manchester, U. K. ->  
<!-- Spec 2100 Rev 3, November 1996 DTD Ver 1 ->  
<!-- Initial Issue ->  
<!--规范2200更改，1999年8月DTD版本2 ->  
<!-- 根据CSDD将属性名称SECNBR更改为SECTNBR ->  
<!-- 规范21005号更改，1999年1月DTD版本1 ->  
<!-- 对%TEXT进行了修改，以包括元素DAMAGE和TABNMET作为选择项 ->  
<!-- 修正纸质版本的DTD以使其与电子版本DTD相匹配(Ed.) ->  
<!-- 删除了sbnbr，mdnbr的重复定义(Ed.) ->  
<!-- 经1998年9月在英国曼彻斯特召开的ATA TEXT工作组会议 ->  
<!-- 确定了RECOMMENDED FOR USE的状态级别 ->  
<!-- 规范21003号更改，1996年11月DTD版本1 ->  
<!-- 初版 ->  
<!-- --->  
<!DOCTYPE smr [  
<!-- The following set of declarations may be referred by using a public identifier as follows:  
<!--以下公共标识符的使用可参考如下声明的集合：  
<!DOCTYPE smr PUBLIC  
"-//ATA-TEXT//DTD SRM-VER2-LEVEL2//EN" ->  
<!-- ENTITIES ->  
<!-- 实体 ->  
<!-- --->  
<!ENTITY % w.c "(warning | caution) *") ->  
<!ENTITY % text "(para|graphic|unlist|damage|ident|note |matlinfo|tabnmet|supllist|numlist |txtgrphc|equi | (idsch, ftnote*) | (repmat, ftnote*) | (sblist, ftnote*) | (modsblst, ftnote*) | table)" ->  
<!ENTITY % yesorno "NUMBER" ->  
<!ENTITY % deleted "(deleted, chgdesc*)" ->  
<!ENTITY % revatt 
"chg (N|R|U|D) #REQUIRED 
key ID #REQUIRED 
revdate NUMBER #REQUIRED">  
<!ENTITY % iddata "idmade,(idmdraw|(idmpn,idmpn?)|idmstd)" ->  
<!ENTITY % ISOtech PUBLIC 
"ISO 8879-1986/ENTITIES General Technical//EN" ->  
<!ENTITY % ISOpub PUBLIC 
"ISO 8879-1986/ENTITIES Publishing//EN" ->
```

```txt
<!ENTITY %ISOnum PUBLIC
"ISO 8879-1986//ENTITIES Numeric and Special Graphic//EN">
<!ENTITY % ISOgrkl PUBLIC
"ISO 8879-1986//ENTITIES Greek Letters//EN" >%
%ISOtech; %ISOpub; %ISOnum; %ISOgrkl;
<-->
<!-- SRM TOP LEVEL STRUCTURE
<!-- SRM 顶层结构 -->
<!-- ELEMENT smr -- ((title, intro, chapter+) | increv | tr++)
+(revst | revend | hotlink) ->>
<-->
spl CDATA #REQUIRED
model CDATA #REQUIRED
oidate NUMBER #REQUIRED
revdate NUMBER #REQUIRED
tsn CDATA #REQUIRED
lang CDATA #REQUIRED
chg (N|R|D|U) #REQUIRED >
<-->
Incremental Revision ->>
<--增加的更改 ->>
<-->
<-- (intro | chapter | section | subject |
topic) +
<-->
<-- TEMPORARY REVISION ->>
<--临时更改 ->>
<-->
<-- (trfmatr, topic)
<-- (title, treason, %text);
<--ATTLIST trfmatr
tmbr CDATA #REQUIRED
issdate NUMBER #REQUIRED
tdel CDATA #IMPLIED
trepl CDATA #IMPLIED >
<-- (#PCDATA) ->>
<-->
<-- ATA SRM breakdown structure ->>
<-- ATA SRM划分结构 ->>
<-->
<-- (chgdesc*, title, topic)
<--ATTLIST intro
%revatt; ->
```

<table><tr><td colspan="3">-- (chgdesc*, title, section+)</td></tr><tr><td>-- (ATTLIST chapter</td><td></td><td></td></tr><tr><td>chapnbr</td><td>NUMBER</td><td>#REQUIRED</td></tr><tr><td>%revatt;</td><td></td><td>&gt;</td></tr><tr><td>-- (ELEMENT section</td><td>-- (chgdesc*, title, subject)+</td><td></td></tr><tr><td>-- (ATTLIST section</td><td></td><td></td></tr><tr><td>chapnbr</td><td>NUMBER</td><td>#REQUIRED</td></tr><tr><td>sectnbr</td><td>NUMBER</td><td>#REQUIRED</td></tr><tr><td>%revatt;</td><td></td><td>&gt;</td></tr><tr><td>-- (ELEMENT subject</td><td>-- ((chgdesc*, title, topic+) | %deleted;)</td><td></td></tr><tr><td>-- (ATTLIST subject</td><td></td><td></td></tr><tr><td>chapnbr</td><td>NUMBER</td><td>#REQUIRED</td></tr><tr><td>sectnbr</td><td>NUMBER</td><td>#REQUIRED</td></tr><tr><td>subjnbr</td><td>NUMBER</td><td>#REQUIRED</td></tr><tr><td>%revatt;</td><td></td><td>&gt;</td></tr><tr><td>-- (ELEMENT topic</td><td>-- ((effect, chgdesc*, title, list1) | %deleted;) &gt;</td><td></td></tr><tr><td>-- (ATTLIST topic</td><td></td><td></td></tr><tr><td>atacsn</td><td>CDATA</td><td>#REQUIRED</td></tr><tr><td>pgblknbr</td><td>NUMBER</td><td>#REQUIRED</td></tr><tr><td>confnbr</td><td>NUMBER</td><td>#IMPLIED</td></tr><tr><td>prtncode</td><td>NUMBER</td><td>#REQUIRED</td></tr><tr><td>part</td><td>CDATA</td><td>#IMPLIED</td></tr><tr><td>confeff</td><td>CDATA</td><td>#IMPLIED</td></tr><tr><td>actype</td><td>CDATA</td><td>#REQUIRED</td></tr><tr><td>%revatt;</td><td></td><td>&gt;</td></tr><tr><td colspan="3">&lt;-- Standard Tables -&gt;</td></tr><tr><td colspan="3">&lt;--标准表 -&gt;</td></tr><tr><td colspan="3">&lt;-- -&gt; -&gt;</td></tr><tr><td colspan="3">&lt;-- 51-33-00 standard table: nonmetallic materials -&gt;</td></tr><tr><td colspan="3">&lt;--51-33-00 标准表: 非金属材料 -&gt;</td></tr><tr><td colspan="3">&lt;-- -&gt; -&gt;</td></tr><tr><td colspan="3">&lt;--ELEMENT tabnmet -- (effect?, nmeline)+ -&gt;</td></tr><tr><td colspan="3">&lt;--ATTLIST tabnmet id ID #REQUIRED -&gt;</td></tr><tr><td colspan="3">&lt;--ELEMENT nmeline -- (spec, (categ, desman+)) + -&gt;</td></tr><tr><td colspan="3">&lt;--ELEMENT desman -- (desig, manu) -&gt;</td></tr><tr><td colspan="3">&lt;--ELEMENT desig -- (#PCDATA) -&gt;</td></tr><tr><td colspan="3">&lt;-- 51-35-00 standard table: consumable material list -&gt;</td></tr><tr><td colspan="3">&lt;--51-35-00 标准表: 消耗性材料清单 -&gt;</td></tr><tr><td colspan="3">&lt;-- -&gt; -&gt;</td></tr><tr><td colspan="3">&lt;-- ELEMENT matlinfo -- (cmltem)+ -&gt;</td></tr><tr><td colspan="3">&lt;--ELEMENT cmltem -- (matlprn, matlname, refcell, supcell) -&gt;</td></tr></table>

```txt
<!ELEMENT matlpnr -- (#PCDATA)  
<!ELEMENT matname -- (#PCDATA)  
<!ELEMENT refcell -- (ref, cspec*)  
<!ELEMENT supcell -- (spl) +  
<!ELEMENT ref -- (#PCDATA)  
<!ELEMENT spl -- (#PCDATA)  
<!ELEMENT cspec -- (country, spec)  
<!ELEMENT country -- (#PCDATA)  
<!---->  
<!---51-35-00 standard table: supplier list-->  
<!---51-35-00 标准表: 供应商清单-->  
<!------>  
<!ELEMENT supllist -- (suplline) +  
<!ELEMENT suplline -- (spl, (suplne) +)  
<!ELEMENT suplne -- (#PCDATA)  
<!---->  
<!--standard table: Mod/SB List-->  
<!---标准表: Mod/SB 清单-->  
<!------>  
<!ELEMENT modsblist -- (effect?, modline+, ftnote*)  
<!ELEMENT modline -- (effect?, mdnbr?, md suff?, model, msneff, sbnbr?) - (revst | revend) >  
<!ELEMENT model -- (#PCDATA | refint) +  
<!ELEMENT msneff -- (#PCDATA | refint) +  
<!ELEMENT md suff -- (#PCDATA | refint) +  
<!---->  
<!--standard table: Identification Scheme-->  
<!---标准表: 标识示意图-->  
<!------>  
<!ELEMENT idsch -- (effect?, schline+, ftnote*)  
<!ELEMENT schlin -- (effect?, sitem, smomcl, sreffo) - (revst | revend) >  
<!ELEMENT sitem -- (#PCDATA | refint) +  
<!ELEMENT snomcl -- (#PCDATA | refint) +  
<!ELEMENT sreffo -- (refext | sfigrefs)  
<!ELEMENT sfigrefs -- (#PCDATA | graphref | refint) +  
<!---->  
<!--standard table: Repair Materials-->  
<!---标准表: 修理用器材-->  
<!------>  
<!ELEMENT repmat -- (effect?, repline+, ftnote*)  
<!ELEMENT repline -- (effect?, ritem, (momcl | matdesc)?, rqty, matrem)
```

```diff
- (revst | revend) >  
<!ELEMENT matrem -- (#PCDATA | graphcref | refext | cmlmat | txtmat | refint) +  
<!ELEMENT ritem -- (#PCDATA | refint) +  
<!ELEMENT momcl -- (#PCDATA | refint) +  
<!ELEMENT matdesc -- (#PCDATA | refint) +  
<!ELEMENT rqty -- (#PCDATA | refint) +  
<-- standard table: SB List  
<--标准表：SB清单  
<-- standard table: SB List  
<-- 标准表：SB清单  
<-- standard table: SB List  
<-- 标准表：SB清单  
<-- standard table: SB List  
<-- 标准表：SB清单  
<-- standard table: SB List  
<-- 标准表：SB清单  
<-- standard table: SB List  
<-- 标准表：SB清单  
<-- standard table: SB List  
<-- 标准表：SB清单  
<-- standard table：sbdata+，fnote*)  
<-- standard table：SBList  
<-- 标准表：SB清单  
<-- standard table：sbdata+，fnnote*)  
<-- 标准表：SB清单  
<-- standard table：sbdata+，fnnote*)  
<-- standard table：sbdata+，fnnote*)  
<-- standard table：sbdata+，fnnote*)  
<-- standard table：sbdata+，fnnote*)  
<-- standard table：sbdata+，fnnote*)  
<-- standard table：sbdata+，fnnote*)  
<-- standard table：sbdata+，fnnote*)  
<-- standard table：sbdata+，fnnote*)  
<-- standard table：sbdata +，dtdesc？,atanbr?， mdnbr*, cocnbr*, ics?, icdate?, custeff?)  
-(revst | revend) >  
<!ELEMENT sbnbr -- (effect?, sbdata+, fnote*)  
<!ELEMENT sbdata -- (effect?, sbnbr, sbrev?, sbdesc?, atanbr?, mdnbr*, cocnbr*, ics?, icdate?, custeff?)  
-(revst | revend) >  
<!ELEMENT sbnbr -- (#PCDATA | refint) +  
<!ELEMENT sbrev -- (#PCDATA | refint) +  
<!ELEMENT ics -- (#PCDATA | refint) +  
<!ELEMENT sbdesc -- (#PCDATA | refint) +  
<!ELEMENT atanbr -- (#PCDATA | refint) +  
<!ELEMENT mdnbr -- (#PCDATA | refint) +  
<!ELEMENT cocnbr -- (#PCDATA | refint) +  
<!ELEMENT icdate -- (#PCDATA | refint) +  
<!ELEMENT custeff -- (#PCDATA | refint) +  
<-- standard table：Damage Table  
<-- 标准表：损伤表  
<-- standard table：Damage Table  
<-- 标准表：损伤表  
<-- standard table：Damage Table  
<-- standard table：Damage Table  
<-- standard table：Damage Table  
<-- standard table：Damage Table  
<-- standard table：Damage Table  
<-- standard table：Damage Table  
<-- standard table：Damage Table  
<-- standard table：Damage Table  
<-- standard table：Damage Table  
<-- standard table：Damage Table  
<-- standard table：Damage Table  
<-- standard table：Damage Table
```

```txt
<!ELEMENT idnhalin -- (idnha, iditem, iditem?, idind, idsh, idvarlin+) >  
<!ELEMENT idvarlin -- (idvar, idstdlin+) >  
<!ELEMENT idstdlin -- (idstd, idstamod*, idillcod+) >  
<!ELEMENT item -- (#PCDATA) >  
<!ELEMENT idnomcl -- (#PCDATA) >  
<!ELEMENT idspsec -- (idspec?, idsec?, idtxt?) >  
<!ELEMENT idspec -- (#PCDATA) >  
<!ELEMENT idsec -- (#PCDATA) >  
<!ELEMENT idtxt -- (#PCDATA) >  
<!ELEMENT idpstd -- (idtxt | (idpn, idpn?, idthick?, (%idata;)) ?) | (iddim, (%idata;)?, idtxt?)) >  
<!ELEMENT idpn -- (#PCDATA) >  
<!ELEMENT idthick -- (#PCDATA) >  
<!ELEMENT idmade -- (#PCDATA) >  
<!ELEMENT idmdraw -- (#PCDATA) >  
<!ELEMENT idmpn -- (#PCDATA) >  
<!ELEMENT idmstd -- (#PCDATA) >  
<!ELEMENT iddim -- (#PCDATA) >  
<!ELEMENT idic -- (#PCDATA) >  
<!ELEMENT idactrp -- (idtxt | refext+) >  
<!ELEMENT idstamod -- (idmodmp | sbnbr | idrc) >  
<!ELEMENT idmodmp -- (#PCDATA) >  
<!ELEMENT idrc -- (#PCDATA) >  
<!ELEMENT idnha -- (#PCDATA) >  
<!ELEMENT iditem -- (#PCDATA) >  
<!ELEMENT idind -- (#PCDATA) >  
<!ELEMENT idsh -- (#PCDATA) >  
<!ELEMENT idvar -- (#PCDATA) >  
<!ELEMENT idstd -- (#PCDATA) >  
<!ATTLIST idstd std CDATA #REQUIRED>  
<!ELEMENT idillcod -- (#PCDATA) >  
<!ATTLIST idillcod refid IDREF #REQUIRED>  
<!-- Nested numbered list structure -->  
<!--嵌套的有编号的清单结构 -->  
<!--——-->  
<!-- nested numbered list structure -->  
<!--嵌套的有编号的清单结构 -->  
<!--——-->  
<!-- nested numbered list structure -->  
<!--嵌套的有编号的清单结构 -->
```

```txt
<!ELEMENT 12step -- (effect?, %w.c.; 12item, (note* | %w.c?))  
<!ELEMENT 12item -- (para, %text; list3?)  
<!ATTLIST 12item id ID #IMPLIED >  
<!--ELEMENT list3 -- (l3step) +  
<!ELEMENT 13step -- (effect?, %w.c.; 13item, (note* | %w.c?))  
<!ELEMENT 13item -- (para, %text; list4?)  
<!ATTLIST 13item id ID #IMPLIED >  
<!--ELEMENT list4 -- (l4step) +  
<!ELEMENT 14step -- (effect?, %w.c.; 14item, note*)  
<!ELEMENT 14item -- (para, %text; list5?)  
<!ATTLIST 14item id ID #IMPLIED >  
<!--ELEMENT list5 -- (l5step) +  
<!ELEMENT 15step -- (effect?, %w.c.; 15item, note*)  
<!ELEMENT 15item -- (para, %text; list6?)  
<!ATTLIST 15item id ID #IMPLIED >  
<!--ELEMENT list6 -- (l6step) +  
<!ELEMENT 16step -- (effect?, %w.c.; 16item, note*)  
<!ELEMENT 16item -- (para, %text; >  
<!ATTLIST 16item id ID #IMPLIED >  
<!--ELEMENT numlist -- (effect?, numltem+)  
<!ATTLIST numlist numtype (NNP|AUP|NNB|ALB|NNS|RUP|RLP|RUR|RLR|NNR|AUR|ALR) 'NNP' >  
<!ELEMENT numltem -- (effect?, para+)  
<!ELEMENT unlist -- (effect?, unltem+)  
<!ATTLIST unlist bulltype (NONE|BULLET|NDASH|MDASH|DIAMOND|ASTERISK |DELTA|SQUARE|SYSTEM)'SYSTEM' >  
<!ELEMENT unltem -- (effect?, %text; >  
<!-- EFFECTIVITY - TBD by ATA Effectivity WG ->  
<!-- - following definition to satisfy parser ->  
<!--有效性 - ATA Effectivity WG 的 TBD ->  
<!-- - 下列定义满足分析器 ->  
<!-- ELEMENT effect -- (#PCDATA)
```

```txt
<!--TABLE(CALS)   
<!--表(CALS)   
<!--   
<!ELEMENT table --((title?, tgroup, ftnote*) | graphic+) - (table) >   
<!ATTLIST table tabstyle NMTOKEN #IMPLIED frame (top|bottom|topbot|all|sides|none) #IMPLIED colsep %yesorno; #IMPLIED rowsep %yesorno; #IMPLIED orient (port | land) #IMPLIED pgwide %yesorno; #IMPLIED id ID #IMPLIED >   
<!ELEMENT tgroup -O (colspec*, spanspec*, thread?, tfoot?, tbody) >   
<!ATTLIST tgroup cols NUMBER #REQUIRED colsep %yesorno; #IMPLIED rowsep %yesorno; #IMPLIED align (left|right|center|justify|char) "left" charoff NUTOKEN "50" char CDATA " " >   
<!ELEMENT colspec -O EMPTY >   
<!ATTLIST colspec colnum NUMBER #IMPLIED colname NMTOKEN #IMPLIED align (left|right|center|justify|char) #IMPLIED charoff NUTOKEN #IMPLIED char CDATA #IMPLIED colwidth CDATA #IMPLIED colsep %yesorno; #IMPLIED rowsep %yesorno; #IMPLIED >   
<!ELEMENT spanspec -O EMPTY >   
<!ATTLIST spanspec namest NMTOKEN #REQUIRED nameend NMTOKEN #REQUIRED spanname NMTOKEN #REQUIRED align (left|right|center|justify|char) "center" charoff NUTOKEN #IMPLIED char CDATA #IMPLIED colsep %yesorno; #IMPLIED rowsep %yesorno; #IMPLIED >   
<!ELEMENT thad -O (colspec*, row+) >   
<!ATTLIST thad
```

<table><tr><td>valign</td><td>(top|middle|bottom)</td><td>&quot;bottom&quot;</td><td>&gt;</td></tr><tr><td>&lt;!ELEMENT tfoot</td><td>-O (colspec*, row+)</td><td></td><td>&gt;</td></tr><tr><td>&lt;!ATTLIST tfoot</td><td></td><td></td><td></td></tr><tr><td>valign</td><td>(top|middle|bottom)</td><td>&quot;top&quot;</td><td>&gt;</td></tr><tr><td>&lt;!ELEMENT tbody</td><td>-O (row+)</td><td></td><td>&gt;</td></tr><tr><td>&lt;!ATTLIST tbody</td><td></td><td></td><td></td></tr><tr><td>valign</td><td>(top|middle|bottom)</td><td>&quot;top&quot;</td><td>&gt;</td></tr><tr><td>&lt;!ELEMENT row</td><td>-O (entry+)</td><td></td><td>&gt;</td></tr><tr><td>&lt;!ATTLIST row</td><td></td><td></td><td></td></tr><tr><td>rowsep</td><td>%yesorno;</td><td>#IMPLIED</td><td>&gt;</td></tr><tr><td>&lt;!ELEMENT entry</td><td>-- (paratab)</td><td></td><td>&gt;</td></tr><tr><td>&lt;!ATTLIST entry</td><td></td><td></td><td></td></tr><tr><td>colname</td><td>NMTOKEN</td><td>#IMPLIED</td><td></td></tr><tr><td>namest</td><td>NMTOKEN</td><td>#IMPLIED</td><td></td></tr><tr><td>nameend</td><td>NMTOKEN</td><td>#IMPLIED</td><td></td></tr><tr><td>spanname</td><td>NMTOKEN</td><td>#IMPLIED</td><td></td></tr><tr><td>morerows</td><td>NUMBER</td><td>&quot;0&quot;</td><td></td></tr><tr><td>colsep</td><td>%yesorno;</td><td>#IMPLIED</td><td></td></tr><tr><td>rowsep</td><td>%yesorno;</td><td>#IMPLIED</td><td></td></tr><tr><td>rotate</td><td>%yesorno;</td><td>&quot;0&quot;</td><td></td></tr><tr><td>valign</td><td>(top|middle|bottom)</td><td>&quot;top&quot;</td><td></td></tr><tr><td>align</td><td>(left|right|center|justify|char)</td><td>#IMPLIED</td><td></td></tr><tr><td>charoff</td><td>NUTOKEN</td><td>#IMPLIED</td><td></td></tr><tr><td>char</td><td>CDATA</td><td>#IMPLIED</td><td>&gt;</td></tr><tr><td>&lt;!ELEMENT ftnote</td><td>-- (effect?, %text;)</td><td></td><td></td></tr><tr><td></td><td>-(graphic)</td><td></td><td></td></tr><tr><td>&lt;!ATTLIST ftnote</td><td></td><td></td><td></td></tr><tr><td>ftnoteid</td><td>ID</td><td>#REQUIRED &gt;</td><td></td></tr><tr><td>&lt;!--</td><td></td><td></td><td>-&gt;</td></tr><tr><td>&lt;!-- GRAPHIC</td><td></td><td></td><td>-&gt;</td></tr><tr><td>&lt;!-- 图形--&gt;</td><td></td><td></td><td></td></tr><tr><td>&lt;!--</td><td></td><td></td><td>-&gt;</td></tr><tr><td>&lt;!ELEMENT graphref</td><td>-- (#PCDATA)</td><td></td><td>&gt;</td></tr><tr><td>&lt;!ATTLIST graphref</td><td></td><td></td><td></td></tr><tr><td>refid</td><td>IDREF</td><td>#IMPLIED</td><td></td></tr><tr><td>sheetnbr</td><td>CDATA</td><td>#IMPLIED</td><td></td></tr><tr><td>structid</td><td>CDATA</td><td>#IMPLIED</td><td></td></tr><tr><td>shownow</td><td>%yesorno;</td><td>&quot;0&quot;</td><td>&gt;</td></tr><tr><td>&lt;!ELEMENT graphic</td><td>-- ((effect?, chgdesc*, title?, sheet+) |</td><td></td><td></td></tr><tr><td></td><td></td><td>%deleted,)</td><td>&gt;</td></tr><tr><td>&lt;!ATTLIST graphic</td><td></td><td></td><td></td></tr><tr><td>%revatt;</td><td></td><td></td><td>&gt;</td></tr><tr><td>&lt;!ELEMENT sheet</td><td>-- ((effect?, chgdesc*, title?, gdesc?) |</td><td></td><td></td></tr><tr><td></td><td></td><td>%deleted,)</td><td>&gt;</td></tr></table>

<table><tr><td colspan="3">&lt;!ATTLIST sheet</td></tr><tr><td>sheetnbr</td><td>CDATA</td><td>#REQUIRED</td></tr><tr><td>gnbr</td><td>ENTITY</td><td>#REQUIRED</td></tr><tr><td>%revatt;</td><td></td><td>&gt;</td></tr><tr><td>&lt;!ELEMENT gdesc</td><td>-- (%text;)</td><td></td></tr><tr><td></td><td>-(graphic)</td><td>&gt;</td></tr><tr><td>&lt;!--警告、注意、注释</td><td>---&gt;</td><td></td></tr><tr><td>&lt;!--警告、注意、注释</td><td></td><td>-&gt;</td></tr><tr><td>&lt;!--警告、注意、注释</td><td></td><td>-&gt;</td></tr><tr><td>&lt;!--警告、注意、注释</td><td></td><td>-&gt;</td></tr><tr><td>&lt;!--警告、注意、注释</td><td></td><td>-&gt;</td></tr><tr><td>&lt;!--警告、注意、注释</td><td></td><td>-&gt;</td></tr><tr><td>&lt;!--警告、注意、注释</td><td></td><td>-&gt;</td></tr><tr><td>&lt;!--警告、注意、注释</td><td></td><td>-&gt;</td></tr><tr><td>&lt;!--警告、注意、注释</td><td></td><td>-&gt;</td></tr></table>

```txt
<!ELEMENT revend -O EMPTY  
<!ELEMENT deleted -O EMPTY  
<!ELEMENT chgdesc -- (#PCDATA)  
<!ELEMENT title -- (#PCDATA)  
<!ELEMENT txtmat -- ((spec, categor) | (manu, categor))  
<!ELEMENT spec -- (#PCDATA)  
<!ELEMENT manu -- (#PCDATA)  
<!ELEMENT categ -- (#PCDATA)  
<!ELEMENT cnnmat -- (#PCDATA)  
]>
```

# 2 结构图表

对于结构图的关键组成部分可参见 DTD 技术要求(参见[4-2-3.22.4])。

![](images/589ee3423a5c8d4e420a6e29c5a5f726dd402a39c15e163805731d523adc9cf9.jpg)  
图4-2-33.1SRMDTD结构一概要(章、节、标题、增加的更改和临时更改)

# 4-2-34 系统说明(SDS)DTD

# 1 SDS(系统说明)DTD

```txt
<!-- This is the DTD for the System Description Section
<!--这是系统说明的DTD
<!--DTD Reference : "/ATA-TEXT//DTD SDS-VER5-LEVEL2//EN"
<!-- DTD 参考: "/ATA-TEXT//DTD SDS-VER5-LEVEL2//EN"
<!-- DTD Level : 2
<!--DTD 级别 : 2
<!-- Rev Date : 01 Dec 1995
<!--更改日期 : 1995年12月1日
```

<!-- Highlights : Updated to incorporate changes in March -->

1996 Technical Requirements Document.

<!-- ->

$<  ! - - 1)$  Increased the "VER" number to 5.

$<  ! - 2)$  Removed poschg and poskey attributes from the revatt

<!-- entity per tech-req 1.2.1 section. -->

$<  ! - -$  更改摘要：为合并1996年3月技术要求文档中的改变进行更新

<!-- 1) "VER"号增加到5.-->

$<  ! - >$  2) 按照tech-req1.2.1节从revatt实体中删除poschg和poskey属性

<!---->

<!DOCTYPE SDS [

$<<$  The following set of declarations may be referred to using a public entity as follows:

<--以下公共实体的使用可参考如下声明的集合：

<!DOCTYPE SDS PUBLIC

"-//ATA-TEXT//DTD SDS-VER5-LEVEL2//EN"[][->

<<

<!-- NOTATIONS

<!-- 符号-->

<<

<!NOTATION cgm PUBLIC

'-//USA-DOD//NOTATION Computer Graphics Metafile//EN'

<!NOTATION ccitt4 PUBLIC

'-//USA-DOD//NOTATION CCITT Group 4 Facsimile//EN'

←

<!-- ENTITIES

实体-->

←

<!ENTITY % text
' (para|table|unlist|glosdata|warning|caution|note) +'

<!ENTITY % deleted '('deleted, chgdesc?)'

<!ENTITY % yesorno 'NUMBER'

<!ENTITY % revatt

'chg (N|R|U|D) #REQUIRED

key ID #REQUIRED

revdate NUMBER #REQUIRED>

<!ENTITY % ISOtech PUBLIC

ISO 8879-1986//ENTITIES General Technical//EN

<!ENTITY % ISOpub PUBLIC

'ISO 8879-1986//ENTITIES Publishing//EN

<!ENTITY % ISOnum PUBLIC

'ISO 8879-1986//ENTITIES Numeric and Special Graphic//EN

<!ENTITY % ISOgrk1 PUBLIC

'ISO 8879-1986//ENTITIES Greek Letters//EN

%ISOtech; %ISOpub; %ISOnum; %ISOgrk1;

<!---->

SDS TOP LEVEL STRUCTURE

<!-- SDS 顶层结构-->

<!-- ---->

<!ELEMENT SDS --((title, mfmatr?, chapter+) | increv|tr+))

+ (revst|revend|cocst|cocend|hotlink)

<!ATTLIST SDS

spl CDATA #REQUIRED

model CDATA #REQUIRED

oidate NUMBER #REQUIRED

revdate NUMBER #REQUIRED

tsn CDATA #REQUIRED

cus CDATA #IMPLIED

cusname CDATA #IMPLIED

docnbr CDATA #IMPLIED

lang CDATA #REQUIRED

>

<!ELEMENT increv -- (transltr?, (chapter|section|subject

|pageset|textset|sheet|graphic|intro

```c
|tlist|effxref|sblist) +)

<!ELEMENT tr -- (trfmatr, (chapter | section+| subject+

| pageset+ | textset+ | sheet+ | graphic+

| effxref | sblist)

<!ELEMENT trfmatr -- (title, treason, (%text;))

<!ATTLIST trfmatr

tmbr CDATA #REQUIRED

trdel CDATA #IMPLIED

```txt
trrepl CDATA #IMPLIED
issdate NUMBER #REQUIRED
<!ELEMENT treason -- (#PCDATA)
<!-- SDS FRONT MATTER
<!-- SDS 前页 -->
<!-- --->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->--(transltr?, trlist, intro, effxref, sblist)>
<!ELEMENT transltr -- (chgdesc*, title, (prclist|%text;))
<!ATTLIST transltr %revatt;
<IELEMENT trlist -- ((%text?), (trdata+|isempty))
<!ATTLIST trlist %revatt;
<IELEMENT trdata -- (tmbr, trstatus, trloc++)
<IELEMENT intro -- (chgdesc*, title, prclist1)
<!ATTLIST intro %revatt;
<IELEMENT effxref -- (chgdesc*, title, (%text?), effdata++)
<!ATTLIST effxref %revatt;
<IELEMENT effdata -- (cus?, modtype?, cec, linenbr?, venbr?, benbr?, msnbr, acn)
<!ELEMENT sblist -- (chgdesc*, title, %text;
(%data+ |isempty))
<!ATTLIST sblist %revatt;
<!ELEMENT sbdata -- (sbnbr?, sbtitle?, eonbr?, atanbr?, mdnbr*, cocnbr*, sc?, ics, custeff?)
<!ELEMENT custeff -- ((cus, effrc)+)
<!ELEMENT custeff -- ((cus, effrc)+)
<!ELEMENT custeff -- ((cus, effrc)+)
<!ELEMENT custeff -- ((cus, effrc)+)
<!ELEMENT custeff -- ((cus, effrc)+)
<!ELEMENT custeff -- ((cus, effrc)+)
<!ELEMENT custeff -- ((cus, effrc)+)
<!ELEMENT custeff -- ((cus, effrc)+)
<!ELEMENT custeff -- ((cus, effrc)+)
<!ELEMENT custeff -- (cusp, effrc)+)
<!ELEMENT custeff -- (cusp, effrc)+)
<!ELEMENT custeff -- (cusp, effrc)+)
<!ELEMENT custeff -- (cusp, effrc)+)
<!ELEMENT custeff -- (cusp, effrc)+)
<!ELEMENT custeff -- (cusp, effrc)+)
<!ELEMENT custeff -- (cusp, effrc)+)
<!ELEMENT custeff -- (cusp, emf)
<!ELEMENT custeff -- (cusp, emf)
<!ELEMENT custeff -- (cusp, emf)
<!ELEMENT custeff -- (cusp, emf)
<!ELEMENT custeff -- (cusp, emf)
<!ELEMENT custeff -- (cusp, emf)
<!ELEMENT custeff -- (cusp, emf)
<!ELEMENT custeff -- (cusp, emf)
<!ELEMENT custeff -- (cusp, emf)
<!ELEMENTcustuff -- ((cus, affrc)+)
<!ELEMENTcustuff -- (cusp, affrc)+)
<!ELEMENTcustuff -- (cusp, affrc)+)
<!ELEMENTcustuff -- (cusp, affrc)+)
<!ELEMENTcustuff -- (cusp, affrc)+)
<!ELEMENTcustuff -- (cusp, affrc)+)
<!ELEMENTcustuff -- (cusp, affrc)+)
<!ELEMENTcustuff -- (cusp, affrc)+)
<!ELEMENTcustuff -- (cusp, affrc)+)
<!ELEMENTcustoff -- ((cus, affrc)+)
<!ELEMENTcustoff -- (cusp, affrc)+)
<!ELEMENTcustoff -- (cusp, affrc)+)
<!ELEMENTcustoff -- (cusp, affrc)+)
<!ELEMENTcustoff -- (cusp, affrc)+)
<!ELEMENTcustoff -- (cusp, affrc)+)
<!ELEMENTcustoff -- (cusp, affrc)+)
<!ELEMENTcustoff -- (cusp, affrc)+)
<!ELEMENTcustoff -- (cusp, affrc)+)
<!ELEMENTcust off -- (cusp, affrc)+)
<!ELEMENTcust off -- (cusp, affrc)+)
<!ELEMENTcust off -- (cusp, affrc)+)
<!ELEMENTcust off -- (cusp, affrc)+)
<!ELEMENTcust off -- (cusp, affrc)+)
<!ELEMENTcust off -- (cusp, affrc)+)
<!ELEMENTcust off -- (cusp, affrc)+)
<!ELEMENTcust off -- (cusp, affrc)+}
<!ELEMENTcust off -- (cusp, affrc)+)
<!ELEMENTcust off -- (cusp, affrc)+)
<!ELEMENTcust off -- (cusp, affrc)+)
<!ELEMENTcust off -- (cusp, affrc)+)
<!ELEMENTcust off -- (cusp, affrc)+)
<!ELEMENTcust off -- (cusp, affrc)+)
<!ELEMENTcust off -- (cusp, affrc)+)
<!ELEMENTcust off -- (cusp,
affrc) >
```

```txt
<!ELEMENT cus -- (#PCDATA)  
<!ELEMENT effrc -- (#PCDATA)  
<!ELEMENT modtype -- (#PCDATA)  
<!ELEMENT cec -- (#PCDATA)  
<!ELEMENT linenbr -- (#PCDATA)  
<!ELEMENT venbr -- (#PCDATA)  
<!ELEMENT sc -- (#PCDATA)  
<!ELEMENT sbnbr -- (#PCDATA)  
<!ELEMENT sbtitle -- (#PCDATA)  
<!ELEMENT eonbr -- (#PCDATA)  
<!ELEMENT can -- (#PCDATA)  
<!ELEMENT atanbr -- (#PCDATA)  
<!ELEMENT benbr -- (#PCDATA)  
<!ELEMENT mdnbr -- (#PCDATA)  
<!ELEMENT cocnbr -- (#PCDATA)  
<!ELEMENT ics -- (#PCDATA)  
<!ELEMENT msnbr -- (#PCDATA)  
<!ELEMENT tmbr -- (#PCDATA)  
<!ELEMENT trstatus -- (#PCDATA)  
<!ELEMENT trloc -- (#PCDATA)
```

```txt
<!-- CHAPTER ->  
<!-- 章->  
<!-- -- (effect?, chgdesc*, title, section+)  
|%deleted;)  
<!ELEMENT chapter -- ((effect?, chgdesc*, title, section+)  
|%deleted;  
<!ATTLIST chapter  
chapnbr NUMBER #REQUIRED  
%revatt;  
<!-- SECTION ->  
<!-- 节 ->  
<!-- SECTION ->  
<!ELEMENT section -- ((effect?, chgdesc*, title, subject+)  
|%deleted;  
<!ATTLIST section  
chapnbr NUMBER #REQUIRED  
sectnbr NUMBER #REQUIRED  
%revatt;
```

```html
<!-- SUBJECT   
<!-- 标题-->   
<!--   
<!ELEMENT subject --((effect?, chgdesc*, title, pageset+) |%deleted;) >   
<!ATTLIST subject chapnbr NUMBER #REQUIRED sectnbr NUMBER #REQUIRED subjnbr NUMBER #REQUIRED %revatt;   
<!-- PAGESET   
<!--   
<!ELEMENT pageset --((effect, chgdesc*, title, textset, graphic+) |%deleted;) >   
<!ATTLIST pageset chapnbr NUMBER #REQUIRED sectnbr NUMBER #REQUIRED subjnbr NUMBER #REQUIRED pgsetnbr NUMBER #REQUIRED perfblk CDATA #IMPLIED level NUMBER #IMPLIED tmgunit CDATA #IMPLIED %revatt;   
<!--   
<!-- TEXTSET   
<!--   
<!ELEMENT textset -- (effect, chgdesc*, textgrp+) >   
<!ATTLIST textset oldkey NAME #IMPLIED %revatt;   
<!--   
<!-- TEXTGRP   
<!--
```

```batch
tip %yesorno; #IMPLIED
```

```txt
<!-- PROCEDURE LIST STRUCTURE -->
```

```txt
程序清单结构
```

```txt
<!ELEMENT prclist1 -- (prcitem1+) + (effect)
```

```txt
<!ELEMENT prclist2 -- (prcitem2+)
```

```txt
<!ELEMENT prclist3 -- (prcitem3+)
```

```txt
<!ELEMENT prclist4 -- (prcitem4+)
```

```txt
<!ELEMENT prclist5 -- (prcitem5+)
```

```txt
<!ELEMENT prclist6 -- (prcitem6+)
```

```txt
<!ELEMENT prclist7 -- (prcitem7+)
```

```txt
<!ELEMENT prcitem1 -- (prcitem, prclist2?, graphic*)
```

```txt
<!ELEMENT prcitem2 -- (prcitem, prclist3?)
```

```txt
<!ELEMENT prcitem3 -- (prcitem, prclist4?)
```

```txt
<!ELEMENT prcitem4 -- (prcitem, prclist5?)
```

```txt
<!ELEMENT prcitem5 -- (prcitem, prclist6?)
```

```txt
<!ELEMENT prcitem6 -- (prcitem, prclist7?)
```

```batch
<!ELEMENT prcitem7 -- (prcitem)
```

```txt
<!ELEMENT prcitem -- (title?, (%text;))
```

```txt
<!-- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
```

```txt
$<  ! - -$  表（单元，基于CALS）  $\rightarrow$ $<  ! - -$
```

```txt
<!ELEMENT table --((title?, tgroup, ftnote*) | graphic+) - (table)
```

```txt
<!ATTLIST table tabstyle NMTOKEN #IMPLIED frame (top|bottom|topbot|all sides|none) #IMPLIED colsep %yesorno; #IMPLIED rowsep %yesorno; #IMPLIED orient (port|land) #IMPLIED pgwide %yesorno; #IMPLIED id ID #IMPLIED
```

```txt
<!ELEMENT tgroup -o (colspec*, spanspec*, thead?, tfoot?, tbody)>
```

```txt
<!ATTLIST tgroup cols NUMBER #REQUIRED
```

```asm
colsep %yesorno; #IMPLIED
rowsep %yesorno; #IMPLIED
align(left|right|center|justify|char)'left'
charoff NUTOKEN '50'
char CDATA "
<!ELEMENT colspec -o EMPTY
<!ATTLIST colspec
    colnum NUMBER #IMPLIED
    colname NMTOKEN #IMPLIED
    align (left|right|center|justify|char) #IMPLIED
    charoff NUTOKEN #IMPLIED
    char CDATA #IMPLIED
    colwidth CDATA #IMPLIED
    colsep %yesorno; #IMPLIED
    rowsep %yesorno; #IMPLIED
<!ELEMENT spanspec -o EMPTY
<!ATTLIST spanspec
    namest NMTOKEN #REQUIRED
    nameend NMTOKEN #REQUIRED
    spanname NMTOKEN #IMPLIED
    align (left|right|center|justify|char) 'center'
    charoff NUTOKEN #IMPLIED
    char CDATA #IMPLIED
    colsep %yesorno; #IMPLIED
    rowsep %yesorno; #IMPLIED
<!ELEMENT (thead|foot) -o (colspec*, row+) > <!ELEMENT tbody -o (row+) > <!ATTLIST thead
valign (top|middle|bottom) 'bottom' >
<!ATTLIST (tfoot|tbody)
valign (top|middle|bottom) 'top' >
<!ELEMENT row -o (entry+) > <!ATTLIST row
rowsep %yesorno; #IMPLIED
<!ELEMENT entry -o (%text|graphic) >
<!ATTLIST entry
colname NMTOKEN #IMPLIED
```

```lisp
nameest NMTOKEN #IMPLIED
nameend NMTOKEN #IMPLIED
spanname NMTOKEN #IMPLIED
morerows NUMBER '0'
colsep %yesorno; #IMPLIED
rowsep %yesorno; #IMPLIED
rotate %yesorno; '0'
valign (top|middle|bottom) 'top'
align (left|right|center|justify|char) #IMPLIED
charoff NUTOKEN #IMPLIED
char CDATA #IMPLIED
<--ELEMENT ftnote --%text;
<--ATTLIST ftnote
tnoteid ID #REQUIRED
<--ELEMENT grphref -- (effect?, #PCDATA)
<--ATTLIST grphref
refid IDREF #IMPLIED
sheetnbr CDATA #IMPLIED
structid CDATA #IMPLIED
shownow %yesorno '0'
<--ELEMENT graphic -- ((effect, chgdesc*, title?, sheet++)
|%deleted);
<--ATTLIST graphic
chapnbr NUMBER #IMPLIED
sectnbr NUMBER #IMPLIED
subjnbr NUMBER #IMPLIED
pgsetnbr NUMBER #IMPLIED
oldkey NAME #IMPLIED
%revatt;
<--ELEMENT sheet -- ((effect, chgdesc*, title?)
```

```txt
|%deleted;）   
<!ATTLIST sheet gnbr ENTITY #REQUIRED sheetnbr CDATA #IMPLIED %revatt;   
<-- UN-NUMBERED LIST -- <-- 无编号的清单   
<-- -- -- (unltem+)   
<!ELEMENT unlist -- (unltem+) > <!ATTLIST unlist bulltype (NONE|BULLET|NDASH|MDASH|DIAMOND |ASTERISK|DELTA|SQUARE|SYSTEM) 'SYSTEM'> <!ELEMENT unltem -- (para+)   
<-- -- -- (PAGRAPH   
<-- -- - ( #PCDATA | cb | equ | graphcref <-- 段-->   
<-- -- -- (PAGRAPH CONTENTS   
<-- -- PARAGRAPH CONTENTS   
<-- -- - ( #PCDATA)   
<-- ELEMENT cb -- (#PCDATA)   
<-- ELEMENT ein -- (#PCDATA)   
<-- ELEMENT equ -- (#PCDATA)   
<-- ELEMENT pan -- (#PCDATA)   
<-- ELEMENT refext -- (#PCDATA)   
<!ATTLIST refext refman CDATA #IMPLIED refspl CDATA #IMPLIED refmodel CDATA #IMPLIED docnbr CDATA #IMPLIED refloc CDATA #IMPLIED
```

<!ELEMENT refint -- (#PCDATA)

<!ATTLIST refint

```txt
retypeof CDATA #IMPLIED  
refid IDREF #IMPLIED
```

<!ELEMENT txtgrphc -- (txtline+)

<!ELEMENT txtline -- (#PCDATA)

<!ELEMENT zone -- (#PCDATA)

<!-- Meanless:-->

GLOSSARY DATA

<!-- 术语表数据-->

<!-- Meanless:-->

<!ELEMENT glosdata -- (term, def)

<!ELEMENT term -- (#PCDATA)

<!ELEMENT def -- (#PCDATA)

<!-- Meanless:  $\rightarrow$ -->

TITLE,WARNING,CAUTION and NOTE

<!-- 标题、警告、注意和注释 -->

<!-- Meanless:-->

<!ELEMENT title -- (#PCDATA | ein | sbnbr) +

<!ELEMENT warning -- (para]unlist)

<!ELEMENT note -- (paraunlist) +

<!ELEMENT caution -- (para|unlist) +

<!-- Meanless:  $< 1 -  >$ -->

EFFECTIVITY

<!-- 有效性 -->

<!-- Meanless: <1-->

<!ELEMENT effect -- (sbeff|coceff)*

```txt
<!ATTLIST effect effrg CDATA #IMPLIED efftext CDATA #IMPLIED
```

<!ELEMENT (sbeff|coceff) -O EMPTY

<!ATTLIST sbeff

```txt
effrg CDATA #IMPLIED
efftext CDATA #IMPLIED
sbnbr CDATA #REQUIRED
sbcond CDATA #REQUIRED
sbrev CDATA #IMPLIED
<!ATTLIST coceff
effrg CDATA #IMPLIED
efftext CDATA #IMPLIED
cocnbr CDATA #REQUIRED
<-- MISCELLANEOUS CONSTRUCTS
--->其它的结构--
<-- -->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->- -(#PCDATA)
<--ELEMENT deleted - O EMPTY
isempty - O EMPTY
(revst|revend|cocst|cocend)
-O EMPTY
- - (#PCDATA)
<--ELEMENT hotlink - O EMPTY
targetid CDATA #IMPLIED
targetrefid CDATA #IMPLIED
>
```

# 2 标准和技术的应用

# 2.1 适用的页集合清单

对SDS有一个特定的要求：它应能提取或参考非ATA(章一节一题目)编号的多个页集合(Pageset)以建立培训教材。很明显，这一点可以通过LEA的特定版本的应用来完成。因为尽管它适合不同的需要，它仍被称为适用的页集合(Pageset)清单(LAP)。

除了SDS的基本LEA外，其它的(培训)教材的LAP可由制造商或操作员建立的文档实例来提供。这些(培训)教材的LAP将仅列出在生成(培训)教材时所需的页集合(Pageset)。每个(培训)教材的LAP将通过在主要更改位置标识清单之前的一个标题元素和一个注元素来标识。这些元素都是#PCDATA。因此，这些(培训)教材LAP的DTD是：

```txt
<!DOCTYPE LAPxxxxx  
<!ELEMENT LAPxxxxx -- (laptitle, lapnote?, pageset+)  
<!ATTLIST LAPxxxxx  
crsnbr CDATA #REQUIRED  
spl CDATA #REQUIRED
```

```txt
model CDATA #REQUIRED
oidate NUMBER #REQUIRED
revdate NUMBER #REQUIRED
tsn CDATA #REQUIRED
cus CDATA #IMPLIED
cusname CDATA #IMPLIED
docnbr CDATA #IMPLIED
lang CDATA #REQUIRED
chg (N|R|U) 'N'
cec CDATA #IMPLIED
<!ATTLIST pageset -0 EMPTY
<!ELEMENT pageset
key ID #REQUIRED
revdate NUMBER #REQUIRED
<!ELEMENT (laptitle|lapnote) -- #PCDATA
```

为了使系统能够将不同的(培训)教材相互区分开来，预留了 doctype(文件类型)的最后 5 个字符，这 5 个字符是该 SDS 唯一的后缀代码。为了使制造商或操作者能够独立的开发(培训)教材，建议该后缀代码以 ICAO(国际民用航空组织)的三个字符开始，在其后加上(培训)教材的两个字母数字字符标识符。如果认为有必要，title(标题)和 note(注)元素可用于标识和限定使用者(人)的(培训)教材。

# 2.2 SDS特殊定义术语表

# Pageset

是由 textset(文本集合)和一个以上的图形组成的系统信息的基本单位。

# Textset

Pageset(页集合)的所有 textgroup(文本组)

# Textgrp

文本组。定义数据的一个单个逻辑组的最小完整信息单位。

# Pgsetnbr

页集合编号。在章-节-题目中的一个Pageset的唯一标识符。

# Perfblk

操作块。[ATA Spec 104]定义的标准操作块，例如，操作，目的和界面等。

# Level

[ATA Spec 104]定义的标准培训级别，例如，Gen Fam，Ramp与通过等。

# Trgunit

培训单元。一个特定培训目标的Pageset逻辑组。

# TIP

将一个Textgrp定义为是(或不是)一个培训信息点。

# LAP

适用的页集合(Pageset)清单。这是技术要求文档中定义的LEA结构的特殊应用。用它从SDS中建立培训教材。

# Crsnbr

培训教材编号。通过分配的唯一标识符。

# Laptitle

培训教材的标题。

Lapnote

附加的教材信息，如描述性注释、更改数据，开发者注释等。

# 3 结构图表

结构图的关键组成部分可参见 DTD 技术要求（参见[4-2-3.22.4])。

![](images/346fab7f8292d2424345c05245f01da33b075a714477ee28363e5bb19d0176f5.jpg)  
图4-2-34.1 SDS DTD结构一概述

![](images/54e5b75a9a839ebd9dfb600d07e6d1084094d0eaaba7fde1744923abd5384faf.jpg)  
图4-2-34.2 SDS DTD结构-Increv和TR

# 4-2-35 工具和设备手册(TEM)DTD

# 1 工具和设备手册(TEM)DTD

<table><tr><td>&lt;--</td><td>DTD for Tool and equipment Manuals, TEM, Version 1.1</td><td>-&gt;</td></tr><tr><td>&lt;--</td><td>工具和设备手册的 DTD, TEM, 版本 1.1</td><td>-&gt;</td></tr><tr><td>&lt;--</td><td>Rev History</td><td>-&gt;</td></tr><tr><td>&lt;--</td><td>更改历史</td><td>-&gt;</td></tr><tr><td>&lt;--</td><td>Rev 1.2 - Pre-release D 01-16-99 - TWR</td><td>-&gt;</td></tr><tr><td>&lt;--</td><td>版本 1.2-预发放 D 01-16-99 - TWR</td><td>-&gt;</td></tr><tr><td>&lt;--</td><td>Changed status of DTD from &quot;In Development&quot; to &quot;Recommended</td><td>-&gt;</td></tr><tr><td>&lt;--</td><td>for Use&quot; per Text Working Group meeting held</td><td>-&gt;</td></tr><tr><td>&lt;--</td><td>September 1998 in Manchester, U.K.</td><td>-&gt;</td></tr><tr><td>&lt;--</td><td>经 1998 年 9 月在英国曼彻斯特召开的 TEXT 工作组会议,将 DTD 的状 态从“正在研发”改为“推荐使用”。</td><td>-&gt;</td></tr><tr><td>&lt;--</td><td>Ver 1.12 - Pre-release C 01-24-98 - TWR/NRS</td><td>-&gt;</td></tr><tr><td>&lt;--</td><td>Changed connector between toolnbr and toolname elements</td><td>-&gt;</td></tr><tr><td>&lt;--</td><td>within ted element from &quot;Sequence&quot; to &quot;And&quot;</td><td>-&gt;</td></tr><tr><td>&lt;--</td><td>Changed type of length, width, height, and dia attributes</td><td>-&gt;</td></tr><tr><td>&lt;--</td><td>of dd element from NUMBER to NUTOKEN</td><td>-&gt;</td></tr><tr><td>&lt;--</td><td>版本 1.2-预发放 C 01-24-98 - TWR/NRS</td><td>-&gt;</td></tr><tr><td>&lt;--</td><td>将 ted 元素内在 toolnbr 和 toolname 之间的连接符 从&quot;Sequence&quot; 改变为&quot;And&quot;。</td><td></td></tr><tr><td>&lt;--</td><td>将 dd 元素的 length、width、height 和 dia 类型属性 从 NUMBER 改变为 NUTOKEN。</td><td></td></tr><tr><td>&lt;--</td><td>&lt;--</td><td>-&gt;</td></tr><tr><td>&lt;--</td><td>Ver 1.11 - Pre-release B 06-24-97 - FJB/NRS</td><td>-&gt;</td></tr><tr><td>&lt;--</td><td>Comments cleaned up and previous pre-release marks removed</td><td>-&gt;</td></tr><tr><td>&lt;--</td><td>Added OTHTYPE attribute to those element which had a &quot;TYPE&quot;</td><td>-&gt;</td></tr><tr><td>&lt;--</td><td>that could be &quot;OTH&quot; (other), to allow further</td><td>-&gt;</td></tr><tr><td>&lt;--</td><td>identification of non-standard types</td><td>-&gt;</td></tr><tr><td>&lt;--</td><td>Removed vestigial attributes in Graphic carried over from</td><td>-&gt;</td></tr><tr><td>&lt;--</td><td>Engine manual</td><td>-&gt;</td></tr><tr><td>&lt;--</td><td>Added DIA to DD (Dimensional Data)</td><td>-&gt;</td></tr><tr><td>&lt;--</td><td>Added Unit to Weight</td><td>-&gt;</td></tr><tr><td>&lt;--</td><td>版本 1.11-预发放 B 06-24-97-FJB/NRS</td><td>-&gt;</td></tr></table>

清除注释和删除预发放的标记

对那些“TYPE”可能是“OTH”类型的元素增加了OTHTYPE属性，以允许对非标准类型的进一步识别。

对来自于发动机手册的图形，将其 vestigal 属性删除。

为DD（尺寸数据)增加了DIA。

为重量增加了单位

<-- Ver 1 - Based on Engine Manual DTD - 08-23-96 - FJB/RB/NRS  
<-- Changes Per Rolls Royce report PRPBT001 -->  
<-- Changes per Ad Hoc DTD Mtg in Seattle March 96 -->  
<!-- 版本1-基于发动机手册DTD-08-23-96-FJB/RB/NRS

根据 Rolls Royce(罗罗公司)的报告 PRPBT001 进行了更改

96年3月在西雅图根据AdHocDTDMtg进行了更改

<!-- ->  
<!-- DTD ref: "/ATA-TEXT//DTD TEM-VER1-LEVEL2//EN" ->  
<!-- DTD参考："://ATA-TEXT//DTDTEM-VER1-LEVEL2//EN" --  
<!-- Meanless:-->  
<!-- Implementation Notes: --  
<!-- 执行注解： -->  
1. Changes are marked in section headings  
<!-- 1.在节标题中对更改作了标记 -->  
<!-- 2.DOCTYPE is TEMAN  
(<!-- (because TEM is used in the IPC with different semantics) -->  
<!-- 2.DOCTYPE是TEMAN

（因为在IPC中使用的TEM具有不同的语义）

3.No TRs in TEM  
3.在TEM中没有TRs(临时更改单)  
<!-- 4. MANUAL DIVISIONS -->  
<!-- 4.手册划分 -->

Manual Front Matter 手册前页

o Transmittal Letter 发送函  
o Introduction 前言

Main Manual Sections (no order implied) 手册主要的节(无顺序)

o Tool Sheets (see below for subsections) 工具图页(参见下面的子节)  
o Material Handling Equipment 材料处理设备  
o Control and Accessory Tooling 操纵和辅助加工  
o Standard Equipment Supplier Code 标准设备供应商代码  
o Tool/Engine Effectivity 工具/发动机有效性  
oIndex索引  
o Manufacturer's support equipment 制造商的支持设备  
o Cross-reference tool list 对照工具清单  
oOther 其它  
o MAINTENANCE INDEX 维修索引  
oOVERHAULINDEX大修索引

<!-- Tool Sheet Subsections 工具图页子节  
o purpose and use 目的和使用  
<!-- o tool name and/or description 工具名称和/或描述 -->

<!-- o dimensions尺寸 -->

<!-- o weight 重量 -->

$<  ! - -$  o supporting tools产品支援工具

$<  ! - -$  o tool maintenance 工具维修

$<  ! - -$  oquantityperunitoperation每个操作单元数量

<!-- o parts list / detail listing 零件表/明细表 -->

$<  ! - -$  o manufacturing category 制造种类

<!-- o tool history 工具历史 -->

<!-- o other 其它 -->

<!-- Meanless:-->

$<  ! - -$  The following set of declarations may be referred

<!-- to using a public entity as follows: -->

$<  ! - -$  （20 以下公共实体的使用可参考如下声明的集合：

<!-- !DOCTYPE iteman PUBLIC "-//ATA-TEXT//DTD TEM-VER1-LEVEL2//EN" --

<!-- Meanless: ->

$<  ! - -$

<!DOCTYPE TEMAN [-->

<!-- Meanless:  $\frac{1 + x - 2}{x} = 1 - x$ -->

<!---->

<!-- NOTATIONS 符号 -->

$<  ! - -$

<!-- Meanless:-->

<!NOTATION cgm PUBLIC

"~/USA-DOD//NOTATION Computer Graphics

Metafile//EN"

<!NOTATION ccitt4 PUBLIC

"  $\cdot / / \mathrm{USA - DOD / / NOTATION CCITT}$  Group 4

Facsimile//EN"

<!-- ->

$<  -$

<!-- ENTITIES 实体

<!---->

<!-- Meanless:-->

<!-- tbltem is a group of elements which may appear anywhere in a

table or a paragraph.

$<  ! - -$  tbltem 是可以在一个表格或段落的任何地方出现的一组元素。

<!-- Meanless: ->

<!-- Meanless: ->

<!ENTITY % tbltem " (

dd

| func

level

mfr

```txt
| mfreec
| mad
| modcode
| pnr
| qualcode
| toolname
| toolnbr
| toolpnr
| toolrev
| tqe
| weight
) "
<!ENTITY % text "(para | tabdat | table | unlist |
numlist | note )+" > <!ENTITY % g.r " (graphhref*, refext*, refint*)" > <!ENTITY % w.c " (warning*, caution*)" > <!ENTITY % deleted " (deleted,chgdesc*)" > <!ENTITY % yesorno "NUMBER" > <!ENTITY % revatt
    "chg (N | D | R | U) #REQUIRED
    key ID #REQUIRED
    revdate NUMBER #REQUIRED" > <!ENTITY % stdwarn SYSTEM "optional system id" > <!ENTITY % stdcaut SYSTEM "optional system id" > <!ENTITY % stdwarn; %stdcaut;
<!ENTITY % ISOtech PUBLIC "ISO 8879-1986//ENTITIES
    General Technical//EN"
<!ENTITY % ISOpub PUBLIC "ISO 8879-1986//ENTITIES
    Publishing//EN"
<!ENTITY % ISOnum PUBLIC "ISO 8879-1986//ENTITIES
    Numeric and Special Graphic//EN"
<!ENTITY % ISOgrk1 PUBLIC "ISO 8879-1986//ENTITIES
    Greek Letters//EN"
<!-- %ISOtech; %ISOpub; %ISOnum; %ISOgrk1;
<!-- =>>
TOP LEVEL STRUCTURE 顶层结构
<!-- =>>
Top level model for TEM with std attributes
<!-- 对于有 std 属性的 TEM 的顶层模型
<!ELEMENT TEMAN(3182) -- ((title, mfmatr, section+) | increv)
+ (revst | revend | hotlink)
```

# <!ATTLIST TEMAN

<table><tr><td></td><td>spl (3183)</td><td>CDATA</td><td>#REQUIRED</td></tr><tr><td></td><td>model (3184)</td><td>CDATA</td><td>#REQUIRED</td></tr><tr><td></td><td>oidate (3185)</td><td>NUMBER</td><td>#REQUIRED</td></tr><tr><td></td><td>tsn (3186)</td><td>CDATA</td><td>#REQUIRED</td></tr><tr><td></td><td>cus (3187)</td><td>CDATA</td><td>#IMPLIED</td></tr><tr><td></td><td>cusname (3188)</td><td>CDATA</td><td>#IMPLIED</td></tr><tr><td></td><td>docnbr (3189)</td><td>CDATA</td><td>#IMPLIED</td></tr><tr><td></td><td>lang (3190)</td><td>CDATA</td><td>#REQUIRED</td></tr><tr><td></td><td>revdate (3191)</td><td>NUMBER</td><td>#REQUIRED</td></tr><tr><td></td><td>chg (3192)</td><td colspan="2">(N|R|U) &#x27;N&#x27;</td></tr><tr><td>&lt;--</td><td>= = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =</td><td>-&gt;</td><td></td></tr><tr><td>&lt;--</td><td colspan="3">SECTION [Anchor]</td></tr><tr><td>&lt;--</td><td colspan="3">节[位置标识]</td></tr><tr><td>&lt;--</td><td colspan="3">A collection of tool sheets or other units</td></tr><tr><td>&lt;--</td><td colspan="3">工具图页或其它单元的集合</td></tr><tr><td>&lt;--</td><td colspan="3">section model (new part)</td></tr><tr><td>&lt;--</td><td colspan="3">节模型(新部分)</td></tr><tr><td>&lt;--</td><td colspan="3">A section is a set of tool sheets of a particular type</td></tr><tr><td>&lt;--</td><td colspan="3">(e.g., a set of Tool Data Sheets, or Mat Handl Data Sheets)</td></tr><tr><td>&lt;--</td><td colspan="3">Or it is a &quot;unit&quot;</td></tr><tr><td>&lt;--</td><td colspan="3">节是一种特殊类型的一组工具图页或者一个“单元”。(例如,一组工具数据页,或Mat Handl 数据页)</td></tr><tr><td>&lt;--</td><td colspan="3">Explanation of section abbreviations: 节缩写的说明</td></tr><tr><td>&lt;--</td><td colspan="3">SYM TITLE</td></tr><tr><td>&lt;--</td><td colspan="3">= = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =</td></tr><tr><td>&lt;--</td><td colspan="3">CAT = Control and Accessory Tooling 操纵和辅助加工</td></tr><tr><td>&lt;--</td><td colspan="3">CTL = Cross-reference tool list 对照工具清单</td></tr><tr><td>&lt;--</td><td colspan="3">IDX = Index 索引</td></tr><tr><td>&lt;--</td><td colspan="3">MDX = MAINTENANCE INDEX 维修索引</td></tr><tr><td>&lt;--</td><td colspan="3">MFR = Standard Equipment Supplier Code 标准设备供应商代码</td></tr><tr><td>&lt;--</td><td colspan="3">MHE = Material Handling Equipment 材料处理设备</td></tr><tr><td>&lt;--</td><td colspan="3">MSE = Manufacturer&#x27;s support equipment 制造商的支持设备</td></tr><tr><td>&lt;--</td><td colspan="3">OVX = OVERHAUL INDEX 大修索引</td></tr><tr><td>&lt;--</td><td colspan="3">TDS = Tool Data Sheets 工具数据页</td></tr><tr><td>&lt;--</td><td colspan="3">TEE = Tool/Engine Effectivity 工具/发动机有效性</td></tr><tr><td>&lt;--</td><td colspan="3">OTH = Other 其它</td></tr><tr><td>&lt;--</td><td colspan="3">Notes on the changes from the EM: 注意来自于EM(发动机手册)的更改:</td></tr><tr><td>&lt;--</td><td colspan="3">section - section model changed to allow</td></tr><tr><td>&lt;--</td><td colspan="3">them to be either collections of</td></tr><tr><td>&lt;--</td><td colspan="3">tool sheets or units.</td></tr><tr><td>&lt;--</td><td colspan="3">节-改变了节模型,以允许它们可作为工具表或单元的任何一个集合。</td></tr><tr><td>&lt;--</td><td colspan="3">= = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =</td></tr></table>

```sgml
<!ELEMENT section(3193) -- ((effect?, chgdesc*, title?, pbfmatr?, (tlsheet+ | unit+))
| %deleted;
  )
>
<!ATTLIST section
sectnbr(3194) NUMBER #REQUIRED -- ID for section--
type(3195) (CAT
| CTL
| IDX
| MDX
| MFR
| MHE
| MSE
| OTH
| OVX
| TDS
| TEE
) #REQUIRED
othype(3196) CDATA #IMPLIED -- V1.11--
%revatt;
>
<!-- => ->->)
<TLSHEET [Anchor]
->->>
<TLSHEET [位置标识]
->->>
A tool sheet of a variety of types
->->>
多种类型的一张工具页
->->>
TLSHEET is a tool sheet, which is comprised of
->->>
sub-sections (tlsect).
->->>
TLSHEET 是一张包括分节 (tlsect) 的工具页。
->->>
The sheet type is inherited from SECTION. Only the following
->->>
types apply:
->->>
从SECTION 继承了页类型。仅在下列类型适用:
->->>
SYM TITLE
->->>
== = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
>->->>
CAT= Control and Accessory Tooling 操纵辅助加工
->->>
MHE= Material Handling Equipment 材料处理设备
->->>
MSE= Manufacturer's support equipment 制造商的支持设备
->->>
TDS= Tool Data Sheets 工具数据表
->->>
For TEM, Control and Accessories tooling, the tool sheet nb
(<!-- control and accessories tooling, the tool sheet nb)
(attrib toolnbr) is the associated CMM number
<!-- control and accessories tooling, the tool sheet nb
(attrib toolnbr) is the associated CMM number
对于TEM,操纵辅助加工,工具页nb(属性toolnbr)是相关的CMM编号
<!-- control and accessories tooling, the tool sheet nb
(<!-- control and accessories tooling, the tool sheet nb
(attrib toolnbr) is the associated CMM number
<!-- control and accessories tooling, the tool sheet nb
(<!-- control and accessories tooling, the tool sheet nb
(attrib toolnbr) is the associated CMM number
<!-- control and accessories tooling, the tool sheet nb
(<!-- control and accessories tooling, the tool sheet nb
(attrib toolnbr) is the associated CMM number
<!-- control and accessories tooling, the tool sheet nb
(<!-- control and accessories tooling,
attrition, toolset, toolnumber, toolnumber, toolnumber, toolnumber, toolnumber, toolnumber, toolnumber, toolnumber, toolnumber, toolnumber, toolnumber, toolnumber, toolnumber, toolnumber, toolnumber, toolnumber, toolnumber, toolnumber, toolnumber, toolnumber, toolnumber, toolnumber, toolnumber, toolnumber, toolnumber, toolnumber, toolnumber, toolnumber, toolnumber, toolnumber, toolnumber, toolnumber, toolnumber, toolnumber,
attrition, toolset, toolnumber, toolnumber, toolnumber, toolnumber, toolnumber, toolnumber, toolnumber, toolnumber, toolnumber, toolnumber, toolnumber,
attrition, toolset, toolnumber, toolnumber,
attrition, toolset, toolnumber,
attrition, toolset, toolnumber,
attrition, toolset, toolnumber,
attrition, toolset, toolnumber,
attrition, toolset, toolnumber,
attrition, toolset, toolnumber,
attrition, toolset, toolnumber,
attrition, toolset, toolnumber,
attrition, toolset, toolnumber,
attrition, toolset, toolnumber,
attrition, toolset, toolnumber,
attrition, toolset,
attrition, toolset,
attrition, toolset,
attrition, toolset,
attrition, toolset,
attrition, toolset,
attrition, toolset,
attrition, toolset,
attrition, toolset,
attrition, toolset,
attrition, toolset,
attrition, toolset,
attrition, toolset,
attrition, toolset,
attrition, toolset,
attrition, toolset,
attrition, toolset,
attrition,
attrition,
attrition,
attrition,
attrition,
attrition,
attrition,
attrition,
attrition,
attrition,
attrition,
attrition,
attrition,
attrition,
attrition,
attrition,
attrition,
attrition,
attrition,
attrition,
attrition,
attrition,
attrition,
attrition,
attrition,
attrition,
attrition,
attrition,
attrition,
attrition,
attrition,
attrition,
attrition,
attrition
>->>
>->>
>->>
>->>
>->>
>->>
>->>
>->>
>->>
>->>
>->>
>->>
>->>
>->>
>->>
>->>
>->>
>->>
>->>
>->>
>->>
>->>
>->>
>->>
>->>
>->>
>->>
>->>
>->>
>->>
>->>
>->>
>->>
>->>
"---"
"---"
"---"
"---"
"---"
"---"
"---"
"---"
"---"
"---"
"---"
"---"
"---"
"---"
"---"
"---"
"---"
"---"
"---"
"---"
"---"
"---"
"---"
"---"
"---"
"---"
"---"
"---"
"---"
"---"
"---"
"---"
"---"
"---"
''
"----"
"----"
"----"
"----"
"----"
"----"
"----"
"----"
"----"
"----"
"----"
"----"
"----"
"----"
"----"
"----"
"----"
"----"
"----"
"----"
"----"
"----"
"----"
"----"
"----"
"----"
"----"
"----"
"----"
"----"
"----"
"----"
"----"
"----"
''
"----"
"----"
"----"
"----"
"----"
"----"
"----"
"----"
"----"
"----"
"----"
"----"
"----"
"----"
"----"
"----"
"----"
"----"
"----"
"----"
"----"
"----"
"----"
"----"
"----"
"----"
"----"
"----"
"----"
"----"
"----"
"----"
''
''
''
''
''
''
''
''
''
''
''
''
''
''
''
''
''
''
''
''
''
''
''
''
''
''
''
''
''
''
''
''
''
''
''
''
''
''
''
''
''
''
''
''
''
''
''
''
''
''
'?
'?
'?
'?
'?
'?
'?
'?
'?
'?
'?
'?
'?
'?
'?
'?
'?
'?
'?
'?
'?
'?
'?
'?
'?
'?
'?
'?
'?
'?
'?
'?
'?
'?
'?
'?
'?
'?
'?
'?
'?
'?
'?
'?
'?
'?
'?
'?
'?
'?
'-
'?
'?
'?
'?
'?
'?
'?
'?
'?
'?
'?
'?
'?
'?
'?
'?
'?
'?
'?
'?
'?
'?
'?
'?
'?
'?
'?
'?
'?
'?
'?
'?
'?
'?
'?
'?
.
'TLHESHEET [Anchor]
->->>
TLSHEET [位置标识]
->->>
A tool sheet of a variety of types
->->>
多种类型的一张工具页
->->>
TLSHEET is a tool sheet, which is comprised of
->->>
sub-sections (tlsect).
- >->>
- >->>
- >->>
- >->>
- >->>
- >->>
- >->>
- >->>
- >->>
- >->>
- >->>
- >->>
- >->>
- >->>
- >->>
- >->>
- >->>
- >->>
- >->>
- >->>
- >->>
- >->>
- >->>
- >->>
- >->>
- >->.
- >->.
- >->.
- >->.
- >->.
- >->.
- >->.
- >->.
- >->.
- >->.
- >->.
- >->.
- >->.
- >->.
- >->.
- >->.
- >->.
- >->.
- >->.
- >->.
- >->.
- >->.
- >->.
- >->.
- >->.
- >->;
- >->.
- >->.
- >->.
- >-
- >-
- >-
- >-
- >-
- >-
- >-
- >-
- >-
- >-
- >-
- >-
- >-
- >-
- >-
- >-
- >-
- >-
- >-
- >-
- >-
- >-
- >-
- >-
- >-
- >-
- >-
- >-
- >-
- >-
- >-
- >-
- >-
- >-
= - - -
= - - -
= - - -
= - - -
= - - -
= - - -
= - - -
= - - -
= - - -
= - - -
= - - -
= - - -
= - - -
= - - -
= - - -
= - - -
= - - -
= - - -
= - - -
= - - -
= - - -
= - - -
= - - -
= - - -
= - - -
= - - +
= - - -
= - - -
= - - -
= - - -
= - - -
= - - -
= - - -
= - - -
= - - -
= - - -
= - - -
= - - -
= - - -
= - - -
= - - -
= - - -
= - - -
= - - -
= - - -
= - - -
= - - -
= - - -
= - - -
= - - -
= - - =
		=
		=
		=
		=
		=
		=
		=
		=
		=
		=
		=
		=
		=
		=
		=
		=
		=
		=
		=
		=
		=
		=
		=
		=
		=
		=
		=
		=
		=
		=
		=
		=
		=
		=
			;
		;
		;
		;
		;
		;
		;
		;
		;
		;
		;
		;
		;
		;
		;
		;
		;
		;
		;
		;
		;
		;
		;
		;
		;
		;
		;
		;
		;
		;
		;
		;
			;
			;
			;
			;
			;
			;
			;
			;
			;
			;
			;
			;
			;
			;
			;
			;
			;
			;
			;
			;
			;
			;
			;
			;
			;
			;
			;
			;
			;
			;
			;
			;
			;
			if (TLSHEET[Anchor])
				TLSHEET[位置标识]
				TLSHEET[位置标识]
				TLSHEET[位置标识]
				TLSHEET[位置标识]
				TLSHEET[位置标识]
				TLSHEET[位置标识]
				TLSHEET[位置标识]
				TLSHEET[位置标识]
				TLSHEET[位置标识]
				TLSHEET[位置标识]
				TLSHEET[位置标识]
				TLSHEET[位置标识]
				TLSHEET[位置标识]
				TLSITEM[工具页]
				TLSITEM[工具页]
				TLSITEM[工具页]
				TLSITEM[工具页]
				TLSITEM[工具页]
				TLSITEM[工具页]
				TLSITEM[工具页]
				TLSITEM[工具页]
				TLSITEM[工具页]
				TLSITEM[工具页]
				TLSITEM[工具页]
				TLSITEM[工具页]
				TLSITEM[工具页]
				TLCIF
				TLCIF
				TLCIF
				TLCIF
				TLCIF
				TLCIF
				TLCIF
				TLCIF
				TLCIF
				TLCIF
				TLCIF
				TLCIF
				TLCIF
				TLCIF
				TLCIF
				TLCIF
				TLCIF
				TLCIF
				TLCIF
				TLCIF
				TLCIF<nl>
```

```txt
<!ELEMENT tlsheet(3197) -- ((effect?, chgdesc*, title?, pbfmatr?, (tlsect|graphic)+) |%deleted; ） >  
<!--  
<!ATTLIST tlsheet  
    toolnbr(3198) CDATA #REQUIRED--ID#forthissheet--  
    sectnbr(3199) NUMBER #IMPLIED--Sect#sheetisin--  
    type(3200) (CAT |MHE |MSE |TDS  
    ) #IMPLIED  
    %revatt;  
<!--  
    ===============  
    ===============  
    ===============  
    ===============  
    ===============  
    ===============  
    ===============  
    ===============  
    ===============  
    ===============  
    ===============  
    ===============  
    ===============  
    ===============  
    ===============  
    ===============  
    ===============  
    ===============  
    ===============  
    ===============  
    ===============  
    ===============  
    ===============  
    ===============  
    ===============  
    ="/>  
<!--  
    TLIETCT
    Tool Sheet Sections工具页节
    MHE
    MSEL
    TDS
    SYMTITLE（名称）
    =====================
    MCT= MANUFACTURING CATEGORY制造商种类
    DES= TOOL NAME AND/OR DESCRIPTION工具名称和/或说明
    DIM= DIMENSIONS尺寸
    HIS= TOOL HISTORY工具历史
    OTH= OTHER其它
    PLI= PARTS LIST/DETAIL LISTING零件表/明细表
    PNU= PURPOSE AND USE目的和使用
    QPU= QUANTITY PER UNIT OPERATION每个操作单元数量
    SPT= SUPPORTING TOOLS产品支援工具
    TLM= TOOL MAINTENANCE工具维修
    WGT= WEIGHT重量
    Title is optional per RR problem report 标题是可按照RR问题报告进行选择的
    =(effect?,(%w.c*)*, title?, (%text; %g.r|graphic)+
      )>  
<!--  
    Title is optional per RR problem report 标题是可按照RR问题报告进行选择的
    %(text; %g.r|graphic)+
      )>  
<!ELEMENT tlsect(3201)--(effect?,(%w.c*)*, title?, (%text; %g.r|graphic)+
      )>  
<!ATTLIST tlsect  
type(3202) (MCT |DES |DIM |HIS
```

```txt
| OTH
| PLI
| PNU
| QPU
| SPT
| TLM
| WGT
) #REQUIRED -- Type identifies the tlsect--
othtype (3203) CDATA #IMPLIED -- V1.11--
toolnbr (3204) CDATA #IMPLIED -- V1.11 Inh TLSHEET nbr--
sectnbr (3205) NUMBER #IMPLIED -- V1.11 Inh SECTION nbr
<-- => -> -UNIT [Anchor] 单位[位置标识]
<-- > Units are sections which are not tool sheets
<-- > 单元不是工具页的节
<-- > A unit is one of the non datasheet areas of the document
<-- > for example, a cross-reference tool list.
<-- > 一个单元是文档的非数据表区域之一
<-- > 例如，一个对照的工具表。
<-- > The unit type is inherited from SECTION. Only the following
<-- > types apply:
<-- > 从 SECTION 继承了表类型。仅在下列类型适用:
<-- > SYM TITLE
<-- > = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
<-- > CTL =
CTX =
IDX =
MDX =
MFR =
OVX =
TEE =
and just to be "safe" 并且恰好是安全的
<-- > OTH =
UNIT [Anchor] 单元[位置标识]
<-- > UNIT [Anchor] 单元[位置标识]
<-- > ELEMENT unit (3206) -- ((effect?, chgdesc*, (%w.c));),
title, pbfmatr?,
(%text; |%g.r; |graphic | vendlist)+
)
| %deleted;
) ->
```

```txt
CTL
| IDX
| MDX
| MFR
| OVX
| TEE
| OTH
) #IMPLIED
othtype(3210) CDATA #IMPLIED--V1.11--
%revatt;>
<!ELEMENT increv(3211)--(transltr?, (section | tlsheet |
unit | intro | howtouse | graphic)+)
<-- -- -- (transltr?, intro, howtouse?)
<-- -- -- (chgdesc*, title, (%text;))+>
<!ELEMENT intro(3214) -- (chgdesc*, title, prclist1)+>
<!ELEMENT howtouse(3215)--(chgdesc*, title, prclist1)+>
<-- -- -- (chgdesc*, title, prclist1)+>
<-- -- -- (chgdesc*, title, prclist1)+>
<-- -- -- (chgdesc*, title, prclist1)+>
<-- -- -- (chgdesc*, title, prclist1)+>
<-- -- -- (chgdesc*, title, prclist1)+>
<-- -- -- (chgdesc*, title, prclist1)+>
<-- -- -- (chgdesc* , title, prclist1)+>
<-- -- -- (chgdesc* , title, prclist1)+>
<-- -- -- (chgdesc* , title, prclist1)+>
<-- -- -- (chgdesc* , title, prclist1)+>
<-- -- -- (chgdesc* , title, prclist1)+>
<-- -- -- (chgdesc* , title, prclist1)+>
<-- -- -- (chgDesc*, title, prclist1)+>
<-- -- -- (chgDesc*, title, prclist1)+>
<-- -- -- (chgDesc*, title, prclist1)+>
<-- -- -- (chgDesc*, title, prclist1)+>
<-- -- -- (chgDesc*, title, prclist1)+>
<-- -- -- (chgDesc*, title, prclist1)+>
<-- -- -- (chgDesc*, title, prplist)
%revatt;
<-- -- -- (chgdesc*, title, prplist)
oldkey(3216) NAME #IMPLIED
%revatt;
<-- -- -- (chgdesc*, title, prplist)
pbfmatr - is used at several levels as generic
<-- -- -- (other than at the manual
level.
<-- -- 注:
pbfmatr--作为通用的前页在几个级别上被使用(而非手册正文级)
<!ELEMENT pbfmatr(3217) -- (title?, %g.r.;,
(list1 | %text;)*) <-- -- -- (chgdesc* , title, prplist)
PROCEDURE LIST STRUCTURE (NON-TASKED)程序清单结构(非任务)
<-- -- -- (chgdesc*, title, prplist)
<-- -- -- (chgdesc* , title, prplist)
+ (effect)
```

```txt
<!--   
<!--   
<!ELEMENT prclist2 (3219) -- (prcitem2+)   
<!ELEMENT prclist3 (3220) -- (prcitem3+)   
<!ELEMENT prclist4 (3221) -- (prcitem4+)   
<!ELEMENT prclist5 (3222) -- (prcitem5+)   
<!ELEMENT prclist6 (3223) -- (prcitem6+)   
<!ELEMENT prclist7 (3224) -- (prcitem7+)   
<!-- -- (prcitem7+)   
<!ELEMENT prcitem1 (3225) -- (prcitem, prclist2?) >   
<!ELEMENT prcitem2 (3226) -- (prcitem, prclist3?) >   
<!ELEMENT prcitem3 (3227) -- (prcitem, prclist4?) >   
<!ELEMENT prcitem4 (3228) -- (prcitem, prclist5?) >   
<!ELEMENT prcitem5 (3229) -- (prcitem, prclist6?) >   
<!ELEMENT prcitem6 (3230) -- (prcitem, prclist7?) >   
<!ELEMENT prcitem7 (3231) -- (prcitem) >   
<!-- -- (prcitem7)   
<!ELEMENT prcitem (3232) -- (title?, (%text;), graphic*)   
<!-- --   
<!--   
<!--   
STANDARD Lists 标准清单   
<!--   
<!--   
<!ELEMENT list1 (3233) -- (l1item+) >   
<!ELEMENT list2 (3234) -- (l2item+) >   
<!ELEMENT list3 (3235) -- (l3item+) >   
<!ELEMENT list4 (3236) -- (l4item+) >   
<!ELEMENT list5 (3237) -- (l5item+) >   
<!ELEMENT list6 (3238) -- (l6item+) >   
<!ELEMENT list7 (3239) -- (l7item+) >   
<!--   
<!ATTLIST (list1 | list2 | list3 | list4 | list5 | list6 | list7) cont(3240)%yesorno;"0" >   
<!--   
<!ELEMENT 11item (3241) -- (((%w.c.;, (%text; | entry*)), (list2, note*)) >   
<!ELEMENT 12item (3242) -- (((%w.c.;, (%text; | entry*)), (list3, note*)) >   
<!ELEMENT 13item (3243) -- ((((%w.c.;, (%text; | entry*)), (list4, note*)) ?) >   
<!ELEMENT 14item (3244) -- ((((%w.c.;, (%text; | entry*)), (list5, note*)) ?)
```

```txt
<!ELEMENT 15item(3245) -- (((%w.c), (%text; | entry*)), (list6, note*)) >  
<!ELEMENT 16item(3246) -- (((%w.c), (%text; | entry*)), (list7, note*)) >  
<!ELEMENT 17item(3247) -- (((%w.c), (%text; | entry*)) >  
<!-- -> ->-->  
<!-- ->-->  
<!--->  
<!-- cont(3248) %yesorno "0"> -->-->  
<!---- Tabular data 表格式数据 -->->  
<!---- tabular data 表格式数据 -->->  
<!---- tabular data 表格式数据 -->->  
<!---- tabular data 表格式数据 -->->  
<!---- tabular data 表格式数据 -->->  
<!---- tabular data 表格式数据 -->->  
<!---- tabular data 表格式数据 -->->  
<!---- tabular data 表格式数据 -->->  
<!---- tabular data 表格式数据 -->->  
<!---- tabular data 衜格数据 -->->  
<!---- tabular data 衜格数据 -->->  
<!---- tabular data 街格数据 -->->  
<!---- tabular data 街格数据 -->->  
<!---- tabular data 街格数据 -->->  
<!---- tabular data 街格数据 -->->  
<!---- tabular data 街格数据 -->->  
<!---- tabular data 街格数据 -->->  
<!---- tabular data 街格数据 -->->  
<!---- tabular data 街格数据 -->->  
<!---- tabular data 街格数据 -->- (tabdat)
```

```tcl
<!ATTLIST tabdat
formal(3250) (F|I)'T
frame(3251)(top | bottom | topbot | all |
sides(3252)|none)#IMPLIED
colsep(3253)%yesorno; #IMPLIED
rowsep(3254)%yesorno; #IMPLIED
orient(3255)(port | land) #IMPLIED
pgwide(3256)%yesorno; #IMPLIED
id(3257)ID#IMPLIED
alt(3258)(C|B)'B'
<!ELEMENT tabgroup(3259)-o (colspec*, spanspec*, thread?, tfoot?)>
<!ATTLIST tabgroup
cols(3260) NUMBER #REQUIRED
colsep(3261)%yesorno; #IMPLIED
rowsep(3262)%yesorno; #IMPLIED
align(3263)(left | right | center | justify | char)
"left"
charoff(3264) NUTOKEN "50"
char(3265) CDATA #IMPLIED
<!
<-- =============================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================- - -
TABLE(CELLULAR, CALSBASED)表（单元，基于CALS）
<-- ======================================================================================================================================================- -
```

```txt
<!ELEMENT table (3266) -- ((title?, tgroup, ftnote*) | graphic+) - (table) >  
<!ATTLIST table tabstyle (3267) NMTOKEN #IMPLIED frame (3268) (top | bottom | topbot | all | sides (3269) | none) #IMPLIED colsep (3270) %yesorno; #IMPLIED rowsep (3271) %yesorno; #IMPLIED orient (3272) (port | land) #IMPLIED pgwide (3273) %yesorno; #IMPLIED id (3274) ID #IMPLIED formal (3275) (F | I) T >  
<!ELEMENT tgroup (3276) - o (colspec*, spanspec*,thead?, tfoot?, tbody) >  
<!ATTLIST tgroup cols (3277) NUMBER #REQUIRED colsep (3278) %yesorno; #IMPLIED rowsep (3279) %yesorno; #IMPLIED align (3280) (left | right | center | justify | char) "left" charoff (3281) NUTOKEN "50" char (3282) CDATA "" >  
<!ELEMENT colspec (3283) - o EMPTY  
>  
<!ATTLIST colspec colnum (3284) NUMBER #IMPLIED colname (3285) NMTOKEN #IMPLIED align (3286) (left | right | center | justify | char) #IMPLIED charoff (3287) NUTOKEN #IMPLIED char (3288) CDATA #IMPLIED colwidth (3289) CDATA #IMPLIED colsep (3290) %yesorno; #IMPLIED rowsep (3291) %yesorno; #IMPLIED <!ELEMENT spanspec (3292) - o EMPTY
```

```txt
<!ATTLIST spanspec  
    namest(3293) NMTOKEN #REQUIRED  
    nameend(3294) NMTOKEN #REQUIRED  
    spanname(3295) NMTOKEN #IMPLIED  
    align(3296) (left | right | center | justify | char) "center"  
    charoff(3297) NUTOKEN #IMPLIED  
    char(3298) CDATA #IMPLIED  
    rowsep(3299) %yesorno; #IMPLIED  
    colsep(3300) %yesorno; #IMPLIED  
<!ELEMENT (thead(3301) | tfoot(3302)) - o (colspec*, row+) >  
<!ELEMENT tbody(3303) - o (row+) >  
<!ATTLIST thead  
    align(3304) (top | middle | bottom) "bottom" >  
<!ATTLIST (tfoot|body)  
    align(3305) (top | middle | bottom) "top" >  
<!ELEMENT row(3306) - o (entry+) >  
<!ATTLIST row  
    rowsep(3307) %yesorno; #IMPLIED >  
<!--(tbitem added here allows "data to be added to table cells -->  
<!--without excessively deep mark-up -->  
<!ELEMENT entry(3308) - o (%text; | graphic | %w.c; | %tbltem); + >  
<!ATTLIST entry  
    colname(3309) NMTOKEN #IMPLIED  
    namest(3310) NMTOKEN #IMPLIED  
    nameend(3311) NMTOKEN #IMPLIED  
    spanname(3312) NMTOKEN #IMPLIED  
    morerows(3313) NUMBER '0'  
    colsep(3314) %yesorno; #IMPLIED  
    rowsep(3315) %yesorno; #IMPLIED  
    rotate(3316) %yesorno; "0"  
    align(3317) (top | bottom | middle) "top"  
    align(3318) (left | right | center | justify | char) #IMPLIED  
    charoff(3319) NUTOKEN #IMPLIED  
    char(3320) CDATA #IMPLIED >  
<!ELEMENT ftnote(3321) -- %text;
```

```txt
fnoteadid(3322) ID #REQUIRED
<-- -- -> ---> <-- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    GRAPHICS [ANCHOR] 图形[位置标识]
<-- -- =----=----=----=----=----=----=----=----=----=----=----=----=----=----=----=----=----=----=----=----=----=----=----=----=----=----=----=----=----=----=----=----=----=----=----=----=----=----=----=----=----=----=----=----=----=----=----=----=----=----=----- > -> <-- -- -> ->-> <-- ELEMENT sheet(3327) -- (effect?, ((chgdesc*, title?, sheet+) | %deleted;)) -> <-- ATTLIST graphic sectnbr(3324) NUMBER #IMPLIED toolnbr(3325) CDATA #IMPLIED -- V1.11 Tool # if appl--
    unitnbr(3326) CDATA #IMPLIED -- V1.11 Unit # if appl--
    %revatt; -> <-- -- -> -> <-- ELEMENT sheet(3327) -- (effect?, ((chgdesc*, title?, gdesc?) | %deleted;)) -> <-- ATTLIST sheet gnbr(3328) ENTITY #REQUIRED sheetnbr(3329) CDATA #REQUIRED %revatt; -> <-- -- -> <-- ELEMENT gdesc(3330) -- (effect?, %text;)
<-- -- -> <-- ELEMENT graphhref(3331) -- (effect?, #PCDATA) -> <-- ATTLIST graphhref refid(3332) IDREF #REQUIRED sheetnbr(3333) CDATA #IMPLIED structid(3334) CDATA #IMPLIED shownow(3335) %yesorno; '0' -> <-- -- -> <-- -- =----=----=----=----=----=----=----=----=----=----=----=----=----=----=----=----=----=----=----=----=----=----=----=----=----=----=----=----=----=----=----=----=----=----=----=----=----=----=----=----=----=----=----=----=----=----=----=----= ----> <-- ATTLIST unlist(3336) -- (unlitem+) -> <-- ATTLIST unlist hulltype(3337) (NONE | BULLET | NDASH | MDASH | DIAMOND | ASTERISK | DELTA | SQUARE | SYSTEM) 'SYSTEM'> <-- ATTLIST numlist(3338) -- (para+) -> <-- ATTLIST numlist numlist
```

```txt
numtype(3340) (NNP | AUP | NNB | ALB | NNS | ALS | DBR |
RUP | RLP | RUR | RLR | NNR | AUR |
ALR)'NNP'>  
<-- -> ->  
<!ELEMENT numlitem(3341) -- (para+) ->  
<!ATTLIST numltem label(3342) CDATA #IMPLIED ->  
<-- => ->  
PARAGRAPH 段 ->  
<-- => ->  
<-- -> ->  
<!ELEMENT para(3343) -- (#PCDATA | con | csn | equ |
graphref| ncon | refext | refint |
std|ted|toc|txtgraphc |
legend |
%tbltem;)+ ->  
<-- -> ->  
<-- => ->  
PARAGRAPH CONTENTS 段内容 ->  
<-- => ->  
<!ELEMENT con(3344) -- (connbr, conname) ->  
<!ELEMENT connbr(3345) -- (#PCDATA) ->  
<!ELEMENT conname(3346) -- (#PCDATA) ->  
<!ELEMENT csn(3347) -o EMPTY ->  
<!ATTLIST csn
chapnbr(3348) NUMBER #REQUIRED
sectnbr(3349) NUMBER #REQUIRED
unitnbr(3350) NUMBER #REQUIRED
fignbr(3351) NUTOKEN #REQUIRED
itemnbr(3352) NUTOKEN #REQUIRED>
<!ELEMENT equ(3353) -- (#PCDATA) ->  
<!ELEMENT dd(3354) -- (#PCDATA) -- dimensions ->  
<!ATTLIST dd
length(3355) NUTOKEN #IMPLIED - V1.12 -
width(3356) NUTOKEN #IMPLIED - V1.12 -
height(3357) NUTOKEN #IMPLIED - V1.12 -
dia(3358) NUTOKEN #IMPLIED - Diameter - V1.12 -
unit(3359) (ft|jin|mm|cm|m) #IMPLIED ->  
<!ELEMENT weight(3360) -- (#PCDATA) -- tool weight ->  
<!ATTLIST weight
unit(3361) (lb|oz|kg|g) #IMPLIED - V1.11 ->  
<!ELEMENT mfrec(3362) -- (#PCDATA) -- mfr recommendation ->  
<!ELEMENT tqe(3363) -- (#PCDATA) -- total quantity used ->
```

```sgml
<!ELEMENT qualcode (3364) -- (#PCDATA) -- tool qualified (tested) -->
<!ELEMENT modcode (3365) -- (#PCDATA) -- module tool is used on -->
<!ELEMENT func (3366) -- (#PCDATA) -- Num rep func for tool -->
<!ELEMENT toolrev (3367) -- (#PCDATA) -- Tool Revision Letter -->
<!ELEMENT toolpnr (3368) -- (#PCDATA) -- Tool Part Number -->
<!-- -- =============== => ->  
<!-- LEGEND 图例 ->  
<!-- A legend offers explanatory information for a chart or table ->  
<!-- in the cross-reference list tool block ->  
-- 一个图例在对照表工具块中为一张图或表格提供说明的信息 ->  
Legend was omitted before version 1.0c. Some legends might be ->  
generated. This tag allows them to be added manually as well ->  
在版本 1.0c 前图例是省略的。一些图例也许存在。这个标签允许它们手工地被增加  
Legend Types: 图例类型 ->  
SYM TITLE ->  
=============== => ->  
EFF = Engine / Effectivity 发动机/有效性 ->  
FUN = Function 功能 ->  
MLV = Maintenance level 维修级别 ->  
MRC = Mfr Release Codes Mfr 发布代码 ->  
MOD = Module 模块 ->  
RCU = Recommended Use 使用推荐 ->  
OTH = Other 其它 ->  
--> ->  
<!-- =============== => ->  
<!-- ELEMENT legend (3369) -- (#PCDATA) -- legend for the text ->  
legend type (3370) (EFF | FUN | MLU | MRC | MOD | RCU | OTH | #IMPLIED othtype (3371) CDATA #IMPLIED - V1.11 ->  
<!ELEMENT level (3372) -- (#PCDATA) -- maintenance level ->  
<!ELEMENT ncon (3373) -- (#PCDATA) >  
<!ELEMENT pnr (3374) -- (#PCDATA) >  
<!ELEMENT refext (3375) -- (#PCDATA) >  
<!ATTLIST refext
```

```txt
refman(3376) CDATA #IMPLIED docnbr(3377) CDATA #IMPLIED refloc(3378) CDATA #IMPLIED refspl(3379) CDATA #IMPLIED refmodel(3380) CDATA #IMPLIED > <!ELEMENT refint(3381)--(#PCDATA) > <!ATTLIST refint reftype(3382) CDATA #IMPLIED refid(3383) IDREF #REQUIRED > <!ELEMENT std(3384)--(stdinbr, stdout) > <!ELEMENT stdnbr(3385)--(#PCDATA) > <!ELEMENT stdout(3386)--(#PCDATA) > <!ELEMENT ted(3387)--(toolnbr & toolname)--V1.12 --> <!ELEMENT toolnbr(3388)--(#PCDATA) > <!ELEMENT toolname(3389)--(#PCDATA) > <!ELEMENT toc(3390)--(#PCDATA) > <!ATTLIST toc readable(3391)%yesorno;1' > <!ELEMENT txtgrphc(3392)--(txtline+) > <!ELEMENT txtline(3393)--(#PCDATA) > <!--  $= = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = 1$  SUPPLIER INFO供应商信息 <!-- The TEM carries the following information which is not in <!-- the esm: TEM提供了以下没有包含在esm中的信息 <!-- -Supplier code(zone）供应商代码（区域） <!-- - Supplier name供应商名称 <!-- - Supplier address供应商地址 <!-- - Supplier Contact(AOG.....)供应商联系方式 <!-- - Supplier Communication(name, <!-- phone,fax,internet,sita,arinc,...>) <!-- 供应商通讯方式(名称、电话、传真、网络、sita,arinc,等.) <!-- To address this,vendata,mfr and mad were added from AIPC.
```

$<  ! - >$  Vendata (mad) was changed to accomodate additional info.  
<!-- 提出了从AIPC中增加vendata，mfr和mad -->  
Vendata (mad) 被改变容纳附加的信息  
$<  ! - >$  Associated with a single mfr code, there can be one or more  
$<  ! - -$  manufacturer's addresses. Within each address, we now mark  
$<  ! - -$  information including:  
$<  ! - >$  与一个单个的mfr代码相关联的可以是一个或多个制造商的地址。  
目前，在每个地址内，我们标记的信息包括  
<!-- Phone 电话 -->  
<!-- URLURL  
<!-- Fax 传真 -->  
<!-- Email 电子邮件 -->  
<!-- Meanless:-->  
<!-- Chg V1.11 - added ADDR to list so the address portion can be ->  
<!-- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -  
<!-- 更改标记 V1.1 -这样列出地址部分增加的 ADDR 可被标记以便识别 -->  
<!---->

```txt
<!ELEMENT vendlist (3394) -- (title, (%text;)?, venddata+)  
>  
<!ELEMENT venddata (3395) -- (mfr, mad+)  
>  
<!ATTLIST vendata  
mfrname (3396) CDATA #REQUIRED  
>  
<!ELEMENT mfr (3397) -- (#PCDATA)  
>  
<!ATTLIST mfr  
zone (3398) CDATA #REQUIRED >  
<!ELEMENT mad (3399) -- (#PCDATA | addr | phone | fax |  
url | email | mfrcont | telex) + >  
<!ELEMENT mfrcont (3400) -- (#PCDATA) -- supplier contact  
-->  
<!ELEMENT addr (3401) -- (#PCDATA) -- supplier address  
-->  
<!ELEMENT phone (3402) -- (#PCDATA) -- supplier phone  
-->  
<!ELEMENT fax (3403) -- (#PCDATA) -- supplier  
fax  
-->  
<!ELEMENT url (3404) -- (#PCDATA) -- supplier www  
url -->  
<!ELEMENT email (3405) -- (#PCDATA) -- supplier email  
addr -->
```

```txt
<!ELEMENT telex(3406)--(#PCDATA)--supplier telex#  
->  
<-- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -  
--->  
<-- -- -- -- -- -- -- -- -- -- -- -- -- -  
--->  
<-- - (note)  
>  
<-- - (note)  
>  
<-- - (note)  
>  
<-- - (note)  
>  
<-- - (note)  
>  
<-- - (note)  
>  
<-- - (note)  
>  
<-- - (note)  
>  
<-- - (note)  
>  
<-- - (note)  
>  
<-- - (note)  
>  
<-- - (note)  
>
```

<table><tr><td>&lt;!--</td><td></td><td>-&gt;</td></tr><tr><td>&lt;!--</td><td>= = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =</td><td>-&gt;</td></tr><tr><td>&lt;!--</td><td>END OF TEM DTD</td><td>-&gt;</td></tr><tr><td>&lt;!--</td><td>TEM DTD 结束</td><td>-&gt;</td></tr><tr><td>] &gt;</td><td></td><td>-&gt;</td></tr></table>

# 2 结构图表

结构图的关键组成部分可参见 DTD 技术要求(参见[4-2-3.22.4])。

![](images/60acdffe83e845f0c762e9edea5d4e1c670f8e37914180c295921c5052adf9df.jpg)  
图4-2-35.1 TEM DTD结构一概述(前页、节、标题页、单元、供应商清单和供应商数据)

![](images/6403f8b535c6ba9b5b2d96a87ac3ac0caf613fd5dc14b940fea642fc5e5db1bb.jpg)  
图4-2-35.2 TEM DTD结构一增加的版本

# 4-2-36 布线手册(WM)DTD

# 1 WM(布线手册)DTD

<!-- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -  
WM DTD HEADER  
$<  ! - -$  WM DTD 程序头  
<!-- DTD Reference: '-//ATA-TEXT//DTD WM-VER5-LEVEL2//EN? --

DTD参考：-/ATA-TEXT//DTDWM-VER5-LEVEL2//EN

<-- Revision Date: Sept 98 更改日期 98年9月 -->  
<!-- DTD Level : 2 DTD级别 : 2  
<!-- Meanless:-->  
<!-- Highlight : -->  
<-- Increased the version number to 5  
<!-- Added optional modcode to extwrow --->  
<!-- 更改摘要： -->

版本号增加到5

extwrow 中增加了可选的 modcode

<!---->  
<!DOCTYPE worm [  
The following set of declarations may be referred to using a public entity as follows: 以下公共实体的使用可参考如下声明的集合：

<!DOCTYPEwmPUBLIC

'-//ATA-TEXT//DTD WM-VER5-LEVEL2//EN' [ ]>

<!-- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -  
<!-- NOTATIONS 符号 -->  
$<  ! - >$

<!NOTATION cgm PUBLIC

"-//USA-DOD//NOTATION Computer Graphics Metafile//EN" >

<!NOTATION ccitt4 PUBLIC

"-//USA-DOD//NOTATION CCITT Group 4 Facsimile//EN" >

<!---->  
<!-- ENTITIES 实体  
<!---->

<!ENTITY % wcn ' (warning | caution | note) +' >

<!ENTITY % text '('para | table | unlist | numlist | graphic

%wcn; |list1)

<!ENTITY % revatt

'chg

(N|R|U|D)

#REQUIRED

key

ID

#REQUIRED

revdate

NUMBER

REQUIRED

<!ENTITY % deleted '('deleted, chgdesc*)'

<!ENTITY % yesorno 'NUMBER'

<!ENTITY % ISOtech

PUBLIC

<!ISO 8879-1986//ENTITIES General Technical//EN>

<!ENTITY % ISOpub

PUBLIC

'ISO 8879-1986//ENTITIES Publishing//EN'

<!ENTITY % ISOnum

PUBLIC

'ISO 8879-1986//ENTITIES Numeric and Special Graphic//EN'

<!ENTITY % ISOgrk1 PUBLIC.

'ISO 8879-1986//ENTITIES Greek Letters//EN'

%ISOtech; %ISOpub; %ISOnum; %ISOgrk1;

<!---->  
<!-- WIRING MANUAL TOP LEVEL STRUCTURE 布线手册顶层结构 ->  
<!---->

<!ELEMENTwm(3422)--((title，mfmatr，spchap?,chapter\*,wmlist?)

| increv | tr+)  
+ (revst | revend | cocst | cocend | hotlink) >

<!ATTLISTwm

model (3423)

CDATA

#REQUIRED

oidate (3424)

NUMBER

#REQUIRED

revdate (3425)

NUMBER

#REQUIRED

tsn (3426)

CDATA

REQUIRED

docnbr(3427)

CDATA

#IMPLIED

spl (3428)

CDATA

#REQUIRED

chg(3429)

(N|R|U)

#REQUIRED

lang (3430)

CDATA

REQUIRED

cus(3431)

CDATA

#IMPLIED

cusname(3432)

CDATA

#IMPLIED

spc (3433)

%yesomo

1

wdm (3434)

%yesomo

1

ssm (3435)

%yesorno

1

w列表(3436)

%yesorno

1

efflen (3437)

NUMBER

#REQUIRED

efftype (3438)

CDATA

REQUIRED

>

<!ELEMENT increv(3439) -- (ttlpage | translr | trlist | mfvrec

|sblist | coclist | effxref | intro

| eqiplist | conlist | eqrow | condrow

```txt
|extwlist | extwrow | spchap|spsect
|spsubj| chapter | section | subject
|graphic| sheet | l1item | l2item
|l3item) + > <!ELEMENT tr(3440) -- (trfmatr, (sblist | coclist | effxref
|intro | eqrow+ | condrow+ | extwrow+
|spchap | spsect+ | spsubj+ | chapter
|section+ | subject+ | graphic+ | sheet+
|l1item+ | l2item+ | l3item+) > <!ELEMENT trfmatr(3441) -- (title, trxref?, trinfo)> <!ATTLIST trfmatr
tmbr(3442) CDATA #REQUIRED
issdate(3443) NUMBER #REQUIRED
trdel(3444) CDATA #IMPLIED
trrepl(3445) CDATA #IMPLIED>
<!ELEMENT trxref(3446) -- (paptnbr+) >
<!ELEMENT paptnbr(3447) -- (#PCDATA) >
<!ATTLIST paptnbr
issdate(3448) NUMBER #REQUIRED>
<!ELEMENT trinfo(3449) -- (%text;)> <!-- =============== => -> <!-- WM FRONT MATTER WM 前页 -> <!-- =============== => -> <!ELEMENT mfmatr(3450) -- (ttlpage?, transltr?, trlist, mfvrec?,,
cusrevrec?, sblist?, coclist?, effxref?, 
intro) + (refint | refext) >
<!ELEMENT ttlpage(3451) -- (chgdesc*, title, graphic?, para*) >
<!ATTLIST ttlpage
%revatt;
<!ELEMENT transltr(3452) -- ((chgdesc*, title, %text;)
%deleted;>
<!ATTLIST transltr
oldkey(3453) NAME #IMPLIED
%revatt;
<!ELEMENT trlist(3454) -- (trdata+ | isempty) >
<!ATTLIST trlist
%revatt;>
<!ELEMENT trdata(3455) -- (tmbr, trstatus, trloc+) >
```

```txt
<!ELEMENT trnbr (3456) -- (#PCDATA)
>
<!ELEMENT trstatus (3457) -- (#PCDATA)
>
<!ELEMENT trloc (3458) -- (#PCDATA)
>
<!ELEMENT mfvrec (3459) -- (chgdesc*, title, %text;)
<!ATTLIST mfrevrec
%revatt;>
<!ELEMENT cusrevrec (3460) -- (chgdesc*, title, %text;)
<!ELEMENT sblist (3461) -- (chgdesc*, title, %text;), (sbdata+|
isEmpty))
<!ATTLIST sblist
%revatt;>
```

```txt
<!ELEMENT sbdata(3462) -- (sbnbr?, sbrev?, atanbr?, mdnbr*, cocnbr*, custeff?, sc?, title, (icdate | ics))
```

```txt
<!ELEMENT sbnbr(3463) -- (#PCDATA)  
<!ELEMENT sbrev(3464) -- (#PCDATA)  
<!ELEMENT atanbr(3465) -- (#PCDATA)  
<!ELEMENT mdnbr(3466) -- (#PCDATA)  
<!ELEMENT custeff(3467) -- (cus, effrc)+  
<!ELEMENT cus(3468) -- (#PCDATA)  
>  
<!ELEMENT effrc(3469) -- (#PCDATA)  
<!ELEMENT sc(3470) -- (#PCDATA)  
>  
<!ELEMENT icdate(3471) -- (#PCDATA)  
<!ELEMENT ics(3472) -- (#PCDATA)
```

```txt
<!ELEMENT coclist (3473) -- (chgdesc*, title, %text; (cocdata+ | isempty)) >
```

```txt
<!ATTLIST coclist %revatt;>
<!ELEMENT cocdata(3474) -- (cocnbr?, cocrev?, atanbr?, mdnbr*, custeff?, sc?, title, (icdate | ics))>
```

```sgml
<!ELEMENT cocnbr (3475) -- (#PCDATA)
>
<!ELEMENT cocrev (3476) -- (#PCDATA)
>
<!ELEMENT effxref (3477) -- (chgdesc*, title, %text; , effdata+)
<!ATTLIST effxref
%revatt;
<!ELEMENT effdata (3478) -- (cus?, modtype?, venbr?, cec,
cac?,
acn, linenbr?, msnbr)
<!ELEMENT modtype (3479) -- (#PCDATA)
>
<!ELEMENT venbr (3480) -- (#PCDATA)
>
<!ELEMENT cec (3481) -- (#PCDATA)
>
<!ELEMENT cac (3482) -- (#PCDATA)
>
<!ELEMENT acn (3483) -- (#PCDATA)
>
<!ELEMENT linenbr (3484) -- (#PCDATA)
>
<!ELEMENT msnbr (3485) -- (#PCDATA)
>
<!ELEMENT intro (3486) -- (#hgdesc*, title, para?, listl)
>
<!ATTLIST intro
oldkey (3487) NAME #IMPLIED
%revatt;
>
<!-- =============== =>-> <!-- Standard Practices CHAPTER 20 标准惯例章 20 =>-> <!-- =============== =>-> <!ELEMENT spchap (3488) -- ((effect?, chgdesc*, title, spsect+) | %deleted;) -> <!ATTLIST spchap
chapnbr (3489) NUMBER '20'
oldkey (3490) NAME #IMPLIED
%revatt; >
```

```txt
<!-- S P SECTION S P节 ->  
<!-- =>  
<!-- =>  
<!ELEMENT spsect(3491) -- ((effect?, chgdesc*, title?, spsubj+) | %deleted;)  
<!ATTLIST spsect chapnbr(3492) NUMBER #REQUIRED sectnbr(3493) NUMBER #REQUIRED %revatt; >  
<!-- =>  
<!-- SP SUBJECT S P 标题 ->  
<!-- =>  
<!ELEMENT spsubj(3494) -- ((effect?, chgdesc*, title?, %text;)| %deleted;)  
<!ATTLIST spsubj chapnbr(3495) NUMBER #REQUIRED sectnbr(3496) NUMBER #REQUIRED subjnbr(3497) NUMBER #REQUIRED %revatt;  
<!-- =>  
<!-- =>  
<!-- =>  
<!ELEMENT chapter(3498) -- ((effect?, chgdesc*, title, section+) | %deleted;)  
<!ATTLIST chapter chapnbr(3499) NUMBER #REQUIRED %revatt;  
<!-- =>  
<!-- =>  
<!-- =>  
<!ELEMENT section(3500) -- ((effect?, chgdesc*, title?, subject+) | %deleted;)  
<!ATTLIST section chapnbr(3501) NUMBER #REQUIRED sectnbr(3502) NUMBER #REQUIRED %revatt;  
<!-- =>  
<!-- =>  
<!-- =>  
<!ELEMENT subject(3503) -- ((effect?, chgdesc*, title?, graphic+)
```

<table><tr><td colspan="3">| %deleted; )</td><td>&gt;</td></tr><tr><td>&lt;!ATTLIST subjectchapnbr(3504)</td><td>NUMBER</td><td>#REQUIRED</td><td></td></tr><tr><td>sectnbr(3505)</td><td>NUMBER</td><td>#REQUIRED</td><td></td></tr><tr><td>subjnbr(3506)</td><td>NUMBER</td><td>#REQUIRED</td><td></td></tr><tr><td>%revatt;</td><td></td><td></td><td>&gt;</td></tr><tr><td>&lt;!--= = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =</td><td>WM LISTS</td><td>WM 清单</td><td>-&gt;</td></tr><tr><td>&lt;!--= = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =</td><td>-- (eqiplist, extwlist, condlist)</td><td></td><td>&gt;</td></tr><tr><td>&lt;!ELEMENT wmlist(3507)</td><td></td><td></td><td></td></tr><tr><td>&lt;!--= = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =</td><td></td><td></td><td></td></tr><tr><td>&lt;!--= = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =</td><td>EQUIPMENT LIST</td><td>设备清单</td><td>-&gt;</td></tr><tr><td>&lt;!--= = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =</td><td>-- (chgdesc*, title, eqrow+)</td><td></td><td>&gt;</td></tr><tr><td>&lt;!ATTLIST eqiplistoldkey(3509)</td><td>NAME</td><td>#IMPLIED</td><td></td></tr><tr><td>%revatt;</td><td></td><td></td><td>&gt;</td></tr><tr><td>&lt;!ELEMENT eqrow(3510)</td><td>-- ((effect, chgdesc*, ein, pnr, alprtnbr?, partdesc, mfr, location, hdiagnbr, tqa?, equivpnr*, mfnname?, optcode?, .dwg?, ch20ref?, pan?, position*, maxpos?, pandesc?, modcode?, gridnbr?) | %deleted;)</td><td></td><td></td></tr><tr><td>&lt;!ATTLIST eqrow%revatt;</td><td></td><td></td><td>&gt;</td></tr><tr><td>&lt;!ELEMENT ein(3511)</td><td>-- (#PCDATA)</td><td></td><td>&gt;</td></tr><tr><td>&lt;!ELEMENT pnr(3512)</td><td>-- (#PCDATA)</td><td></td><td>&gt;</td></tr><tr><td>&lt;!ELEMENT alprtnbr(3513)</td><td>-- (#PCDATA)</td><td></td><td>&gt;</td></tr><tr><td>&lt;!ELEMENT partdesc(3514)</td><td>-- (#PCDATA)</td><td></td><td>&gt;</td></tr><tr><td>&lt;!ELEMENT mfr(3515)</td><td>-- (#PCDATA)</td><td></td><td>&gt;</td></tr><tr><td>&lt;!ELEMENT location(3516)</td><td>-- (stnnbr?, wl?, bl?, zone?)</td><td></td><td>&gt;</td></tr><tr><td>&lt;!ELEMENT stnnbr(3517)</td><td>-- (#PCDATA)</td><td></td><td>&gt;</td></tr><tr><td>&lt;!ELEMENT wl(3518)</td><td>-- (#PCDATA)</td><td></td><td>&gt;</td></tr><tr><td>&lt;!ELEMENT bl(3519)</td><td>-- (#PCDATA)</td><td></td><td>&gt;</td></tr><tr><td>&lt;!ELEMENT zone(3520)</td><td>-- (#PCDATA)</td><td></td><td>&gt;</td></tr><tr><td>&lt;!ELEMENT hdiagnbr(3521)</td><td>-- (refint | refext)</td><td></td><td>&gt;</td></tr><tr><td>&lt;!ELEMENT tqa(3522)</td><td>-- (#PCDATA)</td><td></td><td>&gt;</td></tr><tr><td>&lt;!ELEMENT eqivpnr(3523)</td><td>-- (#PCDATA)</td><td></td><td>&gt;</td></tr><tr><td>&lt;!ELEMENT optcode(3524)</td><td>-- (#PCDATA)</td><td></td><td>&gt;</td></tr><tr><td>&lt;!ELEMENT dwg(3525)</td><td>-- (#PCDATA)</td><td></td><td>&gt;</td></tr><tr><td>&lt;!ELEMENT ch20ref(3526)</td><td>-- (refint | refext)</td><td></td><td>&gt;</td></tr><tr><td>&lt;!ELEMENT pan(3527)</td><td>-- (#PCDATA)</td><td></td><td>&gt;</td></tr><tr><td>&lt;!ELEMENT position (3528)</td><td>--</td><td>(#PCDATA)</td><td>&gt;</td></tr><tr><td>&lt;!ELEMENT maxpos (3529)</td><td>--</td><td>(#PCDATA)</td><td>&gt;</td></tr><tr><td>&lt;!ELEMENT pandesc (3530)</td><td>--</td><td>(#PCDATA)</td><td>&gt;</td></tr><tr><td>&lt;!ELEMENT modcode (3531)</td><td>--</td><td>(#PCDATA)</td><td>&gt;</td></tr><tr><td>&lt;!ELEMENT gridnbr (3532)</td><td>--</td><td>(#PCDATA)</td><td>&gt;</td></tr></table>

<table><tr><td>&lt;!--= = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = EXTENDED Wire LIST 线缆详表 --&gt;</td></tr></table>

<table><tr><td>&lt;--============================================-&gt;</td></tr><tr><td>&lt;!ELEMENT extwlist (3533) -- (chgdesc*, title, extwrow+)</td></tr></table>

<table><tr><td>&lt;!ATTLIST</td><td>extwlist</td><td></td></tr><tr><td></td><td>oldkey (3534)</td><td>NAME #IMPLIED</td></tr><tr><td></td><td>%revatt;</td><td></td></tr></table>

<table><tr><td>&lt;!ELEMENT extwrow(3535) -- ((effect, chgdesc*, (actwire | nactwire | sparepin), modcode?) | %deleted;) &gt;</td></tr></table>

<table><tr><td>&lt;!ATTLIST</td><td>extwrow</td></tr><tr><td></td><td>%revatt;</td></tr></table>

<table><tr><td>&lt;!ELEMENT actuwire (3536)</td><td>--</td><td>(wire, from, to)</td><td>&gt;</td></tr></table>

<table><tr><td>&lt;!ELEMENT nactwire (3537)</td><td>--</td><td>(wire, from?, to?)</td><td>&gt;</td></tr></table>

<table><tr><td>&lt;!ELEMENT sparepin (3538)</td><td>--</td><td>(from)</td></tr></table>

<table><tr><td>&lt;!ELEMENT from (3539)</td><td>--</td><td>((ein | wirecode), termnbr, shunt?, termpnr?, termcode?)</td><td>&gt;</td></tr></table>

<table><tr><td>&lt;!ELEMENT to (3540)</td><td>--</td><td>((ein | wirecode), termnbr, shunt?, termpnr?, termcode?)</td><td>&gt;</td></tr></table>

<table><tr><td>&lt;!ELEMENT wire (3541)</td><td>--</td><td>(wirecode, length+, wiretype+ ,</td></tr></table>

<table><tr><td>hdiagnbr, fam?, wirerte?, bundpnr?,</td></tr></table>

<table><tr><td>bundesc?, feedthru*, sensep?)</td><td>&gt;</td></tr></table>

<table><tr><td>&lt;!ELEMENT wirecode(3542) -- (wirebr, wireawg?, wirectr?, bundnbr?) &gt;</td></tr></table>

<table><tr><td>&lt;!ELEMENT wirenbr(3543)</td><td>--</td><td>(#PCDATA)</td></tr></table>

<table><tr><td>&lt;!ELEMENT wireawg (3544)</td><td>--</td><td>(#PCDATA)</td></tr></table>

<table><tr><td>&lt;!ELEMENT wireaclr (3545)</td><td>--</td><td>(#PCDATA)</td></tr></table>

<table><tr><td>&lt;!ELEMENT bundnbr(3546)</td><td>--</td><td>(#PCDATA)</td></tr></table>

<table><tr><td>&lt;!ELEMENT termnbr(3547)</td><td>--</td><td>(#PCDATA)</td></tr></table>

<table><tr><td>&lt;!ELEMENT shunt(3548)</td><td>--</td><td>(#PCDATA)</td></tr></table>

<table><tr><td>&lt;!ELEMENT termpnr(3549)</td><td>--</td><td>(#PCDATA)</td></tr></table>

<table><tr><td>&lt;!ELEMENT termcode(3550) -- (#PCDATA)</td></tr></table>

<table><tr><td>&lt;!ELEMENT length (3551)</td><td>--</td><td>(#PCDATA)</td></tr></table>

<table><tr><td>&lt;!ATTLIST</td><td>length</td><td></td></tr><tr><td></td><td>unit(3552)</td><td>(ft|in|mm|cm|m) #REQUIRED &gt;</td></tr></table>

<table><tr><td>&lt;!ELEMENT wiretype (3553)</td><td>--</td><td>(#PCDATA)</td></tr></table>

<table><tr><td>&lt;!ATTLIST wiretype wrtc (3554)</td><td>(us|mt)</td><td># IMPLIED</td></tr></table>

<table><tr><td>&lt;!ELEMENT fam (3555)</td><td>--</td><td>(#PCDATA)</td></tr></table>

<table><tr><td>&lt;!ELEMENT wireerte (3556)</td><td>--</td><td>(#PCDATA)</td><td>&gt;</td></tr><tr><td>&lt;!ELEMENT bundpnr (3557)</td><td>--</td><td>(#PCDATA)</td><td>&gt;</td></tr><tr><td>&lt;!ELEMENT bunddesc (3558)</td><td>--</td><td>(#PCDATA)</td><td>&gt;</td></tr><tr><td>&lt;!ELEMENT feedthru (3559)</td><td>--</td><td>(ein, termnbr?)</td><td>&gt;</td></tr><tr><td>&lt;!ELEMENT sensep (3560)</td><td>--</td><td>(#PCDATA)</td><td>&gt;</td></tr></table>

<table><tr><td colspan="3">&lt;--==========================-&gt;</td></tr><tr><td colspan="3">&lt;-- -- CONDuit LIST 导管清单 -&gt;</td></tr><tr><td colspan="3">&lt;--========================-&gt;</td></tr><tr><td colspan="3">&lt;--ELEMENT condlist(3561) -- (chgdesc*, title, condrow+) &gt;</td></tr><tr><td colspan="3">&lt;--ATTLIST condlist oldkey(3562) NAME #IMPLIED %revatt; &gt;</td></tr></table>

<table><tr><td colspan="4">&lt;!ELEMENT condrow(3563) -- ((effect, chgdesc*, condid, zone, zone, dia, length, wirecode+) | %deleted;)</td><td>&gt;</td></tr><tr><td colspan="4">&lt;!ATTLIST condrow %revatt;</td><td>&gt;</td></tr><tr><td colspan="4">&lt;!ELEMENT condid(3564) -- (#PCDATA)</td><td>&gt;</td></tr><tr><td colspan="4">&lt;!ELEMENT dia(3565) -- (#PCDATA)</td><td>&gt;</td></tr><tr><td colspan="4">&lt;!ATTLIST dia unit(3566) (in|cm|mm) #REQUIRED</td><td>&gt;</td></tr></table>

<table><tr><td>&lt;--=----=----=----=----=----=----=----=----=----=----=----=----=----=----=----=----=----=----=----=----=----=----=----=----=----=----=----=----=----=----=----=----=----=----=----=----=----=----=----=----=----=----=----=----=----=----=----=----=----=----=---&gt;</td><td></td></tr><tr><td>&lt;---</td><td>PARAGRAPH, CHANGE DESCR. &amp; TITLE段落、改变说明和标题--&gt;</td></tr></table>

<table><tr><td>&lt;|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--.--</td></tr></table>

<table><tr><td>ELEMENT para (3567)</td><td>--</td><td>(#PCDATA | hwinfo | matlinfo | toolinfo</td></tr><tr><td></td><td>| terminfo | wiretype | pnr | mfrname</td><td></td></tr><tr><td></td><td>| toolpnr | matlpnr | zone | termpnr</td><td></td></tr><tr><td></td><td>| graphcref | refext | refint | txtgraphc) +&gt;</td><td></td></tr></table>

<!ELEMENT hwinfo (3568) -- (mfname, pnr, hname, altentry*) >

<!ELEMENT mfrname(3569) -- (#PCDATA)

<!ELEMENT hname(3570) -- (#PCDATA)

<!ELEMENT altentry(3571) -- (#PCDATA)

<!ELEMENTmatlinfo(3572) -- (mfrname，matlpnr，matname，altentry\*)>

<!ELEMENT matlpnr(3573) -- (#PCDATA)

<!ELEMENT matname (3574) -- (#PCDATA)

<!ELEMENT toolinfo(3575) -- fname, toolprn, toolname, altentry*)>  
<!ELEMENT toolprn(3576) -- PCDATA) >

```txt
<!ELEMENT toolname(3577) -- (#PCDATA)  
<!ELEMENT terminfo(3578) -- (mfrname, termpnr, termname, altentry*)>  
<!ELEMENT termname(3579) -- (#PCDATA)  
<!ELEMENT chgdesc(3580) -- (#PCDATA)  
<!ELEMENT title(3581) -- (#PCDATA)
```

```txt
$<  ! - - = = = = = = = = = = = = = = = = = = = = = >$  TABLE (CELLULAR, CALS BASED)  $\rightarrow$  <!-- 表（单元，基于CALS）->  
 $<  ! - - = = = = = = = = = = = = = = = = = = = = = = >$
```

```txt
<!ELEMENT table (3582) -- ((title?, tgroup, ftnote*) | graphic+) - (table)
```

```txt
<!ATTLIST table tabstyle(3583) NMTOKEN #IMPLIED frame(3584) (top|bottom|topbot|all|sides |none)#IMPLIED
```

```txt
colsep (3585) %yesorno; #IMPLIED
```

```txt
rowsep (3586) %yesorno; #IMPLIED
```

```txt
orient(3587) (port | land) #IMPLIED
```

```txt
pgwide(3588) %yesorno; #IMPLIED
```

```txt
id(3589) ID #IMPLIED
```

```txt
<!ELEMENT tgroup(3590) o olspec*, spanspec*, thead?, tfoot?, tbody)
```

```txt
<!ATTLIST tgroup
cols(3591) NUMBER #REQUIRED
colsep(3592) %yesorno; #IMPLIED
rowsep(3593) %yesorno; #IMPLIED
align(3594) (left | right | center | justify | char) 'left'
charoff(3595) NUTOKEN '50'
char(3596) CDATA
```

```batch
<!ELEMENT colspec (3597) -o EMPTY
```

```txt
<!ATTLIST colspec colnum(3598) NUMBER #IMPLIED colname(3599) NMTOKEN #IMPLIED align(3600) (left | right | center
```

```txt
| justify | char) #IMPLIED
```

```txt
charoff(3601) NUTOKEN #IMPLIED
```

```txt
char(3602) CDATA #IMPLIED
```

```txt
colwidth(3603) CDATA #IMPLIED
```

```txt
colsep(3604) %yesorno; #IMPLIED
```

```erlang
rowsep(3605) %yesorno; #IMPLIED
```

```txt
<!ELEMENT spanspec (3606) -o EMPTY  
<!ATTLIST spanspec  
    :(3607) NMTOKEN #REQUIRED  
    :(3608) NMTOKEN #REQUIRED  
    :nameend (3609) NMTOKEN #IMPLIED  
    :align (3610) (left | right | center  
        | justify (3611) | char) 'center'  
    charoff (3612) NUTOKEN #IMPLIED  
    :char (3613) CDATA #IMPLIED  
    :colsep (3614) %yesorno; #IMPLIED  
    :rowsep (3615) %yesorno; #IMPLIED  
    <!ELEMENT thread (3616) -o (colspec*, row+)  
    <!ATTLIST thread  
        :valign (3617) (top | middle | bottom) 'bottom'  
    <!ELEMENT tfoot (3618) -o (colspec*, row+)  
    <!ATTLIST tfoot  
        :valign (3619) (top | middle | bottom) 'top'  
    <!ELEMENT tbody (3620) -o (row+)  
    <!ATTLIST tbody  
        :valign (3621) (top | middle | bottom) 'top'  
    <!ELEMENT row (3622) -o (entry+)  
    <!ATTLIST row  
        :rowsep (3623) %yesorno; #IMPLIED  
    <!ELEMENT entry (3624) -o ((para | numlist | unlist) + | graphic)>  
    <!ATTLIST entry  
        :colname (3625) NMTOKEN #IMPLIED  
        :namest (3626) NMTOKEN #IMPLIED  
        :nameend (3627) NMTOKEN #IMPLIED  
        :spanname (3628) NMTOKEN #IMPLIED  
        :morerows (3629) NUMBER '0'  
        :colsep (3630) %yesorno; #IMPLIED  
        :rowsep (3631) %yesorno; #IMPLIED  
        :rotate (3632) %yesorno; '0'  
        :align (3633) (top | middle | bottom) 'top'  
        :align (3634) (left | right | center  
        | justify | char) #IMPLIED  
        :charoff (3635) NUTOKEN #IMPLIED  
        :char (3636) CDATA #IMPLIED  
    <!ELEMENT fnote (3637) -- (%text;)
```

```txt
>  
<!ATTLIST ftnote  
ftnoteid(3638) ID #REQUIRED
```

```txt
<--====================================
```

```txt
<-- GRAPHICREFERENCINGMECHANISM 图形参考机制-> <！--= = = = = = = = = = = = = = = = = = = =
```

```txt
<!ELEMENT graphref(3639) -- (effect?, #PCDATA)
```

```txt
<!ATTLIST graphcoef refid (3640) IDREF #IMPLIED sheetnbr (3641) CDATA #IMPLIED structid (3642) CDATA #IMPLIED shownow (3643) %yesorno '0'
```

```txt
<!ELEMENT graphic (3644) -- ((effect, chgdesc*, title?, sheet+) | %deleted;)
```

```txt
<!ATTLIST graphic  
gtype(3645) (ss|wd|il) #IMPLIED  
chapnbr(3646) NUMBER #IMPLIED  
sectnbr(3647) NUMBER #IMPLIED  
subjnbr(3648) NUMBER #IMPLIED  
pagenbr(3649) NUMBER #IMPLIED  
schemnbr(3650) NUMBER #IMPLIED  
oldkey(3651) NAME #IMPLIED  
%revatt;
```

```txt
<!ELEMENT sheet (3652) -- ((effect, chgdesc*, title?, gdesc?) | %deleted;)
```

```txt
<!ATTLIST sheet
gnbr(3653) ENTITY #REQUIRED
gtype(3654)(ss|wd|il) #IMPLIED
chapnbr(3655)NUMBER #IMPLIED
sectnbr(3656)NUMBER #IMPLIED
subjnbr(3657)NUMBER #IMPLIED
pagenbr(3658)NUMBER #IMPLIED
schemnbr(3659)NUMBER #IMPLIED
sheetnbr(3660) CDATA #REQUIRED
%revatt;
```

```txt
<!ELEMENT gdesc (3661) -- (unlist | numlist)
```

```txt
<--=
```

```txt
STANDARD LISTS 标准清单
```

```txt
<1--=
```

```txt
<!ELEMENT list1 (3662) -- (11item+) -- (list1) + (effect) >  
<!ELEMENT list2 (3663) -- (12item+)  
<!ELEMENT list3 (3664) -- (13item+)  
<!ELEMENT list4 (3665) -- (14item+)  
<!ELEMENT list5 (3666) -- (15item+)  
<!ELEMENT list6 (3667) -- (16item+)  
<!ELEMENT list7 (3668) -- (17item+)
```

```matlab
<!ELEMENT 11item (3669) -- ((chgdesc*, title?, (%text?), list2?) | %deleted;)  
<!ATTLIST 11item %revatt;  
<!ELEMENT 12item (3670) -- ((chgdesc*, title?, (%text?), list3?) | %deleted;)  
<!ATTLIST 12item %revatt;  
<!ELEMENT 13item (3671) -- ((chgdesc*, title?, (%text?), list4?) | %deleted;)  
<!ATTLIST 13item %revatt;  
<!ELEMENT 14item (3672) -- (title?, (%text?), list5?)  
<!ELEMENT 15item (3673) -- (title?, (%text?), list6?)  
<!ELEMENT 16item (3674) -- (title?, (%text?), list7?)  
<!ELEMENT 17item (3675) -- (title?, (%text?))
```

```html
<!-- NUMBERED & UN-NUMBERED LIST 有编号的和无编号的清单  
<!-- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
<!ELEMENT unlist(3676) -- (unltem+) >  
<!ATTLIST unlist  
bulltype(3677) (NONE|BULLET|NDASH|MDASH|DIAMOND|ASTERISK  
|DELTA|SQUARE|SYSTEM)  
'SYSTEM' >  
<!ELEMENT unltem(3678) -- (para+) >  
<!ELEMENT numlist(3679) -- (numltem+) >  
<!ATTLIST numlist numtype(3680) (NNP|AUP|NNB|ALB|NNS|RUP|RLP|RUR|RLR|NNR  
|AUR|ALR)  
'NNP' >  
<!ELEMENT numltem(3681) -- (para+) >
```

```txt
$<  ! - - = = = = = = = = = = = = = = = = = = = = = = = = = = >$ $\angle ! - -$  ：WARNING，CAUTIONS&NOTES警告、注意和注释→  
 $<  ! - - = = = = = = = = = = = = = = = = = = = = = = = = >$
```

```txt
<!ELEMENT warning (3682) -- (%text;) - (note | warning | caution) >  
<!ELEMENT note (3683) -- (%text;) - (note | warning | caution) >  
<!ELEMENT caution (3684) -- (%text;) - (note | warning | caution) >
```

```html
<!--= = = = = = = = = = = = = = = = = = >  
<!--  REFERENCES 参考 ->  
<!--= = = = = = = = = = = = = = = = =  
<!ELEMENTrefext(3685) -- (#PCDATA)  
<!ATTLIST refext docnbr(3686) CDATA #IMPLIED refman(3687) CDATA #IMPLIED refloc(3688) CDATA #IMPLIED refmodel(3689) CDATA #IMPLIED refspl(3690) CDATA #IMPLIED
```

```txt
<!ELEMENT refint(3691) -- (#PCDATA)  
<!ATTLIST refint  
    retypeof(3692) CDATA #IMPLIED  
    refid(3693) IDREF #IMPLIED
```

```txt
<!-- EFFECTIVITY 有效性 ->  
<!-- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -  
<!ELEMENT effect (3694) --- ((sbeff | coceff) *) >  
<!ATTLIST effect  
effrg (3695) CDATA #IMPLIED  
efftext (3696) CDATA #IMPLIED  
efftype (3697) CDATA #IMPLIED  
efflen (3698) NUMBER #IMPLIED >
```

```txt
<!ELEMENT sbeff(3699) - O EMPTY  
<!ATTLIST sbeff  
effrg (3700) CDATA #REQUIRED  
sbnbr (3701) CDATA #REQUIRED  
sbcond (3702) CDATA #REQUIRED  
sbrev (3703) CDATA #IMPLIED  
coord (3704) CDATA #IMPLIED  
efftext (3705) CDATA #IMPLIED  
efftype (3706) CDATA #IMPLIED  
efflen (3707) NUMBER #IMPLIED
```

```txt
<!ELEMENT coceff(3708) - O EMPTY  
<!ATTLIST coceff  
effrg (3709) CDATA #REQUIRED
```

<table><tr><td>cocnbr (3710)</td><td>CDATA</td><td>#REQUIRED</td></tr><tr><td>coord (3711)</td><td>CDATA</td><td>#IMPLIED</td></tr><tr><td>efftext (3712)</td><td>CDATA</td><td>#IMPLIED</td></tr><tr><td>e Specialty (3713)</td><td>CDATA</td><td>#IMPLIED</td></tr><tr><td>efflen (3714)</td><td>NUMBER</td><td>#IMPLIED</td></tr></table>

<table><tr><td colspan="4">&lt;--========================================================================================================================================================================================================----&gt;</td></tr><tr><td>&lt;----</td><td>MISCELLANEOUS</td><td>其它</td><td>-&gt;</td></tr><tr><td>&lt;----====================================================================================================================================================================================================----</td><td></td><td></td><td></td></tr><tr><td>&lt;--ELEMENT txtgrphc (3715)</td><td>--</td><td>(txtline+)</td><td>&gt;</td></tr><tr><td>&lt;--ELEMENT txtline (3716)</td><td>--</td><td>(#PCDATA)</td><td>&gt;</td></tr><tr><td>&lt;--ELEMENT deleted (3717)</td><td>-O</td><td>EMPTY</td><td>&gt;</td></tr><tr><td>&lt;--ELEMENT isempty (3718)</td><td>-O</td><td>EMPTY</td><td>&gt;</td></tr><tr><td>&lt;--ELEMENT revst (3719)</td><td>-O</td><td>EMPTY</td><td>&gt;</td></tr><tr><td>&lt;--ELEMENT revend (3720)</td><td>-O</td><td>EMPTY</td><td>&gt;</td></tr><tr><td>&lt;--ELEMENT cocst (3721)</td><td>-O</td><td>EMPTY</td><td>&gt;</td></tr><tr><td>&lt;--ELEMENT cocend (3722)</td><td>-O</td><td>EMPTY</td><td>&gt;</td></tr><tr><td>&lt;--ELEMENT hotlink (3723)</td><td>-O</td><td>EMPTY</td><td>&gt;</td></tr><tr><td>&lt;--ATTLIST hotlink targetid (3724)</td><td>CDATA</td><td>#IMPLIED</td><td></td></tr><tr><td>targetrefid (3725)</td><td>CDATA</td><td>#IMPLIED</td><td>&gt;</td></tr><tr><td>]&gt;</td><td></td><td></td><td></td></tr></table>

# 2 结构图表

结构图的关键组成部分可参见 DTD 技术要求(参见[4-2-3.22.4])

![](images/f702642038675e54758acc39814d2932166a1a5784845bf043a2b28922ce4a9e.jpg)  
图4-2-36.1 WM DTD结构一前页

![](images/0ec1c1b41c511267f623f7f16e4ec7f514a4795427156601707c7411a80c5535.jpg)  
图4-2-36.2 WM DTD结构一概述(标准实施章、节和题目)

![](images/516e11d67f9cdd65e5ed65ec383b4ffe75c5148a3cc699c718c6d2befc1a283f.jpg)  
图4-2-36.3 WM DTD结构-WM清单

![](images/12448071ce2c6053acad5c2e3815cb0e33d54781d0d83c9613e8437420ae9885.jpg)  
图4-2-36.4 WM DTD结构一增加性更改和临时更改

# 4-3 纲要模型

# 4-3-1 ATA 通用纲要模型

# 1 前言

本文件中描述的数据纲要模型以航空运输协会(ATA)和航空航天工业协会(AIA)检索工作组联合开发的功能要求规范[参见本文2-2-1]为基础。航空运输协会的CD-ROM实施概要文件将该标准作为ATA/AIA实现CD-ROM光盘可交换性的必要标准之一。

该规范描绘了符合2200规范文件的逻辑元素，并将它们放置在表中，从而可以利用结构化全文查询语言(SFQL)访问数据。SFQL为客户端的应用程序规定了一种独立于数据库服务器的运行方式，可以使用全文本和结构化查询方法来请求和接收数据。

表格的编排如下。表格的行代表一个数据实体的实例(例如：章)，列包含该数据样本的信息(例如，章标题)。

该文件通过定义一个基本的表(纲要模型)集合来表示用于维修任务中的ATA/AIA文件。每个文件类型具有其纲要模型，并提供了支持该文件所必需的附加表。（例如：[本文4一3一2]中关于飞机维修/发动机大修手册的内容）

该文件由下列各项组成：

[本文4-3-1.2] 详述纲要模型中的假定条件。  
[本文4-3-1.3]描述用于纲要模型中的数据类型  
- [本文4-3-1.4]描述用于纲要模型中的符号约定。  
- [本文4-3-1.5]描述了BITFIELD EFFECTIVITY_MASK的建立和用法。  
- [本文4-3-1.6] 描述了临时更改的处理。  
- [本文4-3-1.6]描述了适用于所有2200规范文件类型的纲要模型。

# 2 假设条件

一个适用的数据库必须定义该文件中规定的每个表。但当该表没有可用的相关数据时，表可以为空。以下是针对这些纲要模型的假定条件列表：

- 纲要模型不能通过纸型手册页码编排来保持逻辑元素的关系。  
- 表描述了数据的逻辑“视图”。SFQL 服务器解决了该文件表中描述的逻辑视图和数据在磁盘上的实际表现之间的差异。就是说，可以假定表不是事实存在的。需要注意的是这并不需要一个 SFQL 视图结构，因为数据定义语言结构不是可交换性标准的必要部分。

# 3 内容

从 SFQL 服务器返回的数据的格式取决于每个表的表栏中所给出的数据类型。例如，在 Doc 表中，“更改代码”栏以 CHAR 格式返回数据。

# 3.1 整数型数据格式

应根据 SFQL 规范返回附录中规定的整数型数据。

# 3.2 字符型数据格式

应根据 SFQL 规范返回附录中规定的 CHAR(字符型)数据。在应用 (软件) 工具中, 可以选择使用VARCHAR 数据类型, 它是当前规定的 CHAR 数据类型。

应用(软件)工具中，可以选择是否对CHAR数据类型执行全文本操作(SFQL列表的栏FULL TEXT INDEXED设置为TRUE)

# 3.3 文本数据格式

纲要模型中的文本格式引用了用SGML标记的ASCII文本，这是依据ATA DTD文件类型方面的相关规定。例如：飞机维修手册应根据ATA飞机维修手册DTD来标记。SFQL数据类型标志符是“TEXT”。SFQL数据类型版本标志符是“SGML/ATA Rxx.xx”，其中xx.xx是针对特定DTD的适当版本号。

注：所有栏描述的是 DTD 元素而不是 TEXT 类型的属性，因为源数据可能包含浮点元素，例如< hotlinks>可能会丢

失。

# 3.3.1 规范形式的文本数据

- 由于在数据库中，一栏 TEXT 类型的(数据)可能只表示文件实例的一个子集，因此要求 TEXT 类型的字段是规范的形式。(例：所有最小限度的扩展)。  
- 已经在 SGML TEXT 中预先定义过的隐含属性值，在使用该隐含属性情况下应明确地叙述。

# 3.3.2 全文本查询操作

TEXT类型的栏预先设计为允许全文本操作——就是说，将SFQL列表的栏FULL_text_INDEXED设置为TRUE。

TEXT栏中的SGML标记对于全文本查询应是“透明”的。例如，只用标记分隔的2个词被认为是直接相邻。所有词，无论是明确的文本或是从标记中生成的，都可以被索引。

# 3.3.3 全文本浏览

每个 TEXT 类型栏必须随着 GEN.DOCS 表中提供的、用于描述元素文本的开始和结束的两个栏。这就允许用户在任何表的边界之外或文档层次结构的上下文中进行浏览。

# 3.3.4 <HOTLINK>标记

TEXT 类型栏可以包含一个特定的 hotlink 特殊标记，它在数据库加载时被增加到数据库中。当文档实例存入数据库时，该标记可将 GEN.References 表中的键值插入到文件实例中。

由数据库加载软件按照 DTD 限定的以下方面的使用限制执行插入动作：hotlink 标记必须总是直接跟在其它元素的起始标记之后，并隐含地由该(父)元素的结束标记来终止。

与该纲要模型有关的 hotlink 标记的使用基于 hotlink 的两个属性: targetid (参考目标) 和 targetrefid (参考来源)。targetid 属性指示了有关 hotlink 父元素中文本的唯一 ID。targetrefid 属性指示了 hotlink 父元素中的全部文本, 是对一个在 targetid 属性中具有相同 ID 值的文本的超级链接参考源。在执行超链接过程中, 如何使用 hotlink 将参考和引用表相关联的例子可见 “参考表” 一节。

# 3.4 GRAPHIC格式

该纲要模型中的图形格式参考了在图形交换规范（[参见本文5-2-4]）中定义的矢量或点阵示图(CGM、TIFF)ATA数字标准。该SFQL数据类型标志符是“GRAPHIC”。对于点阵示图，其SFQL数据类型版本标志符是“TIFF/ATA Rxx.xx”，对于矢量示图，其SFQL数据类型版本标志符是“CGM/ATARxx.xx”。

# 3.5 BITFIELD格式

BITFIELD 格式是一个基于 SFQL CHAR 字符的纲要模型定义的数据类型。它是一个固定长度的字段，每个字符用于表示一个集合中的一个成员。字段中的字符被限定为“0”和“1”，其中“1”表示用一个给定位置来表示的对象是集合的一个成员。例如，它在纲要模型中可用于对有效性进行编码，每个字符位置用于表示一个特定的飞机构型，用数值“0”或“1”表示该构型的可适用性。（见“使用 BITFIELD 的 EFFECTIVITY_MASK”节）。

# 3.6 日期格式

日期是一个整数序列，表示方式为：4位数字表示年，2位数字表示月，2位数字表示日，之间用连字符分隔。这样表示的日期在SFQL查询时或按SFQL规范所返回的数据是有效的。SFQL数据类型标志符是“DATE”。

# 3.7 NULL数据

NULL 数据用 SFQL 数据类型标志符 “NULL” 来表示。NULL 数据表示用行描述的文件子类型样本没有列的值。

# 4符号约定

为保证纲要模型的一致性，制定了若干约定协议。

# 4.1 SGML标记和属性

- SGML 标记或属性在表中被表示为:

（元素名称）或

（元素名称 属性名称）

- 在某些情况下，一个属性可以出现在几个元素中。例如，在更改摘要表中，可根据一个任务或一个子任务(或其它的)元素分配sectnbr属性。在这些情况中，元素名称用一个问号（“?”）来标记，它的表示取决于行的上下文，例如，<?sectnbr>  
如果栏与应用程序无关(例如，由发动机制造商使用，而非飞机制造商使用)，表的说明条目应写为“未使用”。  
如果栏的内容不直接来自SGML，但是当创建SFQL表时，必须构建该内容，表的说明条目应写为“N.A”。

# 4.2 字段名

除了系统产生的ID（例如，诸如DOC ID和外部关键字的行标识值)外，字段名都是小写的。注意这仅仅是为了说明。大小写对于SFQL中的栏名称是无关紧要的。  
- 外部关键字在栏名称前用一个“@”来表示。它们也可以以@GEN.DOCS.DOC_ID中的一个foreignTableName和foreignSchemaName作为前缀。  
- 用“_text”表示的字段名是文件层次结构的一些单元的SGML片段。每个“* text”字段必须用两个相应的字段“* startoff”和“* endoff”来连接，如GEN.DOCS表中所描述的那样，在整个文件实例的相关片段中，这两个字段保存了第一个和最后一个字符之间的内容。参见“Doc表”。

表 4-3-1.1 图例键表  

<table><tr><td>* 主关键字</td></tr><tr><td>** 备用关键字(所有**栏的组合)</td></tr><tr><td>@次关键字</td></tr><tr><td>NA 表示对于该栏值没有适用的必须根据SGML或其它数据源进行计算或提取的SGML标记。</td></tr></table>

# 5 使用BITFIELD的EFFECTIVITY_MASK

# 5.1 EFFECTIVITY_MASK 的定义

ATA_维修纲要模型可以包含一个有效性表。每个纲要模型的有效性表应允许将“key”的任何编号(effectivity_key，序列号，或用户指定的实例号)映射为一个MASK POSITION_NBR。这样，其它的纲要模型表可以包括一个命名为EFFECTIVITY_MASK的栏，以对特定的飞机或发动机构型进行有效性编码。

EFFECTIVITY_MASK 值是根据 SGML 实例中的“EFFECT”元素的“effrg”属性所规定的有效性代码域的内容建立的。发动机和机身在“effrg”编码时有着明显的差别：

- 机身——effrg 是一个用空格分隔的 effectivity_key 值域列表，该值域有 6 个字符（3 个起始关键字，3 个结束关键字）。(参看下面的例子)保留值 999 表示可适用于所有的飞机。  
- 发动机——effrg 是一个用空格分隔的非标准 effectivity_key 的列表，例如：

$$
<   E F F E C T e f f r g = “ O E C O J C O F D O L C ” >
$$

或

$$
<   E F F E C T e f f r g = " M / N U / N W / N X / N Y / N" >
$$

参见 ATA 技术要求有关文本交换的内容（[参见本文 4-2-3]），可获知关于“effrg”属性语义上的更多信息。

EFFECTIVITY_MASK模板的长度恒等于有效表行数。EFFECTIVITY_MASK中字符位置的编号计数应从右至左，且第一个位置用数字1表示起始。换句话说，位置1是最右边的数字。该纲要模型表中任何给定的“candidate(待选)”行应有一个EFFECTIVITY_MASK栏：

1. 任何在给定位置上 ASCII 字符为“0”的值不必进一步说明。

2. 任何给定位置上 ASCII 字符为“1”的值表示该“candidate(待选)”行适用于一个机身或发动机，该机身或发动机可在有效表中找到。

对适用于“candidate”行的effectivity_key的值进行标识：

a）EFFECTIVITY_MASK 中的每个 ASCII 字符“1”的位置号与相对的有效性表中的 MASK POSITION_NBR 进行对照。  
b）相对应的有效性表的行标识了“candidate(待选)”行适用的飞机或发动机。  
c）如果一个适用于所有飞机或发动机的“candidate（待选）”行被数据库参考，所有EFFECTIVITY_MASK字符应为“1”。

# 5.2 在飞机文件中建立 EFFECTIVITY_MASK

下面是一个如何在MSM纲要模型中建立飞机文件的EFFECTIVITY_MASK的例子：

给出以下有效性表：

<table><tr><td>有效性关键字</td><td>G</td></tr><tr><td>001</td><td>1</td></tr><tr><td>002</td><td>2</td></tr><tr><td>014</td><td>3</td></tr><tr><td>015</td><td>4</td></tr><tr><td>016</td><td>5</td></tr><tr><td>021</td><td>6</td></tr><tr><td>022</td><td>7</td></tr><tr><td>200</td><td>8</td></tr></table>

和下列SGML片段：

$$
<   S H E E T k e y = " A" \dots > <   E F F E C T e f f r g = " 1 5 0 2 1" <   / E F F E C T > \dots <   / S H E E T >
$$

$$
<   S H E E T k e y = " B" \dots > <   E F F E C T e f f r g = " 2 1 9 9 9" <   / E F F E C T > \dots <   / S H E E T >
$$

SHEET表应包含：

key_code

EFFECTIVITY_MASK

A

00111000

B

110 00000

位的位置

87654321

# 5.3 查询时使用 EFFECTIVITY_MASK

对于一个给定的有效性集合，可以限定对纲要模型表中的查询结果：

1. 使用关键字的任意组合来查询有效性表，返回适用的飞机或发动机的MASK POSITION_NBR集合。  
2. 使用MASK POSITION_NBR建立一个EFFECTIVITY_MASK模板，其中任意位置的一个ASCII字符‘1’都有返回的MASK POSITION_NBR与其相对应，而其它所有位置都是ASCII字符‘0’。EFFECTIVITY_MASK模板的位置总是从右到左编号。参见前文中所给出的关于SHEET表中EFFECTIVITY_MASK的例子。

使用SFQL‘LIKE’_谓语和SFQL字符串通配符（“%”代表0或多个字符，“_”代表任意单个字符）来与相应的EFFECTIVITY_MASK栏值匹配，以对预期的有效性进行限定查询。

例1：在前一例中，在图页表的任意有效行中查询有效性关键字15或16(掩码位置号4和5)：  $(\%)$

是针对多字符的通配符，是针对单个字符的通配符）

WHERE Sheet.EFFECTIVITY_MASK LIKE '%1'

例2：在图页表的任意有效行中查询有效性关键字15和16：

WHERE Sheet.EFFECTIVITY_MASK LIKE '%11'

# 6 临时更改的处理

表TRINFO和TRLINK用于支持临时更改(TR)。TRINFO表提供了关于TR的信息，包括TR的SGML文本(其使用例子，仅查询TR)。TRLINK表提供数据库的一个底层级别的更新视图——每行代表数据库中某处一个更新的表“单元格”。这在TRINFO表和数据库之间形成一种关系，标识数据库中的行已经更新。关于处理临时更改的进一步讨论，[参见本文2-2-1.3.7]，要求，技术更改。

# 7 ATA 通用纲要模型

该纲要模型称为“GEN”纲要模型，它属于“ATA_维修”类。在本节中定义“GEN”纲要模型中包含的通用表。

# 7.1 Doc表

该表包含了根据“ATA_维修”类的纲要模型进行检索的所有可用文件的一个记录。每行表示一个文件，由该手册类型的纲要模型做进一步描述。(例如，[本文4-3-2]关于AMM和ESM的手册类型的内容)一个特定文件的全部文本用一行中的document_text来表示。其它视图的其它表中可具有相同的部分文本。(例如，一个任务可用于飞机维修/发动机大修手册的工作表中，也可用于该Doc表中。）

按照DTD技术要求文件，元素<manual_name>描述了一个文件的通用模型。

表4-3-1.2Doc表  

<table><tr><td>栏名称</td><td>类型</td><td>飞机标记</td><td>发动机标记</td><td>描述</td></tr><tr><td>DOC_ID*</td><td>INT</td><td>NA</td><td>NA</td><td>唯一分配值(rowid)</td></tr><tr><td>customer_code**</td><td>CHAR</td><td>&lt;manual_name cus&gt;</td><td>&lt;manual_name cus&gt;</td><td>用户代码</td></tr><tr><td>customer_name</td><td>CHAR</td><td>&lt;manual_namecusname&gt;</td><td>&lt;manual_namecusname&gt;</td><td>用户名称</td></tr><tr><td>manual_type_code**</td><td>CHAR</td><td>DTD doctype</td><td>DTD doctype</td><td>手册类型(如:AMM、EIPC)</td></tr><tr><td>revision_number**</td><td>CHAR</td><td>&lt;manual_name tsn&gt;</td><td>&lt;manual_name tsn&gt;</td><td>更改号</td></tr><tr><td>model_code**</td><td>CHAR</td><td>&lt;manual_name model&gt;</td><td>&lt;manual_name model&gt;</td><td>型号名称</td></tr><tr><td>document_code</td><td>CHAR</td><td>&lt;manual_name docnbr&gt;</td><td>&lt;manual_name docnbr&gt;</td><td>文件号</td></tr><tr><td>orig-issue_date</td><td>DATE</td><td>&lt;manual_nameoidate&gt;</td><td>&lt;manual_nameoidate&gt;</td><td>出版日期</td></tr><tr><td>revision_date</td><td>DATE</td><td>&lt;manual_namerevdate&gt;</td><td>&lt;manual_namerevdate&gt;</td><td>更改日期</td></tr><tr><td>supplier_code</td><td>CHAR</td><td>&lt;manual_name spl&gt;</td><td>&lt;manual_name spl&gt;</td><td>飞机或发动机供应商的标识</td></tr><tr><td>update_code</td><td>CHAR</td><td>&lt;manual_namechg&gt;</td><td>&lt;manual_namechg&gt;</td><td>更改代码</td></tr><tr><td>title_text</td><td>TEXT</td><td>&lt;title&gt;</td><td>&lt;title&gt;</td><td>手册标题</td></tr><tr><td>@TEXTINFO_ID</td><td>INT</td><td>NA</td><td>NA</td><td>在Textinfo表中的外部关键字</td></tr><tr><td>document_text</td><td>TEXT</td><td>&lt;manual_name&gt;</td><td>&lt;manual_name&gt;</td><td>全部文件</td></tr></table>

注1：DOCTYPE是AMM、ESM、AIPC或EIPC。

# 7.2 Textinfo表

对于根据“ATA_维修”类中的纲要模型进行检索的所有可用文件，该表包含了关于编码和文本标记的信息。

由于 TEXTINFO_ID 是关于文本编码和标记信息的唯一关键字，因此假定辅助表中的 ATA TEXT 格式数据的所有方面均遵循相同的标记规则。

表4-3-1.3 Textinfo表  

<table><tr><td>栏名称</td><td>类型</td><td>飞机标记</td><td>发动机标记</td><td>描述</td></tr><tr><td>TEXTINFO_ID*</td><td>INT</td><td>NA</td><td>NA</td><td>分配的唯一值(rowid)</td></tr><tr><td>prolog**</td><td>CHAR</td><td>SGML文件序言</td><td>SGML文件</td><td>该文件完整的SGML格式序言,包括SGML声明和文件类型定义</td></tr></table>

# 7.3 参考表

该表包含了便于在全文本数据库中实现交叉参考(热点链接)的信息。它表示在当前 ATA_维修数据库目录中的所有交叉参考目标的一个索引，其中，一个目标被定义为交叉参考的目标位置。对于每个热点链接，在表中都有一个明确的条目：尽管可以有两个或多个(参考)源对同一目标进行参考，但目标在表中只能表示一次。

表4-3-1.4 参考表  

<table><tr><td>栏名称</td><td>类型</td><td>飞机标记</td><td>发动机标记</td><td>描述</td></tr><tr><td>REFERENCE_CODE*</td><td>CHAR</td><td>&lt; hotlink targetid&gt;</td><td>&lt; hot link tar getid&gt;</td><td>唯一分配值(rowid)。该值不是来源于热点链接属性targetid,而是以属性为基础(在数据库建立期间,该代码被分配之后,标记和属性值被插入到热点链接目标的源文本中。)</td></tr><tr><td>target_schema_name**</td><td>CHAR</td><td>NA</td><td>NA</td><td>包含目标表的纲要模型名称</td></tr><tr><td>target_table_name**</td><td>CHAR</td><td>NA</td><td>NA</td><td>包含目标的表名称</td></tr><tr><td>target_key_name**</td><td>CHAR</td><td>NA</td><td>NA</td><td>主关键字名称</td></tr><tr><td>@TARGET_KEY_ID**</td><td>INT</td><td>NA</td><td>NA</td><td>标识目标文本的主关键字的值</td></tr><tr><td>target_column_name**</td><td>CHAR</td><td>NA</td><td>NA</td><td>包含目标文本的栏名称</td></tr><tr><td>target_text</td><td>TEXT</td><td>VARIES</td><td>VARIES</td><td>目标位置处的文本(必须与由TARGET_KEY_ID指向的文本相同)</td></tr><tr><td>target_startoff</td><td>INT</td><td>NA</td><td>NA</td><td>通用纲要模型中的Doc表[参考本文4-3-1.7.1]中描述的target_text栏起始的相对位置</td></tr><tr><td>target_endoff</td><td>INT</td><td>NA</td><td>NA</td><td>通用纲要模型中的Doc表[参考本文4-3-1.7.1]中描述的target_text栏结束的相对位置</td></tr></table>

该处理方法依据数据库中描述的对文本数据格式的如下的特殊定义和限制：

- 在数据库建立过程中，对交叉参考的每个目标(目标位置)分配一个唯一的ID。在计算完关键字之后，使用一个命名为“Hotlinks”的特殊ATA DTD标记，将其嵌入到数据库中存储的SGML格式文本中。targetid属性用于表示标记中的关键字值。这样，根据任意表由服务器返回的一个

热点链接的目标应有一个包含targetid属性的Hotlink标记，该标记是唯一的。

- 在数据库准备期间，参考目标文本的任何文本(源文本)也有一个嵌入的Hotlink标记。在这种情况中，虽然将关键字值放置在一个名称为targetrefid 的属性中，但只表明它是对目标的一个参考，而不是目标本身。显示软件可以将一个Hotlink按钮和上层Hotlink标记中包含的文本链接起来。当选择按钮时，显示软件获取targetrefid 值，并给出一个查询(结果)。例如：如果targetrefid 值是“A1S2P3”：

SELECT target_text, target_schema_name, target_table_name, target_column_name, target_key_name, target_key_id

# FROM References

WHERE REFERENCE_CODE = "A1S2P3";

该查询(结果)可以返回目标文本本身(target_text栏)以及在数据库中查找目标文本的原始内容时所需的信息(纲要模型名称，表名称，栏名称，关键字栏和关键字值)。注意可以使用单个SELECT(没有指针)，因为REFERENCE_CODE是唯一的，并且只返回一个数据行。

注意如果一个 Hotlink 标记既是 (1) 一个参考的目标, 又是 (2) 其它目标的参考源, 那么它可能既有 targetid 属性又有 targetrefid 属性 ([参见本文 4-3-1.3.3], 以及 DTD 技术要求关于 Hotlinks 标记的附加信息)。

- 交叉参考的目标必须用当前目录（“ATA_维修”类）中的一个表的一行中的一栏来表示。例如，一个交叉参考可被设置为对一个任务标题，或对一个任务文本进行参考。参考表的target_schema_name、target_table_name、target_key_name栏和TARGET_KEY_ID共同提供了到“ATA_维修”类内部的任意表中的目标行的一条完整访问路径。target_column_name栏给出了包含target_text的行的栏名。

- target_text 栏能有选择性地提供目标文本，因为 target_text 栏可精确地表述目标行的 target_column_name 栏，该目标行由 target_schema_name、target_table_name、target_key_name 和 target_key_id 来表示。如果参考表中没有提供 target_text，该栏值应为 NULL(空)，需要用户从指定的目标表中检索源文本或目标文本。在任何情况下，target_schema_name、target_table_name 和 target_key_name 必须包含一个有效表和栏参考，并且 TARGET_KEY_ID 应包含相应行的关键字值。

# 7.4 引用表

该表包含了便于在全文本数据库中实现交叉参考（“Hotlink热点链接”）的信息。它表述了交叉参考链接的一个索引，在该索引中一个链接被定义为一对源/目标。在“ATA_维修”类中每个 hotlink只有一行。

引用表用于查找所有参考到一个给定目标的热点链接源。这是通过标识目标的REFERENCE_CODE进行查找来实现的。这样一个查找过程可能会检索到多个行。

使用两种备用限定符(栏)设置，客户端可以对引用(对一个目标的所有参考源)进行查询：

1) REFERENCE_CODE  
2）源纲要模型名、源表名、源关键字名、SOURCE KEY ID(源关键字ID)和源栏名。

第一种方法可用于对参考表中所有参考项目的引用条文进行查找。第二种方法可用于汇集数据库中所有项目的引用条文。注意这两种情况都可以返回多个行，因为对一个目标可以有多个引用。

例如，为了用热点链接的targetid属性值“A1P2S3”来查找参考到一个位置(目标)的源文本，显示软件可以执行查询动作(因为可能返回多行引用条文，所以指针是必需的)：

DECLARE CURSOR citations AS

SELECT source_schema_name, source_table_name, source_key_name,

source_key_id, source_column_name, source_text

FROM Citations

WHERE REFERENCE_CODE = "A1P2S3"

包含引用的文本可以在 source_text 中，但是 source_text 也可以选择为 NULL（空）（建立数据库时建立的一个选项）。在这种情况下，显示软件可通过执行单个选择来检索 source_text，这个选择依据由 source_schema_name、source_table_name、source_key_name、source_key_id 和 source_column_name 确定的表。例如，如果这些值分别是“MSM”，“Task”，“TASK_ID”，“23443”和“task_text”，查询应是：

SELECT task_text

FROM MSM.Task

WHERE TASK_ID = 23443;

为了遍历所有含有指定目标的链接(引用)的文本，对于用上述“引用”指针返回的每行，应执行类似的查询（因为纲要模型、表名和引用文本栏可能会变化，因此执行单个查询是不实际的）。

表 4-3-1.5 引用表  

<table><tr><td>栏名</td><td>类型</td><td>飞机标记</td><td>发动机标记</td><td>描述</td></tr><tr><td>CITATION_ID*</td><td>INT</td><td>NA</td><td>NA</td><td>唯一分配值(rowid)。</td></tr><tr><td>source_schema_name**</td><td>CHAR</td><td>NA</td><td>NA</td><td>包含源表的纲要模型名</td></tr><tr><td>source_table_name**</td><td>CHAR</td><td>NA</td><td>NA</td><td>包含链接源的表名</td></tr><tr><td>source_key_name**</td><td>CHAR</td><td>NA</td><td>NA</td><td>参考源的单个栏的主要或备用关键字名称</td></tr><tr><td>@SOURCE_KEY_ID**</td><td>INT</td><td>NA</td><td>NA</td><td>标识源文本的单个栏的主要或备用关键字值</td></tr><tr><td>source_column_name**</td><td>CHAR</td><td>NA</td><td>NA</td><td>包含参考源的栏名</td></tr><tr><td>target_schema_name**</td><td>CHAR</td><td>NA</td><td>NA</td><td>包含目标表的 schema 名</td></tr><tr><td>target_table_name**</td><td>CHAR</td><td>NA</td><td>NA</td><td>包含目标的表名</td></tr><tr><td>target_key_name**</td><td>CHAR</td><td>NA</td><td>NA</td><td>单个栏的主要或备用关键字名称</td></tr><tr><td>@TARGET_KEY_ID**</td><td>INT</td><td>NA</td><td>NA</td><td>标识目标文本的单个栏的主要或备用关键字值</td></tr><tr><td>target_column_name**</td><td>CHAR</td><td>NA</td><td>NA</td><td>包含目标文本的栏名</td></tr><tr><td>source_text</td><td>TEXT</td><td>Varies</td><td>Varies</td><td>引用源处的文本或文本的一个特定片段</td></tr><tr><td>source_startoff</td><td>INT</td><td>NA</td><td>NA</td><td>通用纲要模型中的 Doc 表[参见本文4-3-1.7.1]中描述的 target_text 栏起始的相对位置</td></tr><tr><td>source_endoff</td><td>INT</td><td>NA</td><td>NA</td><td>通用纲要模型中的 Doc 表[参见本文4-3-1.7.1]中描述的 target_text 栏结束的相对位置</td></tr><tr><td>@REFERENCE_CODE</td><td>CHAR</td><td>&lt; hotlink targetrefid&gt;</td><td>&lt; hotlink targetrefid&gt;</td><td>该值并非来源于热点链接属性targetid,而是该属性的基础(该代码在数据库建立期间被分配之后,标记和属性值被插入到在热点链接目标的原始文本中。)</td></tr></table>

# 7.5 TRinfo表

该表包含了每个临时更改的信息，包括TR的SGML文本。

表 4-3-1.6 Trinfo 表  

<table><tr><td>栏名</td><td>类型</td><td>飞机标记</td><td>发动机标记</td><td>描述</td></tr><tr><td>TRINFO_ID*</td><td>INT</td><td>NA</td><td>NA</td><td>唯一分配值(rowid)</td></tr><tr><td>@GEN.DOC.S.DOC_ID</td><td>INT</td><td>NA</td><td>NA</td><td>文件ID。通用纲要模型中的Doc表[参见本文4-3-1.7.1]中的外部关键字。</td></tr><tr><td>PAPER_TR_NB_R</td><td>CHAR</td><td>&lt;paaptbr&gt;</td><td>&lt;paaptbr&gt;</td><td>纸质TR号。一个纸型的TR号包含了一个单独的数字TR所涉及的一系列更改中的一部分</td></tr><tr><td>INFO</td><td>TEXT</td><td>&lt;trinfo&gt;</td><td>&lt;trinfo&gt;</td><td>合并、定位和通常在一个纸型的TR的封面上的其它说明性数据</td></tr><tr><td>LOC</td><td>TEXT</td><td>&lt;trloc&gt;</td><td>&lt;trloc&gt;</td><td>临时更改位置(主要的(基本的)文件实例中由(部分)临时更改临时代替的每个位置标识的关键字)</td></tr><tr><td>NUMBER</td><td>CHAR</td><td>&lt;tnbr&gt;</td><td>&lt;tnbr&gt;</td><td>临时更改号</td></tr><tr><td>ISSUE_DATE</td><td>CHAR</td><td>&lt;issdate&gt;</td><td>&lt;issdate&gt;</td><td>临时更改发布日期</td></tr><tr><td>REPLACED</td><td>CHAR</td><td>&lt;trrepl&gt;</td><td>&lt;trrepl&gt;</td><td>替换的临时更改</td></tr><tr><td>DELETED</td><td>CHAR</td><td>&lt;trdel&gt;</td><td>&lt;trdel&gt;</td><td>删除的临时更改</td></tr><tr><td>STATUS</td><td>CHAR</td><td>&lt;trstatus&gt;</td><td>&lt;trstatus&gt;</td><td>临时更改的状态。允许的值是:“Active有效”,“Canceled取消”,或“Incorporated合并”</td></tr><tr><td>TRREASON</td><td>CHAR</td><td>&lt;trreason&gt;</td><td>&lt;trreason&gt;</td><td>TR的原因</td></tr><tr><td>ORIGINATOR</td><td>CHAR</td><td>(TR ControlFile)TR控制文件</td><td>(TR ControlFile) TR控制文件</td><td>发布TR的原始数据提供者(航空公司、制造商或组件供应商)</td></tr><tr><td>AIRLINE_REL_DATE</td><td>CHAR</td><td>(TR ControlFile) TR控制文件</td><td>(TR ControlFile) TR控制文件</td><td>航空公司发布制造商TR或他们自己的使用的TR的日期</td></tr><tr><td>AIRLINE/reference</td><td>CHAR</td><td>(TR ControlFile) TR控制文件</td><td>(TR ControlFile) TR控制文件</td><td>仅供本地航空公司使用—授权文件的唯一ID</td></tr><tr><td>AIRLINE_AUTHOR_ID</td><td>CHAR</td><td>(TR ControlFile) TR控制文件</td><td>(TR ControlFile) TR控制文件</td><td>仅供本地航空公司使用—TR作者的唯一ID</td></tr><tr><td>FRONT_MATTER</td><td>TEXT</td><td>&lt;trfmatr&gt;</td><td>&lt;trfmatr&gt;</td><td>TR的前页内容</td></tr><tr><td>TITLE</td><td>TEXT</td><td>&lt;title&gt;</td><td>&lt;title&gt;</td><td>TR的标题</td></tr><tr><td>TR_TEXT</td><td>TEXT</td><td>&lt;tr&gt;</td><td>&lt;tr&gt;</td><td>TR的SGML片段</td></tr></table>

# 7.6 TRlink表

该表提供数据库的一个基本级别更新视图。每行表示数据库某处的一个更新的表“单元格”。这在TRINFO和数据库之间形成了一种关系，保存了已更新的数据库的行信息。

表 4-3-1.7 临时更改链接表  

<table><tr><td>栏名</td><td>类型</td><td>飞机标记</td><td>发动机标记</td><td>描述</td></tr><tr><td>TRLINK_ID*</td><td>INT</td><td>NA</td><td>NA</td><td>唯一分配值(rowid)</td></tr><tr><td>@TRINFO.TRINFO_ID</td><td>INT</td><td>NA</td><td>NA</td><td>指示该链接来自哪个TR</td></tr><tr><td>upd_schema_name**</td><td>CHAR</td><td>NA</td><td>NA</td><td>包含更新表的纲要模型名称</td></tr><tr><td>upd_table_name</td><td>CHAR</td><td>NA</td><td>NA</td><td>包含更新表的表名称</td></tr><tr><td>upd_key_name</td><td>CHAR</td><td>NA</td><td>NA</td><td>主关键字栏的名称</td></tr><tr><td>@UPD_KEY_ID</td><td>INT</td><td>NA</td><td>NA</td><td>标识源自 upd 表名的更新信息的主关键字的值</td></tr><tr><td>upd_column_name</td><td>CHAR</td><td>NA</td><td>NA</td><td>包含更新文本的栏名</td></tr><tr><td>upd_startoff</td><td>INT</td><td>NA</td><td>NA</td><td>通用纲要模型中的 Doc 表[参见本文 4-3-1.7.1]中描述的 target_text栏起始的相对位置</td></tr><tr><td>upd_endoff</td><td>INT</td><td>NA</td><td>NA</td><td>通用纲要模型中的 Doc 表[参见本文 4-3-1.7.1]中描述的 target_text栏结束的相对位置</td></tr><tr><td>upd_data</td><td>BINARY</td><td>VARIES</td><td>VARIES</td><td>数据本身更新(必须与由 TARGET KEY ID 指向的数据相同)</td></tr></table>

# 4-3-2 飞机维修和发动机大修手册(MSM)纲要模型

本文件随同 ATA 通用 schema([参见 4-3-1])一起，提供了适用于面向任务的飞机维修和发动机大修手册的检索 Schema。该 schema 称为本文“MSM” schema，且属于“ATA_维修”类。

# 1 Front_Matter(前页)表

该表包含文件的前页。它将前页划分成若干部分，其中division_name栏指出了DTD标记，按照这些标记导出了正文前内容。

表 4-3-2.1 Front_matter 表  

<table><tr><td>栏名</td><td>类型</td><td>飞机标记</td><td>发动机标记</td><td>描述</td></tr><tr><td>FRONT_MATTER_ID*</td><td>INT</td><td>NA</td><td>NA</td><td>唯一分配ID</td></tr><tr><td>@GEN.DOCS.DOC_ID**</td><td>INT</td><td>NA</td><td>NA</td><td>文件ID。在通用纲要模型的Doc表[参见本文4-3-1.7.1]中</td></tr><tr><td>division_name**</td><td>CHAR</td><td>[见本文4-3-2.2]“标准前页分段名称</td><td>[见本文4-3-2.2]“标准前页分段名称</td><td>前页的分段(部分)的名称</td></tr><tr><td>division_title</td><td>TEXT</td><td>&lt;title&gt;</td><td>&lt;title&gt;</td><td>分段标题</td></tr><tr><td>division_text</td><td>TEXT</td><td>[见本文 4-3-2.2]“标准前页分段名称</td><td>[见本文 4-3-2.2]“标准前页分段名称</td><td>一个分段的全部 SGML 片段</td></tr><tr><td>division_startoff</td><td>INT</td><td>NA</td><td>NA</td><td>通用纲要模型中的 Doc 表[参见本文 4-3-1.7.1]中描述的 division_text 栏起始的相对位置</td></tr><tr><td>division_endoff</td><td>INT</td><td>NA</td><td>NA</td><td>通用纲要模型中的 Doc 表[参见本文 4-3-1.7.1]中描述的 division_text 栏结束的相对位置</td></tr></table>

表 4-3-2.2 标准正文前内容分段名称  

<table><tr><td>Division_name</td><td colspan="2">Division_text</td><td>描述</td></tr><tr><td></td><td>飞机标记</td><td>发动机标记</td><td></td></tr><tr><td>TRANS_LETTER</td><td>&lt;transltr&gt;</td><td>&lt;transltr&gt;</td><td>更改的通用信息</td></tr><tr><td>TRLIST</td><td>&lt;trlist&gt;</td><td>&lt;trlist&gt;</td><td>临时更改单</td></tr><tr><td>INTRO</td><td>&lt;intro&gt;</td><td>&lt;intro&gt;</td><td>文件信息</td></tr><tr><td>EFFECT_X_REF</td><td>&lt;effxref&gt;</td><td>未使用</td><td>关于标识文件实例中的一个基本有效性组的不同方法以及这些方法如何相互联系的数据。</td></tr><tr><td>SB_LIST</td><td>&lt;sblist&gt;</td><td>&lt;sblist&gt;</td><td>维护通报当前合并状态的数据</td></tr><tr><td>DR_INDEX</td><td>&lt;drindex&gt;</td><td>未使用</td><td>手册中链接最低设备清单与相应的维护程序的数据</td></tr><tr><td>HOW_TO_USE</td><td>Not Used</td><td>&lt;howtouse&gt;</td><td>描述如何使用ESM</td></tr><tr><td>CONSUMABLE_ID_X</td><td>Not Used</td><td>&lt;conindex&gt;</td><td>对于ESM的消耗性材料清单</td></tr></table>

# 2 有效性表

本表被当作该纲要模型中其它表的 EFFECTIVITY_MASK 栏中有效性信息编码的“关键字”来使用。对于数据库的 MSM 部分中给出的每个不同的有效性值，在该表中都有一个行来描述。

表 4-3-2.3 有效性表  

<table><tr><td>栏名</td><td>类型</td><td>飞机标记</td><td>发动机标记</td><td>描述</td></tr><tr><td>effectivity_key*</td><td>CHAR</td><td>见注1</td><td>见注2</td><td>有效性关键字，是用于标识资料中一个特定有效性的唯一值。该值在飞机与发动机数据库两者之间有不同的起源和语义（见注1和注2）</td></tr><tr><td>mask_position_nbr**</td><td>INT</td><td>NA</td><td>NA</td><td>EFFECTIVITY_MASK 中唯一的指定位置。MASK POSITION_NBR 应是从 1~n 之间的无符号整数，其中 n 为有效性表中的行数。</td></tr><tr><td>line_nbr</td><td>CHAR</td><td>&lt;linenbr&gt;</td><td>未使用</td><td>制造商的有序的生产流水线号</td></tr><tr><td>var_nbr</td><td>CHAR</td><td></td><td>未使用</td><td>可变的工程号</td></tr><tr><td>basic_nbr</td><td>CHAR</td><td></td><td>未使用</td><td>基本工程号</td></tr><tr><td>serial_nbr</td><td>CHAR</td><td></td><td>未使用</td><td>固定ID号</td></tr><tr><td>registration_nbr</td><td>CHAR</td><td></td><td>未使用</td><td>尾号</td></tr></table>

图例

注1：对于飞机，MSM数据库中所表示的每一个CEC号都与该表中的一行相对应。每行都有一个唯一的有效键值（即一个CEC)，并指出一个唯一的MASK POSITION_NBR值，该值是在数据库创建时随机分配的。  
注2：对于发动机，MSM数据库中所表示的每个不同型号代码都与该表中的一行相对应。每行都有一个唯一的有效键值(即一个型号代码)，并指出一个唯一的MASK POSITION_NBR值，该值是在数据库创建时随机分配的。

# 3 目录表

该表用于存储所有飞机维修和发动机大修手册文件的目录。目录表设计成为可采用一条SFQL查询语句生成可访问文本条目的方式，这样可使目录的生成比较容易。这包括针对表中每个条目的摘要以及对包含实际信息的文件表的一个链接。

表 4-3-2.4 目录表  

<table><tr><td>栏名称</td><td>类型</td><td>飞机标记</td><td>发动机标记</td><td>描述</td></tr><tr><td>CONTENTS_ID*</td><td>INT</td><td>NA</td><td>NA</td><td>分配的唯一行标识符</td></tr><tr><td>@GEN.DOCS.DOC_ID**</td><td>INT</td><td>NA</td><td>NA</td><td>文件 ID。参考通用纲要模型中的 Doc 表[参见本文 4-3-1.7.1]</td></tr><tr><td>entry_sequence_nbr**</td><td>INT</td><td>NA</td><td>NA</td><td>用于放置条目的编号,利用该编号使条目的排列与目录中的 DOC_ID 的顺序完全相同,该编号从1开始</td></tr><tr><td>entry_table_name</td><td>CHAR</td><td>NA</td><td>NA</td><td>该条目指向的 MSM 纲要模型表的名称</td></tr><tr><td>entry_key_name</td><td>CHAR</td><td>NA</td><td>NA</td><td>主关键字的栏名称。参考技术要求,entry_table 有唯一的主关键字栏。</td></tr><tr><td>@ENTRY_KEY_ID</td><td>INT</td><td>NA</td><td>NA</td><td>标识内容文本的主关键字值</td></tr><tr><td>effectivity_mask</td><td>BITFIELD</td><td>NA</td><td>NA</td><td>表示可用有效性的模板(在数据库准备阶段分配)</td></tr><tr><td>effectivity_info</td><td>TEXT</td><td></td><td></td><td>适用于飞机/发动机的有效性信息</td></tr><tr><td>FM_Division_Name</td><td>CHAR</td><td>NA</td><td>NA</td><td>当条目是前页的分段时使用</td></tr><tr><td>entry_level</td><td>INT</td><td>NA See Note 1</td><td>NA</td><td>表中的层次结构级别,其中1为最高级别</td></tr><tr><td>@parent_ID</td><td>INT</td><td>NA</td><td>NA</td><td>父条目的content_id。如果没有父条目(entry_level=1),则PARENT_ID 值为 NULL</td></tr><tr><td>entry_text</td><td>TEXT</td><td>&lt; title &gt; or &lt;TOC&gt;</td><td>&lt; title &gt;</td><td>TOC条目</td></tr><tr><td>entry_startoff</td><td>INT</td><td>NA</td><td>NA</td><td>通用纲要模型中的Doc表[参见本文4-3-1.7.1]中描述的entry_text栏起始的相对位置</td></tr><tr><td>entry_endoff</td><td>INT</td><td>NA</td><td>NA</td><td>通用纲要模型中的Doc表[参见本文4-3-1.7.1]中描述的entry_text栏结束的相对位置</td></tr><tr><td>key_code</td><td>CHAR</td><td>&lt;?key&gt;</td><td>&lt;?key&gt;</td><td>在文件实例中唯一的一个位置标识(标识符)</td></tr><tr><td>chapter_nbr</td><td>CHAR</td><td>&lt;?chapnbr&gt;</td><td>&lt;?chapnbr&gt;</td><td>章号</td></tr><tr><td>section_nbr</td><td>CHAR</td><td>&lt;?sectnbr&gt;</td><td>&lt;?sectnbr&gt;</td><td>节号</td></tr><tr><td>subject_nbr</td><td>CHAR</td><td>&lt;?subjnbr&gt;</td><td>&lt;?subjnbr&gt;</td><td>标题号</td></tr><tr><td>pageblock_nbr</td><td>CHAR</td><td>&lt;?pgblknbr&gt;</td><td>&lt;?pgblknbr&gt;</td><td>页号组编号</td></tr><tr><td>config_nbr</td><td>CHAR</td><td>&lt;?confnbr&gt;</td><td>&lt;?confnbr&gt;</td><td>标识一个页号组的一个唯一构型</td></tr><tr><td>breakout_nbr</td><td>CHAR</td><td>Not Used</td><td>&lt;?reaknbr&gt;</td><td>标识一个页号组的分部分。</td></tr><tr><td>airline_unique_code</td><td>CHAR</td><td>&lt;?alunqi&gt;</td><td>&lt;?alunqi&gt;</td><td>航空公司唯一标识符</td></tr><tr><td>variant_nbr</td><td>CHAR</td><td>&lt;?varnbr&gt;</td><td>&lt;?varnbr&gt;</td><td>差异号</td></tr><tr><td>config_letter</td><td>CHAR</td><td>&lt;?confltr&gt;</td><td>&lt;?confltr&gt;</td><td>构型文字</td></tr><tr><td>sequence_nbr</td><td>CHAR</td><td>&lt;?seq&gt;</td><td>&lt;?seq&gt;</td><td>顺序号</td></tr><tr><td>function_code</td><td>CHAR</td><td>&lt;?func&gt;</td><td>&lt;?func&gt;</td><td>功能代码</td></tr><tr><td>revision_date</td><td>DATE</td><td>&lt;?revdate&gt;</td><td>&lt;?revdate&gt;</td><td>更改日期</td></tr></table>

注1：这是一个在飞机手册中如何使用entry_level的实例。  

<table><tr><td>entry_table_name</td><td>entry_level</td></tr><tr><td>前页</td><td>1</td></tr><tr><td>章</td><td>1</td></tr><tr><td>节</td><td>2</td></tr><tr><td>标题</td><td>3</td></tr><tr><td>页号组</td><td>4</td></tr><tr><td>任务</td><td>5</td></tr></table>

# 4 更改提要表

该表用于返回反映修订中更改的更改提要信息。

表 4-3-2.5 更改提要表  

<table><tr><td>栏名称</td><td>类型</td><td>飞机标记</td><td>发动机标记</td><td>描述</td></tr><tr><td>HIGHLIGHTS_ID*</td><td>INT</td><td>NA</td><td>NA</td><td>分配的唯一行标识符</td></tr><tr><td>entry_table_name</td><td>CHAR</td><td>NA</td><td>NA</td><td>该条目指向的MSM纲要模型中表的名称</td></tr><tr><td>entry_key_name</td><td>CHAR</td><td>NA</td><td>NA</td><td>主关键字的栏名称</td></tr><tr><td>@ENTRY_KEY_ID</td><td>INT</td><td>NA</td><td>NA</td><td>主关键字值，用以标识更改提要适用的文件单元</td></tr><tr><td>@GEN.DOCS.DOC_ID</td><td>INT</td><td>NA</td><td>NA</td><td>文件ID。参考通用纲要模型中(GEN)中的Doc表</td></tr><tr><td>effectivity_mask</td><td>BITFIELD</td><td>NA</td><td>NA</td><td>表示适用的有效性的模板</td></tr><tr><td>effectivity_info</td><td>TEXT</td><td>-effect&gt;</td><td>-effect&gt;</td><td>飞机/发动机的有效性信息</td></tr><tr><td>chapter_nbr</td><td>CHAR</td><td>&lt;? chapnbr&gt;</td><td>&lt;? chapnbr&gt;</td><td>章号</td></tr><tr><td>section_nbr</td><td>CHAR</td><td>&lt;? sectnbr&gt;</td><td>&lt;? sectnbr&gt;</td><td>节号</td></tr><tr><td>subject_nbr</td><td>CHAR</td><td>&lt;? subjnbr&gt;</td><td>&lt;? subjnbr&gt;</td><td>标题号</td></tr><tr><td>pageblock_nbr</td><td>CHAR</td><td>&lt;?pgblknbr&gt;</td><td>&lt;?pgblknbr&gt;</td><td>页号组号</td></tr><tr><td>config_nbr</td><td>CHAR</td><td>&lt;? confnbr&gt;</td><td>&lt;? confnbr&gt;</td><td>标识页号组的一个唯一构型</td></tr><tr><td>breakout_nbr</td><td>CHAR</td><td>Not Used</td><td>?breaknbr&gt;</td><td>标识一个页号组的子部分</td></tr><tr><td>airline_unique_code</td><td>CHAR</td><td>&lt;? alunqi&gt;</td><td>&lt;? alunqi&gt;</td><td>航空公司唯一标识符</td></tr><tr><td>variant_nbr</td><td>CHAR</td><td>&lt;? varnbr&gt;</td><td>&lt;? varnbr&gt;</td><td>差异号</td></tr><tr><td>config_letter</td><td>CHAR</td><td>&lt;? confltr&gt;</td><td>&lt;? confltr&gt;</td><td>构型文字</td></tr><tr><td>sequence_nbr</td><td>CHAR</td><td>&lt;? seq&gt;</td><td>&lt;? seq&gt;</td><td>顺序号</td></tr><tr><td>function_code</td><td>CHAR</td><td>&lt;? func&gt;</td><td>&lt;? func&gt;</td><td>功能代码</td></tr><tr><td>graphic_title</td><td>TEXT</td><td>&lt;title&gt;</td><td>&lt;title&gt;</td><td>当一幅图形或图页为更改目标时使用</td></tr><tr><td>sheet_nbr</td><td>INT</td><td>&lt;sheet sheetnbr&gt;</td><td>&lt;sheet sheetnbr&gt;</td><td>在图形页为更改目标时使用</td></tr><tr><td>FM_Division_Name</td><td>CHAR</td><td>NA</td><td>NA</td><td>在FM为更改目标时使用</td></tr><tr><td>key_code</td><td>CHAR</td><td>&lt;? key&gt;</td><td>&lt;? key&gt;</td><td>文件实例中唯一的一个位置标识(标识符)</td></tr><tr><td>change_description</td><td>CHAR</td><td></td><td></td><td>描述修订过程中的更改</td></tr></table>

# 5 章表

该表用于返回一个或多个手册的章信息。一个章的全部文本用一个给定行中的 chapter_text 栏来表示。

表 4-3-2.6 章列表  

<table><tr><td>栏名称</td><td>类型</td><td>飞机标记</td><td>发动机标记</td><td>描述</td></tr><tr><td>CHAPTER_ID*</td><td>INT</td><td>NA</td><td>NA</td><td>分配的唯一ID</td></tr><tr><td>chapter_nbr**</td><td>CHAR</td><td></td><td></td><td>章号</td></tr><tr><td>@GEN.DOCS.DOC_ID**</td><td>INT</td><td>NA</td><td>NA</td><td>文件ID。参考通用(GEN)纲要模型中的Doc表</td></tr><tr><td>effectivity_mask**</td><td>BITFIELD</td><td>NA</td><td>NA</td><td>表示可用有效性的模板(在数据库准备阶段被分配)</td></tr><tr><td>effectivity_info</td><td>TEXT</td><td></td><td></td><td>飞机/发动机的有效性信息</td></tr><tr><td>revision_date</td><td>DATE</td><td></td><td></td><td>更改日期</td></tr><tr><td>key_code</td><td>CHAR</td><td></td><td></td><td>文件实例中唯一的一个位置标识(标识符)</td></tr><tr><td>seq_nbr</td><td>INT</td><td>NA</td><td>NA</td><td>资料中行的逻辑顺序</td></tr><tr><td>chapter_title</td><td>TEXT</td><td></td><td></td><td>章标题</td></tr><tr><td>chapter_text</td><td>TEXT</td><td></td><td></td><td>一章的所有SGML片段</td></tr><tr><td>chapter_startoff</td><td>INT</td><td>NA</td><td>NA</td><td>通用纲要模型中的Doc表[参见本文4-3-1.7.1]中描述的chapter_text栏起始的相对位置</td></tr><tr><td>chapter_endoff</td><td>INT</td><td>NA</td><td>NA</td><td>通用纲要模型中的Doc表[参见本文4-3-1.7.1]中描述的chapter_text栏结束的相对位置</td></tr></table>

# 6 节表

该表用于返回一个或多个手册的节信息。一节中的全部文本用一个给定行中的section_text栏来表示。

表4-3-2.6 节表  

<table><tr><td>栏名称</td><td>类型</td><td>飞机标记</td><td>发动机标记</td><td>描述</td></tr><tr><td>SECTION_ID*</td><td>INT</td><td>NA</td><td>NA</td><td>分配的唯一ID</td></tr><tr><td>section_nbr**</td><td>CHAR</td><td></td><td></td><td>节号</td></tr><tr><td>@CHAPTER.CHAPTER_ID**</td><td>INT</td><td>NA</td><td>NA</td><td>参考章表</td></tr><tr><td>@GEN.DOCS.DOC_ID**</td><td>INT</td><td>NA</td><td>NA</td><td>文件ID。通用纲要模型中(GEN)中的Doc表的次关键字</td></tr><tr><td>chapter_nbr</td><td>CHAR</td><td></td><td></td><td>章号</td></tr><tr><td>revision_date</td><td>DATE</td><td></td><td></td><td>更改日期</td></tr><tr><td>key_code</td><td>CHAR</td><td></td><td></td><td>文件实例中唯一的一个位置标识(标识符)</td></tr><tr><td>seq_nbr</td><td>INT</td><td>NA</td><td>NA</td><td>资料中行的逻辑顺序</td></tr><tr><td>section_title</td><td>TEXT</td><td>&lt;title&gt;</td><td>&lt;title&gt;</td><td>节标题</td></tr><tr><td>section_text</td><td>TEXT</td><td>&lt;section&gt;</td><td>&lt;section&gt;</td><td>一节的所有SGML片段</td></tr><tr><td>section_startoff</td><td>INT</td><td>NA</td><td>NA</td><td>通用纲要模型中的Doc表[参见本文4-3-1.7.1]中描述的section_text栏起始的相对位置</td></tr><tr><td>section_endoff</td><td>INT</td><td>NA</td><td>NA</td><td>通用纲要模型中的Doc表[参见本文4-3-1.7.1]中描述的section_text栏结束的相对位置</td></tr></table>

# 7 标题表

该表用于返回一个或多个手册的标题信息。一个标题下的全部文本用一个给定行中的 subject_text 栏来表示。

表4-3-2.8 标题表  

<table><tr><td>栏名称</td><td>类型</td><td>飞机标记</td><td>发动机标记</td><td>描述</td></tr><tr><td>SUBJECT_ID*</td><td>INT</td><td>NA</td><td>NA</td><td>分配的唯一ID</td></tr><tr><td>subject_nbr**</td><td>CHAR</td><td></td><td></td><td>标题号</td></tr><tr><td>@SECTION SECTION_ID**</td><td>INT</td><td>NA</td><td>NA</td><td>参考节表</td></tr><tr><td>@GEN.DOCS.DOC_ID**</td><td>INT</td><td>NA</td><td>NA</td><td>文件ID。参考通用(GEN)纲要模型中的Doc表[参见本文4-3-1.7.1]。</td></tr><tr><td>chapter_nbr&#x27;</td><td>CHAR</td><td></td><td></td><td>章号</td></tr><tr><td>section_nbr</td><td>CHAR</td><td></td><td></td><td>节号</td></tr><tr><td>revision_date</td><td>DATE</td><td></td><td></td><td>更改日期</td></tr><tr><td>key_code</td><td>CHAR</td><td></td><td></td><td>文件实例中唯一的一个位置标识(标识符)</td></tr><tr><td>seq_nbr</td><td>INT</td><td>NA</td><td>NA</td><td>资料中行的逻辑顺序</td></tr><tr><td>subject_title</td><td>TEXT</td><td></td><td></td><td>标题标题</td></tr><tr><td>subject_text</td><td>TEXT</td><td></td><td></td><td>一个标题的所有SGML片段</td></tr><tr><td>subject_startoff</td><td>INT</td><td>NA</td><td>NA</td><td>通用纲要模型中的Doc表[参见本文4-3-1.7.1]中描述的 subject_text 栏起始的相对位置</td></tr><tr><td>subject_endoff</td><td>INT</td><td>NA</td><td>NA</td><td>通用纲要模型中的Doc表[参见本文4-3-1.7.1]中描述的 subject_text 栏结束的相对位置</td></tr></table>

# 8 页号组表

该表包含一个或多个手册的页号组的信息。一个页号组中的全部文本用一个给定行中的pageblock_text栏来表示。

表 4-3-2.9 页号组表  

<table><tr><td>栏名称</td><td>类型</td><td>飞机标记</td><td>发动机标记</td><td>描述</td></tr><tr><td>PAGEBLOCK_ID*</td><td>INT</td><td>NA</td><td>NA</td><td>分配的唯一ID</td></tr><tr><td>pageblock_nbr**</td><td>CHAR</td><td>&lt;pgblkpgblknbr&gt;</td><td>&lt;pgblkpgblknbr&gt;</td><td>页号组号</td></tr><tr><td>breakout_nbr**</td><td>CHAR</td><td>Not Used</td><td>&lt;pgblkbreaknbr&gt;</td><td>标识一个页号组的子部分。</td></tr><tr><td>config_nbr**</td><td>CHAR</td><td>&lt;pgblkconfnbr&gt;</td><td>&lt;pgblkconfnbr&gt;</td><td>标识一个页号组的一个唯一构型</td></tr><tr><td>@SUBJECTSUBJECT_ID**</td><td>INT</td><td>NA</td><td>NA</td><td>参考标题表</td></tr><tr><td>effectivity_mask**</td><td>BITFIELD</td><td>NA</td><td>NA</td><td>表示适用的有效性的模板(在数据库准备阶段被分配)</td></tr><tr><td>@GEN.DOCS.DOC_ID</td><td>INT</td><td>NA</td><td>NA</td><td>文件ID。参考通用(GEN)纲要模型中的Doc表[参见4-3-1.7.1]。</td></tr><tr><td>effectivity_info</td><td>TEXT</td><td>-effect&gt;</td><td>-effect&gt;</td><td>飞机/发动机的有效性信息</td></tr><tr><td>revision_date</td><td>DATE</td><td>&lt;pgblkrevdate&gt;</td><td>&lt;pgblkrevdate&gt;</td><td>更改日期</td></tr><tr><td>key_code</td><td>CHAR</td><td>&lt;pgblk key&gt;</td><td>&lt;pgblk key&gt;</td><td>文件实例中唯一的一个位置标识(标识符)</td></tr><tr><td>chapter_nbr</td><td>CHAR</td><td>&lt;pgblkchapnbr&gt;</td><td>&lt;pgblkchapnbr&gt;</td><td>章号</td></tr><tr><td>section_nbr</td><td>CHAR</td><td>&lt;pgblksectnbr&gt;</td><td>&lt;pgblksectnbr&gt;</td><td>节号</td></tr><tr><td>subject_nbr</td><td>CHAR</td><td>&lt;pgblksubjnbr&gt;</td><td>&lt;pgblksubjnbr&gt;</td><td>标题号</td></tr><tr><td>configuration_text</td><td>CHAR</td><td>Not Used</td><td>&lt;pgblkconfgxt&gt;</td><td>定义构型的文本</td></tr><tr><td>seq_nbr</td><td>INT</td><td>NA</td><td>NA</td><td>资料中行的逻辑顺序</td></tr><tr><td>pageblock_title</td><td>TEXT</td><td>&lt;title&gt;</td><td>&lt;title&gt;</td><td>页号组标题</td></tr><tr><td>pageblock_fml_text</td><td>TEXT</td><td>&lt;pbfmatr&gt;</td><td>&lt;pbfmatr&gt;</td><td>页号组的前页内容</td></tr><tr><td>pageblock_text</td><td>TEXT</td><td>&lt;pgblk&gt;</td><td>&lt;pgblk&gt;</td><td>一个页号组的所有SGML片段</td></tr><tr><td>pageblock_startoff</td><td>INT</td><td>NA</td><td>NA</td><td>通用纲要模型中的Doc表[参见本文4-3-1.7.1]中描述的pageblock_text栏起始的相对位置</td></tr><tr><td>pageblock_endoff</td><td>INT</td><td>NA</td><td>NA</td><td>通用纲要模型中的Doc表[参见本文4-3-1.7.1]中描述的pageblock_text栏结束的相对位置</td></tr></table>

# 9 任务表

该表包含一个或多个手册的任务的信息。一个任务中的全部文本用一个给定行中的 task.tex 栏来表示。

表4-3-2-10 任务表  

<table><tr><td>栏名称</td><td>类型</td><td>飞机标记</td><td>发动机标记</td><td>描述</td></tr><tr><td>TASK_ID*</td><td>INT</td><td>NA</td><td>NA</td><td>分配的唯一ID</td></tr><tr><td>function_code**</td><td>CHAR</td><td>&lt;task func&gt;</td><td>&lt;task func&gt;</td><td>功能代码</td></tr><tr><td>sequence_nbr**</td><td>CHAR</td><td>&lt;task seq&gt;</td><td>&lt;task seq&gt;</td><td>顺序号</td></tr><tr><td>airline_unique_code**</td><td>CHAR</td><td>&lt;task alunqi&gt;</td><td>&lt;task alunqi&gt;</td><td>航空公司唯一标识符</td></tr><tr><td>variant_nbr**</td><td>CHAR</td><td>&lt;task varnbr&gt;</td><td>&lt;task varnbr&gt;</td><td>标识任务的差异</td></tr><tr><td>config_letter**</td><td>CHAR</td><td>&lt;task confltr&gt;</td><td>&lt;task confltr&gt;</td><td>任务构型文字一部分AMTOSS代码</td></tr><tr><td>@PAGEBLOCK.PAGEBLOC_K_ID**</td><td>INT</td><td>NA</td><td>NA</td><td>参考页号组表</td></tr><tr><td>effectivity_mask**</td><td>BITFIELD</td><td>NA</td><td>NA</td><td>表示适用的有效性模板(在数据库准备阶段被分配)</td></tr><tr><td>@GEN.DOCS.DOC_ID</td><td>INT</td><td>NA</td><td>NA</td><td>文件ID。参考通用(GEN)纲要模型中的Doc表[参见本文4-3-1.7.1]</td></tr><tr><td>effectivity_info</td><td>TEXT</td><td>-effect&gt;</td><td>-effect&gt;</td><td>飞机/发动机的有效性信息</td></tr><tr><td>chapter_nbr</td><td>CHAR</td><td>&lt;task chapnbr&gt;</td><td>&lt;task chapnbr&gt;</td><td>章号</td></tr><tr><td>section_nbr</td><td>CHAR</td><td>&lt;task sectnbr&gt;</td><td>&lt;task sectnbr&gt;</td><td>节号</td></tr><tr><td>subject_nbr</td><td>CHAR</td><td>&lt;task subjnbr&gt;</td><td>&lt;task subjnbr&gt;</td><td>标题号</td></tr><tr><td>pageblock_nbr</td><td>CHAR</td><td>&lt;task pgblknbr&gt;</td><td>&lt;task pgblknbr&gt;</td><td>页号组分组</td></tr><tr><td>config_nbr</td><td>CHAR</td><td>&lt;task con fnbr&gt;</td><td>&lt;task con fnbr&gt;</td><td>标识一个页号组的一个唯一构型</td></tr><tr><td>breakout_nbr</td><td>CHAR</td><td>Not Used</td><td>&lt;task breaknbr&gt;</td><td>标识一个页号组的子部分。</td></tr><tr><td>key_code</td><td>CHAR</td><td>&lt;task key&gt;</td><td>&lt;task key&gt;</td><td>文件实例中唯一的一个位置标识(标识符)</td></tr><tr><td>revision_date</td><td>DATE</td><td>&lt;task revdate&gt;</td><td>&lt;task revdate&gt;</td><td>更改日期</td></tr><tr><td>configuration_text</td><td>CHAR</td><td>Not Used</td><td>&lt;task config.txt&gt;</td><td>定义构型的文本</td></tr><tr><td>seq_nbr</td><td>INT</td><td>NA</td><td>NA</td><td>资料中行的逻辑顺序</td></tr><tr><td>task_title</td><td>TEXT</td><td>&lt;title&gt;</td><td>&lt;title&gt;</td><td>任务标题</td></tr><tr><td>task_fmt_text</td><td>TEXT</td><td>&lt;tfmatr&gt;</td><td>&lt;tfmatr&gt;</td><td>任务的前页内容</td></tr><tr><td>task_text</td><td>TEXT</td><td>&lt;task&gt;</td><td>&lt;task&gt;</td><td>一个任务的所有SGML片段</td></tr><tr><td>task_startoff</td><td>INT</td><td>NA</td><td>NA</td><td>通用纲要模型中的Doc表[参见本文4-3-1.7.1]中描述的task_text栏起始的相对位置</td></tr><tr><td>task_endoff</td><td>INT</td><td>NA</td><td>NA</td><td>通用纲要模型中的 Doc 表[参见本文 4-3-1.7.1]中描述的task_text栏结束的相对位置</td></tr></table>

图例

# 10 分任务表

该表包含一个或多个手册的分任务的信息。一个分任务的全部文本用一个给定行中的subtask_text栏来表示。

表 4-3-2.11 分任务表  

<table><tr><td>栏名称</td><td>类型</td><td>飞机标记</td><td>发动机标记</td><td>描述</td></tr><tr><td>SUBTASK_ID*</td><td>INT</td><td>NA</td><td>NA</td><td>分配的唯一ID</td></tr><tr><td>airline_unique_code**</td><td>CHAR</td><td></td><td></td><td>航空公司唯一标识符</td></tr><tr><td>variant_nbr**</td><td>CHAR</td><td></td><td></td><td>标识任务的差异</td></tr><tr><td>config_letter**</td><td>CHAR</td><td></td><td></td><td>任务的构型号</td></tr><tr><td>sequence_nbr* *</td><td>CHAR</td><td></td><td></td><td>顺序号</td></tr><tr><td>function_code**</td><td>CHAR</td><td></td><td></td><td>功能代码</td></tr><tr><td>@TASK_TASK_ID**</td><td>INT</td><td>NA</td><td>NA</td><td>参考任务表</td></tr><tr><td>effectivity_mask**</td><td>BITFIELD</td><td>NA</td><td>NA</td><td>表示适用的有效性模板(在数据库准备阶段被分配)</td></tr><tr><td>@GEN.DOCS.DOC_ID</td><td>INT</td><td>NA</td><td>NA</td><td>文件ID。参考通用(GEN)纲要模型中的Doc表[参见本文4-3-1.7.1]</td></tr><tr><td>effectivity_info</td><td>TEXT</td><td></td><td></td><td>飞机/发动机的有效性信息</td></tr><tr><td>chapter_nbr</td><td>CHAR</td><td></td><td></td><td>章号</td></tr><tr><td>section_nbr</td><td>CHAR</td><td></td><td></td><td>节号</td></tr><tr><td>subject_nbr</td><td>CHAR</td><td></td><td></td><td>标题号</td></tr><tr><td>pageblock_nbr</td><td>CHAR</td><td></td><td></td><td>页号组号</td></tr><tr><td>config_nbr</td><td>CHAR</td><td></td><td></td><td>标识一个页号组的一个唯一构型</td></tr><tr><td>key_code</td><td>CHAR</td><td></td><td></td><td>在文件实例中唯一的一个位置标识(标识符)</td></tr><tr><td>revision_date</td><td>DATE</td><td></td><td></td><td>更改日期</td></tr><tr><td></td><td></td><td>revdate&gt;</td><td>revdate&gt;</td><td></td></tr><tr><td>seq_nbr</td><td>INT</td><td>NA</td><td>NA</td><td>资料中行的逻辑顺序</td></tr><tr><td>subtask_title</td><td>TEXT</td><td>Not Used</td><td></td><td>分任务标题</td></tr><tr><td>subtask_text</td><td>TEXT</td><td></td><td></td><td>一个分任务的所有SGML片段</td></tr><tr><td>subtask_startoff</td><td>INT</td><td>NA</td><td>NA</td><td>通用纲要模型中的Doc表[参见本文4-3-1.7.1]中描述的subtask_text栏起始的相对位置</td></tr><tr><td>subtask_endoff</td><td>INT</td><td>NA</td><td>NA</td><td>通用纲要模型(GEN)中的Doc表中描述的subtask_text栏起始的相对位置</td></tr></table>

# 11 图形表

该表包含飞机维修和发动机大修手册中图形的信息。图形页的二进制影像可在图页表中查到。

表 4-3-2.12 图形表  

<table><tr><td>栏名称</td><td>类型</td><td>飞机标记</td><td>发动机标记</td><td>描述</td></tr><tr><td>GRAPHIC_ID*</td><td>INT</td><td>NA</td><td>NA</td><td>分配的唯一ID</td></tr><tr><td>key_code**</td><td>CHAR</td><td>&lt;graphic key&gt;</td><td>&lt;graphic key&gt;</td><td>图形的唯一标识符</td></tr><tr><td>@GEN.DOCS.DOC_ID**</td><td>INT</td><td>NA</td><td>NA</td><td>文件ID。参考通用(GEN)纲要模型中的Doc表[参见本文4-3-1.7.1]</td></tr><tr><td>effectivity_mask</td><td>BITFIELD</td><td>NA</td><td>NA</td><td>表示适用的有效性模板(在数据库准备阶段被分配)</td></tr><tr><td>effectivity_info</td><td>TEXT</td><td>-effect&gt;</td><td>-effect&gt;</td><td>飞机/发动机的有效性信息</td></tr><tr><td>graphic_title</td><td>TEXT</td><td>&lt;title&gt;</td><td>&lt;title&gt;</td><td>图形的标题</td></tr><tr><td>sheet_count</td><td>INT</td><td>NA</td><td>NA</td><td>图形中的图页编号</td></tr><tr><td>revision_date</td><td>DATE</td><td>&lt;graphic revdate&gt;</td><td>&lt;graphic revdate&gt;</td><td>更改日期</td></tr><tr><td>seq_nbr</td><td>INT</td><td>NA</td><td>NA</td><td>资料中行的逻辑顺序</td></tr><tr><td>graphic_text</td><td>TEXT</td><td>&lt;graphic&gt;</td><td>&lt;graphic&gt;</td><td>图形编号的所有SGML片段</td></tr></table>

图例

# 12 图页表

该表包含飞机维修和发动机大修手册中图形的图页，并显示它们与该图形的关系。示图可按 ATA 标准格式根据 sheet_bin 栏检索，并可选择根据 file_name 栏中显示的文件来检索。

表4-3-2.13 图页表  

<table><tr><td>栏名称</td><td>类型</td><td>飞机标记</td><td>发动机标记</td><td>描述</td></tr><tr><td>SHEET_ID*</td><td>INT</td><td>NA</td><td>NA</td><td>分配的唯一ID</td></tr><tr><td>@GRAPHIC.GRAPHIC_ID**</td><td>INT</td><td>NA</td><td>NA</td><td>参考图形表</td></tr><tr><td>sheet_nbr**</td><td>INT</td><td></td><td></td><td>父图形中该图页的顺序号</td></tr><tr><td>key_code**</td><td>CHAR</td><td></td><td></td><td>图页的唯一标识符</td></tr><tr><td>@GEN.DOCS.DOC_ID* *</td><td>INT</td><td>NA</td><td>NA</td><td>文件ID。参考通用(GEN)纲要模型中的Doc表[参见本文4-3-1.7.1]</td></tr><tr><td>EFFECTIVITY_MASK</td><td>BITFIEL D</td><td>NA</td><td>NA</td><td>表示适用的有效性的模板(在数据库准备阶段被分配)</td></tr><tr><td>effectivity_info</td><td>TEXT</td><td></td><td></td><td>飞机/发动机的有效性信息</td></tr><tr><td>graphic_title</td><td>TEXT</td><td></td><td></td><td>该图页的父图形标题</td></tr><tr><td>sheet_title</td><td>TEXT</td><td></td><td></td><td>图页标题</td></tr><tr><td>sheet_type_code</td><td>CHAR</td><td>NA</td><td>NA</td><td>标识图形编码格式</td></tr><tr><td>sheet_text</td><td>TEXT</td><td></td><td></td><td>一个图页编号的所有SGML片段</td></tr><tr><td>revision_date</td><td>DATE</td><td></td><td></td><td>更改日期</td></tr><tr><td>sheet_bin</td><td>GRA-PHIC</td><td>NA</td><td>NA</td><td>二进制编码的图形</td></tr><tr><td>file_name</td><td>CHAR</td><td>NA</td><td>NA</td><td>包含图形的可选文件名</td></tr></table>

# 4-3-3 图解零件目录(IPC)纲要模型

# 1 前言

本文件与 ATA 通用纲要模型 ([参见本文 4-3-1]) 共同提供了适用于飞机和发动机示图零件目录手册检索的纲要模型。该纲要模型称为 “IPC” 纲要模型, 它属于 “ATA 维修” 类。

# 2 Front_Matter(前页)表

该表包含文件的前页。它将前页划分成若干部分，其中，division_name栏指出了DTD标记，按照这些标记可导出前页。

表4-3-3.1 前页表  

<table><tr><td>栏名</td><td>类型</td><td>飞机标记</td><td>发动机标记</td><td>描述</td></tr><tr><td>FRONT_MATTER_ID*</td><td>INT</td><td>NA</td><td>NA</td><td>分配的唯一ID</td></tr><tr><td>@GEN.DOCS.DOC_ID**</td><td>INT</td><td>NA</td><td>NA</td><td>文件ID。参考通用(GEN)纲要模型中的Doc表[参见本文4-3-1.7.1]</td></tr><tr><td>division_name**</td><td>CHAR</td><td>见“标准分段名称”</td><td>见“标准分段名称”</td><td>正文前内容的分部(部分)的名称,标准名称在表2中给出</td></tr><tr><td>division_title</td><td>TEXT</td><td>&lt;title&gt;</td><td>&lt;title&gt;</td><td>分部标题</td></tr><tr><td>division_text</td><td>TEXT</td><td>见“标准分段名称”</td><td>见“标准分段名称”</td><td>分部的全部文本</td></tr><tr><td>division_startoff</td><td>INT</td><td>NA</td><td>NA</td><td>通用纲要模型中的Doc表[参见本文4-3-1.7.1]中描述的division_text栏起始的相对位置</td></tr><tr><td>division_endoff</td><td>INT</td><td>NA</td><td>NA</td><td>通用纲要模型中的Doc表[参见本文4-3-1.7.1]中描述的division_text栏结束的相对位置</td></tr></table>

表 4-3-3.2 标准分段名称  

<table><tr><td rowspan="2">分部名称</td><td colspan="2">分部正文</td><td rowspan="2">描述</td></tr><tr><td>飞机标记</td><td>发动机标记</td></tr><tr><td>INTRO</td><td></td><td></td><td>文件信息</td></tr><tr><td>ILLTECH</td><td></td><td>?</td><td>文件中使用的示图技术说明</td></tr><tr><td>EFFECT_X_REF</td><td></td><td></td><td>关于标识文件实例中的一个基本有效性组的不同方法以及这些方法如何相互联系的数据</td></tr><tr><td>STATION_DIAGRAM</td><td></td><td>Not Used未使用</td><td>描述飞机结构部分的框图</td></tr><tr><td>ZONE_DIAGRAMS</td><td></td><td>Not Used未使用</td><td>描述飞机的主要装配件和分段并标识不同区域的框图</td></tr><tr><td>KITLST</td><td></td><td>Not Used</td><td>过滤器维修工具包清单</td></tr><tr><td>VENDLIST</td><td></td><td></td><td>供应商清单</td></tr><tr><td>SB_LIST</td><td></td><td></td><td>维护通报的当前合并状态的数据</td></tr><tr><td>MAJOR_DRAWING</td><td></td><td>Not Used未使用</td><td>主要的飞机部件/系统安装图的分类</td></tr><tr><td>GLOSSARY</td><td></td><td></td><td>术语和定义清单</td></tr><tr><td>OPLIST</td><td></td><td>&lt;optlist&gt;</td><td>可选的标准硬件清单</td></tr><tr><td>NUOPT</td><td></td><td>&lt;nuopt&gt;</td><td>标识可选的螺母</td></tr><tr><td>CLMPOPT</td><td></td><td>&lt;clmpopt&gt;</td><td>标识可选的卡箍</td></tr><tr><td>MATLIST</td><td></td><td>&lt;matlist&gt;</td><td>由材料成分代码,材料说明和各成分的百分比组成的一个清单</td></tr></table>

# 3 FM_Kitlist表

该表用于返回过滤器维修工具包的信息(只适用于机身)。

表4-3-3.3 FmKitlist表  

<table><tr><td>栏名</td><td>类型</td><td>飞机标记</td><td>发动机标记</td><td>描述</td></tr><tr><td>FM_KITLIST_ID*</td><td>INT</td><td>NA</td><td>未使用</td><td>分配的唯一行标识符</td></tr><tr><td>@GEN.DOCS.DOC_ID**</td><td>INT</td><td>NA</td><td>未使用</td><td>文件 ID。参考通用 (GEN) 纲要模型中的 Doc 表 [参见本文 4-3-1.7.1]</td></tr><tr><td>kit_code**</td><td>CHAR</td><td>&lt;kitnbr&gt;</td><td>未使用</td><td>工具包编号</td></tr><tr><td>kit_text</td><td>TEXT</td><td>&lt;fmktdata&gt;</td><td>未使用</td><td>过滤器维护工具包内容</td></tr></table>

# 4 Vendlist表

该表用于返回基于供应商代码的一个供应商地址。

表4-3-3.4 Vendlist表  

<table><tr><td>栏名</td><td>类型</td><td>飞机标记</td><td>发动机标记</td><td>描述</td></tr><tr><td>VEND_ID*</td><td>INT</td><td>NA</td><td>NA</td><td>分配的唯一行标识符</td></tr><tr><td>@GEN.DOCS.DOC_ID**</td><td>INT</td><td>NA</td><td>NA</td><td>文件 ID。参考通用 (GEN) 纲要模型中的 Doc 表 [参见本文 4-3-1.7.1]</td></tr><tr><td>vend_code**</td><td>CHAR</td><td>&lt;mfr&gt;</td><td>未使用</td><td>承包商代码</td></tr><tr><td>vend_text</td><td>TEXT</td><td>&lt; vendata&gt;</td><td>未使用</td><td>承包商代码和地址</td></tr></table>

# 5 Sblist表

该表用于返回维护通报的信息。

表4-3-3.5 Sblist表  

<table><tr><td>栏 名</td><td>类型</td><td>飞机标记</td><td>发动机标记</td><td>描 述</td></tr><tr><td>SBLIST_ID*</td><td>INT</td><td>NA</td><td>NA</td><td>分配的唯一行标识符</td></tr><tr><td>@GEN.DOCS.DOC_ID**</td><td>INT</td><td>NA</td><td>NA</td><td>文件 ID。参考通用 (GEN) 纲要模型中的 Doc 表 [参见本文 4-3-1.7.1]</td></tr><tr><td>sb_code**</td><td>CHAR</td><td></td><td></td><td>维护通报编号</td></tr><tr><td>md_code</td><td>CHAR</td><td></td><td>Not Used未使用</td><td>改型编号</td></tr><tr><td>coc_code</td><td>CHAR</td><td></td><td></td><td>COC 编号</td></tr><tr><td>sblist_text</td><td>TEXT</td><td></td><td></td><td>维护通报数据</td></tr></table>

# 6 有效性表

本表被当作该纲要模型中其它表的 EFFECTIVITY_MASK 栏中有效性信息编码的“关键字”来使用。对于数据库的 IPC 部分中所给出的每个不同的有效性值，在该表中都有一个行来描述。

表4-3-3.6 有效性表  

<table><tr><td>栏 名</td><td>类型</td><td>飞机标记</td><td>发动机 标记</td><td>描 述</td></tr><tr><td>effectivity_key*</td><td>CHAR</td><td>见注1</td><td>见注2</td><td>飞机用户的有效性代码或发动机的模型号</td></tr><tr><td>MASK POSITION_NBR**</td><td>INT</td><td>NA</td><td>NA</td><td>EFFECTIVITY_mask 中唯一的指定位置。通用纲要模型文件的第5节“EFFECTIVITY_MASK 中BITFIELD 的使用”中描述该编号的建立和使用</td></tr><tr><td>serial_nbr</td><td>CHAR</td><td></td><td>未使用</td><td>固定的ID号</td></tr><tr><td>registration_nbr</td><td>CHAR</td><td></td><td>未使用</td><td>尾翼号</td></tr><tr><td>basic_nbr</td><td>CHAR</td><td></td><td>未使用</td><td>基本工程号</td></tr><tr><td>var_nbr</td><td>CHAR</td><td></td><td>未使用</td><td>可变工程号</td></tr><tr><td>esn_nbr</td><td>CHAR</td><td></td><td>未使用</td><td>发动机装置号</td></tr><tr><td>fslg_nbr</td><td>CHAR</td><td></td><td>未使用</td><td>机身号</td></tr></table>

注1：对于机身，IPC数据库中所表示的每一个CEC号都与该表中的一行相对应。每行都有一个唯一的effectivity_key值(即一个CEC)，并给出一个唯一的MASK POSITION_NBR值，该值是在数据库创建时随机分配的。

注2：对于发动机，IPC数据库中所表示的每个不同型号代码都与该表中的一行相对应。每行都有一个唯一的effectivity_key值(即一个号型代码)，并且显示一个唯一的MASK POSITION_NBR值，该值是在数据库创建时随机分配的。

# 7 目录表

该表用于存储所有图解零件目录文件的目录。该表设计成为可使用一条SFQL查询语句生成可访问的文本条目的方式，这样使目录的生成比较容易。这包括表中每个条目的摘要以及对包含实际信息的文件表的一个链接。

表 4-3-3.7 目录表  

<table><tr><td>栏 名</td><td>类型</td><td>飞机标记</td><td>发动机
标记</td><td>描 述</td></tr><tr><td>CONTENTS_ID*</td><td>INT</td><td>NA</td><td>NA</td><td>分配的唯一行标识符</td></tr><tr><td>@GEN.DOCS.DOC_ID**</td><td>INT</td><td>NA</td><td>NA</td><td>文件 ID。参考通用 (GEN) 纲要模型 [参见本文 4-3-1.7.1] 中的 Doc 表</td></tr><tr><td>entry_sequence_nbr**</td><td>INT</td><td>NA</td><td>NA</td><td>用于排放条目的编号，利用该编号使条目的排列与目录中的 DOC_ID 的顺序完全相同，该编号从 1 开始</td></tr><tr><td>entry_table_name</td><td>CHAR</td><td>NA</td><td>NA</td><td>由该条目指向的纲要模型表名</td></tr><tr><td>entry_key_name</td><td>CHAR</td><td>NA</td><td>NA</td><td>主关键字的栏名称。参考技术要求，目录表有单一的主关键字栏</td></tr><tr><td>@ENTRY_KEY_ID</td><td>INT</td><td>NA</td><td>NA</td><td>标识内容文本的主关键字值</td></tr><tr><td>effectivity_mask</td><td>BITFIELD</td><td>NA</td><td>NA</td><td>表示适用的有效性模板(在数据库准备阶段分配)</td></tr><tr><td>effectivity_info</td><td>TEXT</td><td>-effect&gt;</td><td>-effect&gt;</td><td>该条目有效性信息的全部SGML片段</td></tr><tr><td>FM_Division_name</td><td>CHAR</td><td>NA</td><td>NA</td><td>当条目是前页的分部时使用</td></tr><tr><td>entry_level</td><td>INT</td><td>见飞机目录例子。</td><td>NA</td><td>表中的层次结构级别,其中1为最高级别</td></tr><tr><td>@parent_ID</td><td>INT</td><td>NA</td><td>NA</td><td>父条目的content_id。如果没有父条目(entry_level=1),则PARENT_ID值为NULL</td></tr><tr><td>entry_text</td><td>TEXT</td><td>NA</td><td>NA</td><td>TOC条目</td></tr><tr><td>entry_startoff</td><td>INT</td><td>NA</td><td>NA</td><td>通用纲要模型中的Doc表[参见本文4-3-1.7.1]中描述的entry_text栏起始的相对位置</td></tr><tr><td>entry_endoff</td><td>INT</td><td>NA</td><td>NA</td><td>通用纲要模型中的Doc表[参见本文4-3-1.7.1]中描述的entry_text栏结束的相对位置</td></tr><tr><td>key_code</td><td>CHAR</td><td>&lt;?key&gt;</td><td>&lt;?key&gt;</td><td>文件实例中唯一的一个位置标识(标识符)</td></tr><tr><td>chapter_nbr</td><td>CHAR</td><td>&lt;?chapnbr&gt;</td><td>&lt;?chapnbr&gt;</td><td>章号</td></tr><tr><td>section_nbr</td><td>CHAR</td><td>&lt;?sectnbr&gt;</td><td>&lt;?sectnbr&gt;</td><td>节号</td></tr><tr><td>unit_nbr</td><td>CHAR</td><td>&lt;?unitnbr&gt;</td><td>&lt;?unitnbr&gt;</td><td>单元号</td></tr><tr><td>figure_nbr</td><td>CHAR</td><td>&lt;?fignbr&gt;</td><td>&lt;?fignbr&gt;</td><td>图号</td></tr><tr><td>revision_date</td><td>DATE</td><td>&lt;?revdate&gt;</td><td>&lt;?revdate&gt;</td><td>更改日期</td></tr></table>

注：[表4-3-3.8]显示了在飞机手册中如何使用entry_level的一个例子。

图例

表 4-3-3.8 飞机目录实例  

<table><tr><td>entry_table_name</td><td>entry_level</td></tr><tr><td>前页</td><td>1</td></tr><tr><td>章</td><td>1</td></tr><tr><td>节</td><td>2</td></tr><tr><td>CSU图</td><td>3</td></tr></table>

# 8 章表

该表用于返回一个或多个手册的章信息。一个章的全部文本用一个给定行中的 chapter_text 栏来表示。

表4-3-3.9 章表  

<table><tr><td>栏 名</td><td>类型</td><td>飞机标记</td><td>发动机标记</td><td>描 述</td></tr><tr><td>CHAPTER_ID*</td><td>INT</td><td>NA</td><td>NA</td><td>分配的唯一标识符</td></tr><tr><td>chapter_nbr**</td><td>CHAR</td><td></td><td></td><td>ATA 章号</td></tr><tr><td>@GEN.DOCS.DOC_ID**.</td><td>INT</td><td>NA</td><td>NA</td><td>文件 ID。参考通用(GEN)纲要模型中的 Doc 表[参见本文 4-3-1.7.1]</td></tr><tr><td>revision_date</td><td>DATE</td><td></td><td></td><td>更改日期</td></tr><tr><td>key_code</td><td>CHAR</td><td></td><td></td><td>文件实例中唯一的一个位置标识(标识符)</td></tr><tr><td>seq_nbr</td><td>INT</td><td>NA</td><td>NA</td><td>数据中行的逻辑顺序</td></tr><tr><td>chapter_title</td><td>TEXT</td><td></td><td></td><td>章标题</td></tr><tr><td>chapter_text</td><td>TEXT</td><td></td><td></td><td>一个章的所有 SGML 片段</td></tr><tr><td>chapter_startoff</td><td>INT</td><td>NA</td><td>NA</td><td>通用纲要模型中的 Doc 表[参见本文 4-3-1.7.1]中描述的 chapter_text 栏起始的相对位置</td></tr><tr><td>chapter_endoff</td><td>INT</td><td>NA</td><td>NA</td><td>通用纲要模型中的 Doc 表[参见本文 4-3-1.7.1]中描述的 chapter_text 栏结束的相对位置</td></tr></table>

# 9 节表

该表用于返回一个或多个手册的节信息。一节的全部文本用一个给定行中的section_text栏来表示。

表 4-3-3.10 节标题  

<table><tr><td>栏 名</td><td>类型</td><td>飞机标记</td><td>发动机
标记</td><td>描 述</td></tr><tr><td>SECTION_ID*</td><td>INT</td><td>NA</td><td>NA</td><td>分配的唯一 ID</td></tr><tr><td>section_nbr**</td><td>CHAR</td><td>&lt;section
sectnbr&gt;</td><td>&lt;section
sectnbr&gt;</td><td>节号</td></tr><tr><td>@CHAPTER.CHAPTER_ID**</td><td>INT</td><td>NA</td><td>NA</td><td>参考章表</td></tr><tr><td>@GEN.DOCS.DOC_ID</td><td>INT</td><td>NA</td><td>NA</td><td>文件 ID。参考通用 (GEN) 纲要模型中的 Doc 表[参见本文 4-3-1.7.1]</td></tr><tr><td>chapter_nbr</td><td>CHAR</td><td>&lt;section
chapnbr&gt;</td><td>&lt;section
chapnbr&gt;</td><td>章号</td></tr><tr><td>revision_date</td><td>DATE</td><td>&lt;section
revdate&gt;</td><td>&lt;section
revdate&gt;</td><td>更改日期</td></tr><tr><td>key_code</td><td>CHAR</td><td>&lt;section
key&gt;</td><td>&lt;section
key&gt;</td><td>文件实例中唯一的一个位置标识(标识符)</td></tr><tr><td>seq_nbr</td><td>INT</td><td>NA</td><td>NA</td><td>数据中行的逻辑顺序</td></tr><tr><td>section_title</td><td>TEXT</td><td>&lt;title&gt;</td><td>&lt;title&gt;</td><td>节标题</td></tr><tr><td>section_text</td><td>TEXT</td><td></td><td></td><td>一个节的所有 SGML 片段</td></tr><tr><td>section_startoff</td><td>INT</td><td>NA</td><td>NA</td><td>通用纲要模型中的 Doc 表[参见本 文 4-3-1.7.1]中描述的 section_text 栏起始的相对位置</td></tr><tr><td>section_endoff</td><td>INT</td><td>NA</td><td>NA</td><td>通用纲要模型中的 Doc 表[参见本 文 4-3-1.7.1]中描述的 section_text 栏结束的相对位置</td></tr></table>

# 10 单元表

该表用于返回一个或多个手册的单元信息。一个单元的全部文本用一个给定行中的unit_text栏来表示。

表4-3-3.11 单元表  

<table><tr><td>栏 名</td><td>类型</td><td>飞机标记</td><td>发动机标记</td><td>描 述</td></tr><tr><td>UNIT_ID*</td><td>INT</td><td>NA</td><td>NA</td><td>分配的唯一ID</td></tr><tr><td>unit_nbr**</td><td>CHAR</td><td>&lt;unit unitnbr&gt;</td><td>&lt;unit unitnbr&gt;</td><td>单元号</td></tr><tr><td>@SECTION SECTION_ID**</td><td>INT</td><td>NA</td><td>NA</td><td>参考节表</td></tr><tr><td>section_nbr</td><td>CHAR</td><td>&lt;unit sectnbr&gt;</td><td>&lt;unit sectnbr&gt;</td><td>节号</td></tr><tr><td>chapter_nbr</td><td>CHAR</td><td>&lt;unit chapnbr&gt;</td><td>&lt;unit chapnbr&gt;</td><td>章号</td></tr><tr><td>@GEN.DOCS.DOC_ID</td><td>INT</td><td>NA</td><td>NA</td><td>文件ID。参考通用(GEN)纲要模型中的Doc表[参见本文4-3-1.7.1]</td></tr><tr><td>revision_date</td><td>DATE</td><td>&lt;unit revdate&gt;</td><td>&lt;unit revdate&gt;</td><td>更改日期</td></tr><tr><td>key_code</td><td>CHAR</td><td>&lt;unit key&gt;</td><td>&lt;unit key&gt;</td><td>文件实例中唯一的一个位置标识(标识符)</td></tr><tr><td>seq_nbr</td><td>INT</td><td>NA</td><td>NA</td><td>数据中行的逻辑顺序</td></tr><tr><td>unit_title</td><td>TEXT</td><td>&lt;title&gt;</td><td>&lt;title&gt;</td><td>单元标题。在飞机手册数据中是可选的(通常缺省)</td></tr><tr><td>unit_text</td><td>TEXT</td><td>&lt;unit&gt;</td><td>&lt;unit&gt;</td><td>一个单元的所有SGML片段</td></tr><tr><td>unit_startoff</td><td>INT</td><td>NA</td><td>NA</td><td>通用纲要模型中的Doc表[参见本文4-3-1.7.1]中描述的unit_text栏起始的相对位置</td></tr><tr><td>unit_endoff</td><td>INT</td><td>NA</td><td>NA</td><td>通用纲要模型中的Doc表[参见本文4-3-1.7.1]中描述的unit_text栏结束的相对位置</td></tr></table>

# 11 CSU图表

该表用于返回一个或者多个IPC的章一节一单元(CUS)图的信息。

表4-3-3.12 CSU图表  

<table><tr><td>栏 名</td><td>类型</td><td>飞机标记</td><td>发动机标记</td><td>描 述</td></tr><tr><td>CSUFIGURE_ID*</td><td>INT</td><td>NA</td><td>NA</td><td>分配的唯一ID</td></tr><tr><td>figure_nbr**</td><td>CHAR</td><td></td><td></td><td>图号</td></tr><tr><td>@UNIT.UNIT_ID**</td><td>INT</td><td>NA</td><td>NA</td><td>参考单元表</td></tr><tr><td>effectivity_mask**</td><td>BITFIELD</td><td>NA</td><td>NA</td><td>有效性标签</td></tr><tr><td>unit_nbr</td><td>CHAR</td><td></td><td></td><td>单元号</td></tr><tr><td>section_nbr</td><td>CHAR</td><td></td><td></td><td>节号</td></tr><tr><td>chapter_nbr</td><td>CHAR</td><td></td><td></td><td>章号</td></tr><tr><td>@GEN.DOCS.DOC_ID</td><td>INT</td><td>NA</td><td>NA</td><td>文件ID。参考通用(GEN)纲要模型中的Doc表[参见本文4-3-1.7.1]</td></tr><tr><td>revision_date</td><td>DATE</td><td></td><td></td><td>更改日期</td></tr><tr><td>key_code</td><td>CHAR</td><td></td><td></td><td>文件实例中唯一的一个位置标识(标识符)</td></tr><tr><td>seq_nbr</td><td>INT</td><td>NA</td><td>NA</td><td>数据中行的逻辑顺序</td></tr><tr><td>CSUFIGure_title</td><td>TEXT</td><td></td><td></td><td>图标题</td></tr><tr><td>CSUFIGure_text</td><td>TEXT</td><td></td><td></td><td>零件清单和相关示图</td></tr><tr><td>csufigure_startoff</td><td>INT</td><td>NA</td><td>NA</td><td>通用纲要模型中的Doc表[参见本文4-3-1.7.1]中描述的csufigure_text栏起始的相对位置</td></tr><tr><td>csufigure_endoff</td><td>INT</td><td>NA</td><td>NA</td><td>通用纲要模型中的Doc表[参见本文4-3-1.7.1]中描述的csufigure_text栏结束的相对位置</td></tr></table>

# 12 项目表

该表包含IPC CSU图的单独项目。

表 4-3-3.13 项目表  

<table><tr><td>栏 名</td><td>类型</td><td>飞机标记</td><td>发动机标记</td><td>描述</td></tr><tr><td>ITEM_ID*</td><td>INT</td><td>NA</td><td>NA</td><td>分配的唯一值</td></tr><tr><td>item_nbr**</td><td>CHAR</td><td>&lt;item itemnbr&gt;</td><td>&lt;item itemnbr&gt;</td><td>在图中的唯一标识符</td></tr><tr><td>@CSFIGURE.CSFIGURE_ID**</td><td>INT</td><td>NA</td><td>NA</td><td>在包含该项目的CSU图表中的图形ID</td></tr><tr><td>effectivity_mask</td><td>BITFIELD</td><td>NA</td><td>NA</td><td>表示适用的有效性模板</td></tr><tr><td>effectivity_info</td><td>TEXT</td><td>-effect&gt;</td><td>-effect&gt;</td><td>飞机/发动机的有效信息</td></tr><tr><td>chapter_nbr</td><td>CHAR</td><td>&lt;item chapnbr&gt;</td><td>&lt;item chapnbr&gt;</td><td>章号</td></tr><tr><td>section_nbr</td><td>CHAR</td><td>&lt;item sectnbr&gt;</td><td>&lt;item sectnbr&gt;</td><td>节号</td></tr><tr><td>unit_nbr</td><td>CHAR</td><td>&lt;item unitnbr&gt;</td><td>&lt;item unitnbr&gt;</td><td>单元号</td></tr><tr><td>figure_nbr</td><td>CHAR</td><td>&lt;item fignbr&gt;</td><td>&lt;item fignbr&gt;</td><td>图号</td></tr><tr><td>@GEN.DOCS.DOC_ID</td><td>INT</td><td>NA</td><td>NA</td><td>文件ID。参考通用(GEN)纲要模型中的Docs表[参见本文4-3-1.7.1]</td></tr><tr><td>revision_date</td><td>DATE</td><td>&lt;item revdate&gt;</td><td>&lt;item revdate&gt;</td><td>更改日期</td></tr><tr><td>key_code</td><td>CHAR</td><td>&lt;item key&gt;</td><td>&lt;item key&gt;</td><td>文件实例中唯一的一个位置标识(标识符)</td></tr><tr><td>seq_nbr</td><td>INT</td><td>NA</td><td>NA</td><td>数据中行的逻辑顺序</td></tr><tr><td>indenture</td><td>INT</td><td>&lt;itemindent&gt;</td><td>&lt;itemindent&gt;</td><td>标识装配结构中的位置</td></tr><tr><td>attaching_part</td><td>INT</td><td>&lt;item attach&gt;</td><td>&lt;item attach&gt;</td><td>标识该零件是否是附属连接件</td></tr><tr><td>illustrated</td><td>INT</td><td>&lt;item illusind&gt;</td><td>&lt;item illusind&gt;</td><td>标识项目是否在图上示出</td></tr><tr><td>manufacturer_code</td><td>CHAR</td><td>&lt;mfr&gt;</td><td>&lt;mfr&gt;</td><td>分配给零件制造商的5位数字代码</td></tr><tr><td>item_text</td><td>TEXT</td><td>&lt;item&gt;</td><td>&lt;item spec&gt;</td><td>一个包含在图内的特定项目的定义</td></tr><tr><td>item_startoff</td><td>INT</td><td>NA</td><td>NA</td><td>通用纲要模型中的Doc表[参见本文4-3-1.7.1]中描述的item_text栏起始的相对位置</td></tr><tr><td>item_endoff</td><td>INT</td><td>NA</td><td>NA</td><td>通用纲要模型中的Doc表[参见本文4-3-1.7.1]中描述的item_text栏结束的相对位置</td></tr><tr><td>@PART.PART_NBR</td><td>CHAR</td><td>&lt;pnr&gt;</td><td>&lt;pnr&gt;</td><td>零件号</td></tr></table>

# 13 零件表

该表包含 IPC 中参考的零件集合。

表4-3-3.14 零件表  

<table><tr><td>栏 名</td><td>类型</td><td>飞机标记</td><td>发动机标记</td><td>描 述</td></tr><tr><td>PART_ID*</td><td>INT</td><td>NA</td><td>NA</td><td>分配的唯一值</td></tr><tr><td>part_nbr**</td><td>CHAR</td><td>&lt;pnr&gt;</td><td>&lt;pnr&gt;</td><td>零件号</td></tr><tr><td>@GEN.DOCS.DOC_ID</td><td>INT</td><td>NA</td><td>NA</td><td>文件ID。参考通用(GEN)纲要模型中的Doc表[参见本文4-3-1.7.1]</td></tr><tr><td>Keyword</td><td>CHAR</td><td>&lt;kwd&gt;</td><td>&lt;kwd&gt;</td><td>由制造商定义的显示在零件号字段的条目名</td></tr><tr><td>manufacturer_code</td><td>CHAR</td><td>&lt;mfr&gt;</td><td>&lt;mfr&gt;</td><td>分配给零件制造商的5位数字代码</td></tr><tr><td>revision_date</td><td>DATE</td><td>&lt;pnrdatarevdate&gt;</td><td>&lt;itemrevdate&gt;</td><td>更改日期</td></tr><tr><td>key_code</td><td>CHAR</td><td>&lt;pnrdatakey&gt;</td><td>&lt;item key&gt;</td><td>文件实例中是唯一的一个位置标识(标识符)</td></tr><tr><td>seq_nbr</td><td>INT</td><td>NA</td><td>NA</td><td>资料中行的逻辑顺序</td></tr><tr><td>customer_nomen</td><td>TEXT</td><td>Not Used未使用</td><td>&lt;cusnom&gt;</td><td>由用户分配的名称术语</td></tr><tr><td>part_text</td><td>TEXT</td><td>&lt;pnrdata&gt;</td><td>&lt;part&gt;</td><td>零件号信息</td></tr><tr><td>part_startoff</td><td>INT</td><td>NA</td><td>NA</td><td>通用纲要模型中的Doc表[参见本文4-3-1.7.1]中描述的 part_text栏起始的相对位置</td></tr><tr><td>part_endoff</td><td>INT</td><td>NA</td><td>NA</td><td>通用纲要模型中的Doc表[参见本文4-3-1.7.1]中描述的 part_text栏结束的相对位置</td></tr><tr><td>airline_part_nbr</td><td>CHAR</td><td>&lt;alprtnbr&gt;</td><td>&lt;alprn&gt;</td><td>航空公司零件号</td></tr><tr><td>addtext</td><td>CHAR</td><td>未使用</td><td>&lt;adt&gt;</td><td>附加的描述性文本</td></tr></table>

# 14 项目详细信息表

该表包含了项目表中任意给定项目的详细内容。标准项目行类型值在表中给出。

表 4-3-3.15 详细项目表  

<table><tr><td>栏名</td><td>类型</td><td>飞机标记</td><td>发动机标记</td><td>描述</td></tr><tr><td>ITEM_DETAIL_ID*</td><td>INT</td><td>NA</td><td>NA</td><td>分配的唯一值</td></tr><tr><td>@ITEM_ID**</td><td>INT</td><td>NA</td><td>NA</td><td>参考项目表</td></tr><tr><td>item_line_type**</td><td>CHAR</td><td>见“标准项目行类型”</td><td>见“标准项目行类型”</td><td>Item_line_types之一</td></tr><tr><td>item_line_text</td><td>TEXT</td><td>见“标准项目行类型”</td><td>见“标准项目行类型”</td><td>Item_line_types的文本</td></tr></table>

表 4-3-3.16 标准项目行类型  

<table><tr><td rowspan="2">item_line_type</td><td colspan="2">item_line_text</td><td rowspan="2">描 述</td></tr><tr><td>飞机标记</td><td>发动机标记</td></tr><tr><td>descriptive_text</td><td></td><td>未使用</td><td>修改关键字名称的附加术语</td></tr><tr><td>equipment_identification</td><td></td><td>&lt;ein&gt;</td><td>分配给零件特殊用法的功能标识号</td></tr><tr><td>filterkeit</td><td></td><td>&lt;fmk&gt;</td><td>标识过滤器维修工具包编号的注释</td></tr><tr><td>incomplete_pnr</td><td></td><td></td><td>标识零件号未完全定义的条件</td></tr><tr><td>limited_opt_data</td><td></td><td></td><td>用特定限制规定标识可选零件的用法</td></tr><tr><td>modification_levels</td><td></td><td></td><td>标识一个给定项目适用的改型级别,这时,(改型)级别作为用零件号标识构型的必要补充部分</td></tr><tr><td>miscellaneous_text</td><td></td><td></td><td>各种附加信息</td></tr><tr><td>over_under Parts</td><td></td><td>未使用</td><td>标识大于或小于原始设计定义尺寸的零件</td></tr><tr><td>panel</td><td></td><td>未使用</td><td>标识检修口盖信息</td></tr><tr><td>restricted_opnote</td><td></td><td></td><td>对未经批准的双发动机操作延伸范围的项目进行标识的一条注意</td></tr><tr><td>replaced_inter_part</td><td></td><td>未使用</td><td>来自一个适用于一个机群的一个先前构型的零件</td></tr><tr><td>rework_variations</td><td></td><td></td><td>对IPC中显示的定义再加工/改型状态的图号的一个参考</td></tr><tr><td>service_bn_chgset</td><td></td><td>未使用</td><td>包括有效性的维护通报更改的分组</td></tr><tr><td>selective_from(note)</td><td></td><td></td><td>标识尺寸的上、下偏差范围分组以选择零件</td></tr><tr><td>stowed_information</td><td></td><td>未使用</td><td>标识装载在飞机上但未安装的零件</td></tr><tr><td>temporary_breakdown</td><td></td><td>未使用</td><td>标识IPC中的一个有效区域,该区域以一个临时单元为基础而被包括在IPC中,直到有效数据被接收和合并</td></tr><tr><td>temporary_opnote</td><td></td><td>未使用</td><td>对临时许可的双发动机操作延伸范围的项目进行标识的一条注释</td></tr><tr><td>used_on_assy_nbr</td><td></td><td></td><td>标识一个装配件,某零件安装在该装配件中,但并没有用于所有装配件(相同的)上</td></tr><tr><td>used_with_pnr</td><td></td><td></td><td>标识和零件号字段的零件号一起使用的零件</td></tr><tr><td>totalquantity</td><td></td><td></td><td>标识在完整的装配件中使用的主要零件的单位总数量</td></tr><tr><td>units_per_assy</td><td></td><td></td><td>在上一较高级装配件上的零件号的数量</td></tr><tr><td>replaced_by.note</td><td></td><td></td><td>与该零件可完全互换的其它零件</td></tr><tr><td>superceded_by.note</td><td></td><td></td><td>与该零件不能互换或单向交换的其它零件</td></tr><tr><td>service_btn_nbr</td><td></td><td></td><td>适用于该项目的维护通报号</td></tr><tr><td>etops_indicator</td><td></td><td></td><td>标识ETOPS授权的强制使用零件</td></tr><tr><td>interchangeable_data</td><td></td><td>未使用</td><td>合格的可交换数据</td></tr><tr><td>placard_content</td><td></td><td>未使用</td><td>布告内容</td></tr><tr><td>position_data</td><td></td><td>未使用</td><td>位置数据</td></tr><tr><td>sbdata_cmm</td><td></td><td>未使用</td><td>来自CMM的维护通报数据</td></tr><tr><td>config_cmm</td><td></td><td>未使用</td><td>来自CMM的构型更改数据</td></tr><tr><td>ext_ref</td><td></td><td></td><td>参考一个外部文件</td></tr><tr><td>int_ref</td><td></td><td></td><td>一个内部参考</td></tr><tr><td>select_from</td><td>未使用。</td><td></td><td>标识“选自”零件的总数</td></tr><tr><td>over_parts</td><td>未使用。</td><td></td><td>标识那些为达到修理目而用来替换原始零件的过尺寸零件</td></tr><tr><td>under_parts</td><td>未使用。</td><td></td><td>标识那些为达到修理目而用来替换原始零件的欠尺寸零件</td></tr><tr><td>alternate_pnr</td><td>未使用。</td><td></td><td>标识可在某个位置上使用的一个备用零件</td></tr><tr><td>usage_code</td><td>未使用。</td><td></td><td>定义一个零件模型或者可互换条件和限制的一个,两个或三个字母代码</td></tr><tr><td>computer_sware</td><td></td><td>未使用。</td><td>在硬件设备上使用的磁盘中所包含的软件</td></tr><tr><td>limited_opt_part</td><td></td><td>未使用。</td><td>标识限定的可选数据及与其相对应的限定可选零件</td></tr><tr><td>rework_spt</td><td></td><td>未使用。</td><td>标识支持维护通报或其它更改的再加工的零件</td></tr><tr><td>part_nbr</td><td></td><td>未使用。</td><td>零件号</td></tr><tr><td>manufacturer_code</td><td></td><td>未使用。</td><td>分配给该零件制造商的5位数字代码</td></tr><tr><td>rework</td><td>未使用。</td><td></td><td>表示可将该零件再加工成其它零件,或将其它零件再加工成该零件</td></tr></table>

# 15 零件详细信息表

该表包含了零件表中任意给定零件的详细内容。每个零件可能具有多个条目。part_detail_types 的标准命名在“标准零件详细类型”表中给出。

表4-3-3.17 Part_detail表  

<table><tr><td>栏名</td><td>类型</td><td>飞机标记</td><td>发动机标记</td><td>描述</td></tr><tr><td>PNRDETAIL_ID*</td><td>INT</td><td>NA</td><td>NA</td><td>分配的唯一值</td></tr><tr><td>@PNR_ID**</td><td>INT</td><td>NA</td><td>NA</td><td>参考零件表</td></tr><tr><td>part_detail_type**</td><td>CHAR</td><td>“标准项目行类型”</td><td>见“标准项目行类型”</td><td>根据表标识的 part_detail_types 之一</td></tr><tr><td>part_detail_text</td><td>TEXT</td><td>见“标准项目行类型”</td><td>见“标准项目行类型”</td><td>根据表标识的 part detail type 文本</td></tr></table>

表 4-3-3.18 标准详细零件类型(关键字)  

<table><tr><td rowspan="2">part_detail_type</td><td colspan="2">part_detail_text</td><td rowspan="2">描述</td></tr><tr><td>飞机标记</td><td>发动机标记</td></tr><tr><td>airline_pnr</td><td>&lt;alprtnbr&gt;</td><td>&lt;alpnr&gt;</td><td>分配给航空公司的用以标识和控制零件的编号</td></tr><tr><td>overlength_pnr</td><td>&lt;opn&gt;</td><td>&lt;opn&gt;</td><td>超过15个字符的零件号</td></tr><tr><td>optionalSUPPLIER_CODE</td><td>&lt;osc&gt;</td><td>未使用。</td><td>标识授权的可选零件供应商</td></tr><tr><td>altered_pnbr</td><td>&lt;afpmfr&gt;</td><td>&lt;afp&gt;</td><td>标识已经变更或修改(为其它零件号)的零件号</td></tr><tr><td>buy_next_higher_assy</td><td>&lt;bnpmfr&gt;</td><td>未使用</td><td>标识根据零件号字段中的零件号必须替换的零件</td></tr><tr><td>buy_with_part</td><td>&lt;bwpmfr&gt;</td><td>未使用</td><td>标识根据零件号字段中的零件号必须购买的零件</td></tr><tr><td>controlSpecific_MFR</td><td>&lt;csdmfr&gt;</td><td>未使用</td><td>详细说明各种构成、安装和操作要求的简要说明书</td></tr><tr><td>local_fabric_material</td><td>&lt;lfmmfr&gt;</td><td>未使用</td><td>标识制造主要零件所需的原材料和零件,它们可选择为制造或购买</td></tr><tr><td>optional_parts</td><td>&lt;optmfr&gt;</td><td>未使用</td><td>与主要零件可完全互换的零件</td></tr><tr><td>preferred_spare_part</td><td>&lt;pspmfr&gt;</td><td>未使用</td><td>首选的替换零件</td></tr><tr><td>ext_ref</td><td>&lt;refext&gt;</td><td>&lt;refext&gt;</td><td>包含对其它手册的参考</td></tr><tr><td>symbol</td><td>未使用</td><td>&lt;symbol&gt;</td><td>在零件号前面的一个符号,表示一个零件的分类和/或零件的状态</td></tr><tr><td>nonprovisioned</td><td>未使用</td><td>&lt;np&gt;</td><td>一个非供应项目</td></tr><tr><td>material</td><td>未使用</td><td>&lt;matl&gt;</td><td>标识成分代码</td></tr><tr><td>control Specific_nbr</td><td>未使用</td><td>&lt;csd&gt;</td><td>图号规范</td></tr><tr><td>spare_partdrawing</td><td>未使用</td><td>&lt;sp&gt;</td><td>与修理相关的零件</td></tr><tr><td>alternate_part</td><td>&lt;apnmfr&gt;</td><td>未使用</td><td>标识一个备用零件</td></tr><tr><td>int_reference</td><td>未使用</td><td>&lt;refint&gt;</td><td>内部参考</td></tr><tr><td>dim_data</td><td>未使用</td><td>&lt;dd&gt;</td><td>标识零件的尺寸数据</td></tr><tr><td>customer_nomen</td><td>未使用</td><td>&lt;cusnom&gt;</td><td>由用户分配的名称术语</td></tr><tr><td>assy_pnr</td><td>未使用</td><td>&lt;ee&gt;</td><td>标识一个在装配后分配的零件号</td></tr><tr><td>keyword</td><td>&lt;kwd&gt;</td><td>&lt;kwd&gt;</td><td>零件号字段中显示的条目名</td></tr></table>

# 16 图形表

该表包含了图解零件目录中插图的信息。图形页的二进制图像可在图页表中查到。

表 4-3-3.19 图形表  

<table><tr><td>栏 名</td><td>类型</td><td>飞机标记</td><td>发动机标记</td><td>描述</td></tr><tr><td>GRAPHIC_ID*</td><td>INT</td><td>NA</td><td>NA</td><td>分配的唯一标识符</td></tr><tr><td>key_code**</td><td>CHAR</td><td>未使用</td><td></td><td>图形的唯一标识符</td></tr><tr><td>@GEN.DOCS.DOC_ID**</td><td>INT</td><td>NA</td><td>NA</td><td>文件ID。参考通用(GEN)纲要模型中的Doc表[参见本文4-3-1.7.1]</td></tr><tr><td>@CSUFIGURE.CSUFIGURE_ID</td><td>INT</td><td>NA</td><td>NA</td><td>CSU图形表参考</td></tr><tr><td>effectivity_mask</td><td>BITFIELD</td><td>未使用</td><td>NA</td><td>表示适用的有效性模板(在数据库准备阶段被分配)</td></tr><tr><td>effectivity_info</td><td>TEXT</td><td>未使用</td><td></td><td>该条目的有效性信息的所有SGML片段</td></tr><tr><td>graphic_title</td><td>TEXT</td><td>未使用</td><td></td><td>图标题</td></tr><tr><td>sheet_count</td><td>INT</td><td>NA</td><td>NA</td><td>图形中的图页号</td></tr><tr><td>revision_date</td><td>DATE</td><td>未使用</td><td></td><td>更改日期</td></tr><tr><td>seq_nbr</td><td>INT</td><td>NA</td><td>NA</td><td>数据中行的逻辑顺序</td></tr><tr><td>graphic_text</td><td>TEXT</td><td></td><td></td><td>图形号的所有SGML片段</td></tr></table>

# 17 图页表

该表包含了IPC中的示图图页。CSU圈中在何编号的一个图页都可以被使用。

表 4-3-3.20 图页列表  

<table><tr><td>栏名</td><td>类型</td><td>飞机标记</td><td>发动机标记</td><td>描述</td></tr><tr><td>SHEET_ID*</td><td>INT</td><td>NA</td><td>NA</td><td>分配的唯一ID</td></tr><tr><td>gnbr_code**</td><td>CHAR</td><td>&lt;sheetgnbr&gt;</td><td>&lt;sheetgnbr&gt;</td><td>文件实例中唯一的一个位置标识(标识符)</td></tr><tr><td>@GEN.DOCS.DOC_ID**</td><td>INT</td><td>NA</td><td>NA</td><td>文件ID。参考通用(GEN)纲要模型中的Doc表[参见本文4-3-1.7.1]</td></tr><tr><td>@GRAPHIC.GRAPHIC_ID**</td><td>INT</td><td>NA</td><td>NA</td><td>参考图形表</td></tr><tr><td>sheet_nbr**</td><td>INT</td><td>&lt;sheetsheetnbr&gt;</td><td>&lt;sheetsheetnbr&gt;</td><td>图形中该图页的顺序号</td></tr><tr><td>effectivity_mask</td><td>BITFIELD</td><td>未使用</td><td>NA</td><td>表示适用的有效性模板(在数据库准备阶段被分配)</td></tr><tr><td>effectivity_info</td><td>TEXT</td><td>未使用</td><td>-effect&gt;</td><td>该条目有效性信息的完整SGML片段</td></tr><tr><td>revision_date</td><td>DATE</td><td></td><td></td><td>更改日期</td></tr><tr><td>key_code</td><td>CHAR</td><td></td><td></td><td>图页的唯一标识符</td></tr><tr><td>sheet_type_code</td><td>CHAR</td><td>NA</td><td>NA</td><td>标识图形编码格式</td></tr><tr><td>sheet_title</td><td>TEXT</td><td></td><td></td><td>图页标题</td></tr><tr><td>sheet_text</td><td>TEXT</td><td></td><td></td><td>一个图页的所有SGML片段</td></tr><tr><td>sheet_bin</td><td>GRAPHIC</td><td>NA</td><td>NA</td><td>二进制编码的图形</td></tr><tr><td>file_name</td><td>CHAR</td><td>NA</td><td>NA</td><td>包含图形的可选文件名</td></tr></table>

# 4-3-4 服务通报(SB)纲要模型

# 1 前言

本文件随同 ATA 通用纲要模型(参见[本文 4-3-1])一起，提供了适用于服务通报(SB)的检索纲要模型。该纲要模型称为“SB”纲要模型，它属于“ATA_维修”类。SB DTD 组织在如下所示的表中。

表 4-3-4.1 SB DTD 结构  

<table><tr><td>服务通报</td><td>见通用(GEN)纲要模型中的Doc表。</td></tr><tr><td>TS</td><td>见SECTION表[表4-3-4.5]</td></tr><tr><td>TSSECT</td><td>见SUBSECT表[表4-3-4.7]</td></tr><tr><td>BODY</td><td></td></tr><tr><td>PLAN</td><td>见SECTION表[表4-3-4.5]</td></tr><tr><td>PLANSECT</td><td>见SUBSECT表[表4-3-4.7]</td></tr><tr><td>MATINFO</td><td>见SECTION表[表4-3-4.5]</td></tr><tr><td>MATSECT</td><td>见SUBSECT表[表4-3-4.7]</td></tr><tr><td>INSTR</td><td>见SECTION表[表4-3-4.5]</td></tr><tr><td>INSTSECT</td><td>见SUBSECT表[表4-3-4.7]</td></tr><tr><td>APPEND</td><td>见SECTION表[表4-3-4.5]</td></tr></table>

由于SBFMatr(SB正文前)，主体(正文)部分和附录是通用的结构，因此该纲要模型将这些部分汇集到一个两个层次的表结构中，并在“type类型”栏中使用标记名来标识节类型。然后对于分节TSSect、SBFMsect、PlanSect、MatSect和InstSect也采用相同的方法。表也包含序列号，这些序列号是在文件实例中出现的标记编号。

# 2 有效性表

本表被当作该纲要模型中其它表的 EFFECTIVITY_MASK 栏中有效性信息编码的“关键字”来使用。对于数据库的 SB 部分中所给出的每个不同的有效性值，在该表中都有一个行来描述。

表 4-3-4.2 有效性表  

<table><tr><td>栏名</td><td>类型</td><td>飞机标记</td><td>发动机标记</td><td>描述</td></tr><tr><td>effectivity_key*</td><td>CHAR</td><td>见注</td><td>见注</td><td>有效性关键字是用于标识数据中一个特定有效性的唯一值。该值在飞机与发动机数据库两者之间有不同的起源和语义</td></tr><tr><td>mask_position_nbr**</td><td>INT</td><td>NA</td><td>NA</td><td>EFFECTIVITY_MASK 中唯一的指定位置。MASK POSITION_NBR 应是从 1~n之间的无符号整数,其中 n 为有效性表中的行数</td></tr><tr><td>serial_nbr</td><td>CHAR</td><td>&lt;msnbr&gt;</td><td>未使用</td><td>固定的 ID 编号</td></tr></table>

注：对于飞机，数据库中所表示的每一个CEC号都与该表中的一行相对应。每行都有一个唯一的effectivity_key值（即一个CEC)，并给出唯一的MASK POSITION_NBR值，该值是在数据库创建时随机分配的。

注2：对于发动机，数据库中所表示的每个不同型号代码都与该表中有一行相对应。每行都有一个唯一的effectivity_key值(即一个型号代码)，并给出唯一的MASK POSITION_NBR值，该值是在数据库创建时随机分配的。

# 3 目录表

该表用于存储所有SB文件的目录。该表设计成为可使用一条SFQL查询语句生成可访问的文本条目的方式，这样使目录的生成比较容易。这包括表中每个条目的摘要以及对包含实际信息的文件表的一个链接。

表 4-3-4.3 目录表  

<table><tr><td>栏名</td><td>类型</td><td>飞机标记</td><td>发动机标记</td><td>描述</td></tr><tr><td>CONTENTS_ID*</td><td>INT</td><td>NA</td><td>NA</td><td>分配的唯一行标识符</td></tr><tr><td>@GEN.DOCS.DOC_ID*</td><td>INT</td><td>NA</td><td>NA</td><td>文件 ID。在通用纲要模型(GEN)中的Doc表的次关键字</td></tr><tr><td>entry_sequence_nbr**</td><td>INT</td><td>NA</td><td>NA</td><td>用于放置条目的编号,利用该编号使条目的排列与目录中的DOC_ID的顺序完全相同,该编号从1开始</td></tr><tr><td>entry_table_name</td><td>CHAR</td><td>NA</td><td>NA</td><td>该条目指向的纲要模型表名</td></tr><tr><td>entry_key_name</td><td>CHAR</td><td>NA</td><td>NA</td><td>主关键字的栏名称。见注</td></tr><tr><td>@ENTRY_KEY_ID</td><td>INT</td><td>NA</td><td>NA</td><td>标识内容文本的主关键字值</td></tr><tr><td>effectivity_mask</td><td>BITFIELD</td><td>NA</td><td>NA</td><td>表示适用的有效性模板(在数据库准备阶段分配)</td></tr><tr><td>effectivity_info</td><td>TEXT</td><td>见注1</td><td>未使用。</td><td>飞机/发动机的有效性信息</td></tr><tr><td>entry_level</td><td>INT</td><td>见注2</td><td>见注2。</td><td>表中的层次结构级别,其中1为最高级别</td></tr><tr><td>@PARENT_ID</td><td>INT</td><td>NA</td><td>NA</td><td>父条目的content_id。如果没有父条目(entry_level=1),则PARENT_ID值为NULL</td></tr><tr><td>entry_text</td><td>TEXT</td><td>&lt;title&gt; or &lt;TOC&gt;</td><td>&lt;title&gt;</td><td>TOC条目</td></tr><tr><td>entry_startoff</td><td>INT</td><td>NA</td><td>NA</td><td>通用纲要模型中的Doc表[参见本文4-3-1.7.1]中描述的entry_text栏起始的相对位置</td></tr><tr><td>entry_endoff</td><td>INT</td><td>NA</td><td>NA</td><td>通用纲要模型中的Doc表[参见本文4-3-1.7.1]中描述的entry_text栏结束的相对位置</td></tr><tr><td>section_type</td><td>CHAR</td><td>NA</td><td>NA</td><td>适用的节的类型(见节表)</td></tr><tr><td>subject_name</td><td>CHAR</td><td>NA</td><td>NA</td><td>适用的分节名(见分节表)</td></tr><tr><td>subject_type</td><td>CHAR</td><td>NA</td><td>NA</td><td>适用的分节类型(见节表)</td></tr><tr><td>key_code</td><td>CHAR</td><td>&lt;?key&gt;</td><td>&lt;?key&gt;</td><td>文件实例中唯一的一个位置标识(标识符)</td></tr><tr><td>revision_date</td><td>DATE</td><td>&lt;?revdate&gt;</td><td>&lt;?revdate&gt;</td><td>更改日期</td></tr></table>

注1：对于飞机，如果effectivity_text存在，它将只包含EFFECT元素的efftext属性值。  
注2：这是一个如何使用entry_level的例子。

<table><tr><td>entry_table_name</td><td>entry_level</td></tr><tr><td>节</td><td>1</td></tr><tr><td>分节</td><td>2</td></tr></table>

注：参考技术要求，entry_table具有单一的主关键字字栏。

# 4 更改提要表

该表用于返回反映更改过程中所作更改的更改提要信息。表的每一行内容表示了对纲要模型中其它表的一行中数据的一组修订摘要(在SGML中以一个位置标识出现)。

表 4-3-4.4 更改提要表  

<table><tr><td>栏名</td><td>类型</td><td>飞机标记</td><td>发动机
标记</td><td>描述</td></tr><tr><td>HIGHLIGHTS_ID*</td><td>INT</td><td>NA</td><td>NA</td><td>分配的唯一行标识符</td></tr><tr><td>entry_table_name**</td><td>CHAR</td><td>NA</td><td>NA</td><td>由该条目指向的纲要模型表名</td></tr><tr><td>entry_key_name**</td><td>CHAR</td><td>NA</td><td>NA</td><td>主关键字的栏名称</td></tr><tr><td>@ENTRY_KEY_ID**</td><td>INT</td><td>NA</td><td>NA</td><td>主关键字值，用以标识更改提要适用的文件单元</td></tr><tr><td>@GEN.DOCS.DOC_ID**</td><td>INT</td><td>NA</td><td>NA</td><td>文件ID。通用纲要模型(GEN)中的Doc表的外部关键字</td></tr><tr><td>EFFECTIVITY_MASK**</td><td>BITFIELD</td><td>NA</td><td>NA</td><td>表示适用的有效性模板</td></tr><tr><td>effectivity_info</td><td>TEXT</td><td>-effect&gt;</td><td>-effect&gt;</td><td>飞机/发动机的有效性信息</td></tr><tr><td>graphic_title</td><td>TEXT</td><td>&lt;title&gt;</td><td>&lt;title&gt;</td><td>当图形或图页为更改目标时使用</td></tr><tr><td>sheet_nbr</td><td>INT</td><td></td><td></td><td>当图页为更改目标时使用</td></tr><tr><td>section_type</td><td>CHAR</td><td>NA</td><td>NA</td><td>适用的节类型(见节表)</td></tr><tr><td>subject_name</td><td>CHAR</td><td>NA</td><td>NA</td><td>适用的分节名称(见分节表)</td></tr><tr><td>subject_type</td><td>CHAR</td><td>NA</td><td>NA</td><td>适用的分节类型(见节表)</td></tr><tr><td>key_code</td><td>CHAR</td><td></td><td></td><td>文件实例中唯一的一个位置标识(标识符)</td></tr><tr><td>revision_date</td><td>DATE</td><td></td><td></td><td>更改日期</td></tr><tr><td>change_description</td><td>CHAR</td><td></td><td></td><td>描述更改过程中的所作的改变</td></tr></table>

# 5 节表

该表用于返回一个或多个维护通报的节信息。一节的全部文本用一个给定行中的section_text栏来表示。维护通报中的一节包含下列DTD元素：

- sbfmatr(服务通报正文前内容)  
plan(计划)  
- matinfo(材料信息)  
instr（指令）  
append(附录)

表4-3-4.5 节表  

<table><tr><td>栏名</td><td>类型</td><td>飞机标记</td><td>发动机标记</td><td>描述</td></tr><tr><td>SECTION_ID*</td><td>INT</td><td>NA</td><td>NA</td><td>分配的唯一ID</td></tr><tr><td>Section_type**</td><td>CHAR</td><td>NA</td><td>NA</td><td>节类型(见下表)</td></tr><tr><td>Seq_nbr**</td><td>INT</td><td>NA</td><td>NA</td><td>数据中行的逻辑顺序。(与sect_type相对应)</td></tr><tr><td>@GEN.DOCS.DOC_ID**</td><td>INT</td><td>NA</td><td>NA</td><td>文件ID。通用纲要模型(GEN)中的Doc表的外部关键字</td></tr><tr><td>revision_date</td><td>DATE</td><td></td><td></td><td>更改日期</td></tr><tr><td>key_code</td><td>CHAR</td><td></td><td></td><td>文件实例中唯一的一个位置标识(标识符)</td></tr><tr><td>section_title</td><td>TEXT</td><td></td><td></td><td>节标题</td></tr><tr><td>section_text</td><td>TEXT</td><td></td><td></td><td>一节的所有SGML片段</td></tr><tr><td>section_startoff</td><td>INT</td><td>NA</td><td>NA</td><td>通用纲要模型中的Doc表[参见本文4-3-1.7.1]中描述的section_text栏起始的相对位置</td></tr><tr><td>section_endoff</td><td>INT</td><td>NA</td><td>NA</td><td>通用纲要模型中的Doc表[参见本文4-3-1.7.1]中描述的section_text栏结束的相对位置</td></tr></table>

表 4-3-4.6 标准节类型  

<table><tr><td>类型</td><td>描述</td></tr><tr><td>APPEND</td><td>可选的附录信息。注意APPEND没有下级的SUBJECT关系</td></tr><tr><td>INSTR</td><td>执行指令</td></tr><tr><td>MATINFO</td><td>材料信息</td></tr><tr><td>PLAN</td><td>计划信息</td></tr><tr><td>SBF MATR</td><td>用于摘要或主体之前的服务通报前页</td></tr></table>

# 6 分节表

该表用于返回一个节中的分节信息。一个单独分节的全部文本包含在一个给定行中的 subsect_text 栏。维护通报中的节包含下列 DTD 元素：

- sbfmsect(服务通报正文前内容分节)  
plansect(计划分节)  
- matsect(材料信息分节)  
- instsect(指令分节)

表 4-3-4.7 分节表  

<table><tr><td>栏 名</td><td>类型</td><td>飞机标记</td><td>发动机 标记</td><td>描述</td></tr><tr><td>SUBJECT_ID*</td><td>INT</td><td>NA</td><td>NA</td><td>分配的唯一ID</td></tr><tr><td>subject_name**</td><td>CHAR</td><td>&lt;subsection sect name&gt;</td><td>&lt;subsection sect name&gt;</td><td>节名称</td></tr><tr><td>seq_nbr**</td><td>INT</td><td>NA</td><td>NA</td><td>数据中行的逻辑顺序</td></tr><tr><td>subject_type**</td><td>CHAR</td><td>NA</td><td>NA</td><td>分节的标准类型</td></tr><tr><td>@SECTION SECTION_ID**</td><td>INT</td><td>NA</td><td>NA</td><td>参考节表</td></tr><tr><td>@GEN.DOCS.DOC_ID</td><td>INT</td><td>NA</td><td>NA</td><td>文件 ID。通用纲要模型(GEN)中的 Doc 表的次关键字</td></tr><tr><td>revision_date</td><td>DATE</td><td>&lt;subsection revdate&gt;</td><td>&lt;subsection revdate&gt;</td><td>更改日期</td></tr><tr><td>key_code</td><td>CHAR</td><td>&lt;subsection key&gt;</td><td>&lt;subsection key&gt;</td><td>在文件实例中唯一的一个位置标识(标识符)</td></tr><tr><td>subject_title</td><td>TEXT</td><td>&lt;title&gt;</td><td>&lt;title&gt;</td><td>分节标题</td></tr><tr><td>subject_text</td><td>TEXT</td><td>&lt;subsection&gt;</td><td>&lt;subsection&gt;</td><td>一个分节的所有 SGML 片段</td></tr><tr><td>subject_startoff</td><td>INT</td><td>NA</td><td>NA</td><td>通用纲要模型中的 Doc 表[参见本文 4-3-1.7.1] 中描述的subsection_text 栏起始的相对位置</td></tr><tr><td>subject_endoff</td><td>INT</td><td>NA</td><td>NA</td><td>通用纲要模型中的 Doc 表[参见本文 4-3-1.7.1] 中描述的subsection_text 栏结束的相对位置</td></tr></table>

表 4-3-4.8 标准分节类型  

<table><tr><td>类型</td><td>描述</td></tr><tr><td>INSTRSECT</td><td>执行指令分节</td></tr><tr><td>MATSECT</td><td>材料信息分节</td></tr><tr><td>PLANSECT</td><td>计划信息分节</td></tr><tr><td>SBFMSECT</td><td>用于摘要或者主体内容前的 SB Fmatr 的分节</td></tr><tr><td>TSSECT</td><td>发送函</td></tr></table>

# 7 图形表

该表包含手册中的图形信息。图形图页的二进制图像可在图页表中查到。

表4-3-4.9 图形表  

<table><tr><td>栏名</td><td>类型</td><td>飞机标记</td><td>发动机
标记</td><td>描述</td></tr><tr><td>GRAPHIC_ID*</td><td>INT</td><td>NA</td><td>NA</td><td>分配的唯一ID</td></tr><tr><td>key_code**</td><td>CHAR</td><td>&lt;graphic
key&gt;</td><td>&lt;graphic
key&gt;</td><td>图形的唯一标识符</td></tr><tr><td>@GEN.DOCS.DOC_ID**</td><td>INT</td><td>NA</td><td>NA</td><td>文件 ID。通用纲要模型(GEN)
中的 Doc 表的外部关键字</td></tr><tr><td>Effectivity_mask</td><td>BITFIELD</td><td>NA</td><td>NA</td><td>表示适用的有效性模板(在数据库准备阶段被分配)</td></tr><tr><td>effectivity_info</td><td>TEXT</td><td>-effect&gt;</td><td>-effect&gt;</td><td>飞机/发动机的有效性信息</td></tr><tr><td>graphic_title</td><td>TEXT</td><td>&lt;title&gt;</td><td>&lt;title&gt;</td><td>图题</td></tr><tr><td>sheet_count</td><td>INT</td><td>NA</td><td>NA</td><td>图形中的图页编号</td></tr><tr><td>revision_date</td><td>DATE</td><td>&lt;graphic
revdate&gt;</td><td>&lt;graphic
revdate&gt;</td><td>更改日期</td></tr><tr><td>seq_nbr</td><td>INT</td><td>NA</td><td>NA</td><td>数据中行的逻辑顺序</td></tr><tr><td>graphic_text</td><td>TEXT</td><td>&lt;graphic&gt;</td><td>&lt;graphic&gt;</td><td>图形编号的所有 SGML 片段</td></tr></table>

# 8 图页表

该表包含图形的图页，并显示它们与该图形的关系。

示图可按 ATA 标准格式根据 sheet_bin 栏检索，或可选择根据 file_name 栏中显示的文件来检索。

表4-3-4.10 图页表  

<table><tr><td>栏 名</td><td>类型</td><td>飞机标记</td><td>发动机 标记</td><td>描述</td></tr><tr><td>SHEET_ID*</td><td>INT</td><td>NA</td><td>NA</td><td>分配的唯一ID</td></tr><tr><td>@GRAPHIC.GRAPHIC_ID**</td><td>INT</td><td>NA</td><td>NA</td><td>参考图形表</td></tr><tr><td>sheet_nbr**</td><td>INT</td><td></td><td></td><td>父图形中该图页的顺序号</td></tr><tr><td>key_code**</td><td>CHAR</td><td></td><td></td><td>图页的唯一标识符</td></tr><tr><td>@GEN.DOCS.DOC_ID**</td><td>INT</td><td>NA</td><td>NA</td><td>文件 ID。通用纲要模型(GEN) 中的 Doc 表的次关键字</td></tr><tr><td>EFFECTIVITY_MASK</td><td>BITFIELD</td><td>NA</td><td>NA</td><td>表示适用的有效性的模板(在数据库准备阶段被分配)</td></tr><tr><td>effectivity_info</td><td>TEXT</td><td>-effect&gt;</td><td>-effect&gt;</td><td>飞机/发动机的有效性信息</td></tr><tr><td>sheet_title</td><td>TEXT</td><td>&lt;title&gt;</td><td>&lt;title&gt;</td><td>图页标题</td></tr><tr><td>sheet_type_code</td><td>CHAR</td><td>NA</td><td>NA</td><td>标识图形编码格式</td></tr><tr><td>sheet_text</td><td>TEXT</td><td>&lt;sheet&gt;</td><td>&lt;sheet&gt;</td><td>一个图页编号的所有SGML片段</td></tr><tr><td>revision_date</td><td>DATE</td><td>&lt;sheet revdate&gt;</td><td>&lt;sheet revdate&gt;</td><td>更改日期</td></tr><tr><td>sheet_bin</td><td>GRAPHIC</td><td>NA</td><td>NA</td><td>二进制编码图形</td></tr><tr><td>file_name</td><td>CHAR</td><td>NA</td><td>NA</td><td>包含图形的可选文件名</td></tr></table>

# 4-3-5 消耗品手册(CPM)纲要模型

# 1 前言

本文件与ATA通用纲要模型([参见本文4-3-1])共同提供了适用于消耗品手册的检索纲要模型。该纲要模型称为“CPM”纲要模型，它属于“ATA维修”类。

# 2 前页表

该表包含文件的前页内容。它将前页内容划分成若干部分，其中division_name栏指出了DTD标记，按照这些标记可导出前页内容。

表 4-3-5.1 Front_matter 表  

<table><tr><td>栏名称</td><td>类型</td><td>飞机标记</td><td>发动机标记</td><td>描述</td></tr><tr><td>FRONT_MATTER_ID*</td><td>INT</td><td>NA</td><td>NA</td><td>分配的唯一ID</td></tr><tr><td>@GEN.DOCS.DOC_ID**</td><td>INT</td><td>NA</td><td>NA</td><td>文件ID。通用纲要模型(GEN)中Doc表的外部关键字</td></tr><tr><td>division_name**</td><td>CHAR</td><td>([参见本文4-3-5-2])</td><td>([参见本文4-3-5-2])</td><td>前页内容的分段(部分)的名称。标准名称在下面给出</td></tr><tr><td>division_title</td><td>TEXT</td><td>&lt;title&gt;</td><td>&lt;title&gt;</td><td>分段标题</td></tr><tr><td>division_text</td><td>TEXT</td><td>([参见本文4-3-5-2])</td><td>([参见本文4-3-5-2])</td><td>一个分段的全部SGML片段</td></tr><tr><td>division_startoff</td><td>INT</td><td>NA</td><td>NA</td><td>通用纲要模型中的Doc表[参见本文4-3-1.7.1]中描述的division_text栏起始的相对位置</td></tr><tr><td>division_endoff</td><td>INT</td><td>NA</td><td>NA</td><td>通用纲要模型中的Doc表[参见本文4-3-1.7.1]中描述的division_text栏结束的相对位置</td></tr></table>

表 4-3-5.2 Front_matter 表 “division_name” 栏的标准分段名称值  

<table><tr><td>分割部分名称</td><td>类型</td><td>飞机标记</td><td>发动机标记</td><td>描述</td></tr><tr><td>TRAN Letter</td><td>TEXT</td><td>&lt;transltr&gt;</td><td>&lt;transltr&gt;</td><td>更改的通用信息</td></tr><tr><td>INTRO</td><td>TEXT</td><td>&lt;intro&gt;</td><td>&lt;intro&gt;</td><td>文件信息</td></tr></table>

注1：“如何使用”信息位于INTRO(部分)。  
注2：可以从CPSHEET表生成消耗品的数字和字母索引

# 3 有效性表

本表被当作该纲要模型中其它表的 EFFECTIVITY_MASK 栏中有效性信息编码的“关键字”来使用。对于数据库的 MSM 部分中所给出的每个不同的有效性值，在该表中都有一个行来描述。

表 4-3-5.3 有效性表  

<table><tr><td>栏名称</td><td>类型</td><td>飞机标记</td><td>发动机标记</td><td>描述</td></tr><tr><td>effectivity_key*</td><td>CHAR</td><td>见注1</td><td>见注1</td><td>有效性关键字,用于标识资料中一个特定有效性的唯一值。该值在飞机与发动机数据库两者之间有不同的起源和语义(见注1和注2)</td></tr><tr><td>mask_position_nbr**</td><td>INT</td><td>NA</td><td>NA</td><td>EFFECTIVITY_MASK 中唯一的指定位置。MASK POSITION_NBR 应是从 1~n之间的无符号整数,其中 n 为有效性表中的行数。</td></tr></table>

注1：对于机身，数据库中所表示的每一个CEC号都与该表中的一行相对应。每行都有一个唯一的effectivity_key值(即一个CEC)，并给出一个唯一的MASK POSITION_NBR值，该值是在数据库创建时随机分配的。  
注2：对于发动机，MSM数据库中所表示的每个不同型号代码都与该表中的一行相对应。每行都有一个唯一的effectivity_key值(即一个型号代码)，并给出一个唯一的MASK POSITION_NBR值，该值是在数据库创建时随机分配的。

# 4 目录表

该表用于存储所有CPM文件的目录。目录表设计成为可使用一条SFQL查询语句生成可访问的文本条目的方式，这样使目录的生成比较容易。这包括针对表中每个条目的一个摘要以及对包含实际信息的文件表的一个链接。

表4-3-5.4 目录表  

<table><tr><td>栏名称</td><td>类型</td><td>飞机标记</td><td>发动机标记</td><td>描述</td></tr><tr><td>CONTENTS_ID*</td><td>INT</td><td>NA</td><td>NA</td><td>分配的唯一行标识符</td></tr><tr><td>@GEN.DOCS.DOC_ID* *</td><td>INT</td><td>NA</td><td>NA</td><td>文件ID。参考通用纲要模型中的Doc表</td></tr><tr><td>entry_sequence_nbr**</td><td>INT</td><td>NA</td><td>NA</td><td>用于排放条目的编号，利用该编号使条目的排列与目录中的DOC_ID的顺序完全相同，该编号从1开始</td></tr><tr><td>entry_table_name</td><td>CHAR</td><td>NA</td><td>NA</td><td>由该条目指向的纲要模型表名称</td></tr><tr><td>entry_key_name</td><td>CHAR</td><td>NA</td><td>NA</td><td>主关键字的栏名。见注3</td></tr><tr><td>@ENTRY_KEY_ID</td><td>INT</td><td>NA</td><td>NA</td><td>标识目录文本的主关键字值</td></tr><tr><td>Effectivity_mask</td><td>BITFIELD</td><td>NA</td><td>NA</td><td>表示适用的有效性模板(在数据库准备阶段分配)</td></tr><tr><td>Effectivity_info</td><td>TEXT</td><td>见注1</td><td>未使用</td><td>飞机/发动机的有效性信息</td></tr><tr><td>FM_Division_Name</td><td>CHAR</td><td>NA</td><td>NA</td><td>当条目是前页内容的分段时使用</td></tr><tr><td>Entry_level</td><td>INT</td><td>NA 见注2</td><td>NA 见注2</td><td>表中的层次结构级别,其中1为最高级别</td></tr><tr><td>@PARENT_ID</td><td>INT</td><td>NA</td><td>NA</td><td>父条目的content_id。如果没有父条目(entry_level=1),则PARENT_ID值为NULL</td></tr><tr><td>entry_text</td><td>TEXT</td><td>&lt; title&gt; or &lt;TOC&gt;</td><td>&lt; title&gt;</td><td>TOC条目</td></tr><tr><td>entry_startoff</td><td>INT</td><td>NA</td><td>NA</td><td>通用纲要参见本文中的Doc表[标题4-3-1.7.1]中描述的entry_text栏起始的相对位置</td></tr><tr><td>entry_endoff</td><td>INT</td><td>NA</td><td>NA</td><td>通用纲要模型中的Doc表[参见本文4-3-1.7.1]中描述的entry_text栏结束的相对位置</td></tr><tr><td>key_code</td><td>CHAR</td><td>&lt;?key&gt;</td><td>&lt;?key&gt;</td><td>一个位置标识(标识符),在文件样本中是唯一的</td></tr><tr><td>section_nbr</td><td>CHAR</td><td>&lt;?sectnbr&gt;</td><td>&lt;?sectnbr&gt;</td><td>节号</td></tr><tr><td>cpsheet_nbr</td><td>CHAR</td><td>&lt;?connbr&gt;</td><td>&lt;?connbr&gt;</td><td>消耗品号</td></tr><tr><td>unit_nbr</td><td>CHAR</td><td>&lt;?unitnbr&gt;</td><td>&lt;?unitnbr&gt;</td><td>单元号</td></tr><tr><td>revision_date</td><td>DATE</td><td>&lt;?revdate&gt;</td><td>&lt;?revdate&gt;</td><td>更改日期</td></tr></table>

注1：对于飞机，如果effectivity_text存在，它应只包含EFFECT元素的effext属性值。  
注2：这是在飞机手册中如何使用entry_level的一个例子。

<table><tr><td>entry_table_name</td><td>entry_level</td></tr><tr><td>前页</td><td>1</td></tr><tr><td>节</td><td>1</td></tr><tr><td>单元或 CPSHEET</td><td>2</td></tr><tr><td>CPSECT</td><td>3</td></tr><tr><td>CPCHAR</td><td>4</td></tr></table>

注3：参考技术要求，entry_table应具有单一的主关键字栏。

# 5 更改提要表

该表用于返回反映修订中更改的提要信息。

表4-3-5.5 更改提要表  

<table><tr><td>栏名称</td><td>类型</td><td>飞机标记</td><td>发动机标记</td><td>描述</td></tr><tr><td>HIGHLIGHTS_ID*</td><td>INT</td><td>NA</td><td>NA</td><td>分配的唯一行标识符</td></tr><tr><td>entry_table_name**</td><td>CHAR</td><td>NA</td><td>NA</td><td>由该条目指向的纲要模型表名称</td></tr><tr><td>entry_key_name**</td><td>CHAR</td><td>NA</td><td>NA</td><td>主关键字的栏名称</td></tr><tr><td>@ENTRY_KEY_ID**</td><td>INT</td><td>NA</td><td>NA</td><td>主关键字值,用以标识适用于更改提要的文件单元</td></tr><tr><td>@GEN.DOCS.DOC_ID* *</td><td>INT</td><td>NA</td><td>NA</td><td>文件ID。参考通用纲要模型中的Doc表(GEN)</td></tr><tr><td>EFFECTIVITY_MASK* *</td><td>BITFIELD</td><td>NA</td><td>NA</td><td>表示适用的有效性模板</td></tr><tr><td>effectivity_info</td><td>TEXT</td><td></td><td></td><td>飞机/发动机的有效性信息</td></tr><tr><td>section_nbr</td><td>CHAR</td><td></td><td></td><td>节号</td></tr><tr><td>cpsheet_nbr</td><td>CHAR</td><td></td><td></td><td>消耗品编号</td></tr><tr><td>unit_nbr</td><td>CHAR</td><td></td><td></td><td>单元号</td></tr><tr><td>graphic_title</td><td>TEXT</td><td></td><td></td><td>当一幅图形或图页为更改目标时使用</td></tr><tr><td>sheet_nbr</td><td>INT</td><td></td><td></td><td>在图形图页为更改目标时使用</td></tr><tr><td>FM_Division_Name</td><td>CHAR</td><td>NA</td><td>NA</td><td>在FM为更改目标时使用</td></tr><tr><td>key_code</td><td>CHAR</td><td></td><td></td><td>文件实例中唯一的一个位置标识(标识符)</td></tr><tr><td>change_description</td><td>CHAR</td><td></td><td></td><td>描述修订过程中的更改</td></tr></table>

# 6 节表

该表用于返回一个或多个消耗品手册的节信息。一节的全部文本用一个给定行中的section_text栏来表示。

表4-3-5.6 节表  

<table><tr><td>栏名称</td><td>类型</td><td>飞机标记</td><td>发动机标记</td><td>描述</td></tr><tr><td>SECTION_ID*</td><td>INT</td><td>NA</td><td>NA</td><td>分配的唯一ID</td></tr><tr><td>section_nbr**</td><td>CHAR</td><td>&lt;section sectnbr&gt;</td><td>&lt;section sectnbr&gt;</td><td>节号</td></tr><tr><td>@GEN.DOCS.DOC_ID**</td><td>INT</td><td>NA</td><td>NA</td><td>文件ID。参考通用纲要模型中的Doc表(GEN)</td></tr><tr><td>sect_type</td><td>CHAR</td><td>&lt;section type&gt;</td><td>&lt;section type&gt;</td><td>节类型(见下表)</td></tr><tr><td>sect_type_other</td><td>CHAR</td><td>&lt;section othtype&gt;</td><td>&lt;section othtype&gt;</td><td>其它类型</td></tr><tr><td>revision_date</td><td>DATE</td><td>&lt;section revdate&gt;</td><td>&lt;section revdate&gt;</td><td>更改日期</td></tr><tr><td>key_code</td><td>CHAR</td><td>&lt;section key&gt;</td><td>&lt;section key&gt;</td><td>文件实例中唯一的一个位置标识(标识符)</td></tr><tr><td>seq_nbr</td><td>INT</td><td>NA</td><td>NA</td><td>资料中行的逻辑顺序</td></tr><tr><td>Section_title</td><td>TEXT</td><td>&lt;title&gt;</td><td>&lt;title&gt;</td><td>节标题</td></tr><tr><td>Section_text</td><td>TEXT</td><td>&lt;section&gt;</td><td>&lt;section&gt;</td><td>一节的所有SGML片段</td></tr><tr><td>Section_startoff</td><td>INT</td><td>NA</td><td>NA</td><td>通用纲要模型中的Doc表[参见本文4-3-1.7.1]中描述的section_text栏起始的相对位置</td></tr><tr><td>Section_endoff</td><td>INT</td><td>NA</td><td>NA</td><td>通用纲要模型中的Doc表[参见本文4-3-1.7.1]中描述的section_text栏结束的相对位置</td></tr></table>

表 4-3-5.7 节表的标准类型  

<table><tr><td>类型</td><td>描述</td></tr><tr><td>IDX</td><td>索引</td></tr><tr><td>MFR</td><td>标准消耗品供应商表</td></tr><tr><td>TDS</td><td>消耗品清单</td></tr><tr><td>OTH</td><td>其它</td></tr></table>

# 7 CPSHEET表

该表用于返回节内的消耗品信息。单个消耗品清单的全部文本用一个给定行中的 CPSHEET.Text 栏来表示。

表4-3-5.8 Cpsheet表  

<table><tr><td>栏名称</td><td>类型</td><td>飞机标记</td><td>发动机标记</td><td>描述</td></tr><tr><td>CPSHEET_ID*</td><td>INT</td><td>NA</td><td>NA</td><td>分配的唯一ID</td></tr><tr><td>cpsheet_nbr**</td><td>CHAR</td><td>&lt;psheet connbr&gt;</td><td>&lt;psheet connbr&gt;</td><td>消耗品编号</td></tr><tr><td>@SECTION SECTION_ID**</td><td>INT</td><td>NA</td><td>NA</td><td>参考节表</td></tr><tr><td>@GEN.DOCS.DOC_ID</td><td>INT</td><td>NA</td><td>NA</td><td>文件ID。参考通用纲要模型中的Doc表(GEN)</td></tr><tr><td>section_nbr</td><td>INT</td><td>&lt;psheet sectnbr&gt;</td><td>&lt;psheet sectnbr&gt;</td><td>节号</td></tr><tr><td>revision_date</td><td>DATE</td><td>&lt;psheet revdate&gt;</td><td>&lt;psheet revdate&gt;</td><td>更改日期</td></tr><tr><td>key_code</td><td>CHAR</td><td>&lt;psheet key&gt;</td><td>&lt;psheet key&gt;</td><td>文件实例中唯一的一个位置标识(标识符)</td></tr><tr><td>cpsheet_type</td><td>CHAR</td><td>&lt;cpsheet type&gt;</td><td>&lt;cpsheet type&gt;</td><td>CPSHEET 的标准化类型</td></tr><tr><td>cpsheet_type_other</td><td>CHAR</td><td>&lt;cpsheet othtype&gt;</td><td>&lt;cpsheet othtype&gt;</td><td>“其它” CPSHEET 类型的非标准化文本或标题。在 cpsheet_type = “OTH”时使用</td></tr><tr><td>seq_nbr</td><td>INT</td><td>NA</td><td>NA</td><td>资料中行的逻辑顺序</td></tr><tr><td>cpsheet_title</td><td>TEXT</td><td>&lt;title&gt;</td><td>&lt;title&gt;</td><td>消耗品清单的标题</td></tr><tr><td>cpsheet_fm_text</td><td>TEXT</td><td>&lt;pbfmatr&gt;</td><td>&lt;pbfmatr&gt;</td><td>前页内容</td></tr><tr><td>cpsheet_text</td><td>TEXT</td><td>&lt;cpsheet&gt;</td><td>&lt;psheet&gt;</td><td>一个 CPSHEET 的所有 SGML 片段</td></tr><tr><td>cpsheet_startoff</td><td>INT</td><td>NA</td><td>NA</td><td>通用纲要模型中的 Doc 表[参见本文 4-3-1.7.1] 中描述的 cpsheet_text 栏起始的相对位置</td></tr><tr><td>cpsheet_endoff</td><td>INT</td><td>NA</td><td>NA</td><td>通用纲要模型中的 Doc 表[参见本文 4-3-1.7.1] 中描述的 cpsheet_text 栏结束的相对位置</td></tr></table>

# 8 单元表

单元在手册中是等同于消耗品清单级的一个级别，而不是 CPSHEETS 本身。该表的每一行表示这样的一个单元。一个单元的全部文本包含在一个给定行中的 unit_text 栏。

表4-3-5.9 单元表  

<table><tr><td>栏名称</td><td>类型</td><td>飞机标记</td><td>发动机
标记</td><td>描述</td></tr><tr><td>UNIT_ID*</td><td>INT</td><td>NA</td><td>NA</td><td>分配的唯一ID</td></tr><tr><td>@SECTION.SECTION_ID**</td><td>INT</td><td>NA</td><td>NA</td><td>参考节表</td></tr><tr><td>unit_nbr**</td><td>CHAR</td><td></td><td></td><td>单元号</td></tr><tr><td>unit_type**</td><td>CHAR</td><td></td><td></td><td>类型(见下表)</td></tr><tr><td>unit_type_other</td><td>CHAR</td><td></td><td></td><td>“其它”单元类型的非标准化文本或标题。在unit_type="OTH"时使用</td></tr><tr><td>@GEN.DOCS.DOC_ID</td><td>INT</td><td>NA</td><td>NA</td><td>文件ID。参考通用纲要模型中的Doc表(GEN)</td></tr><tr><td>section_nbr</td><td>INT</td><td></td><td></td><td>节号</td></tr><tr><td>revision_date</td><td>DATE</td><td></td><td></td><td>更改日期</td></tr><tr><td>key_code</td><td>CHAR</td><td></td><td></td><td>文件实例中唯一的一个位置标识(标识符)</td></tr><tr><td>seq_nbr</td><td>INT</td><td>NA</td><td>NA</td><td>资料中行的逻辑顺序</td></tr><tr><td>unit_title</td><td>TEXT</td><td></td><td></td><td>消耗品清单的标题</td></tr><tr><td>unit_fm_text</td><td>TEXT</td><td></td><td></td><td>前页内容</td></tr><tr><td>unit_text</td><td>TEXT</td><td></td><td></td><td>所有 SGML 片段</td></tr><tr><td>unit_startoff</td><td>INT</td><td>NA</td><td>NA</td><td>通用纲要模型中的 Doc 表[参见本文 4-3-1.7.1]中描述的 unit_text栏起始的相对位置</td></tr><tr><td>unit_endoff</td><td>INT</td><td>NA</td><td>NA</td><td>通用纲要模型中的 Doc 表[参见本文 4-3-1.7.1]中描述的 unit_text栏结束的相对位置</td></tr></table>

表 4-3-5.10 单元表的标准类型  

<table><tr><td>类型</td><td>描述</td></tr><tr><td>IDX</td><td>索引</td></tr><tr><td>MDX</td><td>维修索引</td></tr><tr><td>MFR</td><td>标准设备供应商列表</td></tr><tr><td>OTH</td><td>其它类型</td></tr></table>

# 9 CPSECT表

该表的每一行包含针对一个消耗品清单的单个节，称为“CPSECT”。该部分的全部文本用给定行中的cpsect_text栏来表示。

表4-3-5.11 Cpsect表  

<table><tr><td>栏名称</td><td>类型</td><td>飞机标记</td><td>发动机标记</td><td>描述</td></tr><tr><td>CPSECT_ID*</td><td>INT</td><td>NA</td><td>NA</td><td>分配的唯一ID</td></tr><tr><td>@CPSHEET.CPSHEET_ID**</td><td>INT</td><td>NA</td><td>NA</td><td>参考包含该 CPSECT 的 CPSHEET</td></tr><tr><td>cpsect_type**</td><td>CHAR</td><td></td><td></td><td>节类型。见下面的 CPSECT 类型表</td></tr><tr><td>cpsect_type_other</td><td>CHAR</td><td></td><td></td><td>“其它”类型的非标准化文本或标题。在 cpsect_type = “OTH”时使用</td></tr><tr><td>effectivity_mask</td><td>BITFIELD</td><td>NA</td><td>NA</td><td>表示适用的有效性模板(在数据库准备阶段被分配)</td></tr><tr><td>@GEN.DOCS.DOC_ID</td><td>INT</td><td>NA</td><td>NA</td><td>文件 ID。参考通用纲要模型中的 Doc 表 (GEN)</td></tr><tr><td>effectivity_info</td><td>TEXT</td><td></td><td></td><td>飞机/发动机的有效性信息</td></tr><tr><td>section_nbr</td><td>INT</td><td></td><td></td><td>包含该清单的节号</td></tr><tr><td>cpsheet_nbr</td><td>CHAR</td><td></td><td></td><td>这一图页清单的编号</td></tr><tr><td>seq_nbr</td><td>INT</td><td>NA</td><td>NA</td><td>资料中行的逻辑顺序</td></tr><tr><td>cpsect_title</td><td>TEXT</td><td>&lt;title&gt;</td><td>&lt;title&gt;</td><td>标题</td></tr><tr><td>cpsect_text</td><td>TEXT</td><td>&lt;cpsect&gt;</td><td>&lt;cpsect&gt;</td><td>所有 SGML 片段</td></tr><tr><td>cpsect_startoff</td><td>INT</td><td>NA</td><td>NA</td><td>通用纲要模型中的 Doc 表[参见本文 4-3-1.7.1] 中描述的cpsect_text 栏起始的相对位置</td></tr><tr><td>cpsect_endoff</td><td>INT</td><td>NA</td><td>NA</td><td>通用纲要模型中的 Doc 表[参见本文 4-3-1.7.1] 中描述的cpsect_text 栏结束的相对位置</td></tr></table>

表 4-3-5.12 标准 Cpsect 类型  

<table><tr><td>类型</td><td>描述</td></tr><tr><td>MCT</td><td>制造类别</td></tr><tr><td>DES</td><td>工具名称和/或描述</td></tr><tr><td>DIM</td><td>规格</td></tr><tr><td>HIS</td><td>工具历史记录</td></tr><tr><td>OTH</td><td>其它</td></tr><tr><td>PLI</td><td>零件清单/详细清单</td></tr><tr><td>PNU</td><td>目的和用途</td></tr><tr><td>TEXT</td><td>Consumable_idx</td></tr><tr><td>QPU</td><td>每操作单元所需的数量</td></tr><tr><td>SPT</td><td>支持工具</td></tr><tr><td>TLM</td><td>工具维修</td></tr><tr><td>WGT</td><td>重量</td></tr></table>

# 10 CPCHAR表

该表的每一行包含消耗品清单的一个“特征”信息，称为“CPCHAR”。该部分的全部文本用一个给定行中的cpchar_text栏来表示。

表4-3-5.13 CPCHAR表  

<table><tr><td>栏名称</td><td>类型</td><td>飞机标记</td><td>发动机
标记</td><td>描述</td></tr><tr><td>CPCHAR_ID*</td><td>INT</td><td>NA</td><td>NA</td><td>分配的唯一ID</td></tr><tr><td>@CPSHEET.CPSHEET_ID**</td><td>INT</td><td>NA</td><td>NA</td><td>参考包含该 CPCHAR 的 CPSHEET</td></tr><tr><td>cpchar_type**</td><td>CHAR</td><td>&lt;cpchar type&gt;</td><td>&lt;cpchar type&gt;</td><td>节类型。见下面的 CPCHAR 类型表</td></tr><tr><td>cpchar_type_other</td><td>CHAR</td><td>&lt;cpchar othtype&gt;</td><td>&lt;cpchar othtype&gt;</td><td>“其它”类型的非标准化文本或标题。在 cpchar_type = “OTH”时使用</td></tr><tr><td>effectivity_mask</td><td>BITFIELD</td><td>NA</td><td>NA</td><td>表示适用的有效性模板(在数据库准备阶段被分配)</td></tr><tr><td>@GEN.DOCS.DOC_ID</td><td>INT</td><td>NA</td><td>NA</td><td>文件ID。参考通用纲要模型中的Doc表(GEN)</td></tr><tr><td>effectivity_info</td><td>TEXT</td><td></td><td></td><td>飞机/发动机的有效性信息</td></tr><tr><td>section_nbr</td><td>INT</td><td></td><td></td><td>包含该表的节号</td></tr><tr><td>cpsheet_nbr</td><td>CHAR</td><td></td><td></td><td>该表编号</td></tr><tr><td>seq_nbr</td><td>INT</td><td>NA</td><td>NA</td><td>资料中行的逻辑顺序</td></tr><tr><td>cpchar_title</td><td>TEXT</td><td></td><td></td><td>标题</td></tr><tr><td>cpchar_text</td><td>TEXT</td><td></td><td></td><td>所有SGML片段</td></tr><tr><td>cpchar_startoff</td><td>INT</td><td>NA</td><td>NA</td><td>通用纲要模型中的Doc表[参见本文4-3-1.7.1]中描述的cpchar_text栏起始的相对位置</td></tr><tr><td>cpchar_endoff</td><td>INT</td><td>NA</td><td>NA</td><td>通用纲要模型中的Doc表[参见本文4-3-1.7.1]中描述的cpchar_text栏结束的相对位置</td></tr></table>

表 4-3-5.14 标准 Cpchar 类型  

<table><tr><td>类型</td><td>描述</td></tr><tr><td>APP</td><td>外观</td></tr><tr><td>CLR</td><td>颜色/气味</td></tr><tr><td>CMP</td><td>化学/物理成分</td></tr><tr><td>CTT</td><td>特定内容</td></tr><tr><td>FRM</td><td>形态/硬度</td></tr><tr><td>MET</td><td>使用方法</td></tr><tr><td>MOI</td><td>湿度</td></tr><tr><td>PAR</td><td>微粒大小/形状</td></tr><tr><td>PH</td><td>ph值</td></tr><tr><td>RLD</td><td>相对密度</td></tr><tr><td>TMP</td><td>闪点/用处/自燃/沸腾</td></tr><tr><td>VIS</td><td>粘性</td></tr><tr><td>OTH</td><td>其它</td></tr></table>

# 11 附录表

该表的每一行包含一个附录的文本。附录的全部文本用一个给定行中的 append_text 栏来表示。

表 4-3-5.15 附录表  

<table><tr><td>栏名称</td><td>类型</td><td>飞机标记</td><td>发动机标记</td><td>描述</td></tr><tr><td>APPEND_ID*</td><td>INT</td><td>NA</td><td>NA</td><td>分配的唯一ID</td></tr><tr><td>append_nbr**</td><td>CHAR</td><td></td><td></td><td>节类型。见下面的APPEND类型表</td></tr><tr><td>effectivity_mask</td><td>BITFIELD</td><td>NA</td><td>NA</td><td>表示适用的有效性模板(在数据库准备阶段被分配)</td></tr><tr><td>@GEN.DOCS.DOC_ID</td><td>INT</td><td>NA</td><td>NA</td><td>文件ID。参考通用纲要模型中的Doc表(GEN)</td></tr><tr><td>effectivity_info</td><td>TEXT</td><td></td><td></td><td>飞机/发动机的有效性信息</td></tr><tr><td>seq_nbr</td><td>INT</td><td>NA</td><td>NA</td><td>资料中行的逻辑顺序</td></tr><tr><td>append_title</td><td>TEXT</td><td></td><td></td><td>标题</td></tr><tr><td>append_text</td><td>TEXT</td><td></td><td></td><td>所有SGML片段</td></tr><tr><td>append_startoff</td><td>INT</td><td>NA</td><td>NA</td><td>通用纲要模型中的Doc表a[参见本文4-3-1.7.1]中描述的append_text栏起始的相对位置</td></tr><tr><td>append_endoff</td><td>INT</td><td>NA</td><td>NA</td><td>通用纲要模型中的Doc表[参见本文4-3-1.7.1]中描述的append_text栏结束的相对位置</td></tr></table>

# 12 图形表

该表包含飞机维修和发动机大修手册中图形的信息。图形图页的二进制图像可在图页表中查到。

表 4-3-5.16 图形表  

<table><tr><td>栏名称</td><td>类型</td><td>飞机标记</td><td>发动机
标记</td><td>描 述</td></tr><tr><td>GRAPHIC_ID*</td><td>INT</td><td>NA</td><td>NA</td><td>分配的唯一ID</td></tr><tr><td>key_code**</td><td>CHAR</td><td>&lt;graphic
key&gt;</td><td>&lt;graphic
key&gt;</td><td>图形的唯一标识符</td></tr><tr><td>@GEN.DOCS.DOC_ID* *</td><td>INT</td><td>NA</td><td>NA</td><td>文件 ID。参考通用纲要模型中的Doc表(GEN)</td></tr><tr><td>effectivity_mask</td><td>BITFIELD</td><td>NA</td><td>NA</td><td>表示适用的有效性模板(在数据库准备阶段被分配</td></tr><tr><td>effectivity_info</td><td>TEXT</td><td>-effect&gt;</td><td>-effect&gt;</td><td>飞机/发动机的有效性信息</td></tr><tr><td>graphic_title</td><td>TEXT</td><td>&lt;title&gt;</td><td>&lt;title&gt;</td><td>图形标题</td></tr><tr><td>sheet_count</td><td>INT</td><td>NA</td><td>NA</td><td>图形中的图页编号</td></tr><tr><td>revision_date</td><td>DATE</td><td>&lt;graphic
revdate&gt;</td><td>&lt;graphic
revdate&gt;</td><td>更改日期</td></tr><tr><td>seq_nbr</td><td>INT</td><td>NA</td><td>NA</td><td>资料中行的逻辑顺序</td></tr><tr><td>graphic_text</td><td>TEXT</td><td>&lt;graphic&gt;</td><td>&lt;graphic&gt;</td><td>图形编号的所有SGML片段</td></tr></table>

# 13 图页表

该表包含维修和发动机手册中图形的页，并显示它们与该图形的关系。

示图可按ATA标准格式根据sheet_bin栏检索，并可选择根据file_name栏中显示的文件来检索。

表 4-3-5.17 图页表  

<table><tr><td>栏名称</td><td>类型</td><td>飞机标记</td><td>发动机标记</td><td>描述</td></tr><tr><td>SHEET_ID*</td><td>INT</td><td>NA</td><td>NA</td><td>分配的唯一ID</td></tr><tr><td>@GRAPHIC.GRAPHIC_ID**</td><td>INT</td><td>NA</td><td>NA</td><td>参考图形表</td></tr><tr><td>sheet_nbr**</td><td>INT</td><td></td><td></td><td>父图形中该图页的顺序号</td></tr><tr><td>key_code**</td><td>CHAR</td><td></td><td></td><td>图页的唯一标识符</td></tr><tr><td>@GEN.DOCS.DOC_ID* *</td><td>INT</td><td>NA</td><td>NA</td><td>文件ID。参考通用纲要模型中的Doc表(GEN)</td></tr><tr><td>EFFECTIVITY_MASK</td><td>BITFIELD</td><td>NA</td><td>NA</td><td>表示适用有效性的模板(在数据库准备阶段被分配)</td></tr><tr><td>effectivity_info</td><td>TEXT</td><td></td><td></td><td>飞机/发动机的有效性信息</td></tr><tr><td>sheet_title</td><td>TEXT</td><td></td><td></td><td>图页标题</td></tr><tr><td>sheet_type_code</td><td>CHAR</td><td>NA</td><td>NA</td><td>标识图形编码格式</td></tr><tr><td>sheet_text</td><td>TEXT</td><td></td><td></td><td>一个图页编号的所有SGML片段</td></tr><tr><td>revision_date</td><td>DATE</td><td></td><td></td><td>更改日期</td></tr><tr><td>sheet_bin</td><td>GRAPHIC</td><td>NA</td><td>NA</td><td>二进制编码图形</td></tr><tr><td>file_name</td><td>CHAR</td><td>NA</td><td>NA</td><td>包含图形的可选文件名</td></tr></table>

# 4-3-6 工具和设备手册(TEM)纲要模型

# 1 前言

本文件随同 ATA 通用纲要模型 ([参见本文 4-3-1]) 一起，提供了适用于工具和设备手册的检索纲要模型。该纲要模型称为“TEM”纲要模型，它属于“ATA_维修”类。

TEM的核心结构(每个DTD)由若干节组成，每节都由若干单元或工具表组成，如下图所示。下图中，每个节、单元或工具表可以是许多“类型”之一。

表 4-3-6.1 TEM DTD 结构  

<table><tr><td colspan="2">节</td></tr><tr><td colspan="2">·索引</td></tr><tr><td colspan="2">·操纵和辅助辅助工具</td></tr><tr><td colspan="2">·交叉参考工具清单</td></tr><tr><td colspan="2">·维修索引</td></tr><tr><td colspan="2">·标准设备供应商代码</td></tr><tr><td colspan="2">·材料处理设备</td></tr><tr><td colspan="2">·制造商的支持设备</td></tr><tr><td colspan="2">·检修索引</td></tr><tr><td colspan="2">·工具数据表</td></tr><tr><td colspan="2">·工具/发动机有效性</td></tr><tr><td>·其它</td><td></td></tr><tr><td>单元</td><td>见SECTION表</td></tr><tr><td>·交叉参考工具清单</td><td></td></tr><tr><td>·索引</td><td></td></tr><tr><td>·维修索引</td><td></td></tr><tr><td>·标准设备供应商清单</td><td></td></tr><tr><td>·检修索引</td><td></td></tr><tr><td>·工具/发动机有效性</td><td></td></tr><tr><td>TLSHEET</td><td>见单元表</td></tr><tr><td>·操纵和辅助加工</td><td></td></tr><tr><td>·材料处理设备</td><td></td></tr><tr><td>·制造商的支持设备</td><td></td></tr><tr><td>·工具数据表</td><td></td></tr><tr><td>·其它</td><td></td></tr><tr><td>TLSECT</td><td>见TLSHEET表</td></tr><tr><td>·制造类别</td><td></td></tr><tr><td>·工具名称和/或</td><td></td></tr><tr><td>·描述</td><td></td></tr><tr><td>·规格</td><td></td></tr><tr><td>·工具历史记录</td><td></td></tr><tr><td>·其它</td><td></td></tr><tr><td>·零件清单/详细清单</td><td></td></tr><tr><td>·目的和用途</td><td></td></tr><tr><td>·Consumable_idx</td><td></td></tr><tr><td>·每单元的数量</td><td></td></tr><tr><td>·操作</td><td></td></tr><tr><td>·支持工具</td><td></td></tr><tr><td>·工具维护</td><td></td></tr><tr><td>·重量</td><td></td></tr></table>

# 2 前页表

该表包含文件的前页内容。它将前页内容划分成若干部分，其中division_name栏给出了DTD标记，按照这些标记可找到相应的前页内容。

表4-3-6.2 FrontMatter表  

<table><tr><td>栏名称</td><td>类型</td><td>飞机标记</td><td>发动机
标记</td><td>描述</td></tr><tr><td>FRONT_MATTER_ID*</td><td>INT</td><td>NA</td><td>NA</td><td>分配的唯一ID</td></tr><tr><td>@GEN.DOCS.DOC_ID**</td><td>INT</td><td>NA</td><td>NA</td><td>文件ID。通用纲要模型（GEN）中Docs表的外部关键字</td></tr><tr><td>division_name**</td><td>CHAR</td><td>([参见本文4-3-5-2])</td><td>([参见本文4-3-5-2])</td><td>前页内容的分段(部分)的名称。标准名称在下面给出</td></tr><tr><td>division_title</td><td>TEXT</td><td>&lt;title&gt;</td><td>&lt;title&gt;</td><td>分段标题</td></tr><tr><td>division_text</td><td>TEXT</td><td>([参见本文4-3-5-2])</td><td>([参见本文4-3-5-2])</td><td>一个分段的全部SGML片段</td></tr><tr><td>division_startoff</td><td>INT</td><td>NA</td><td>NA</td><td>通用纲要模型中的Doc表[参见本文4-3-1.7.1]中描述的division_text栏起始的相对位置</td></tr><tr><td>division_endoff</td><td>INT</td><td>NA</td><td>NA</td><td>通用纲要模型中的Doc表[参见本文4-3-1.7.1]中描述的division_text栏结束的相对位置</td></tr></table>

表 4-3-6.3 前页表 “division_name” 栏的标准分段名称值  

<table><tr><td>分段名称</td><td>类型</td><td>飞机标记</td><td>发动机
标记</td><td>描述</td></tr><tr><td>TRANS_letter</td><td>TEXT</td><td>&lt;transltr&gt;</td><td>&lt;transltr&gt;</td><td>更改的通用信息</td></tr><tr><td>INTRO</td><td>TEXT</td><td>&lt;intro&gt;</td><td>&lt;intro&gt;</td><td>文件信息</td></tr><tr><td>HOW_TO_USE</td><td>TEXT</td><td>没使用</td><td>&lt;howtouse&gt;</td><td>描述如何使用 TEM</td></tr></table>

# 3 有效性表

本表被当作该纲要模型中其它表的 EFFECTIVITY_MASK 栏中有效性信息编码的“关键字”来使用。对于数据库的 TEM 部分中给出的每个不同的有效性值，在该表中都有一个行来描述。

表 4-3-6.4 有效性表  

<table><tr><td>栏名称</td><td>类型</td><td>飞机标记</td><td>发动机标记</td><td>描述</td></tr><tr><td>effectivity_key*</td><td>CHAR</td><td>见注</td><td>见注</td><td>有效性关键字,用于标识资料中一个特定有效性的唯一值。该值在飞机与发动机数据库两者之间有不同的起源和语义(见注)</td></tr><tr><td>mask_position_nbr**</td><td>INT</td><td>NA</td><td>NA</td><td>EFFECTIVITY_MASK 中唯一的指定位置。MASK POSITION_NBR 应是从 1~n 之间的无符号整数,其中 n 为有效性表中的行数</td></tr></table>

注1：对于机身，数据库中所表示的每一个CEC号都与该表中的一行相对应。每行都有一个唯一的effectivity_key值(即一个CEC)，并给出一个唯一的MASK POSITION_NBR值，该值是在数据库创建时随机分配的。

注2：对于发动机，MSM数据库中所表示的每个不同型号代码都与该表中的一行相对应。每行都有一个唯一的effectivity_key值(即一个型号代码)，并给出一个唯一的MASK POSITION_NBR值，该值是在数据库创建时随机分配的。

# 4 目录表

该表用于存储所有 TEM 文件的目录。目录表设计成为可使用一条 SFQL 查询语句生成可访问的文本条目的方式，这样使目录的生成比较容易。这包括表中每个条目的摘要以及对包含实际信息的文件表的一个链接。

表 4-3-6.5 目录表  

<table><tr><td>栏名称</td><td>类型</td><td>飞机标记</td><td>发动机标记</td><td>描述</td></tr><tr><td>CONTENTS_ID*</td><td>INT</td><td>NA</td><td>NA</td><td>分配的唯一行标识符</td></tr><tr><td>@GEN.DOCS.DOC_ID**</td><td>INT</td><td>NA</td><td>NA</td><td>文件ID。通用纲要模型（GEN）中Doc表的外部关键字</td></tr><tr><td>entry_sequence_nbr**</td><td>INT</td><td>NA</td><td>NA</td><td>用于排放条目的编号，利用该编号使条目的排列与目录中的DOC_ID的顺序完全相同，该编号从1开始</td></tr><tr><td>entry_table_name</td><td>CHAR</td><td>NA</td><td>NA</td><td>该条目指向的纲要模型表名称</td></tr><tr><td>entry_key_name</td><td>CHAR</td><td>NA</td><td>NA</td><td>主关键字的栏名称。见注</td></tr><tr><td>@ENTRY_KEY_ID</td><td>INT</td><td>NA</td><td>NA</td><td>标识内容文本的主关键字值</td></tr><tr><td>effectivity_mask</td><td>BITFIELD</td><td>NA</td><td>NA</td><td>表示适用的有效性的模板（在数据库准备阶段分配）</td></tr><tr><td>effectivity_info</td><td>TEXT</td><td>See Note</td><td>Not Used</td><td>飞机/发动机的有效性信息</td></tr><tr><td>FM_Division_Name</td><td>CHAR</td><td>NA</td><td>NA</td><td>当条目是前文的分段时使用</td></tr><tr><td>entry_level</td><td>INT</td><td>NA See Note</td><td>NA See Note</td><td>表中的层次结构级别，其中1为最高级别</td></tr><tr><td>@PARENT_ID</td><td>INT</td><td>NA</td><td>NA</td><td>父条目的content_id。如果没有父条目（entry_level=1），则PARENT_ID值为NULL</td></tr><tr><td>entry_text</td><td>TEXT</td><td>&lt;title&gt; or &lt;TOC&gt;</td><td>&lt;title&gt;</td><td>TOC条目</td></tr><tr><td>entry_startoff</td><td>INT</td><td>NA</td><td>NA</td><td>通用纲要模型中的Doc表[参见本文4-3-1.7.1]中描述的entry_text栏起始的相对位置</td></tr><tr><td>entry_endoff</td><td>INT</td><td>NA</td><td>NA</td><td>通用纲要模型中的Doc表[参见本文4-3-1.7.1]中描述的entry_text栏结束的相对位置</td></tr><tr><td>key_code</td><td>CHAR</td><td>?key&gt;</td><td>?key&gt;</td><td>文件实例中唯一的一个位置标识（标识符）</td></tr><tr><td>section_nbr</td><td>CHAR</td><td>?sectnbr&gt;</td><td>?sectnbr&gt;</td><td>节号</td></tr><tr><td>tlsheet_nbr</td><td>CHAR</td><td>&lt;? toolnbr&gt;</td><td>&lt;? toolnbr&gt;</td><td>图页号</td></tr><tr><td>unit_nbr</td><td>CHAR</td><td>&lt;? unitnbr&gt;</td><td>&lt;? unitnbr&gt;</td><td>单元号</td></tr><tr><td>revision_date</td><td>DATE</td><td>&lt;? revdate&gt;</td><td>&lt;? revdate&gt;</td><td>更改日期</td></tr></table>

注：对于飞机，如果effectivity_text存在，它将只包含EFFECT元素的efftext属性值。  
注：这是如何使用entry_level的一个例子。

表 4-3-6.6 Front Matter 表  

<table><tr><td>entry_table_name</td><td>entry_level</td></tr><tr><td>前页</td><td>1</td></tr><tr><td>节</td><td>1</td></tr><tr><td>单元</td><td>2</td></tr><tr><td>TLSheet</td><td>2</td></tr><tr><td>TLSect</td><td>3</td></tr></table>

注：参考技术要求，entry_table具有单一的主关键字字栏。

# 5 更改提要表

该表用于返回反映修订中的更改提要信息。表的每一行内容表示了对纲要模型中其它表的一行中数据的一组修订摘要(在SGML中以一个位置标识出现)。

表 4-3-6.7 更改提要表  

<table><tr><td>栏名称</td><td>类型</td><td>飞机标记</td><td>发动机
标记</td><td>描述</td></tr><tr><td>HIGHLIGHTS_ID*</td><td>INT</td><td>NA</td><td>NA</td><td>分配的唯一行标识符</td></tr><tr><td>entry_table_name**</td><td>CHAR</td><td>NA</td><td>NA</td><td>该条目指向的纲要模型表名称</td></tr><tr><td>entry_key_name**</td><td>CHAR</td><td>NA</td><td>NA</td><td>主关键字的栏名称</td></tr><tr><td>@ENTRY_KEY_ID**</td><td>INT</td><td>NA</td><td>NA</td><td>主关键字值，用以标识适用于更改提要的文件单元</td></tr><tr><td>@GEN.DOCS.DOC_ID**</td><td>INT</td><td>NA</td><td>NA</td><td>文件ID。通用纲要模型中的Doc表(GEN)的外部关键字</td></tr><tr><td>EFFECTIVITY_MASK**</td><td>BITFIELD</td><td>NA</td><td>NA</td><td>表示适用的有效性模板。</td></tr><tr><td>effectivity_info</td><td>TEXT</td><td></td><td></td><td>飞机/发动机的有效性信息</td></tr><tr><td>section_nbr</td><td>CHAR</td><td></td><td></td><td>节号</td></tr><tr><td>tlsheet_nbr</td><td>CHAR</td><td></td><td></td><td>工具表编号</td></tr><tr><td>unit_nbr</td><td>CHAR</td><td></td><td></td><td>单元编号</td></tr><tr><td>graphic_title</td><td>TEXT</td><td></td><td></td><td>当图形或图页为更改目标时使用。</td></tr><tr><td>sheet_nbr</td><td>INT</td><td></td><td></td><td>当图页(示图)为更改目标时使用。</td></tr><tr><td>FM_Division_Name</td><td>CHAR</td><td>NA</td><td>NA</td><td>当FM为更改目标时使用</td></tr><tr><td>key_code</td><td>CHAR</td><td>&lt;?key&gt;</td><td>&lt;?key&gt;</td><td>文件实例中唯一的一个位置标识(标识符)</td></tr><tr><td>change_description</td><td>CHAR</td><td></td><td></td><td>修订过程中所作更改的描述</td></tr></table>

# 6 节表

该表用于返回一个或多个手册的节信息。一节的全部文本用一个给定行中的section_text栏来表示。

表4-3-6.8 节表  

<table><tr><td>栏名称</td><td>类型</td><td>飞机标记</td><td>发动机标记</td><td>描述</td></tr><tr><td>SECTION_ID*</td><td>INT.</td><td>NA</td><td>NA</td><td>分配的唯一ID</td></tr><tr><td>section_nbr**</td><td>CHAR</td><td>&lt;section sectnbr&gt;</td><td>&lt;section sectnbr&gt;</td><td>节号</td></tr><tr><td>@GEN.DOCS.DOC_ID**</td><td>INT</td><td>NA</td><td>NA</td><td>文件ID。通用纲要模型中的Doc表(GEN)的外部关键字</td></tr><tr><td>revision_date</td><td>DATE</td><td>&lt;section revdate&gt;</td><td>&lt;section revdate&gt;</td><td>更改日期</td></tr><tr><td>section_type</td><td>CHAR</td><td>&lt;section type&gt;</td><td>&lt;section type&gt;</td><td>节类型(见下表)</td></tr><tr><td>key_code</td><td>CHAR</td><td>&lt;section key&gt;</td><td>&lt;section key&gt;</td><td>文件实例中唯一的一个位置标识(标识符)</td></tr><tr><td>seq_nbr</td><td>INT</td><td>NA</td><td>NA</td><td>资料中行的逻辑顺序</td></tr><tr><td>section_title</td><td>TEXT</td><td>&lt;title&gt;</td><td>&lt;title&gt;</td><td>节标题</td></tr><tr><td>section_text</td><td>TEXT</td><td>&lt;section&gt;</td><td>&lt;section&gt;</td><td>一节的所有SGML片段</td></tr><tr><td>section_startoff</td><td>INT</td><td>NA</td><td>NA</td><td>通用纲要模型中的Doc表[标题4-3-1.7.1]中描述的section_text栏起始的相对位置</td></tr><tr><td>section_endoff</td><td>INT</td><td>NA</td><td>NA</td><td>通用纲要模型中的Doc表[参见本文4-3-1.7.1]中描述的section_text栏结束的相对位置</td></tr></table>

表 4-3-6.9 标准节类型表  

<table><tr><td>类型</td><td>描述</td></tr><tr><td>IDX</td><td>索引</td></tr><tr><td>CAT</td><td>操纵和辅助工具</td></tr><tr><td>CTL</td><td>交叉参考工具清单</td></tr><tr><td>MDX</td><td>维修索引</td></tr><tr><td>MFR</td><td>标准设备供应商代码</td></tr><tr><td>MHE</td><td>材料处理设备</td></tr><tr><td>MSE</td><td>制造商的支持设备</td></tr><tr><td>OVX</td><td>检修索引</td></tr><tr><td>TDS</td><td>工具数据表</td></tr><tr><td>TEE</td><td>工具/发动机有效性</td></tr><tr><td>OTH</td><td>其它</td></tr></table>

# 7 TLSHEET表

该表用于返回节内的工具表信息。一个工具表的全部文本用一个给定行中的TLSHEET_TEXT栏来表示。

表4-3-6.10 Tlsheet表  

<table><tr><td>栏名称</td><td>类型</td><td>飞机标记</td><td>发动机标记</td><td>描述</td></tr><tr><td>TLSHEET_ID*</td><td>INT</td><td>NA</td><td>NA</td><td>分配的唯一ID</td></tr><tr><td>tlsheet_nbr**</td><td>CHAR</td><td></td><td></td><td>工具号</td></tr><tr><td>@SECTION.SECTION_ID**</td><td>INT</td><td>NA</td><td>NA</td><td>对节表的参考</td></tr><tr><td>@GEN.DOCS.DOC_ID</td><td>INT</td><td>NA</td><td>NA</td><td>文件ID。通用纲要模型中的Doc表(GEN)的外部关键字</td></tr><tr><td>section_nbr</td><td>CHAR</td><td></td><td></td><td>节号</td></tr><tr><td>revision_date</td><td>DATE</td><td></td><td></td><td>更改日期</td></tr><tr><td>key_code</td><td>CHAR</td><td></td><td></td><td>文件实例中唯一的一个位置标识(标识符)</td></tr><tr><td>tlsheet_type</td><td>CHAR</td><td></td><td></td><td>TLSHEET的标准化类型</td></tr><tr><td>tlsheet_type_other</td><td>CHAR</td><td></td><td></td><td>“其它”TLSHEET类型的非标准化文本或标题。在tlsheet_type=&quot;OTH&quot;时使用</td></tr><tr><td>seq_nbr</td><td>INT</td><td>NA</td><td>NA</td><td>资料中行的逻辑顺序</td></tr><tr><td>tlsheet_title</td><td>TEXT</td><td></td><td></td><td>工具表标题</td></tr><tr><td>tlsheet_fim_text</td><td>TEXT</td><td></td><td></td><td>表的前页内容</td></tr><tr><td>tlsheet_text</td><td>TEXT</td><td></td><td></td><td>一个TLSHEET的所有SGML片段</td></tr><tr><td>tlsheet_startoff</td><td>INT</td><td>NA</td><td>NA</td><td>通用纲要模型中的Doc表[参见本文4-3-1.7.1]中描述的tlsheet_text栏起始的相对位置</td></tr><tr><td>tlsheet_endoff</td><td>INT</td><td>NA</td><td>NA</td><td>通用纲要模型中的Doc表[参见本文4-3-1.7.1]中描述的tlsheet_text栏结束的相对位置</td></tr></table>

# 8 单元表

单元在手册中是等同于工具表级别的一个级别，但它并不是工具表。该表的每一行表示一个单元。一个单元的全部文本包含在给定行中的unit_text栏。

表 4-3-6.11 单元表  

<table><tr><td>栏名称</td><td>类型</td><td>飞机标记</td><td>发动机标记</td><td>描述</td></tr><tr><td>UNIT_ID*</td><td>INT</td><td>NA</td><td>NA</td><td>分配的唯一ID</td></tr><tr><td>@SECTION.SECTION_ID**</td><td>INT</td><td>NA</td><td>NA</td><td>参考节表</td></tr><tr><td>unit_nbr**</td><td>CHAR</td><td></td><td></td><td>单元号</td></tr><tr><td>unit_type**</td><td>CHAR</td><td></td><td></td><td>类型(见下表)</td></tr><tr><td>unit_type_other</td><td>CHAR</td><td></td><td></td><td>“其它”单元类型的非标准化文本或标题。在unit_type=“OTH”时使用</td></tr><tr><td>@GEN.DOCS.DOC_ID</td><td>INT</td><td>NA</td><td>NA</td><td>文件ID。通用纲要模型中的Doc表(GEN)的外部关键字</td></tr><tr><td>section_nbr</td><td>CHAR</td><td></td><td></td><td>节号</td></tr><tr><td>revision_date</td><td>DATE</td><td></td><td></td><td>更改日期</td></tr><tr><td>key_code</td><td>CHAR</td><td></td><td></td><td>文件实例中唯一的一个位置标识(标识符)</td></tr><tr><td>seq_nbr</td><td>INT</td><td>NA</td><td>NA</td><td>资料中行的逻辑顺序</td></tr><tr><td>unit_title</td><td>TEXT</td><td></td><td></td><td>单元标题</td></tr><tr><td>unit_fmt_text</td><td>TEXT</td><td></td><td></td><td>单元的前页内容</td></tr><tr><td>unit_text</td><td>TEXT</td><td></td><td></td><td>一个单元的所有SGML片段</td></tr><tr><td>unit_startoff</td><td>INT</td><td>NA</td><td>NA</td><td>通用纲要模型中的Doc表[参见本文4-3-1.7.1]中描述的unit_text栏起始的相对位置</td></tr><tr><td>unit_endoff</td><td>INT</td><td>NA</td><td>NA</td><td>通用纲要模型中的Doc表[参见本文4-3-1.7.1]中描述的unit_text栏结束的相对位置]</td></tr></table>

表 4-3-6.12 单元表的标准类型  

<table><tr><td>类型</td><td>描述</td></tr><tr><td>CTL</td><td>交叉参考工具清单</td></tr><tr><td>IDX</td><td>索引</td></tr><tr><td>MDX</td><td>维修索引</td></tr><tr><td>MFR</td><td>标准设备供应商清单</td></tr><tr><td>OVX</td><td>检修索引</td></tr><tr><td>TEE</td><td>工具/发动机有效性</td></tr></table>

# 9 TLSECT表

该表的每一行包含针对一个工具表的单个节，称为“CPSECT”。该部分的全部文本用给定行中的cpsect_text栏来表示。

表 4-3-6.13 Tlsect 表  

<table><tr><td>栏名称</td><td>类型</td><td>飞机标记</td><td>发动机标记</td><td>描述</td></tr><tr><td>TLSECT_ID*</td><td>INT</td><td>NA</td><td>NA</td><td>分配的唯一ID</td></tr><tr><td>@TLSHEET.TLSHEET_ID**</td><td>INT</td><td>NA</td><td>NA</td><td>参考TLSHEET表</td></tr><tr><td>tlsect_type**</td><td>CHAR</td><td></td><td></td><td>工具节类型。见下面的TLSECT类型表</td></tr><tr><td>tlsect_type_other</td><td>CHAR</td><td></td><td></td><td>“其它”类型的非标准化文本或标题。在tlsect_type=&quot;OTH&quot;时使用</td></tr><tr><td>EFFECTIVITY_MASK</td><td>BITFIELD</td><td>NA</td><td>NA</td><td>表示适用的有效性模板(在数据库准备阶段被分配)</td></tr><tr><td>@GEN.DOCS.DOC_ID</td><td>INT</td><td>NA</td><td>NA</td><td>文件ID。通用纲要模型中的Doc表(GEN)的外部关键字</td></tr><tr><td>effectivity_info</td><td>TEXT</td><td></td><td></td><td>飞机/发动机的有效性信息</td></tr><tr><td>section_nbr</td><td>INT</td><td></td><td></td><td>包含该图页的节号</td></tr><tr><td>tlsheet_nbr</td><td>CHAR</td><td></td><td></td><td>该表编号</td></tr><tr><td>seq_nbr</td><td>INT</td><td>NA</td><td>NA</td><td>资料中行的逻辑顺序</td></tr><tr><td>tlsect_title</td><td>TEXT</td><td></td><td></td><td>TLSECT标题</td></tr><tr><td>tlsect_text</td><td>TEXT</td><td></td><td></td><td>所有SGML片段</td></tr><tr><td>tlsect_startoff</td><td>INT</td><td>NA</td><td>NA</td><td>通用纲要模型中的Doc表[参见本文4-3-1.7.1]中描述的tlsect_text栏起始的相对位置</td></tr><tr><td>tlsect_endoff</td><td>INT</td><td>NA</td><td>NA</td><td>通用纲要模型中的Doc表[参见本文4-3-1.7.1]中描述的tlsect_text栏结束的相对位置</td></tr></table>

表 4-3-6.14 Tlsect 表的标准类型  

<table><tr><td>类型</td><td>描述</td></tr><tr><td>MCT</td><td>制造类别</td></tr><tr><td>DES</td><td>工具名称和/或描述</td></tr><tr><td>DIM</td><td>规格</td></tr><tr><td>HIS</td><td>工具历史记录</td></tr><tr><td>OTH</td><td>其它</td></tr><tr><td>PLI</td><td>零件清单/详细清单</td></tr><tr><td>PNU</td><td>目的和用途</td></tr><tr><td>TEXT</td><td>CONSUMABLE_IDX</td></tr><tr><td>QPU</td><td>每操作单元所需的数量</td></tr><tr><td>SPT</td><td>支持工具</td></tr><tr><td>TLM</td><td>工具维护</td></tr><tr><td>WGT</td><td>重量</td></tr></table>

# 10 图形列表

该表包含手册中图形的信息。图形页的二进制图像可在图页表中查到。

表 4-3-6.15 图形表  

<table><tr><td>栏名称</td><td>类型</td><td>飞机标记</td><td>发动机标记</td><td>描述</td></tr><tr><td>GRAPHIC_ID*</td><td>INT</td><td>NA</td><td>NA</td><td>分配的唯一ID</td></tr><tr><td>key_code**</td><td>CHAR</td><td>&lt;graphic key&gt;</td><td>&lt;graphic key&gt;</td><td>图形的唯一标识符</td></tr><tr><td>@GEN.DOCS.DO C_ID**</td><td>INT</td><td>NA</td><td>NA</td><td>文件ID。通用纲要模型(GEN)中的Doc表的外部关键字</td></tr><tr><td>effectivity_mask</td><td>BITFIELD</td><td>NA</td><td>NA</td><td>表示适用的有效性模板(在数据库准备阶段被分配</td></tr><tr><td>effectivity_info</td><td>TEXT</td><td>-effect&gt;</td><td>-effect&gt;</td><td>飞机/发动机的有效性信息</td></tr><tr><td>graphic_title</td><td>TEXT</td><td>&lt;title&gt;</td><td>&lt;title&gt;</td><td>图形标题</td></tr><tr><td>sheet_count</td><td>INT</td><td>NA</td><td>NA</td><td>图形中的图页编号</td></tr><tr><td>revision_date</td><td>DATE</td><td>&lt;graphic revdate&gt;</td><td>&lt;graphic revdate&gt;</td><td>更改日期</td></tr><tr><td>seq_nbr</td><td>INT</td><td>NA</td><td>NA</td><td>资料中行的逻辑顺序</td></tr><tr><td>graphic_text</td><td>TEXT</td><td>&lt;graphic&gt;</td><td>&lt;graphic&gt;</td><td>图形编号的所有SGML片段</td></tr></table>

# 11 图页表

该表包含图形的图页，并显示它们与该图形的关系。示图可按ATA标准格式根据sheet_bin栏检索，并可选择根据file_name栏中显示的文件来检索。

表4-3-6.16 图页表  

<table><tr><td>栏名称</td><td>类型</td><td>飞机标记</td><td>发动机标记</td><td>描述</td></tr><tr><td>SHEET_ID*</td><td>INT</td><td>NA</td><td>NA</td><td>分配的唯一ID</td></tr><tr><td>@GRAPHIC.GRAPH
IC_ID**</td><td>INT</td><td>NA</td><td>NA</td><td>对图形表的参考</td></tr><tr><td>sheet_nbr**</td><td>INT</td><td></td><td></td><td>父图形中该图页的顺序号</td></tr><tr><td>key_code**</td><td>CHAR</td><td>&lt;sheet key&gt;</td><td>&lt;sheet key&gt;</td><td>图页的唯一标识符</td></tr><tr><td>@GEN.DOCS.DOC_ID**</td><td>INT</td><td>NA</td><td>NA</td><td>文件 ID。通用纲要模型(GEN)中的 Doc 表的外部关键字</td></tr><tr><td>EFFECTIVITY_MASK_K</td><td>BITFIELD</td><td>NA</td><td>NA</td><td>表示适用的有效性模板(在数据库准备阶段被分配)</td></tr><tr><td>effectivity_info</td><td>TEXT</td><td>-effect&gt;</td><td>-effect&gt;</td><td>飞机/发动机的有效性信息</td></tr><tr><td>sheet_title</td><td>TEXT</td><td>&lt;title&gt;</td><td>&lt;title&gt;</td><td>图页标题</td></tr><tr><td>sheet_type_code</td><td>CHAR</td><td>NA</td><td>NA</td><td>标识图形编码格式</td></tr><tr><td>sheet_text</td><td>TEXT</td><td>&lt;sheet&gt;</td><td>&lt;sheet&gt;</td><td>一个图页编号的所有 SGML 片段</td></tr><tr><td>revision_date</td><td>DATE</td><td>&lt;sheet revdate&gt;</td><td>&lt;sheet revdate&gt;</td><td>更改日期</td></tr><tr><td>sheet_bin</td><td>GRAPHIC</td><td>NA</td><td>NA</td><td>二进制编码图形</td></tr><tr><td>file_name</td><td>CHAR</td><td>NA</td><td>NA</td><td>包含图形的可选文件名</td></tr></table>

# 4-3-7 布线手册(WM)纲要模型

# 1 前言

本文件随同 ATA 通用纲要模型 ([参见本文 4-3-1])一起, 提供适用于 ATA 布线手册 (WM) 的检索纲要模型。该纲要模型称为 “WDM” 纲要模型, 它属于 “ATA_维修” 目录。该纲要模型仅适用于飞机。

# 2 Front_Matter(前页内容)表

该表包含文件的前页内容。它将正文前内容划分成若干部分，在division_name栏显示了WDM DTD标记的来源。

表 4-3-7.1 Front matter 表  

<table><tr><td>栏名称</td><td>类型</td><td>飞机标志</td><td>描述</td></tr><tr><td>FRONT_MATTER_ID*</td><td>INT</td><td>NA</td><td>分配的唯一ID</td></tr><tr><td>@GEN.DOCS.DOC_ID**</td><td>INT</td><td>NA</td><td>文件ID。通用纲要模型 (GEN)中Doc表的外部关键字</td></tr><tr><td>division_name**</td><td>CHAR</td><td>([参见4-3-7-2])</td><td>前页内容的分段(部分)的名称。标准名称在下面给出</td></tr><tr><td>division_title</td><td>TEXT</td><td>&lt;title&gt;</td><td>分段标题</td></tr><tr><td>division_text</td><td>TEXT</td><td>([参见4-3-7-2])</td><td>一个分段的全部SGML片段</td></tr><tr><td>division_startoff</td><td>INT</td><td>NA</td><td>通用纲要模型中的Doc表[参见本文4-3-1.7.1]中描述的division_text栏起始的相对位置</td></tr><tr><td>division_endoff</td><td>INT</td><td>NA</td><td>通用纲要模型中的Doc表[参见本文4-3-1.7.1]中描述的division_text栏结束的相对位置</td></tr></table>

表 4-3-7.2 “division_name” 栏的标准分段名称的值  

<table><tr><td>分段名称</td><td>类型</td><td>飞机标志</td><td>描述</td></tr><tr><td>TRANS LETTER</td><td>TEXT</td><td>&lt;transltr&gt;</td><td>数据位于被修订文件实例的开始，以给出修订的概括信息。也有可能包含临时更改的合并信息。</td></tr><tr><td>TRLIST</td><td>TEXT</td><td>&lt;trlist&gt;</td><td>标识文件修订时的TR及其状态</td></tr><tr><td>INTRO</td><td>TEXT</td><td>&lt;intro&gt;</td><td>标识整个文件或主要文件结构的前言信息</td></tr><tr><td>EFFECT_X_REF</td><td>TEXT</td><td>&lt;effxref&gt;</td><td>关于用不同方法标识文件实例中的一个基本有效性组以及这些方法如何相互联系的数据。</td></tr><tr><td>CUSTOMER_REV.Record</td><td>TEXT</td><td>&lt;cusrevrec&gt;</td><td>提供给用户的页，以记录每项更改归入手册的时间和相关责任人</td></tr><tr><td>SB_LIST</td><td>TEXT</td><td>&lt;sblist&gt;</td><td>如果存在服务通报，该分段用来标识服务通报的当前合并状态数据，。[编辑者注：在SGML中，如果没有发布或没有有效的飞机/发动机维护通报，则在发送时用IEMPTY元素代替SBDATA，以指出这种情况。]</td></tr><tr><td>COC_LIST</td><td>TEXT</td><td>&lt;coclist&gt;</td><td>标识COC的当前合并状态的数据。如果没有发布或没有有效的飞机/发动机COC，则在发送时用IEMPTY元素代替COCDATA元素。</td></tr><tr><td>MANUFACTURER_REV.Record</td><td>TEXT</td><td>&lt;mfrrevrec&gt;</td><td>针对一个手册所发布更改单的累计清单。</td></tr><tr><td>TITLE_PAGE</td><td>TEXT</td><td>&lt;ttlpage&gt;</td><td>手册的首页；通常包含文件所有者的名称、文件编号以及制造商的名称和地址</td></tr></table>

注：机身手册“如何使用”的信息位于INTRO。

# 3 有效性表

本表被当作该纲要模型中其它表的 EFFECTIVITY_MASK 栏中有效性信息编码的“关键字”来使用。对于 WM 中表示的每个不同的有效性值，在该表中都有一个行来描述。

表 4-3-7.3 有效性表  

<table><tr><td>栏名称</td><td>类型</td><td>飞机标志</td><td>描述</td></tr><tr><td>Effectivity_key*</td><td>CHAR</td><td>见注1</td><td>有效性关键字是用于标识资料中一个特定有效性的唯一值。</td></tr><tr><td>mask_position_nbr**</td><td>INT</td><td>NA</td><td>EFFECTIVITY_MASK 中唯一的指定位置。MASK POSITION NBR 应是从 1~n 之间的无符号整数，其中 n 为有效性表中的行数。</td></tr><tr><td>line_nbr</td><td>CHAR</td><td></td><td>制造商的有序的生产流水线号</td></tr><tr><td>var_nbr</td><td>CHAR</td><td></td><td>改型的工程号</td></tr><tr><td>serial_nbr</td><td>CHAR</td><td>&lt;msnbr&gt;</td><td>固定ID号</td></tr><tr><td>Registration_nbr</td><td>CHAR</td><td>&lt;acn&gt;</td><td>尾翼号</td></tr><tr><td>customer_code</td><td>CHAR</td><td>&lt;cus&gt;</td><td>ICAO字母数字代码，以标识航空公司接收或发送的数据</td></tr><tr><td>model_type</td><td>CHAR</td><td>&lt;modtype&gt;</td><td>飞机有效性交叉参考表中的型号/类型。标识文件实例所涉及的飞机型号或类型。</td></tr></table>

注：对于飞机，数据库中所表示的每一个CEC号都与该表中的一行相对应。每行都有一个唯一的effectivity_key值（即一个CEC），并给出一个唯一的MASK POSITION_NBR值，该值是在数据库创建时随机分配的。

# 4 目录表

该表用于存储所有 WM 文件的目录。目录表设计成为可使用一条 SFQL 查询语句生成可访问的文本条目的方式，这样使目录的生成比较容易。这包括表中每个条目的摘要以及对包含实际信息的文件表的一个链接。

表 4-3-7.4 目录表  

<table><tr><td>栏名称</td><td>类型</td><td>飞机标志</td><td>描述</td></tr><tr><td>CONTENTS_ID*</td><td>INT</td><td>NA</td><td>分配的唯一行标识符</td></tr><tr><td>@GEN.DOCS.DOC_ID**</td><td>INT</td><td>NA</td><td>文件ID。通用纲要模型 (GEN)中Doc表的外部关键字</td></tr><tr><td>entry_sequence_nbr**</td><td>INT</td><td>NA</td><td>用于排放条目的编号,利用该编号使条目的排列与目录中的DOC_ID的顺序完全相同,该编号从1开始</td></tr><tr><td>entry_table_name</td><td>CHAR</td><td>NA</td><td>该条目指向的纲要模型表名称</td></tr><tr><td>entry_key_name</td><td>CHAR</td><td>NA</td><td>主关键字的栏名称。见注1</td></tr><tr><td>@ENTRY_KEY_ID</td><td>INT</td><td>NA</td><td>标识目录文本的主关键字值</td></tr><tr><td>Effectivity_mask</td><td>BITFIELD</td><td>NA</td><td>表示适用的有效性模板(在数据库准备阶段分配)</td></tr><tr><td>Effectivity_info</td><td>TEXT</td><td></td><td>飞机/发动机的有效性信息</td></tr><tr><td>FM_Division_Name</td><td>CHAR</td><td>NA</td><td>当条目是前页内容的分段时使用</td></tr><tr><td>entry_level</td><td>INT</td><td>NA 见注2</td><td>表中的层次结构级别,其中1为最高级别</td></tr><tr><td>@parent_ID</td><td>INT</td><td>NA</td><td>父条目的content_id。如果没有父条目(entry_level=1),则PARENT_ID值为NULL</td></tr><tr><td>entry_text</td><td>TEXT</td><td></td><td>提供该内容条目“文本”的“位置标识”标题</td></tr><tr><td>entry_startoff</td><td>INT</td><td>NA</td><td>通用纲要模型中的Doc表[参见本文4-3-1.7.1]中描述的entry_text栏起始的相对位置</td></tr><tr><td>entry_endoff</td><td>INT</td><td>NA</td><td>通用纲要模型中的Doc表[参见本文4-3-1.7.1]中描述的entry_text栏结束的相对位置</td></tr><tr><td>key_code</td><td>CHAR</td><td>&lt;?key&gt;</td><td>文件实例中唯一的一个位置标识(标识符)</td></tr><tr><td>Chapter_nbr</td><td>CHAR</td><td>&lt;?chapnbr&gt;</td><td>章号</td></tr><tr><td>Section_nbr</td><td>CHAR</td><td>&lt;?sectnbr&gt;</td><td>节号</td></tr><tr><td>Subject_nbr</td><td>CHAR</td><td>&lt;?subjnbr&gt;</td><td>题目号</td></tr><tr><td>page_nbr</td><td>CHAR</td><td>&lt;?pagerbr&gt;</td><td>在章一节一题目编号法中的布线图或系统原理图的顺序页编号。布线图通常以001开始,系统原理图以101开始。这些编号删除后不能重新定制、使用或分配。</td></tr><tr><td>schematic_nbr</td><td>CHAR</td><td>&lt;? schemnbr&gt;</td><td>标识一个飞机的构型中或章一节一题目一页编号范围内的偏差</td></tr><tr><td>revision_date</td><td>DATE</td><td>&lt;? revdate&gt;</td><td>更改日期</td></tr></table>

注3：这是一个在飞机手册中如何使用entry_level的实例。

<table><tr><td>entry_table_name</td><td>entry_level</td></tr><tr><td>前页</td><td>1</td></tr><tr><td>章</td><td>1</td></tr><tr><td>节</td><td>2</td></tr><tr><td>题目</td><td>3</td></tr><tr><td>页号组</td><td>4</td></tr><tr><td>原理图</td><td>5</td></tr></table>

注4：参考技术要求，entry_table具有单一的主关键字栏。

# 5 更改提要表

该表用于返回反映修订中的更改提要信息。

表 4-3-7.5 更改提要表  

<table><tr><td>栏名称</td><td>类型</td><td>飞机标志</td><td>描 述</td></tr><tr><td>HIGHLIGHTS_ID*</td><td>INT</td><td>NA</td><td>分配的唯一行标识符</td></tr><tr><td>entry_table_name</td><td>CHAR</td><td>NA</td><td>该条目指向的纲要模型表名称</td></tr><tr><td>entry_key_name</td><td>CHAR</td><td>NA</td><td>主关键字的栏名称</td></tr><tr><td>@ENTRY_KEY_ID</td><td>INT</td><td>NA</td><td>主关键字值，用以标识适用于更改提要的文件单元</td></tr><tr><td>@GEN.DOC
CS.DOC_ID</td><td>INT</td><td>NA</td><td>文件ID。通用纲要模型(GEN)中Doc表的外部关键字</td></tr><tr><td>effectivity_mask</td><td>BITFIELD</td><td>NA</td><td>表示适用的有效性模板</td></tr><tr><td>effectivity_info</td><td>TEXT</td><td>-effect&gt;</td><td>飞机/发动机的有效性信息</td></tr><tr><td>chapter_nbr</td><td>CHAR</td><td>&lt;? chapnbr&gt;</td><td>章号</td></tr><tr><td>section_nbr</td><td>CHAR</td><td>&lt;? sectnbr&gt;</td><td>节号</td></tr><tr><td>subject_nbr</td><td>CHAR</td><td>&lt;? subjbr&gt;</td><td>题目号</td></tr><tr><td>page_nbr</td><td>CHAR</td><td>&lt;? págenbr&gt;</td><td>在章一节一题目编号中的布线图或系统原理图的顺序页编号。布线图通常以001开始，系统原理图以101开始。这些编号删除后不能重新定制、使用或分配。</td></tr><tr><td>schematic_nbr</td><td>CHAR</td><td>&lt;? schemnbr&gt;</td><td>标识一个飞机的构型中或章一节一题目一页编号范围内的偏差</td></tr><tr><td>title</td><td>TEXT</td><td>&lt;title&gt;</td><td>当适用时，指参考对象的标题</td></tr><tr><td>sheet_nbr</td><td>INT</td><td>&lt;sheet sheetnbr&gt;</td><td>在图形的页为更改目标时使用</td></tr><tr><td>FM_Division_Name</td><td>CHAR</td><td>NA</td><td>在FM为更改目标时使用。详细内容见FRONT_MATTER表。</td></tr><tr><td>key_code</td><td>CHAR</td><td>&lt;? key&gt;</td><td>文件实例中唯一的一个位置标识(标识符)</td></tr><tr><td>change_description</td><td>CHAR</td><td>&lt;chgdesc&gt;</td><td>对修订过程中所作更改的描述</td></tr></table>

# 6 章表

该表用于返回一个或多个手册的章信息。一个章的全部文本用一个给定行中的 chapter_text 栏来表示。

表4-3-7.6 章表  

<table><tr><td>栏名称</td><td>类型</td><td>飞机标志</td><td>描述</td></tr><tr><td>CHAPTER_ID*</td><td>INT</td><td>NA</td><td>分配的唯一ID</td></tr><tr><td>chapter_nbr**</td><td>CHAR</td><td>&lt;chapter chapnbr&gt;</td><td>章号</td></tr><tr><td>@GEN.DOCS.DOC_ID**</td><td>INT</td><td>NA</td><td>文件ID。通用纲要模型(GEN)中Doc表的外部关键字</td></tr><tr><td>effectivity_mask**</td><td>BITFIELD</td><td>NA</td><td>表示适用的有效性模板(在数据库准备阶段分配)</td></tr><tr><td>effectivity_info</td><td>TEXT</td><td>-effect&gt;</td><td>飞机/发动机的有效性信息</td></tr><tr><td>revision_date</td><td>DATE</td><td>&lt;chapter revdate&gt;</td><td>更改日期</td></tr><tr><td>key_code</td><td>CHAR</td><td>&lt;chapter key&gt;</td><td>文件实例中唯一的一个位置标识(标识符)</td></tr><tr><td>seq_nbr</td><td>INT</td><td>NA</td><td>资料中行的逻辑顺序</td></tr><tr><td>chapter_title</td><td>TEXT</td><td>&lt;title&gt;</td><td>章标题</td></tr><tr><td>chapter_text</td><td>TEXT</td><td>&lt;chapter&gt;</td><td>一章的所有SGML片段</td></tr><tr><td>chapter_startoff</td><td>INT</td><td>NA</td><td>通用纲要模型中的Doc表[参见本文4-3-1.7.1]中描述的chapter_text栏起始的相对位置</td></tr><tr><td>chapter_endoff</td><td>INT</td><td>NA</td><td>通用纲要模型中的Doc表[参见本文4-3-1.7.1]中描述的chapter_text栏结束的相对位置</td></tr></table>

# 7 节表

该表用于返回一个或多个手册的节信息。一节的全部文本用一个给定行中的section_text栏来表示。

表4-3-7.7 节表  

<table><tr><td>栏名称</td><td>类型</td><td>飞机标志</td><td>描述</td></tr><tr><td>SECTION_ID*</td><td>INT</td><td>NA</td><td>分配的唯一ID</td></tr><tr><td>section_nbr**</td><td>CHAR</td><td>&lt;section sectnbr&gt;</td><td>节号</td></tr><tr><td>@CHAP TER.CHAPTER_ID**</td><td>INT</td><td>NA</td><td>参考章表</td></tr><tr><td>@GEN.DOCS.DOC_ID* *</td><td>INT</td><td>NA</td><td>文件ID。通用纲要模型(GEN)中Doc表的外部关键字</td></tr><tr><td>chapter_nbr</td><td>CHAR</td><td>&lt;section chapnbr&gt;</td><td>章号</td></tr><tr><td>revision_date</td><td>DATE</td><td>&lt;section revdate&gt;</td><td>更改日期</td></tr><tr><td>key_code</td><td>CHAR</td><td>&lt;section key&gt;</td><td>一个位置标识(标识符),在文件样本中是唯一的</td></tr><tr><td>seq_nbr</td><td>INT</td><td>NA</td><td>资料中行的逻辑顺序</td></tr><tr><td>section_title</td><td>TEXT</td><td>&lt;title&gt;</td><td>节标题</td></tr><tr><td>section_text</td><td>TEXT</td><td>&lt;section&gt;</td><td>一节的所有SGML片段</td></tr><tr><td>section_startoff</td><td>INT</td><td>NA</td><td>通用纲要模型中的Doc表[参见本文4-3-1.7.1]中描述的section_text栏起始的相对位置</td></tr><tr><td>section_endoff</td><td>INT</td><td>NA</td><td>通用纲要模型中的Doc表[参见本文4-3-1.7.1]中描述的section_text栏结束的相对位置</td></tr></table>

# 8 题目表

该表用于返回一个或多个手册的题目信息。一个题目的全部文本用一个给定行中的 subject_text 栏来表示。

表 4-3-7.8 题目表  

<table><tr><td>栏名称</td><td>类型</td><td>飞机标志</td><td>描述</td></tr><tr><td>SUBJECT_ID*</td><td>INT</td><td>NA</td><td>分配的唯一ID</td></tr><tr><td>subject_nbr**</td><td>CHAR</td><td>&lt;sub&gt;subject sub jnbr&gt;</td><td>题目号</td></tr><tr><td>@SECTION SECTION_ID**</td><td>INT</td><td>NA</td><td>参考节表</td></tr><tr><td>@GEN.DOCS.DOC_ID* *</td><td>INT</td><td>NA</td><td>文件ID。通用纲要模型(GEN)中Doc表的外部关键字</td></tr><tr><td>chapter_nbr</td><td>CHAR</td><td>&lt;sub&gt;chapnbr&gt;</td><td>章号</td></tr><tr><td>section_nbr</td><td>CHAR</td><td>&lt;sub&gt;sectnbr&gt;</td><td>节号</td></tr><tr><td>revision_date</td><td>DATE</td><td>&lt;sub&gt;revdate&gt;</td><td>更改日期</td></tr><tr><td>key_code</td><td>CHAR</td><td>&lt;sub&gt;subject key&gt;</td><td>文件实例中唯一的一个位置标识(标识符)</td></tr><tr><td>seq_nbr</td><td>INT</td><td>NA</td><td>资料中行的逻辑顺序</td></tr><tr><td>subject_title</td><td>TEXT</td><td>&lt;title&gt;</td><td>题目的标题</td></tr><tr><td>subject_text</td><td>TEXT</td><td>&lt;object&gt;</td><td>一个标题的所有SGML片段</td></tr><tr><td>subject_startoff</td><td>INT</td><td>NA</td><td>通用纲要模型中的Doc表[参见本文4-3-1.7.1]中描述的 subject_text 栏起始的相对位置</td></tr><tr><td>subject_endoff</td><td>INT</td><td>NA</td><td>通用纲要模型中的Doc表[参见本文4-3-1.7.1]中描述的 subject_text 栏结束的相对位置</td></tr></table>

# 9 页号组表

该表用于返回一个或多个手册的页号组的信息。将一个页号组(用DTD中题目元素下的图形元素进行描述)定义为一组原理图。一个页号组的全部文本用一个给定行中的pagegroup_text栏来表示。

表 4-3-7.9 页号组表  

<table><tr><td>栏名称</td><td>类型</td><td>飞机标记(见注1)</td><td>描述</td></tr><tr><td>PAGEGROUP_ID*</td><td>INT</td><td>NA</td><td>分配的唯一ID</td></tr><tr><td>pagegroup_nbr**</td><td>CHAR</td><td>&lt;graphic pagenbrr&gt;</td><td>页号组编号</td></tr><tr><td>@SECTION SECTION_ID**</td><td>INT</td><td>NA</td><td>参见节表</td></tr><tr><td>@GEN.DOCS.DOC_ID* *</td><td>INT</td><td>NA</td><td>文件ID。通用纲要模型(GEN)中Doc表的外部关键字</td></tr><tr><td>effectivity_mask**</td><td>BITFIELD</td><td>NA</td><td>表示适用的有效性模板(在数据库准备阶段分配)</td></tr><tr><td>chapter_nbr</td><td>CHAR</td><td>&lt;graphicchapnbr&gt;</td><td>章号</td></tr><tr><td>section_nbr</td><td>CHAR</td><td></td><td>节号</td></tr><tr><td>subject_nbr</td><td>CHAR</td><td></td><td>题目号</td></tr><tr><td>revision_date</td><td>DATE</td><td></td><td>更改日期</td></tr><tr><td>key_code</td><td>CHAR</td><td></td><td>文件实例中是唯一的一个位置标识(标识符)</td></tr><tr><td>seq_nbr</td><td>INT</td><td>NA</td><td>资料中行的逻辑顺序</td></tr><tr><td>pagegroup_title</td><td>TEXT</td><td></td><td>页号组(DTD中的图形)的标题</td></tr><tr><td>pagegroup_text</td><td>TEXT</td><td></td><td>一个页号组的所有SGML片段</td></tr><tr><td>pagegroup_startoff</td><td>INT</td><td>NA</td><td>通用纲要模型中的Doc表[参见本文4-3-1.7.1]中描述的 pagegroup_text 栏起始的相对位置</td></tr><tr><td>pagegroup_endoff</td><td>INT</td><td>NA</td><td>通用纲要模型中的Doc表[参见本文4-3-1.7.1]中描述的 pagegroup_text 栏结束的相对位置</td></tr></table>

注1：该表的<graphic>仅从<chapter><section><subject>层次结构中的那些图形标记导出。

# 10 原理图表

该表包含一个页号组的原理图页(在 DTD 中定义为标记图形的指定上下文：题目下的图形下的图页)。

表 4-3-7.10 原理图表  

<table><tr><td>栏名称</td><td>类型</td><td>飞机标记(见注1)</td><td>描述</td></tr><tr><td>SCHEMATIC_ID*</td><td>INT</td><td>NA</td><td>分配的唯一ID</td></tr><tr><td>@PAGEGROUP.</td><td></td><td></td><td></td></tr><tr><td>PAGEGROUP_ID**</td><td>INT</td><td>NA</td><td>参考图形表</td></tr><tr><td>schematic_nbr**</td><td>INT</td><td></td><td>标识章一节一题目一页编号中的飞机或区域的构型中的差异</td></tr><tr><td>sheet_nbr**</td><td>INT</td><td></td><td>在一个页号组中的一个原理图页的顺序编号(但不必连续)</td></tr><tr><td>key_code**</td><td>CHAR</td><td></td><td>图页的唯一标识符</td></tr><tr><td>effectivity_mask**</td><td>BITFIELD</td><td>NA</td><td>表示适用的有效性模板(在数据库准备阶段分配)</td></tr><tr><td>effectivity_info</td><td>TEXT</td><td></td><td>飞机/发动机的有效性信息</td></tr><tr><td>chapter_nbr</td><td>CHAR</td><td></td><td>章号</td></tr><tr><td>section_nbr</td><td>CHAR</td><td>&lt;sheet sectnbr&gt;</td><td>节号</td></tr><tr><td>subject_nbr</td><td>CHAR</td><td>&lt;sheet sub jnbr&gt;</td><td>题目号</td></tr><tr><td>pagegroup_nbr</td><td>CHAR</td><td>&lt;sheet pagenbr&gt;</td><td>页号组编号</td></tr><tr><td>revision_date</td><td>DATE</td><td>&lt;sheet revdate&gt;</td><td>更改日期</td></tr><tr><td>seq_nbr</td><td>INT</td><td>NA</td><td>资料中行的逻辑顺序</td></tr><tr><td>schematic_title</td><td>TEXT</td><td>&lt;title&gt;</td><td>原理图的标题</td></tr><tr><td>schematic_text</td><td>TEXT</td><td>&lt;sheet&gt;</td><td>一个图页编号的所有SGML片段</td></tr><tr><td>revision_date</td><td>DATE</td><td>&lt;sheet revdate&gt;</td><td>更改日期</td></tr><tr><td>schematic_startoff</td><td>INT</td><td>NA</td><td>通用纲要模型中的Doc表[参见本文4-3-1.7.1]中描述的schematic_text栏起始的相对位置</td></tr><tr><td>schematic_endoff</td><td>INT</td><td>NA</td><td>通用纲要模型中的Doc表[参见本文4-3-1.7.1]中描述的schematic_text栏结束的相对位置</td></tr><tr><td>schematic_type_code</td><td>CHAR</td><td>NA</td><td>标识图形编码格式</td></tr><tr><td>file_name</td><td>CHAR</td><td>NA</td><td>包含图形的可选文件名</td></tr><tr><td>schematic_bin</td><td>GRAPHIC</td><td>NA</td><td>二进制编码的图形</td></tr></table>

注1：该表中的<sheet>仅从<chapter><section><subject><graphic>层次结构中的那些图形标记导出。

# 11 表线清单表

该表包含一个或多个手册的布线清单信息。一个布线手册清单的全部文本用一个给定行中的wmlist_text栏来表示。第二关键字是文件ID，因为每个文件只有一行(一个WMLIST)(WMLIST表)。

表 4-3-7.11 Wmlist 表  

<table><tr><td>栏名称</td><td>类型</td><td>飞机标记</td><td>描述</td></tr><tr><td>WMLIST_ID*</td><td>INT</td><td>NA</td><td>分配的唯一ID</td></tr><tr><td>@GEN.DOCS.DOC_ID**</td><td>INT</td><td>NA</td><td>文件ID。通用纲要模型(GEN)中Doc表的外部关键字</td></tr><tr><td>wmlist_text</td><td>TEXT</td><td>&lt;wmlist&gt;</td><td>WMLIST的所有SGML片段</td></tr><tr><td>wmlist_startoff</td><td>INT</td><td>NA</td><td>通用纲要模型中的Doc表[参见本文4-3-1.7.1]中描述的WMLIST_text栏起始的相对位置</td></tr><tr><td>wmlist_endoff</td><td>INT</td><td>NA</td><td>通用纲要模型中的Doc表[参见本文4-3-1.7.1]中描述的WMLIST_text栏结束的相对位置</td></tr></table>

# 12 布线子清单表

该表包含一个或多个手册的布线清单信息。一个布线手册清单的全部文本用一个给定行中的wmsublis_text栏来表示。

表4-3-7.12 Wmsublist表  

<table><tr><td>栏名称</td><td>类型</td><td>飞机标记</td><td>描述</td></tr><tr><td>WMSUBLIST_ID*</td><td>INT</td><td>NA</td><td>分配的唯一ID</td></tr><tr><td>@GEN.DOCS.DOC_ID**</td><td>INT</td><td>NA</td><td>文件ID。通用纲要模型(GEN)中Doc表的外部关键字</td></tr><tr><td>revision_date</td><td>DATE</td><td>&lt;? revdate&gt;</td><td>更改日期</td></tr><tr><td>key_code</td><td>CHAR</td><td>&lt;? key&gt;</td><td>文件实例中唯一的一个位置标识(标识符)</td></tr><tr><td>wmsublist_title</td><td>TEXT</td><td>&lt;title&gt;</td><td>特定的sublist标题</td></tr><tr><td>wmsublist_type</td><td>CHAR</td><td>NA</td><td>表示sublist类型的常数。必须是下列文字之一：EQIPLIST、EXTWLIST或CONDLIST</td></tr><tr><td>wmsublist_text</td><td>TEXT</td><td>&lt;?&gt;</td><td>一个WMSUBLIST的所有SGML片段，可以是&lt;eqiList&gt;、&lt;extwlist&gt;或&lt;conlist&gt;</td></tr><tr><td>wmsublist_startoff</td><td>INT</td><td>NA</td><td>通用纲要模型中的Doc表[参见本文4-3-1.7.1]中描述的wmsublist_text栏起始的相对位置</td></tr><tr><td>wmsublist_endoff</td><td>INT</td><td>NA</td><td>通用纲要模型中的Doc表[参见本文4-3-1.7.1]中描述的wmsublist_text栏结束的相对位置</td></tr></table>

# 13 设备项目表

该表包含了设备项信息。表的每一行包含了关于共同定义设备项所有方面的信息，相当于 DTD 中的<eqrow>。<eqrow>的全部文本用一个给定行中的 eqipitem_text 栏来表示。

表4-3-7.13 Eqipitem表  

<table><tr><td>栏名称</td><td>类型</td><td>飞机标记</td><td>描述</td></tr><tr><td>EQIPITEM_ID*</td><td>INT</td><td>NA</td><td>分配的唯一ID</td></tr><tr><td>@WMSUBLIST.</td><td></td><td></td><td></td></tr><tr><td>WMSUBLIST_ID**</td><td>INT</td><td>NA</td><td>WMSUBLIST 表的外部关键字</td></tr><tr><td>seq_nbr**</td><td>INT</td><td>NA</td><td>资料中行的逻辑顺序</td></tr><tr><td>key_code**</td><td>CHAR</td><td>&lt;eqrow key&gt;</td><td>文件实例中唯一的一个位置标识(标识符)</td></tr><tr><td>part_nbr**</td><td>CHAR</td><td>&lt;pnr&gt;</td><td>按照制造商或供应商的行业标准,对主要零件、装配件、工具包或材料项所做的标识。当零件号与它的制造商代码链接时,对给定项目提供了唯一的标识</td></tr><tr><td>manufacturer**</td><td>CHAR</td><td>&lt;mfr&gt;</td><td>分配的5位数字代码，用以标识零件制造商，通常为商业和政府实体代码(CAGE)。可以是本地代码</td></tr><tr><td>effectivity_mask</td><td>BITFIELD</td><td>NA</td><td>表示适用的有效性模板(在数据库准备阶段分配)</td></tr><tr><td>effectivity_info</td><td>TEXT</td><td>-effect&gt;</td><td>飞机/发动机的有效性信息</td></tr><tr><td>revision_date</td><td>DATE</td><td>&lt;eqrowrevdate&gt;</td><td>更改日期</td></tr><tr><td>airline_part_nbr</td><td>CHAR</td><td>&lt;alprtpnr&gt;</td><td>航空公司分配的编号，用以标识和控制它们的库存和控制系统中的零件。</td></tr><tr><td>part_description</td><td>CHAR</td><td>&lt;partdesc&gt;</td><td>对一个设备项给出的文字描述或功能名称</td></tr><tr><td>location</td><td>CHAR</td><td>LOCATION&gt;</td><td>分配给一个分离支架的起始位置编号</td></tr><tr><td>home(diagram_nbr</td><td>CHAR</td><td>&lt;Hdiagnbr&gt;</td><td>对一个组件进行图示时其主要框图或原理图的ATA编号</td></tr><tr><td>totalquantity</td><td>CHAR</td><td>&lt;ta&gt;</td><td>为达到航线维修目的，一架飞机的全部装配件中使用的主要零件的总数(按每个隐含单位)</td></tr><tr><td>equivalent_partnbr</td><td>CHAR</td><td>&lt;eqivpnr&gt;</td><td>是组件的零件号，以满足EQROW的零件号标记的标识规范</td></tr><tr><td>manufacturer_name</td><td>CHAR</td><td>&lt;mfmame&gt;</td><td>制造商名称</td></tr><tr><td>option_code</td><td>CHAR</td><td>&lt;optcode&gt;</td><td>用于标识首选零件的代码，以便使用或订购这些零件</td></tr><tr><td>drawing_nbr</td><td>CHAR</td><td>&lt;dwg&gt;</td><td>定义飞机部件和系统安装的生产图纸编号</td></tr><tr><td>chapter_20_ref</td><td>CHAR</td><td>&lt;ch20ref&gt;</td><td>[20章(系统)]题目的ATA参考，在该部分可查找关于设备项的详细信息。</td></tr><tr><td>panel</td><td>CHAR</td><td>&lt;pan&gt;</td><td>该标记标识检修面板信息一面板号</td></tr><tr><td>position</td><td>CHAR</td><td>&lt;position&gt;</td><td>分配给一个分离支架的起始位置编号</td></tr><tr><td>maximum positions</td><td>CHAR</td><td>&lt;maxpos&gt;</td><td>分离支架的最大位置编号</td></tr><tr><td>panel_description</td><td>CHAR</td><td>&lt; Pandesc&gt;</td><td>飞机上面板的文字标识</td></tr><tr><td>modification_code</td><td>CHAR</td><td>&lt;modcode&gt;</td><td>分配给设备项的代码，用以标识它的改型状态</td></tr><tr><td>grid_nbr</td><td>CHAR</td><td>&lt;gridnbr&gt;</td><td>面板上的X和Y位置，用数字和字母描述</td></tr><tr><td>equipitem_text</td><td>TEXT</td><td>&lt;eqrow&gt;</td><td>一个&lt;eqrow&gt;的所有SGML片段</td></tr><tr><td>equipitem_startoff</td><td>INT</td><td>NA</td><td>通用纲要模型中的Doc表[参见本文4-3-1.7.1]中描述的eqipitem_text栏起始的相对位置</td></tr><tr><td>eqipitem_endoff</td><td>INT</td><td>NA</td><td>通用纲要模型中的 Doc 表 [参见本文 4-3-1.7.1]中描述的 eqipitem_text 栏结束的相对位置</td></tr></table>

# 14 EQIVPNR表

该表包含组件的等价零件号信息，该信息符合设备清单的零件号标记的标识规范。表中的每一行表示一个等价零件号信息。一个等价零件号的全部文本用一个给定行中的eqivpn_text栏来表示。

表 4-3-7.14 Eqivpnr 表  

<table><tr><td>栏名称</td><td>类型</td><td>飞机标记</td><td>描述</td></tr><tr><td>EQIVPNR_ID*</td><td>INT</td><td>NA</td><td>分配的唯一ID</td></tr><tr><td>seq_nbr**</td><td>INT</td><td>NA</td><td>资料中行的逻辑顺序</td></tr><tr><td>@EQIPITEM.EQIPITEM_ID**</td><td>INT</td><td>NA</td><td>参考 EQIPITEM 表的外部关键字</td></tr><tr><td>eqivpnr_text</td><td>TEXT</td><td>&lt;eqipnr&gt;</td><td>一个&lt;eqipnr&gt;的所有SGML片段</td></tr><tr><td>eqivpnr_startoff</td><td>INT</td><td>NA</td><td>通用纲要模型中的 Doc 表[参见本文4-3-1.7.1]中描述的 equivpnr_text 栏起始的相对位置</td></tr><tr><td>eqivpnr_endoff</td><td>INT</td><td>NA</td><td>通用纲要模型中的 Doc 表[参见本文4-3-1.7.1]中描述的 equivpnr_text 栏结束的相对位置</td></tr></table>

# 15EXTWLISTITEM表

该表包含导线及端接的信息。该表的每一行表示布线清单中的一个特定导线和它在扩展布线清单(<extwlist>)中端接的信息。一个扩展布线清单的全部文本用一个给定行中的extwlistitem_text栏来表示。

表4-3-7.15 Extwlistem表  

<table><tr><td>栏名称</td><td>类型</td><td>飞机标记</td><td>描述</td></tr><tr><td>EXTWLISTITEM_ID*</td><td>INT</td><td>NA</td><td>分配的唯一ID</td></tr><tr><td>@WMSUBLIST.</td><td></td><td></td><td></td></tr><tr><td>WMSUBLIST_ID**</td><td>INT</td><td>NA</td><td>WMSUBLIST表的外部关键字</td></tr><tr><td>key_code**</td><td>CHAR</td><td></td><td>文件实例中唯一的一个位置标识(标识符)</td></tr><tr><td>seq_nbr</td><td>INT</td><td>NA</td><td>资料中行的逻辑顺序</td></tr><tr><td>effectivity_mask</td><td>BITFIELD</td><td>NA</td><td>表示适用的有效性模板(在数据库准备阶段分配)</td></tr><tr><td>effectivity_info</td><td>TEXT</td><td></td><td>飞机/发动机的有效性信息</td></tr><tr><td>revision_date</td><td>DATE</td><td></td><td>更改日期</td></tr><tr><td>extwlistItem_type</td><td>CHAR</td><td>NA</td><td>以下文字串之一(不包括引号):“ACTWIRE”、“NACPWIRE”、“SPAREPIN”,该项目的相应类型反映在 DTD 中是以下三个标记选项之一{&lt;actwire&gt;, &lt;nacp wire&gt;, &lt;sparepin&gt;}</td></tr><tr><td>extwlistItem_text</td><td>TEXT</td><td>&lt;extwrow&gt;</td><td>所有 SGML 片段的目录</td></tr><tr><td>extwlistItem_startoff</td><td>INT</td><td>NA</td><td>通用纲要模型中的 Doc 表[参见本文 4-3-1.7.1]中描述的 extwlistItem_text 栏起始的相对位置</td></tr><tr><td>extwlistItem_endoff</td><td>INT</td><td>NA</td><td>通用纲要模型中的 Doc 表[参见本文 4-3-1.7.1]中描述的 extwlistItem_text 栏结束的相对位置</td></tr></table>

# 16 CONDLISTITEM表

该表包含一个或多个手册的布线手册清单中的电缆管路信息。该表的每一行表示隶属于一个特殊电缆管路的信息。condlist项目的全部文本用一个给定行中的condlistitem_text栏来表示。

表 4-3-7.16 ConlistItem 表  

<table><tr><td>栏名称</td><td>类型</td><td>飞机标记</td><td>描述</td></tr><tr><td>CONDLISTITEM_ID*</td><td>INT</td><td>NA</td><td>分配的唯一ID</td></tr><tr><td>@WMSUBLIST.WMSUBLISTID**</td><td>INT</td><td>NA</td><td>WMSUBLIST表的外部关键字</td></tr><tr><td>EFFECTIVITY_MASK**</td><td>BITFIELD</td><td>NA</td><td>表示适用的有效性模板(在数据库准备阶段分配)</td></tr><tr><td>seq_nbr</td><td>INT</td><td>NA</td><td>资料中行的逻辑顺序</td></tr><tr><td>condid</td><td>TEXT</td><td></td><td>在一个区域内分配的导线管编号</td></tr><tr><td>effectivity_info</td><td>TEXT</td><td></td><td>飞机/发动机的有效性信息</td></tr><tr><td>revision_date</td><td>DATE</td><td></td><td>更改日期</td></tr><tr><td>key_code</td><td>CHAR</td><td></td><td>文件实例中唯一的一个位置标识(标识符)</td></tr><tr><td>zone_1</td><td>CHAR</td><td></td><td>标识[参见本文3-1-3.3]中定义的飞机区域号</td></tr><tr><td>zone_2</td><td>CHAR</td><td></td><td>标识[参见本文3-1-3.3]中定义的飞机区域号</td></tr><tr><td>diameter</td><td>CHAR</td><td></td><td>电缆管路内径的数值。注:测量单位在相关的UNIT属性中给出</td></tr><tr><td>length</td><td>CHAR</td><td></td><td>电缆长度数值。注:测量单位在相关的UNIT属性中给出</td></tr><tr><td>condlistItem_text</td><td>CHAR</td><td></td><td>标识一组共同定义电缆管路所有方面的元素</td></tr><tr><td>condlistItem_startoff</td><td>INT</td><td>NA</td><td>通用纲要模型中的 Doc 表 [参见本文 4-3-1.7.1] 中描述的 condlistItem_text 栏起始的相对位置</td></tr><tr><td>condlistItem_endoff</td><td>INT</td><td>NA</td><td>通用纲要模型中的 Doc 表 [参见本文 4-3-1.7.1] 中描述的 condlistItem_text 栏结束的相对位置</td></tr></table>

# 17 Wirecode表

该表包含了标识导线唯一性所必需的一组元素。该表的每一行表示给定手册中的唯一一个导线。wirecode 的全部文本用一个给定行中的 wirecode_text 栏来表示。

表 4-3-7.17 Wirecode 表  

<table><tr><td>栏名称</td><td>类型</td><td>飞机标记</td><td>描述</td></tr><tr><td>WIRE_CODE_ID*</td><td>INT</td><td>NA</td><td>分配的唯一ID</td></tr><tr><td>@GEN.DOCS.DOC_ID**</td><td>INT</td><td>NA</td><td>文件ID。通用纲要模型(GEN)中Doc表的外部关键字</td></tr><tr><td>wire_nbr* *</td><td>CHAR</td><td></td><td>导线号</td></tr><tr><td>wire_gauge</td><td>CHAR</td><td></td><td>美国导线测量单位中表示的导线粗细</td></tr><tr><td>wire_color</td><td>CHAR</td><td></td><td>在必要时标识导线唯一性的颜色</td></tr><tr><td>bundle_number</td><td>CHAR</td><td></td><td>导线束编号</td></tr><tr><td>wirecode_text</td><td>TEXT</td><td></td><td>wirecode的全部SGML片段</td></tr><tr><td>wirecode_startoff</td><td>INT</td><td>NA</td><td>通用纲要模型中的Doc表[参见本文4-3-1.7.1]中描述的wirecode_text栏起始的相对位置</td></tr><tr><td>wirecode_endoff</td><td>INT</td><td>NA</td><td>通用纲要模型中的Doc表[参见本文4-3-1.7.1]中描述的wirecode_text栏结束的相对位置</td></tr></table>

# 18 图形表

该表包含图形的信息。图形页的二进制图像可在图页表中查到。

表 4-3-7.18 图形列表  

<table><tr><td>栏名称</td><td>类型</td><td>飞机标记</td><td>描述</td></tr><tr><td>GRAPHIC_ID*</td><td>Type</td><td>NA</td><td>分配的唯一ID</td></tr><tr><td>key_code**</td><td>INT</td><td>&lt;graphic key&gt;</td><td>图形的唯一标识符</td></tr><tr><td>@GEN.DOCS.DOC_ID**</td><td>CHAR</td><td>NA</td><td>文件ID。通用纲要模型(GEN)中Doc表的外部关键字</td></tr><tr><td>effectivity_mask</td><td>INT</td><td>NA</td><td>表示适用的有效性模板(在数据库准备阶段分配)</td></tr><tr><td>effectivity_info</td><td>BITFIELD</td><td>-effect&gt;</td><td>飞机/发动机的有效性信息</td></tr><tr><td>graphic_title</td><td>TEXT</td><td>&lt;title&gt;</td><td>图形标题</td></tr><tr><td>sheet_count</td><td>TEXT</td><td>NA</td><td>图形中的图页号</td></tr></table>

# 19 图页表

该表包含图形的图页，并显示它们与该图形的关系。

示图可按 ATA 标准格式根据 sheet_bin 栏检索，并可选择根据 file_name 栏中显示的文件来检索。

表 4-3-7.19 图页表  

<table><tr><td>栏名称</td><td>类型</td><td>飞机标记</td><td>描述</td></tr><tr><td>SHEET_ID*</td><td>INT</td><td>NA</td><td>分配的唯一ID</td></tr><tr><td>@GRAPHIC.GRAPHIC ID**</td><td>INT</td><td>NA</td><td>参考图形表</td></tr><tr><td>sheet_nbr**</td><td>INT</td><td></td><td>父图形中的该图页的顺序号</td></tr><tr><td>key_code**</td><td>CHAR</td><td></td><td>图页的唯一标识符</td></tr><tr><td>@GEN.DOCS.DOC_ID**</td><td>INT</td><td>NA</td><td>文件ID。通用纲要模型(GEN)中Doc 表的外部关键字</td></tr><tr><td>EFFECTIVITY_MASK</td><td>BITFIELD</td><td>NA</td><td>表示适用的有效性模板(在数据库准备阶段分配)</td></tr><tr><td>effectivity_info</td><td>TEXT</td><td></td><td>飞机/发动机的有效性信息</td></tr><tr><td>sheet_title</td><td>TEXT</td><td></td><td>图页标题</td></tr><tr><td>sheet_type_code</td><td>CHAR</td><td>NA</td><td>标识图形编码格式</td></tr><tr><td>sheet_text</td><td>TEXT</td><td></td><td>一个图形图页编号的所有SGML片段</td></tr><tr><td>revision_date</td><td>DATE</td><td></td><td>更改日期</td></tr><tr><td>sheet_bin</td><td>GRAPHIC</td><td>NA</td><td>二进制编码图形</td></tr><tr><td>file_name</td><td>CHAR</td><td>NA</td><td>包含图形的可选文件名</td></tr></table>

# 4-3-8 系统说明(SDS)纲要模型

# 1 前言

本文件与 ATA 通用纲要模型([参见本文 4-3-1]) 共同提供了适用于 SDS 的检索纲要模型。该纲要模型称为 “SDS” 纲要模型, 属于 “ATA_维修” 类。

该纲要模型只适用于飞机。

# 2 Front_Matter(前页)表

该表包含文件的前页。它将前页划分成若干部分，其中division_name栏指出了DTD标记，按照这些标记可导出前页。

表 4-3-8.1 前页表  

<table><tr><td>栏名</td><td>类型</td><td>飞机标记</td><td>描 述</td></tr><tr><td>FRONT_MATTER_ID*</td><td>INT</td><td>NA</td><td>分配的唯一ID</td></tr><tr><td>@GEN.DOCS.DOC_ID**</td><td>INT</td><td>NA</td><td>文件ID。通用纲要模型(GEN)中Doc表的外部关键字</td></tr><tr><td>division_name**</td><td>CHAR</td><td>(见.[表4-3-8.2])</td><td>前页的分段(部分)的名称。标准名称在下面给出</td></tr><tr><td>division_title</td><td>TEXT</td><td>&lt;title&gt;</td><td>分段标题</td></tr><tr><td>division_text</td><td>TEXT</td><td>(见.[表4-3-8.2])</td><td>一个分段的所有SGML片段</td></tr><tr><td>division_startoff</td><td>INT</td><td>NA</td><td>通用纲要模型中的Doc表[参见本文4-3-1.7.1]中描述的division_text栏起始的相对位置</td></tr><tr><td>division_endoff</td><td>INT</td><td>NA</td><td>通用纲要模型中的Doc表[参见本文4-3-1.7.1]中描述的division_text栏结束的相对位置</td></tr></table>

表 4-3-8.2 标准的分段名  

<table><tr><td>分割名</td><td>类型</td><td>飞机标记</td><td>描述</td></tr><tr><td>TRANS_letter</td><td>TEXT</td><td>&lt;transltr&gt;</td><td>更改的通用信息</td></tr><tr><td>TRLIST</td><td>TEXT</td><td>&lt;trlist&gt;</td><td>临时更改单</td></tr><tr><td>INTRO</td><td>TEXT</td><td>&lt;intro&gt;</td><td>文件信息</td></tr><tr><td>EFFECT_X_REF</td><td>TEXT</td><td>&lt;effxref&gt;</td><td>关于标识文件实例中的一个基本有效性组的不同方法以及这些方法如何相互联系的数据</td></tr><tr><td>SB_LIST</td><td>TEXT</td><td>&lt;sblist&gt;</td><td>维护通报的当前合并状态的数据</td></tr></table>

注：有关机身手册的“如何使用”信息位于INTRO。

# 3 有效性表

本表被当作该纲要模型中其它表的 EFFECTIVITY_MASK 栏中有效性信息编码的“关键字”来使用。对于数据库中表示的每个不同的有效性值，在该表中都有一个行来描述。

表 4-3-8.3 有效性表  

<table><tr><td>栏 名</td><td>类型</td><td>飞机标记</td><td>描 述</td></tr><tr><td>Effectivity_key*</td><td>CHAR</td><td>见注</td><td>有效性关键字是用于标识资料中一个特定有效性的唯一值(见注)</td></tr><tr><td>mask_position_nbr**</td><td>INT</td><td>NA</td><td>EFFECTIVITY_MASK 中唯一的指定位置。MASK POSITION NBR 应是从1~n之间的无符号整数,其中n为有效性表中的行数</td></tr><tr><td>line_nbr</td><td>CHAR</td><td></td><td>制造商的有序的生产流水线号</td></tr><tr><td>var_nbr</td><td>CHAR</td><td></td><td>可变的工程号</td></tr><tr><td>basic_nbr</td><td>CHAR</td><td></td><td>基本的工程号</td></tr><tr><td>serial_nbr</td><td>CHAR</td><td></td><td>固定的ID号</td></tr><tr><td>Registration_nbr</td><td>CHAR</td><td></td><td>尾号</td></tr><tr><td>customer_code</td><td>CHAR</td><td></td><td>标识航空公司用户接收或发送数据的ICAO 字母数字代码</td></tr><tr><td>Model_type</td><td>CHAR</td><td></td><td>飞机有效性交叉参考表中的型号/类型。标识文件样本涉及的飞机型号或类型</td></tr></table>

注：对于飞机，数据库中所表示的每一个CEC号都与该表中的一行相对应。每行都有一个唯一的effectivity_key值（即一个CEC），并给出一个唯一的MASK POSITION_NBR值，该值是在数据库创建时随机分配的。

# 4 目录表

该表用于存储所有 SDS 文件的一个目录。目录表设计成为可使用一条 SFQL 查询语句生成可访问的文本条目的方式，这样使目录的生成比较容易。这包括表中每个条目的摘要以及对包含实际信息的文件表的一个链接。

表 4-3-8.4 目录表  

<table><tr><td>栏 名</td><td>类型</td><td>飞机标记</td><td>描 述</td></tr><tr><td>CONTENTS_ID*</td><td>INT</td><td>NA</td><td>分配的唯一行标识符。</td></tr><tr><td>@GEN.DOCS.DOC_ID**</td><td>INT</td><td>NA</td><td>文件 ID。通用纲要模型(GEN)中的 Doc 表的外部关键字。</td></tr><tr><td>entry_sequence_nbr* *</td><td>INT</td><td>NA</td><td>用于排放条目的编号,利用该编号使条目的排列与目录中的 DOC_ID 的顺序完全相同,该编号从1开始。</td></tr><tr><td>entry_table_name**</td><td>CHAR</td><td>NA</td><td>该条目指向的纲要模型表名称。</td></tr><tr><td>entry_key_name**</td><td>CHAR</td><td>NA</td><td>主关键字的栏名称。见注3</td></tr><tr><td>@ENTRY_KEY_ID**</td><td>INT</td><td>NA</td><td>标识内容文本的主关键字值。</td></tr><tr><td>EFFECTIVITY_MASK</td><td>BITFIELD</td><td>NA</td><td>表示适用的有效性模板(在数据库准备阶段分配)</td></tr><tr><td>effectivity_info</td><td>TEXT</td><td>&lt;effect efftext&gt; See Note 1.</td><td>有效性信息。</td></tr><tr><td>FM_Division_Name</td><td>CHAR</td><td>NA</td><td>当条目是前页的分段时使用</td></tr><tr><td>entry_level</td><td>INT</td><td>NA See Note2</td><td>表中的级别划分,1为表中所分级别最高的级别。</td></tr><tr><td>@parent_ID</td><td>INT</td><td>NA</td><td>父条目的content_id。如果没有父条目(entry_level=1),则PARENT_ID值为NULL</td></tr><tr><td>entry_text</td><td>TEXT</td><td>&lt;title&gt;</td><td>提供该内容条目“文本”的“位置标识”标题</td></tr><tr><td>entry_startoff</td><td>INT</td><td>NA</td><td>通用纲要模型中的Doc表[参见本文4-3-1.7.1]中描述的entry_text栏起始的相对位置</td></tr><tr><td>entry_endoff</td><td>INT</td><td>NA</td><td>通用纲要模型中的Doc表[参见本文4-3-1.7.1]中描述的entry_text栏结束的相对位置</td></tr><tr><td>key_code</td><td>CHAR</td><td>&lt;?key&gt;</td><td>文件实例中唯一的一个位置标识(标识符)</td></tr><tr><td>Chapter_nbr</td><td>CHAR</td><td>&lt;?chapnbr&gt;</td><td>章号</td></tr><tr><td>Section_nbr</td><td>CHAR</td><td>&lt;?sectnbr&gt;</td><td>节号。</td></tr><tr><td>Subject_nbr</td><td>CHAR</td><td>&lt;? subjnbr&gt;</td><td>题目号</td></tr><tr><td>Pageset_nbr</td><td>CHAR</td><td>&lt;? pgsetnbr&gt;</td><td>系统信息的基本单元，由一个文本集合以 及一个或多个图形组合而成。</td></tr><tr><td>revision_date</td><td>DATE</td><td>&lt;? revdate&gt;</td><td>更改日期。</td></tr></table>

注1：对于飞机，如果effectivity_text存在，它将只包含EFFECT元素的efftext属性值。  
注2：这是在飞机手册中如何使用entry_level的一个实例。

表 4-3-8.5 目录级别表  

<table><tr><td>entry_table_name</td><td>entry_level</td></tr><tr><td>前页</td><td>1</td></tr><tr><td>章</td><td>1</td></tr><tr><td>节</td><td>2</td></tr><tr><td>题目</td><td>3</td></tr><tr><td>页面设置</td><td>4</td></tr></table>

注3：参考技术要求，entry_table具有单一的主关键字栏。

# 5 更改提要表

该表用于返回反映修订过程中的更改提要信息。

表 4-3-8.6 更改提要表  

<table><tr><td>栏名</td><td>类型</td><td>飞机标记</td><td>描述</td></tr><tr><td>HIGHLIGHTS_ID*</td><td>INT</td><td>NA</td><td>分配的唯一行标识符</td></tr><tr><td>entry_table_name**</td><td>CHAR</td><td>NA</td><td>该条目指向的MSM纲要模型表名称</td></tr><tr><td>entry_key_name**</td><td>CHAR</td><td>NA</td><td>主关键字的栏名称</td></tr><tr><td>@ENTRY_KEY_ID**</td><td>INT</td><td>NA</td><td>主关键字值，用以标识适用于更改提要的文件单元</td></tr><tr><td>@GEN.DOCS.DOC_ID</td><td>INT</td><td>NA</td><td>文件ID。通用纲要模型(GEN)中的Doc表的外部关键字</td></tr><tr><td>effectivity_mask</td><td>BITFIELD</td><td>NA</td><td>表示适用的有效性模板</td></tr><tr><td>effectivity_info</td><td>TEXT</td><td>-effect&gt;</td><td>有效性信息</td></tr><tr><td>chapter_nbr</td><td>CHAR</td><td>&lt;? chapnbr&gt;</td><td>章号</td></tr><tr><td>section_nbr</td><td>CHAR</td><td>&lt;? sectnbr&gt;</td><td>节号</td></tr><tr><td>subject_nbr</td><td>CHAR</td><td>&lt;? subjnbr&gt;</td><td>题目号</td></tr><tr><td>graphic_title</td><td>TEXT</td><td>&lt;title&gt;</td><td>当图形或图页为更改目标时使用</td></tr><tr><td>sheet_nbr</td><td>INT</td><td>&lt; sheet sheetnbr&gt;</td><td>在图形图页为更改目标时使用</td></tr><tr><td>FM_Division_Name</td><td>CHAR</td><td>NA</td><td>当FM为更改目标时使用</td></tr><tr><td>key_code</td><td>CHAR</td><td>&lt;? key&gt;</td><td>文件实例中唯一的一个位置标识(标识符)</td></tr><tr><td>change_description</td><td>CHAR</td><td>&lt;chgdesc&gt;</td><td>描述修订过程中的更改</td></tr></table>

# 6 章表

该表用于返回一个或多个手册的章信息。一个章的全部文本用一个给定行中的chapter_text栏来表示。

表4-3-8.7 章表  

<table><tr><td>栏 名</td><td>类型</td><td>飞机标记</td><td>描 述</td></tr><tr><td>CHAPTER_ID*</td><td>INT</td><td>NA</td><td>分配的唯一ID。</td></tr><tr><td>chapter_nbr**</td><td>CHAR</td><td>&lt;chapter chapnbr&gt;</td><td>章号</td></tr><tr><td>@GEN.DOCS.DOC_ID**</td><td>INT</td><td>NA</td><td>文件ID。参考通用纲要模型(GEN)中的Doc表</td></tr><tr><td>EFFECTIVITY_MASK**</td><td>BITFIELD</td><td>NA</td><td>表示适用的有效性模板。(在数据库准备期间分配)</td></tr><tr><td>effectivity_info</td><td>TEXT</td><td>-effect&gt;</td><td>有效性信息</td></tr><tr><td>revision_date</td><td>DATE</td><td>&lt;chapter revdate&gt;</td><td>更改日期</td></tr><tr><td>key_code</td><td>CHAR</td><td>&lt;chapter key&gt;</td><td>文件实例中唯一的位置标识(标识符)。</td></tr><tr><td>seq_nbr</td><td>INT</td><td>NA</td><td>资料中行的逻辑顺序</td></tr><tr><td>chapter_title</td><td>TEXT</td><td>&lt;title&gt;</td><td>章标题</td></tr><tr><td>chapter_text</td><td>TEXT</td><td>&lt;chapter&gt;</td><td>一章的所有SGML片段</td></tr><tr><td>chapter_startoff</td><td>INT</td><td>NA</td><td>通用纲要模型中的Doc表[参见本文4-3-1.7.1]中描述的chapter_text栏起始的相对位置</td></tr><tr><td>chapter_endoff</td><td>INT</td><td>NA</td><td>通用纲要模型中的Doc表[参见本文4-3-1.7.1]中描述的chapter_text栏结束的相对位置</td></tr></table>

# 7 节表

该表用于返回一个或多个手册的节信息。一节的全部文本用一个给定行中的section_text栏来表示。

表4-3-8.8 节表  

<table><tr><td>栏 名</td><td>类型</td><td>飞机标记</td><td>描 述</td></tr><tr><td>SECTION_ID*</td><td>INT</td><td>NA</td><td>分配的唯一ID</td></tr><tr><td>section_nbr**</td><td>CHAR</td><td>&lt;section sectnbr&gt;</td><td>节号</td></tr><tr><td>@CHAP
TER.CHAPTER_ID* *</td><td>INT</td><td>NA</td><td>参考章表</td></tr><tr><td>@GEN.DOCS.DOC_ID**</td><td>INT</td><td>NA</td><td>文件 ID。参考通用纲要模型 (GEN) 中的 Doc 表</td></tr><tr><td>chapter_nbr</td><td>CHAR</td><td>&lt;section chapnbr&gt;</td><td>章号</td></tr><tr><td>revision_date</td><td>DATE</td><td>&lt;section revdate&gt;</td><td>更改日期</td></tr><tr><td>key_code</td><td>CHAR</td><td>&lt;section key&gt;</td><td>文件实例中唯一的一个位置标识(标识符)</td></tr><tr><td>seq_nbr</td><td>INT</td><td>NA</td><td>资料中行的逻辑顺序</td></tr><tr><td>section_title</td><td>TEXT</td><td>&lt;title&gt;</td><td>节标题</td></tr><tr><td>section_text</td><td>TEXT</td><td>&lt;section&gt;</td><td>一节的所有 SGML 片段</td></tr><tr><td>section_startoff</td><td>INT</td><td>NA</td><td>通用纲要模型中的 Doc 表[参见本文 4-3 -1.7.1]中描述的 section_text 栏起始的相对位置</td></tr><tr><td>section_endoff</td><td>INT</td><td>NA</td><td>通用纲要模型中的 Doc 表[参见本文 4-3 -1.7.1]中描述的 section_text 栏结束的相对位置</td></tr></table>

# 8 题目表

该表用于返回一个或多个手册的题目信息。一个题目的全部文本用一个给定行中的 subject_text 栏来表示。

表 4-3-8.9 题目表  

<table><tr><td>栏 名</td><td>类型</td><td>飞机标记</td><td>描 述</td></tr><tr><td>SUBJECT_ID*</td><td>INT</td><td>NA</td><td>分配的唯一ID</td></tr><tr><td>subject_nbr**</td><td>CHAR</td><td>&lt;sub&gt;subject
subjbr&gt;&lt;/sub&gt;</td><td>题目号</td></tr><tr><td>EFFECTIVITY_MASK**</td><td>BITFIELD</td><td>NA</td><td>表示适用的有效性模板。(在数据库准备期间分配)</td></tr><tr><td>@SECTION SECTION_ID* *</td><td>INT</td><td>NA</td><td>参考节表</td></tr><tr><td>@GEN.DOCS.DOC_ID**</td><td>INT</td><td>NA</td><td>文件 ID。参考通用纲要模型(GEN)中的Doc表</td></tr><tr><td>chapter_nbr</td><td>CHAR</td><td>&lt;sub&gt;subject
chapnbr&gt;&lt;/sub&gt;</td><td>章号</td></tr><tr><td>section_nbr</td><td>CHAR</td><td>&lt;sub&gt;subject
sectnbr&gt;&lt;/sub&gt;</td><td>节号</td></tr><tr><td>revision_date</td><td>DATE</td><td>&lt;sub&gt;subject
revdate&gt;&lt;/sub&gt;</td><td>更改日期</td></tr><tr><td>key_code</td><td>CHAR</td><td>&lt;sub&gt;subject key&gt;&lt;/sub&gt;</td><td>文件实例中唯一的一个位置标识(标识符)</td></tr><tr><td>seq_nbr</td><td>INT</td><td>NA</td><td>资料中行的逻辑顺序</td></tr><tr><td>subject_title</td><td>TEXT</td><td>&lt;title&gt;</td><td>题目标题</td></tr><tr><td>subject_text</td><td>TEXT</td><td>&lt;sub&gt;subject&gt;&lt;/sub&gt;</td><td>一个题目的所有SGML片段</td></tr><tr><td>subject_startoff</td><td>INT</td><td>NA</td><td>通用纲要模型中的Doc表[参见本文4-3-1.7.1]中描述的 subject_text 栏起始的相对位置</td></tr><tr><td>subject_endoff</td><td>INT</td><td>NA</td><td>通用纲要模型中的Doc表[参见本文4-3-1.7.1]中描述的 subject_text 栏结束的相对位置</td></tr></table>

# 9 Pageset表

该表包含一个或者多个手册页集合的信息。页集合是由一个文本集以及一个或多个图形组合而成。一个页集合的全部文本用一个给定行中的 pageset_text 栏来表示。

表4-3-8.10 Pageset表  

<table><tr><td>栏 名</td><td>类型</td><td>飞机标记</td><td>描 述</td></tr><tr><td>PAGESET_ID*</td><td>INT</td><td>NA</td><td>分配的唯一ID</td></tr><tr><td>pageset_nbr**</td><td>CHAR</td><td>&lt;pagesetpgsetnbr&gt;</td><td>在章一节一题目内的一个页集合的唯一标识符</td></tr><tr><td>@SUBJECT.SUBJECT_ID**</td><td>INT</td><td>NA</td><td>参考题目表</td></tr><tr><td>EFFECTIVITY_MASK**</td><td>BITFIELD</td><td>NA</td><td>表示可用有效性的模板。(在数据库准备期间分配)</td></tr><tr><td>@GEN.DOCS.DOC_ID</td><td>INT</td><td>NA</td><td>文件ID。参考通用纲要模型(GEN)中的Doc表</td></tr><tr><td>performance_block</td><td>CHAR</td><td>&lt;pagesetperfblk&gt;</td><td>[ATA104 规范]中定义的标准执行块之一,例如,操作、目的和界面等</td></tr><tr><td>training_level</td><td>CHAR</td><td>&lt;pageset level&gt;</td><td>[ATA104 规范]中定义的标准培训级别之一。例如,Gen Fam.,Ramp &amp; Transit等</td></tr><tr><td>training_unit</td><td>CHAR</td><td>&lt;pagesettrmgunit&gt;</td><td>页集合的逻辑分组,以实现一个特定的培训目标</td></tr><tr><td>effectivity_info</td><td>TEXT</td><td>-effect&gt;</td><td>有效性信息</td></tr><tr><td>revision_date</td><td>DATE</td><td>&lt;pagesetrevdate&gt;</td><td>更改日期</td></tr><tr><td>key_code</td><td>CHAR</td><td>&lt;pagesetkey&gt;</td><td>文件实例中唯一的一个位置标识(标识符)</td></tr><tr><td>chapter_nbr</td><td>CHAR</td><td>&lt;Pagesetchapnbr&gt;</td><td>章号</td></tr><tr><td>section_nbr</td><td>CHAR</td><td>&lt;Pagesetsectnbr&gt;</td><td>节号</td></tr><tr><td>subject_nbr</td><td>CHAR</td><td>&lt;Pagesetsubjnbr&gt;</td><td>题目号</td></tr><tr><td>seq_nbr</td><td>INT</td><td>NA</td><td>资料中行的逻辑顺序</td></tr><tr><td>pageset_title</td><td>TEXT</td><td>&lt;title&gt;</td><td>页集合标题</td></tr><tr><td>pageset_text</td><td>TEXT</td><td>&lt;pageset&gt;</td><td>一个页集合的所有SGML片段</td></tr><tr><td>pageset_startoff</td><td>INT</td><td>NA</td><td>通用纲要模型中的Doc表[参见本文4-3-1.7.1]中描述的pageset_text栏起始的相对位置</td></tr><tr><td>pageset_endoff</td><td>INT</td><td>NA</td><td>通用纲要模型中的Doc表[参见本文4-3-1.7.1]中描述的pageset_text栏结束的相对位置</td></tr></table>

# 10 extgroup表

该表包含一个或多个手册的文本分组信息。一个文本分组是页集合中的一组(带标题的)文本块，一个文本分组的全部文本用一个给定行中的Textgroup_栏来表示。

表 4-3-8.11 正文分组表  

<table><tr><td>栏 名</td><td>类型</td><td>飞机标记</td><td>描 述</td></tr><tr><td>TEXTGROUP_ID*</td><td>INT</td><td>NA</td><td>分配的唯一ID</td></tr><tr><td>pageset_nbr**</td><td>CHAR</td><td>&lt;textgrppgsetnbr&gt;</td><td>在章一节一题目内的一个页集合的唯一标识符</td></tr><tr><td>@PAGESET.PAGESET_ID**</td><td>INT</td><td>NA</td><td>参考节表</td></tr><tr><td>EFFECTIVITY_MA SK**</td><td>BITFIELD</td><td>NA</td><td>表示适用的有效性模板。(在数据库准备期间分配)</td></tr><tr><td>@GEN.DOCS.DOC_ID</td><td>INT</td><td>NA</td><td>文件ID。参考通用纲要模型(GEN)中的Doc表</td></tr><tr><td>tip</td><td>CHAR</td><td>&lt;textgrp tip&gt;</td><td>将Textgrp定义为训练信息点(或非训练信息点)</td></tr><tr><td>chapter_nbr</td><td>CHAR</td><td>&lt;pagesetchapnbr&gt;</td><td>章号</td></tr><tr><td>section_nbr</td><td>CHAR</td><td>&lt;pagesetsectnbr&gt;</td><td>节号</td></tr><tr><td>subject_nbr</td><td>CHAR</td><td>&lt;pagesetsubjnbr&gt;</td><td>题目号</td></tr><tr><td>pageset_nbr**</td><td>CHAR</td><td>&lt;pagesetpgsetnbr&gt;</td><td>在章一节一题目内的一个页集合的唯一标识符</td></tr><tr><td>seq_nbr</td><td>INT</td><td>NA</td><td>资料中行的逻辑顺序</td></tr><tr><td>textgroup_title</td><td>TEXT</td><td>&lt;title&gt;</td><td>文本分组标题</td></tr><tr><td>textgroup_text</td><td>TEXT</td><td>&lt;textgrp&gt;</td><td>一个文本分组所有SGML片段</td></tr><tr><td>textgroup_startoff</td><td>INT</td><td>NA</td><td>通用纲要模型中的Doc表[参见本文4-3-1.7.1]中描述的textgroup_text栏起始的相对位置</td></tr><tr><td>textgroup_endoff</td><td>INT</td><td>NA</td><td>通用纲要模型中的Doc表[参见本文4-3-1.7.1]中描述的textgroup_text栏起始的相对位置</td></tr></table>

# 11 图形表

该表包含飞机维修和发动机大修手册中图形的信息。图形图页的二进制图像可在图页表中查到。

表4-3-8.12 图形表  

<table><tr><td>栏 名</td><td>类型</td><td>飞机标记</td><td>描 述</td></tr><tr><td>GRAPHIC_ID*</td><td>INT</td><td>NA</td><td>分配的唯一ID</td></tr><tr><td>key_code**</td><td>CHAR</td><td>&lt;graphic key&gt;</td><td>图形的唯一标识符</td></tr><tr><td>EFFECTIVITY_MASK**</td><td>BITFIELD</td><td>NA</td><td>表示适用的有效性模板。(在数据库准备期间分配)</td></tr><tr><td>@GEN.DOCS.DOC_ID**</td><td>INT</td><td>NA</td><td>文件 ID。参考通用纲要模型(GEN)中的Doc表</td></tr><tr><td>effectivity_info</td><td>TEXT</td><td>-effect&gt;</td><td>有效性信息</td></tr><tr><td>graphic_title</td><td>TEXT</td><td>&lt;title&gt;</td><td>图形标题</td></tr><tr><td>sheet_count</td><td>INT</td><td>NA</td><td>图形中的图页编号</td></tr><tr><td>revision_date</td><td>DATE</td><td>&lt;graphic revdate&gt;</td><td>更改日期</td></tr><tr><td>seq_nbr</td><td>INT</td><td>NA</td><td>资料中行的逻辑顺序</td></tr><tr><td>graphic_text</td><td>TEXT</td><td>&lt;graphic&gt;</td><td>图形编号的所有SGML片段</td></tr></table>

# 12 图页表

该表包含图形的图页，并显示它们与该图形的关系。

示图可按 ATA 标准格式根据 sheet_bin 栏检索，并可选择根据 file_name 栏中显示的文件来检索。

表4-3-8.13 图页表  

<table><tr><td>栏 名</td><td>类型</td><td>飞机标记</td><td>描 述</td></tr><tr><td>SHEET_ID*</td><td>INT</td><td>NA</td><td>分配的唯一ID</td></tr><tr><td>@GRAPHIC.GRAPHIC_ID**</td><td>INT</td><td>NA</td><td>参考图形表</td></tr><tr><td>sheet_nbr**</td><td>INT</td><td>&lt;sheet sheetnbr&gt;</td><td>父图形中该图页的顺序号</td></tr><tr><td>key_code</td><td>CHAR</td><td>&lt;sheet key&gt;</td><td>图页的唯一标识符</td></tr><tr><td>EFFECTIVITY_MASK</td><td>BITFIELD</td><td>NA</td><td>表示适用的有效性模板。(在数据库准备期间分配)</td></tr><tr><td>@GEN.DOCS.DOC_ID</td><td>INT</td><td>NA</td><td>文件ID。参考通用纲要模型(GEN)中的Doc 表</td></tr><tr><td>effectivity_info</td><td>TEXT</td><td>-effect&gt;</td><td>有效性信息</td></tr><tr><td>sheet_title</td><td>TEXT</td><td>&lt;title&gt;</td><td>图页标题</td></tr><tr><td>sheet_type_code</td><td>CHAR</td><td>NA</td><td>标识图形编码格式</td></tr><tr><td>sheet_text</td><td>TEXT</td><td>&lt;sheet&gt;</td><td>一个图页编号的所有SGML片段</td></tr><tr><td>revision_date</td><td>DATE</td><td>&lt;sheet revdate&gt;</td><td>更改日期</td></tr><tr><td>sheet_bin</td><td>GRAPHIC</td><td>NA</td><td>二进制编码图形</td></tr><tr><td>file_name</td><td>CHAR</td><td>NA</td><td>包含图形的可选文件名</td></tr></table>

# 4-3-9 故障报告/故障隔离手册（FRM/FIM）纲要模型

# 1 前言

本文件与 ATA 通用纲要模型([参见本文 4-3-1]) 共同提供了适用于故障报告/故障隔离手册的检索纲要模型。该纲要模型称为“FRMFIM”纲要模型，它属于“ATA_维修”类。

该纲要模型只适用于飞机。

# 2 Front_Matter表

该表包含文件的前页。它将前页划分成若干部分，其中division_name栏指出了DTD标记，按照这些标记可导出正文前内容。

表4-3-9.1 Front_matter表  

<table><tr><td>栏 名</td><td>类型</td><td>飞机标记</td><td>描 述 .</td></tr><tr><td>FRONT_MATTER_ID*</td><td>INT</td><td>NA</td><td>分配的唯一ID</td></tr><tr><td>@GEN.DOCS.DOC_ID**</td><td>INT</td><td>NA</td><td>文件ID。通用纲要模型(GEN)中的 Doc 表的外部关键字</td></tr><tr><td>division_name**</td><td>CHAR</td><td>(Ref. [Table 4-3-9.2])</td><td>前页的分段(部分)的名称</td></tr><tr><td>division_title</td><td>TEXT</td><td>&lt;title&gt;</td><td>分段标题</td></tr><tr><td>division_text</td><td>TEXT</td><td>(Ref. [Table 4-3-9.2])</td><td>一个分段的所有SGML片段</td></tr><tr><td>division_startoff</td><td>INT</td><td>NA</td><td>通用纲要模型中的Doc表[参见本文4-3-1.7.1]中描述的 division_text 栏起始的相对位置</td></tr><tr><td>division_endoff</td><td>INT</td><td>NA</td><td>通用纲要模型中的Doc表[参见本文4-3-1.7.1]中描述的 division_text 栏结束的相对位置</td></tr></table>

表 4-3-9.2 标准分段名称  

<table><tr><td>栏 名</td><td>类型</td><td>飞机标记</td><td>描述</td></tr><tr><td>TRANS LETTER</td><td>TEXT</td><td>&lt;transltr&gt;</td><td>更改的通用信息</td></tr><tr><td>TRLIST</td><td>TEXT</td><td>&lt;frmtrl&gt; or &lt;fimtrl&gt;</td><td>临时更改单</td></tr><tr><td>INTRO</td><td>TEXT</td><td>&lt;frmintro&gt; or &lt;fimintro&gt;</td><td>文件信息</td></tr><tr><td>EFFECT_X_REF</td><td>TEXT</td><td>&lt;effxref&gt;</td><td>关于标识文件实例中一个基本有效性组的不同方法以及这些方法如何相互联系的数据</td></tr><tr><td>SB_LIST</td><td>TEXT</td><td>&lt;sblist&gt;</td><td>服务通报的当前合并状态的数据</td></tr><tr><td>FIM_USAGE</td><td>TEXT</td><td>&lt;fimusage&gt;</td><td>描述如何使用故障隔离章的流程图</td></tr></table>

# 3 有效性表

本表被当作该纲要模型中其它表的 EFFECTIVITY_MASK 栏中有效性信息编码的“关键字”来使用。对于数据库中表示的每个不同的有效性值，在该表中都有一个行来描述。

表 4-3-9.3 有效性表  

<table><tr><td>栏 名</td><td>类型</td><td>飞机标记</td><td>描 述</td></tr><tr><td>effectivity_key*</td><td>CHAR</td><td>&lt;cec&gt;</td><td>有效性关键字是用于标识资料中一个特定有效性的唯一值。该标记标识了一个由航空公司选择的3字符代码,以用该代码在客户化的文件样本中标识飞机</td></tr><tr><td>mask_position_nbr**</td><td>INT</td><td>NA</td><td>EFFECTIVITY_MASK 中唯一的指定位置。MASK POSITION_NBR 应是从1~n之间的无符号整数,其中n为有效性表中的行数</td></tr><tr><td>line_nbr</td><td>CHAR</td><td>&lt;linenbr&gt;</td><td>制造商的顺序生产线号</td></tr><tr><td>var_nbr</td><td>CHAR</td><td>&lt;venbr&gt;</td><td>可变工程号</td></tr><tr><td>basic_nbr</td><td>CHAR</td><td>&lt;benbr&gt;</td><td>基本工程号</td></tr><tr><td>serial_nbr</td><td>CHAR</td><td>&lt;msnbr&gt;</td><td>固定ID编号</td></tr><tr><td>registration_nbr</td><td>CHAR</td><td>&lt;acn&gt;</td><td>尾号</td></tr><tr><td>customer_code</td><td>CHAR</td><td>&lt;cus&gt;</td><td>标识航空公司用户接收或发送数据的ICAO字母数字代码</td></tr><tr><td>model_type</td><td>CHAR</td><td>&lt;modtype&gt;</td><td>飞机有效性交叉参照表中的型号/类型。标识文件实例中包括的飞机型号/类型</td></tr></table>

# 4 目录表

该表用于存储所有FRM和FIM手册的一个目录。目录表设计成为可使用一条SFQL查询语句生成可访问的文本条目的方式，这样使目录的生成比较容易。这包括表中每个条目的摘要以及对包含实际信息的文件表的一个链接。

表 4-3-9.4 目录表  

<table><tr><td>栏 名</td><td>类型</td><td>飞机标记</td><td>描 述</td></tr><tr><td>CONTENTS_ID*</td><td>INT</td><td>NA</td><td>分配的唯一行标识符</td></tr><tr><td>@GEN.DOCS.DOC_ID**</td><td>INT</td><td>NA</td><td>文件 ID。参考通用纲要模型 (GEN) 中的 Doc 表</td></tr><tr><td>entry_sequence_nbr**</td><td>INT</td><td>NA</td><td>用于排放条目的编号, 利用该编号使条目的排列与目录中的 DOC_ID 的顺序完全相同, 该编号从 1 开始</td></tr><tr><td>entry_table_name</td><td>CHAR</td><td>NA</td><td>该条目指向的纲要模型表名称</td></tr><tr><td>entry_key_name</td><td>CHAR</td><td>NA</td><td>主关键字的栏名称。见注 1</td></tr><tr><td>@ENTRY_KEY_ID</td><td>INT</td><td>NA</td><td>标识内容文本的主关键字值</td></tr><tr><td>EFFECTIVITY_MASK</td><td>BITFIELD</td><td>NA</td><td>表示适用的有效性模板。(在数据库准备期间分配)</td></tr><tr><td>Effectivity_info</td><td>TEXT</td><td></td><td>有效性信息</td></tr><tr><td>FM_Division_Name</td><td>CHAR</td><td>NA</td><td>当条目是正文前的分段时使用</td></tr><tr><td>entry_level</td><td>INT</td><td>NA See Note 1</td><td>表中的层外部结构级别, 其中 1 为最高级别</td></tr><tr><td>@parent_ID</td><td>INT</td><td>NA</td><td>父条目的content_id。如果没有父条目(entry_level=1)，则PARENT_ID值为NULL</td></tr><tr><td>entry_text</td><td>TEXT</td><td>&lt;title&gt;</td><td>提供了该内容条目“文本”的“位置标识”的标题</td></tr><tr><td>entry_startoff</td><td>INT</td><td>NA</td><td>通用纲要模型中的Doc表[参见本文4-3-1.7.1]中描述的entry_text栏起始的相对位置</td></tr><tr><td>entry_endoff</td><td>INT</td><td>NA</td><td>通用纲要模型中的Doc表[参见本文4-3-1.7.1]中描述的entry_text栏结束的相对位置</td></tr><tr><td>key_code</td><td>CHAR</td><td>&lt;?key&gt;</td><td>一个位置标识(标识符)，在文件样本中是唯一的</td></tr><tr><td>chapter_nbr</td><td>CHAR</td><td>&lt;?chapnbr&gt;</td><td>章号</td></tr><tr><td>section_nbr</td><td>CHAR</td><td>&lt;?sectnbr&gt;</td><td>节号</td></tr><tr><td>subject_nbr</td><td>CHAR</td><td>&lt;?subjnbr&gt;</td><td>题目号</td></tr><tr><td>pageblock_nbr</td><td>CHAR</td><td>&lt;?pgblknbr&gt;</td><td>页号组编号</td></tr><tr><td>config_nbr</td><td>CHAR</td><td>&lt;?confnbr&gt;</td><td>标识页号组的一个唯一构型</td></tr><tr><td>airline_unique_code</td><td>CHAR</td><td>&lt;?alunqi&gt;</td><td>航空公司唯一标识符</td></tr><tr><td>variant_nbr</td><td>CHAR</td><td>&lt;?varnbr&gt;</td><td>差异号</td></tr><tr><td>config_letter</td><td>CHAR</td><td>&lt;?confltr&gt;</td><td>构型字母</td></tr><tr><td>sequence_nbr</td><td>CHAR</td><td>&lt;?seq&gt;</td><td>顺序号</td></tr><tr><td>function_code</td><td>CHAR</td><td>&lt;?func&gt;</td><td>功能代码</td></tr><tr><td>revision_date</td><td>DATE</td><td>&lt;?revdate&gt;</td><td>更改日期</td></tr></table>

<table><tr><td>entry_table_name</td><td>entry_level</td></tr><tr><td>前页</td><td>1</td></tr><tr><td>章</td><td>1</td></tr><tr><td>节</td><td>2</td></tr><tr><td>题目</td><td>3</td></tr><tr><td>页号组</td><td>4</td></tr><tr><td>任务</td><td>5</td></tr></table>

# 5 更改提要表

该表用于返回反映修订过程中的更改提要信息。

表 4-3-9.5 更改提要表  

<table><tr><td>列 表</td><td>类型</td><td>飞机标记</td><td>描 述</td></tr><tr><td>HIGHLIGHTS_ID*</td><td>INT</td><td>NA</td><td>分配的唯一标识符</td></tr><tr><td>entry_table_name**</td><td>CHAR</td><td>NA</td><td>该条目指向的纲要模型表的名称</td></tr><tr><td>entry_key_name**</td><td>CHAR</td><td>NA</td><td>主关键字的栏名称</td></tr><tr><td>@ENTRY_KEY_ID**</td><td>INT</td><td>NA</td><td>主关键字值,用以标识更改提要适用的文件单元</td></tr><tr><td>@GEN.DOCS.DOC_ID**</td><td>INT</td><td>NA</td><td>文件ID。通用纲要模型(GEN)中的Doc表的外部关键字</td></tr><tr><td>EFFECTIVITY_MASK</td><td>BITFIELD</td><td>NA</td><td>表示适用的有效性模板</td></tr><tr><td>effectivity_info</td><td>TEXT</td><td>-effect&gt;</td><td>有效性信息</td></tr><tr><td>chapter_nbr</td><td>CHAR</td><td>&lt;? chapnbr&gt;</td><td>章号</td></tr><tr><td>section_nbr</td><td>CHAR</td><td>&lt;? sectnbr&gt;</td><td>节号</td></tr><tr><td>subject_nbr</td><td>CHAR</td><td>&lt;? subjnbr&gt;</td><td>题目号</td></tr><tr><td>pageblock_nbr</td><td>CHAR</td><td>&lt;? pgblknbr&gt;</td><td>页号组号</td></tr><tr><td>config_nbr</td><td>CHAR</td><td>&lt;? confnbr&gt;</td><td>标识页号组的一个唯一构型</td></tr><tr><td>airline_unique_code</td><td>CHAR</td><td>&lt;? alunqi&gt;</td><td>航空公司唯一标识符</td></tr><tr><td>variant_nbr</td><td>CHAR</td><td>&lt;? varnbr&gt;</td><td>差异号</td></tr><tr><td>config_letter</td><td>CHAR</td><td>&lt;? confltr&gt;</td><td>构型号</td></tr><tr><td>sequence_nbr</td><td>CHAR</td><td>&lt;? seq&gt;</td><td>顺序号</td></tr><tr><td>function_code</td><td>CHAR</td><td>&lt;? func&gt;</td><td>功能代码</td></tr><tr><td>graphic_title</td><td>TEXT</td><td>&lt;title&gt;</td><td>当一幅图形或图页为更改目标时使用</td></tr><tr><td>sheet_nbr</td><td>INT</td><td>&lt;sheet sheetnbr&gt;</td><td>在图形的图页为更改目标时使用</td></tr><tr><td>FM_Division_Name</td><td>CHAR</td><td>NA</td><td>当FM为更改目标时使用</td></tr><tr><td>key_code</td><td>CHAR</td><td>&lt;? key&gt;</td><td>文件实例中唯一的一个位置标识(标识符)</td></tr><tr><td>change_description</td><td>CHAR</td><td>&lt;chgdesc&gt;</td><td>修订过程中更改的描述</td></tr></table>

# 6 章表

该表用于返回一个或多个手册的章信息。一个章的全部文本用一个给定行中的 chapter_text 栏来表示。

表4-3-9.6 章表  

<table><tr><td>栏 名</td><td>类型</td><td>飞机标记</td><td>描 述</td></tr><tr><td>CHAPTER_ID*</td><td>INT</td><td>NA</td><td>分配的唯一ID</td></tr><tr><td>Chapter_nbr**</td><td>CHAR</td><td>&lt;chapter chapnbr&gt;</td><td>章号</td></tr><tr><td>@GEN.DOCS.DOC_ID**</td><td>INT</td><td>NA</td><td>文件ID。通用纲要模型(GEN)中的 Doc 表的外部关键字</td></tr><tr><td>EFFECTIVITY_MASK**</td><td>BITFIELD</td><td>NA</td><td>表示适用的有效性模板。(在数据库准备期间分配)</td></tr><tr><td>Effectivity_info</td><td>TEXT</td><td>-effect&gt;</td><td>有效性信息</td></tr><tr><td>Revision_date</td><td>DATE</td><td>&lt;chapter revdate&gt;</td><td>更改日期</td></tr><tr><td>Key_code</td><td>CHAR</td><td>&lt;chapter key&gt;</td><td>一个位置标识(标识符),在文件样本中是唯一的</td></tr><tr><td>Seq_nbr</td><td>INT</td><td>NA</td><td>资料中行的逻辑顺序。</td></tr><tr><td>Chapter_title</td><td>TEXT</td><td>&lt;title&gt;</td><td>章标题</td></tr><tr><td>Chapter_text</td><td>TEXT</td><td>&lt;chapter&gt;</td><td>一章的所有 SGML 片段</td></tr><tr><td>Chapter_startoff</td><td>INT</td><td>NA</td><td>通用纲要模型中的 Doc 表[参见本文4-3-1.7.1]中描述的 chapter _text 栏起始的相对位置</td></tr><tr><td>Chapter_endoff</td><td>INT</td><td>NA</td><td>通用纲要模型中的 Doc 表[参见本文4-3-1.7.1]中描述的 chapter _text 栏结束的相对位置</td></tr></table>

# 7 节表

该表用于返回一个或多个手册的节信息。一节的全部文本用一个给定行中的section_text栏来表示。

表4-3-9.7 节表  

<table><tr><td>栏 名</td><td>类型</td><td>飞机标记</td><td>描 述</td></tr><tr><td>SECTION_ID*</td><td>INT</td><td>NA</td><td>分配的唯一ID</td></tr><tr><td>Section_nbr**</td><td>CHAR</td><td>&lt;section sectnbr&gt;</td><td>节号</td></tr><tr><td>@CHAPTER.CHAPTER_ID**</td><td>INT</td><td>NA</td><td>章表的参考</td></tr><tr><td>@GEN.DOCS.DOC_ID</td><td>INT</td><td>NA</td><td>文件ID。通用纲要模型(GEN)中的Doc表的外部关键字</td></tr><tr><td>Chapter_nbr</td><td>CHAR</td><td>&lt;section chapnbr&gt;</td><td>章号</td></tr><tr><td>Revision_date</td><td>DATE</td><td>&lt;section revdate&gt;</td><td>更改日期。</td></tr><tr><td>Key_code</td><td>CHAR</td><td>&lt;section key&gt;</td><td>文件实例中唯一的一个位置标识(标识符)</td></tr><tr><td>Seq_nbr</td><td>INT</td><td>NA</td><td>资料行的逻辑顺序</td></tr><tr><td>Section_title</td><td>TEXT</td><td>&lt;title&gt;</td><td>节标题</td></tr><tr><td>Section_text</td><td>TEXT</td><td>&lt;section&gt;</td><td>一节的所有 SGML 片段</td></tr><tr><td>Section_startoff</td><td>INT</td><td>NA</td><td>通用纲要模型中的 Doc 表[参见本文 4-3 -1.7.1]中描述的 section_text 栏起始的相对位置</td></tr><tr><td>Section_endoff</td><td>INT</td><td>NA</td><td>通用纲要模型中的 Doc 表[参见本文 4-3 -1.7.1]中描述的 section_text 栏结束的相对位置</td></tr></table>

# 8 题目表

该表用于返回一个或多个手册的题目信息。一个题目的全部文本用一个给定行中的 subject_text 栏来表示。

表 4-3-9.8 题目表  

<table><tr><td>栏 名</td><td>类型</td><td>飞机标记</td><td>描 述</td></tr><tr><td>SUBJECT_ID*</td><td>INT</td><td>NA</td><td>分配的唯一ID</td></tr><tr><td>Subject_nbr**</td><td>CHAR</td><td>&lt;sub&gt;subject sub jnbr&gt;</td><td>题目号</td></tr><tr><td>@SECTION SECTION_ID**</td><td>INT</td><td>NA</td><td>参考节表</td></tr><tr><td>@GEN.DOCS.DOC_ID</td><td>INT</td><td>NA</td><td>文件ID。通用纲要模型(GEN)中的Docs表的外部关键字</td></tr><tr><td>Chapter_nbr</td><td>CHAR</td><td>&lt;object chapnbr&gt;</td><td>章号</td></tr><tr><td>Section_nbr</td><td>CHAR</td><td>&lt;object sectnbr&gt;</td><td>节号</td></tr><tr><td>Revision_date</td><td>DATE</td><td>&lt;object revdate&gt;</td><td>更改日期</td></tr><tr><td>key_code</td><td>CHAR</td><td>&lt;object key&gt;</td><td>文件实例中唯一的一个位置标识(标识符)</td></tr><tr><td>seq_nbr</td><td>INT</td><td>NA</td><td>资料中行的逻辑顺序</td></tr><tr><td>Subject_title</td><td>TEXT</td><td>&lt;title&gt;</td><td>题目的标题</td></tr><tr><td>Subject_text</td><td>TEXT</td><td>&lt;object&gt;</td><td>一个题目的所有SGML片段</td></tr><tr><td>Subject_startoff</td><td>INT</td><td>NA</td><td>通用纲要模型中的Doc表[参见本文4-3-1.7.1]中描述的 subject_text 栏起始的相对位置</td></tr><tr><td>Subject_endoff</td><td>INT</td><td>NA</td><td>通用纲要模型中的Doc表[参见本文4-3-1.7.1]中描述的 subject_text 栏结束的相对位置</td></tr></table>

# 9 页号组表

该表包含一个或多个手册的页号组的信息。一个页号组的全部文本用一个给定行中的 pageblock_text 栏来表示。

表 4-3-9.9 页号组表  

<table><tr><td>栏 名</td><td>类型</td><td>飞机标记</td><td>描 述</td></tr><tr><td>PAGEBLOCK_ID*</td><td>INT</td><td>NA</td><td>分配的唯一ID。</td></tr><tr><td>Pageblock_nbr**</td><td>CHAR</td><td>&lt;pgblk pgblknbr&gt;</td><td>页号组编号。</td></tr><tr><td>config_nbr**</td><td>CHAR</td><td>&lt;pgblk confnbr&gt;</td><td>标识页号组的一个唯一构型。</td></tr><tr><td>@SUBJECT.SUBJECT_ID* *</td><td>INT</td><td>NA</td><td>参考题目表。</td></tr><tr><td>EFFECTIVITY_MASK**</td><td>BITFIELD</td><td>NA</td><td>表示适用的有效性模板。(在数据库准备期间分配)。</td></tr><tr><td>@GEN.DOCS.DOC_ID</td><td>INT</td><td>NA</td><td>文件ID。通用纲要模型(GEN)中的Doc表的外部关键字。</td></tr><tr><td>Effectivity_info</td><td>TEXT</td><td>-effect&gt;</td><td>有效性信息。</td></tr><tr><td>Revision_date</td><td>DATE</td><td>&lt;pgblk revdate&gt;</td><td>更改日期。</td></tr><tr><td>key_code</td><td>CHAR</td><td>&lt;pgblk key&gt;</td><td>文件实例中唯一的一个位置标识(标识符)。</td></tr><tr><td>Chapter_nbr</td><td>CHAR</td><td>&lt;pgblk chapnbr&gt;</td><td>章号。</td></tr><tr><td>Section_nbr</td><td>CHAR</td><td>&lt;pgblk sectnbr&gt;</td><td>节号。</td></tr><tr><td>Subject_nbr</td><td>CHAR</td><td>&lt;pgblk sub jnbr&gt;</td><td>题目号。</td></tr><tr><td>Configuration_text</td><td>CHAR</td><td>Not Used</td><td>定义构型的文本。</td></tr><tr><td>seq_nbr</td><td>INT</td><td>NA</td><td>资料中行的逻辑顺序。</td></tr><tr><td>Pageblock_title</td><td>TEXT</td><td>&lt;title&gt;</td><td>页号组标题。</td></tr><tr><td>Pageblock_fml_text</td><td>TEXT</td><td>&lt;pbfmatr&gt;</td><td>页号组的前页内容。</td></tr><tr><td>Pageblock_text</td><td>TEXT</td><td>&lt;pgblk&gt;</td><td>一个页号组的所有SGML片段。</td></tr><tr><td>Pageblock_startoff</td><td>INT</td><td>NA</td><td>通用纲要模型中的Doc表[参见本文4-3-1.7.1]中描述的pageblock_text栏起始的相对位置</td></tr><tr><td>pageblock_endoff</td><td>INT</td><td>NA</td><td>通用纲要模型中的Doc表[参见本文4-3-1.7.1]中描述的pageblock_text栏结束的相对位置</td></tr></table>

图例

# 10 任务表

该表包含一个或多个手册的任务的信息。一个任务的全部文本用一个给定行中的 task.tex 栏来表示。

表 4-3-9.10 任务表  

<table><tr><td>栏 名</td><td>类型</td><td>飞机标记</td><td>描 述</td></tr><tr><td>TASK_ID*</td><td>INT</td><td>NA</td><td>分配的唯一ID</td></tr><tr><td>function_code**</td><td>CHAR</td><td>&lt;task func&gt;</td><td>功能代码</td></tr><tr><td>sequence_nbr**</td><td>CHAR</td><td>&lt;task seq&gt;</td><td>顺序号</td></tr><tr><td>airline_unique_code**</td><td>CHAR</td><td>&lt;task alunqi&gt;</td><td>航空公司唯一标识符</td></tr><tr><td>variant_nbr**</td><td>CHAR</td><td>&lt;task varnbr&gt;</td><td>标识任务的差异</td></tr><tr><td>config_letter**</td><td>CHAR</td><td>&lt;task confltr&gt;</td><td>任务构型文字-AMTOSS代码的部分</td></tr><tr><td>@PAGEBLOCK.PAGEBLOCK_ID* *</td><td>INT</td><td>NA</td><td>参考页号组表</td></tr><tr><td>Effectivity_Mask**</td><td>BITFIELD</td><td>NA</td><td>表示适用的有效性模板。(在数据库准备期间分配)</td></tr><tr><td>@GEN.DOCS.DOC_ID</td><td>INT</td><td>NA</td><td>文件ID。通用纲要模型(GEN)中的Doc表的外部关键字</td></tr><tr><td>effectivity_info</td><td>TEXT</td><td>-effect&gt;</td><td>有效性信息</td></tr><tr><td>chapter_nbr</td><td>CHAR</td><td>&lt;task chapnbr&gt;</td><td>章号</td></tr><tr><td>Section_nbr</td><td>CHAR</td><td>&lt;task sectnbr&gt;</td><td>节号</td></tr><tr><td>subject_nbr</td><td>CHAR</td><td>&lt;task sub jnbr&gt;</td><td>题目号</td></tr><tr><td>pageblock_nbr</td><td>CHAR</td><td>&lt;task pgblknbr&gt;</td><td>页号组分组</td></tr><tr><td>config_nbr</td><td>CHAR</td><td>&lt;task con fnbr&gt;</td><td>标识页号组的一个唯一构型</td></tr><tr><td>key_code</td><td>CHAR</td><td>&lt;task key&gt;</td><td>文件实例中唯一的一个位置标识(标识符)</td></tr><tr><td>revision_date</td><td>DATE</td><td>&lt;task revdate&gt;</td><td>更改日期</td></tr><tr><td>seq_nbr</td><td>INT</td><td>NA</td><td>资料中行的逻辑顺序</td></tr><tr><td>task_title</td><td>TEXT</td><td>&lt;title&gt;</td><td>任务标题</td></tr><tr><td>task_fmt_text</td><td>TEXT</td><td>&lt;tfmatr&gt;</td><td>任务的前页</td></tr><tr><td>task_text</td><td>TEXT</td><td>&lt;task&gt;</td><td>一个任务的所有SGML片段</td></tr><tr><td>task_startoff</td><td>INT</td><td>NA</td><td>通用纲要模型中的Doc表[参见本文4-3-1.7.1]中描述的task_text栏起始的相对位置</td></tr><tr><td>task_endoff</td><td>INT</td><td>NA</td><td>通用纲要模型中的Doc表[参见本文4-3-1.7.1]中描述的task_text栏结束的相对位置</td></tr></table>

# 11 主题

该表包含一个或多个手册的主题信息。一个主题的全部文本用一个给定行中的 Topic_text 栏来表示。

表4-3-9.11 主题表  

<table><tr><td>栏 名</td><td>类型</td><td>飞机标记</td><td>描 述</td></tr><tr><td>TOPIC_ID*</td><td>INT</td><td>NA</td><td>分配的唯一ID</td></tr><tr><td>@TASK.TASK_ID**</td><td>INT</td><td>NA</td><td>参考任务表</td></tr><tr><td>seq_nbr</td><td>INT</td><td>NA</td><td>资料中行的逻辑顺序</td></tr><tr><td>EFFECTIVITY_MASK**</td><td>BITFIELD</td><td>NA</td><td>表示适用的有效性模板。(在数据库准备期间分配)</td></tr><tr><td>@GEN.DOCS.DOC_ID</td><td>INT</td><td>NA</td><td>文件ID。通用纲要模型(GEN)中的Doc表的外部关键字</td></tr><tr><td>Effectivity_info</td><td>TEXT</td><td>-effect&gt;</td><td>有效性信息</td></tr><tr><td>chapter_nbr</td><td>CHAR</td><td>&lt;task chapnbr&gt;</td><td>章号</td></tr><tr><td>section_nbr</td><td>CHAR</td><td>&lt;task sectnbr&gt;</td><td>节号</td></tr><tr><td>subject_nbr</td><td>CHAR</td><td>&lt;task subjnbr&gt;</td><td>题目号</td></tr><tr><td>Pageblock_nbr</td><td>CHAR</td><td>&lt;task pgblknbr&gt;</td><td>页号组号</td></tr><tr><td>config_nbr</td><td>CHAR</td><td>&lt;task confnbr&gt;</td><td>标识页号组的一个唯一构型</td></tr><tr><td>topic_title</td><td>TEXT</td><td>&lt;title&gt;</td><td>主题的标题</td></tr><tr><td>topic_text</td><td>TEXT</td><td>&lt;topic&gt;</td><td>一个主题的所有SGML片段</td></tr><tr><td>topic_tartoff</td><td>INT</td><td>NA</td><td>通用纲要模型中的Doc表[参见本文4-3-1.7.1]中描述的topic_text栏起始的相对位置</td></tr><tr><td>topic_endoff</td><td>INT</td><td>NA</td><td>通用纲要模型中的Doc表[参见本文4-3-1.7.1]中描述的topic_text栏结束的相对位置</td></tr></table>

# 12 分任务表

该表包含一个或多个手册的分任务的信息。一个分任务的全部文本用一个给定行中的 subtask_text 栏来表示。

表 4-3-9.12 分任务表  

<table><tr><td>栏 名</td><td>类型</td><td>飞机标记</td><td>描述</td></tr><tr><td>SUBTASK_ID*</td><td>INT</td><td>NA</td><td>分配的唯一ID。</td></tr><tr><td>@TOPIC.TOPIC_ID**</td><td>INT</td><td>NA</td><td>参考主题表的外部关键字。</td></tr><tr><td>airline_unique_code**</td><td>CHAR</td><td>&lt;sub&gt;subtask alunqi&lt;/sub&gt;</td><td>航空公司唯一标识符</td></tr><tr><td>variant_nbr**</td><td>CHAR</td><td>&lt;sub&gt;subtask varnbr&lt;/sub&gt;</td><td>标识任务的差异</td></tr><tr><td>config_letter**</td><td>CHAR</td><td>&lt;sub&gt;subtask confltr&lt;/sub&gt;</td><td>任务构型字母。</td></tr><tr><td>sequence_nbr**</td><td>CHAR</td><td>&lt;sub&gt;subtask seq&lt;/sub&gt;</td><td>顺序号。</td></tr><tr><td>function_code**</td><td>CHAR</td><td>&lt;sub&gt;subtask func&gt;&lt;/sub&gt;</td><td>功能代码。</td></tr><tr><td>EFFECTIVITY_MASK**</td><td>BITFIELD</td><td>NA</td><td>表示适用的有效性模板。(在数据库准备期间分配)。</td></tr><tr><td>@GEN.DOCS.DOC_ID</td><td>INT</td><td>NA</td><td>文件 ID。通用纲要模型(GEN)中的 Doc表的外部关键字。</td></tr><tr><td>effectivity_info</td><td>TEXT</td><td>-effect&gt;</td><td>有效性信息。</td></tr><tr><td>chapter_nbr</td><td>CHAR</td><td>&lt;sub&gt;subtask chapnbr&gt;&lt;/sub&gt;</td><td>章号。</td></tr><tr><td>section_nbr</td><td>CHAR</td><td>&lt;sub&gt;subtask sectnbr&gt;&lt;/sub&gt;</td><td>节号。</td></tr><tr><td>subject_nbr</td><td>CHAR</td><td>&lt;sub&gt;subtask subjnbr&gt;&lt;/sub&gt;</td><td>题目号。</td></tr><tr><td>pageblock_nbr</td><td>CHAR</td><td>&lt;sub&gt;subtask pgblknbr&gt;&lt;/sub&gt;</td><td>页号组号。</td></tr><tr><td>config_nbr</td><td>CHAR</td><td>&lt;sub&gt;subtask confnbr&gt;&lt;/sub&gt;</td><td>标识页号组的一个唯一构型。</td></tr><tr><td>key_code</td><td>CHAR</td><td>&lt;sub&gt;subtask key&gt;&lt;/sub&gt;</td><td>文件实例中唯一的一个位置标识(标识符)。</td></tr><tr><td>revision_date</td><td>DATE</td><td>&lt;sub&gt;subtask revdate&gt;&lt;/sub&gt;</td><td>更改日期。</td></tr><tr><td>seq_nbr</td><td>INT</td><td>NA</td><td>资料中行的逻辑顺序。</td></tr><tr><td>subtask_text</td><td>TEXT</td><td>&lt;sub&gt;subtask&gt;&lt;/sub&gt;</td><td>一个分任务的所有 SGML 片段。</td></tr><tr><td>subtask_startoff</td><td>INT</td><td>NA</td><td>通用纲要模型中的 Doc 表 [参见本文 4-3-1.7.1]中描述的 subtask_text 栏起始的相对位置</td></tr><tr><td>subtask_endoff</td><td>INT</td><td>NA</td><td>通用纲要模型(GEN)中的 Doc 表中描述的 subtask_text 栏起始的相对位置</td></tr></table>

# 13 图形

该表包含飞机维修和发动机大修手册中图形的信息。图形图页的二进制图像可在图页表中查到。

表4-3-9.13 图形表  

<table><tr><td>栏 名</td><td>类型</td><td>飞机标记</td><td>描 述</td></tr><tr><td>GRAPHIC_ID*</td><td>INT</td><td>NA</td><td>分配的唯一ID</td></tr><tr><td>key_code**</td><td>CHAR</td><td>&lt;graphic key&gt;</td><td>图形的唯一标识符</td></tr><tr><td>EFFECTIVITY_MASK**</td><td>BITFIELD</td><td>NA</td><td>表示适用的有效性模板。(在数据库准备期间分配)</td></tr><tr><td>@GEN.DOCS.DOC_ID**</td><td>INT</td><td>NA</td><td>文件 ID。通用纲要模型(GEN)中的Doc 表的外部关键字</td></tr><tr><td>effectivity_info</td><td>TEXT</td><td>-effect&gt;</td><td>有效性信息</td></tr><tr><td>graphic_title</td><td>TEXT</td><td>&lt;title&gt;</td><td>图形标题</td></tr><tr><td>sheet_count</td><td>INT</td><td>NA</td><td>图形中的图页编号</td></tr><tr><td>revision_date</td><td>DATE</td><td>&lt;graphic revdate&gt;</td><td>更改日期</td></tr><tr><td>seq_nbr</td><td>INT</td><td>NA</td><td>资料中行的逻辑顺序</td></tr><tr><td>graphic_text</td><td>TEXT</td><td>&lt;graphic&gt;</td><td>图形编号的所有SGML片段</td></tr></table>

# 14 图页表

该表包含飞机维修和发动机大修手册中图形的图页，并显示它们与该图形的关系。

示图可按 ATA 标准格式根据 sheet_bin 栏检索，并可选择根据 file_name 栏中显示的文件来检索。

表4-3-9.14 图页表  

<table><tr><td>栏 名</td><td>类型</td><td>飞机标记</td><td>描 述</td></tr><tr><td>SHEET_ID*</td><td>INT</td><td>NA</td><td>分配的唯一ID</td></tr><tr><td>@GRAPHIC.GRA
PHIC_ID**</td><td>INT</td><td>NA</td><td>参考图形表</td></tr><tr><td>sheet_nbr**</td><td>INT</td><td></td><td>父图形中该图页的顺序号</td></tr><tr><td>key_code**</td><td>CHAR</td><td></td><td>图页的唯一标识符</td></tr><tr><td>EFFECTIVITY_MASK**</td><td>BITFIELD</td><td>NA</td><td>表示可用有效性的模板。(在数据库准备期间分配)</td></tr><tr><td>@GEN.DOCS.DO C_ID**</td><td>INT</td><td>NA</td><td>文件ID。通用纲要模型(GEN)中的Doc 表的外部关键字</td></tr><tr><td>effectivity_info</td><td>TEXT</td><td></td><td>有效性信息</td></tr><tr><td>sheet_title</td><td>TEXT</td><td></td><td>图页标题</td></tr><tr><td>sheet_type_code</td><td>CHAR</td><td>NA</td><td>识别图形编码的格式</td></tr><tr><td>sheet_text</td><td>TEXT</td><td></td><td>一个图页编号的所有SGML片段</td></tr><tr><td>revision_date</td><td>DATE</td><td></td><td>更改日期</td></tr><tr><td>sheet_bin</td><td>GRAPHIC</td><td>NA</td><td>二进制编码图形</td></tr><tr><td>file_name</td><td>CHAR</td><td>NA</td><td>包含图形的可选文件名</td></tr></table>

# 第5章 介质、协议和资料包装

# 5-1 介质和标签

# 5-1-1 概述

飞机、发动机和主要系统的制造商应根据合同对提供必需的各种形式的出版物做好准备，这些出版物的形式包括磁带、缩微胶卷、缩微胶片或适合缩微拍摄的纸型拷贝。技术“出版物索引”可以根据用户的选择，以符合这些要求的纸质、缩微胶卷或缩微胶片的形式提供。

除了原始实际尺寸的制造商布线图中的字符或数字应符合5一3一1中规定的要求之外，本章的所有规定均适用于“布线手册”。

# 5-1-2 纸质

# 1 物理介质规范

印刷用纸应是强度良好的白纸，具有足够的克数和良好的质地，以避免双面印刷时出现印迹渗透现象，并适于最小化图像的显示(例如：大约20磅)。在满足这些要求的前提下，还应限制纸张的尺寸。

对于临时更改，除缩微胶卷拷贝外，应用黄色纸张印刷。在打印过程可以控制纸张的克数和材质。对于制造商提供的缩微胶卷拷贝，包括临时更改，应将其印制在单面、未打孔的白纸上。

紧急服务通报应用浅蓝色纸张印刷。

对于印刷的字符、线条等的反射率，如果用一个印刷对比仪表进行测量，例如MacbethPCMII，使用像柯达Wratten106号一类的滤镜时，应该最大不应超过  $8\%$  。白纸的反射率应不小于  $75\%$  。

尺寸：

1. 标准——8.5英寸  $\times 11$  英寸  
2. 加大尺寸——11英寸  $\times 16$  英寸（仅图解/图表/示图）  
3. 自定义——6.5英寸  $\times 8.5$  英寸

第5章的所有规定除文本尺寸参见5-3-1.1.1.1.2和页边距限制(参见5-3-1.1.1.2)外均适用于“布线手册”。

制造商应按照与用户签订的合同规定，为以下布线资料提供印刷好的硬拷贝：

表 5-1-2.1 接线图手册  

<table><tr><td>范围</td><td>印刷方式</td><td>页面尺寸</td><td>页面方向</td></tr><tr><td>前页和引言</td><td>双面</td><td>8.5&quot;×11&quot;</td><td>纵向</td></tr><tr><td>索引和目录表</td><td>双面</td><td>8.5&quot;×11&quot;</td><td>纵向</td></tr></table>

布线手册：

当原理图作为《布线图册》的一部分出版时，其尺寸和格式应与如下的布线图相同：

表5-1-2.2 集成原理图  

<table><tr><td>范围</td><td>印刷方式</td><td>页面尺寸</td><td>页面方向</td></tr><tr><td>系统原理图手册</td><td>单面</td><td>11&quot;×16&quot;</td><td>横向</td></tr></table>

当原理图作为单独的“原理图册”出版时，应根据3一1一12.2.5.2中的说明，按电路布局的顺序，一张接一张地连续排放，并且打好装订孔。

表 5-1-2.3 单独的原理图册  

<table><tr><td>范围</td><td>印刷方式</td><td>页面尺寸</td><td>页面方向</td></tr><tr><td>系统原理图手册</td><td>单面</td><td>8.5&quot;×11&quot;</td><td>横向</td></tr></table>

当“电气和电子设备清单”作为布线手册的一部分单独提供时，应以横向方式排版，页面尺寸为  $8.5 \times 11$  英寸，单面或双面印刷。

“电气布线和接线清单”应以横向方式排版，页面尺寸为  $8.5 \times 11$  英寸，单面或双面印刷。

标准布线实施应以双面印刷，页面尺寸为  $8.5 \times 11$  英寸，并包括“布线手册中”要求说明的所有信息（参见3-4-7）。

“微缩的布线图和原理图”：制造商应按照与用户签订的合同规定，提供单面的、 $11 \times 16$  英寸有足够分辨率的微缩图像，以便能够生成清晰的缩微胶卷和/或300dpi的扫描图像。根据“布线手册”的要求，页眉和页脚应一起使用(参见图5-1-2.1和图5-1-2.2)。

“布线图和原理图实际尺寸的底图”：制造商应按照与用户签订的合同规定，提供与制造商原始生产底图相同尺寸的可复制的布线图和原理图复本，将其印刷在半透明介质上，以便修改时可以用铅笔或墨水笔标记并擦除；以此为蓝本，可以采用晒图、直接照相或缩微摄影的方式进行复制。将原始的生产底图制成加大尺寸或标准尺寸页时，图像区域的尺寸应与本规范中的要求(参见5-1-2.1)保持一致。原始实际尺寸的布线图和原理图中的字符和数字，右缩减到最小程度后，或在加大尺寸或标准尺寸页中，最终的印刷品应清晰可辨，并应符合5-3-1.1.1.1中有关手册尺寸的规定。

![](images/bef312a83855f47b48b60bc1bb125455b87dcf6559a7813fa6f0732f7b591681.jpg)  
图5-1-2.1 系统原理框图

![](images/00a7d944802984c2dd99529bf4d667c3445fd1463f2a6cef509a5eccbb56d2f6.jpg)  
图5-1-2.2 系统原理图

# 1.1 装订

除了下面进行特殊说明的出版物之外，所有出版物都应以活页形式装订。飞机和发动机制造商的出版物及零件目录应装订在硬壳活页夹中，在书脊处应注明制造商的名称、飞机或发动机的型号以及出版物的名称。

装订应保证活页能够展开，可从右向左打开任意选定的页。

“服务通报”(SB)不要求装订。

对于按标准的3孔活页形式整理归档的文档，除了为缩微拍摄提供的页之外，所有页都应装订。孔的直径尺寸应为0.31英寸或再大一些，从装订边到孔的圆心距离为0.44英寸。为缩微拍摄提供的页不应打孔。

对于按7孔活页形式整理归档的文档，除了为缩微拍摄提供的页之外，所有页都应打孔。为缩微拍摄提供的页不应打孔。

# 1.2 索引舌

应为每章分配一个编号，每个编号都用一个写有系统标题和章号的索引舌来标记。应尽最大可能在每个出版物中使用相同的基本机群和系统索引。

以下各表反映了适用手册的要求(参见表5-1-2.4、表5-1-2.6、表5-1-2.7、表5-1-2.8、表5-1-2.9、表5-1-2.10、表5-1-2.11、表5-1-2.12、表5-1-2.13)。

表 5-1-2.4 标准出版物中维修手册索引舌的要求  

<table><tr><td></td><td>说明</td><td>索引舌</td></tr><tr><td></td><td>标题页</td><td></td></tr><tr><td></td><td>修订记录</td><td></td></tr><tr><td></td><td>有效页目录</td><td></td></tr><tr><td></td><td>目录表</td><td></td></tr><tr><td></td><td>临时更改单记录</td><td></td></tr><tr><td></td><td>发送函</td><td></td></tr><tr><td></td><td>服务通报清单</td><td></td></tr><tr><td></td><td>引言</td><td>X</td></tr><tr><td></td><td>章目录</td><td></td></tr><tr><td></td><td>飞机概述</td><td>X</td></tr><tr><td>05</td><td>时限/维护检查</td><td>X</td></tr><tr><td>06</td><td>尺寸和区域</td><td>X</td></tr><tr><td>07</td><td>顶起和支撑</td><td>X</td></tr><tr><td>08</td><td>调平和称重</td><td>X</td></tr><tr><td>09</td><td>牵引和滑行</td><td>X</td></tr><tr><td>10</td><td>停放和系留</td><td>X</td></tr><tr><td>11</td><td>标牌和标志</td><td>X</td></tr><tr><td>12</td><td>保养</td><td>X</td></tr><tr><td></td><td></td><td></td></tr><tr><td></td><td>机体系统</td><td>X</td></tr><tr><td></td><td></td><td></td></tr><tr><td>20</td><td>标准实施-机体</td><td>X</td></tr><tr><td>21</td><td>空调</td><td>X</td></tr><tr><td>22</td><td>自动飞行</td><td>X</td></tr><tr><td>23</td><td>通信</td><td>X</td></tr><tr><td>24</td><td>电源</td><td>X</td></tr><tr><td>25</td><td>设备/装备</td><td>X</td></tr><tr><td>26</td><td>防火</td><td>X</td></tr><tr><td>27</td><td>飞行控制</td><td>X</td></tr><tr><td>28</td><td>燃油</td><td>X</td></tr><tr><td>29</td><td>液压源</td><td>X</td></tr><tr><td>30</td><td>防冰和防雨</td><td>X</td></tr><tr><td>31</td><td>显示/记录系统</td><td>X</td></tr><tr><td>32</td><td>起落架</td><td>X</td></tr><tr><td>33</td><td>照明</td><td>X</td></tr><tr><td>34</td><td>导航</td><td>X</td></tr><tr><td>35</td><td>氧气</td><td>X</td></tr><tr><td>36</td><td>气动</td><td>X</td></tr><tr><td>37</td><td>真空</td><td>X</td></tr><tr><td>38</td><td>水/污物</td><td>X</td></tr><tr><td>41</td><td>压舱水</td><td>X</td></tr><tr><td>45</td><td>中央维修系统</td><td>X</td></tr><tr><td>46</td><td>信息系统</td><td>X</td></tr><tr><td>49</td><td>机载辅助动力</td><td>X</td></tr><tr><td></td><td></td><td></td></tr><tr><td></td><td>结构</td><td>X</td></tr><tr><td></td><td></td><td></td></tr><tr><td>51</td><td>标准实施一结构</td><td>X</td></tr><tr><td>52</td><td>舱门</td><td>X</td></tr><tr><td>53</td><td>机身</td><td>X</td></tr><tr><td>54</td><td>短舱/吊舱</td><td>X</td></tr><tr><td>55</td><td>安定面</td><td>X</td></tr><tr><td>56</td><td>窗</td><td>X</td></tr><tr><td>57</td><td>机翼</td><td>X</td></tr><tr><td></td><td>螺旋桨/旋翼</td><td>X</td></tr><tr><td>60</td><td>标准实施一螺旋桨/旋翼</td><td>X</td></tr><tr><td>61</td><td>螺旋桨</td><td>X</td></tr><tr><td>62</td><td>旋翼</td><td>X</td></tr><tr><td>63</td><td>旋翼驱动</td><td>X</td></tr><tr><td>64</td><td>尾旋翼</td><td>X</td></tr><tr><td>65</td><td>尾旋翼驱动</td><td>X</td></tr><tr><td>66</td><td>可折叠桨叶/挂架</td><td>X</td></tr><tr><td>67</td><td>旋翼飞行控制</td><td>X</td></tr><tr><td></td><td></td><td></td></tr><tr><td></td><td>动力装置</td><td>X</td></tr><tr><td></td><td></td><td></td></tr><tr><td>70</td><td>标准实施一发动机</td><td>X</td></tr><tr><td>71</td><td>动力装置</td><td>X</td></tr><tr><td>72</td><td>发动机</td><td>X</td></tr><tr><td>73</td><td>发动机燃油及控制</td><td>X</td></tr><tr><td>74</td><td>点火</td><td>X</td></tr><tr><td>75</td><td>引气</td><td>X</td></tr><tr><td>76</td><td>发动机控制</td><td>X</td></tr><tr><td>77</td><td>发动机指示</td><td>X</td></tr><tr><td>78</td><td>排气</td><td>X</td></tr><tr><td>79</td><td>滑油</td><td>X</td></tr><tr><td>80</td><td>起动</td><td>X</td></tr><tr><td>81</td><td>涡轮机</td><td>X</td></tr><tr><td>82</td><td>注水</td><td>X</td></tr><tr><td>83</td><td>附件齿轮箱</td><td>X</td></tr><tr><td>84</td><td>助推装置</td><td>X</td></tr><tr><td>94</td><td>图表</td><td>X</td></tr></table>

表 5-1-2.5 标准出版物中布线手册索引舌的要求  

<table><tr><td></td><td>说明</td><td>索引舌</td></tr><tr><td></td><td>标题页</td><td></td></tr><tr><td></td><td>更改记录</td><td></td></tr><tr><td></td><td>有效页目录</td><td></td></tr><tr><td></td><td>目录表</td><td></td></tr><tr><td></td><td>字母索引</td><td></td></tr><tr><td></td><td>临时更改单记录</td><td></td></tr><tr><td></td><td>转送函</td><td></td></tr><tr><td></td><td>服务通报清单</td><td></td></tr><tr><td></td><td>引言</td><td>X</td></tr><tr><td></td><td>章目录</td><td>X</td></tr><tr><td></td><td>设备清单</td><td></td></tr><tr><td></td><td>飞机概述</td><td>X</td></tr><tr><td>05</td><td>时限/维护检查</td><td></td></tr><tr><td>06</td><td>尺寸和区域</td><td></td></tr><tr><td>07</td><td>顶起和支撑</td><td></td></tr><tr><td>08</td><td>调平和称重</td><td></td></tr><tr><td>09</td><td>牵引和滑行</td><td></td></tr><tr><td>10</td><td>停放和系留</td><td></td></tr><tr><td>11</td><td>标牌和标志</td><td></td></tr><tr><td>12</td><td>保养</td><td></td></tr><tr><td></td><td></td><td></td></tr><tr><td></td><td></td><td>X</td></tr><tr><td></td><td>机体系统</td><td></td></tr><tr><td>20</td><td>标准实施-机体</td><td>X</td></tr><tr><td>21</td><td>空调</td><td>X</td></tr><tr><td>22</td><td>自动飞行</td><td>X</td></tr><tr><td>23</td><td>通信</td><td>X</td></tr><tr><td>24</td><td>电源</td><td>X</td></tr><tr><td>25</td><td>设备/装备</td><td>X</td></tr><tr><td>26</td><td>防火</td><td>X</td></tr><tr><td>27</td><td>飞行控制</td><td>X</td></tr><tr><td>28</td><td>燃油</td><td>X</td></tr><tr><td>29</td><td>液压源</td><td>X</td></tr><tr><td>30</td><td>防冰和防雨</td><td>X</td></tr><tr><td>31</td><td>显示/记录系统</td><td>X</td></tr><tr><td>32</td><td>起落架</td><td>X</td></tr><tr><td>33</td><td>照明</td><td>X</td></tr><tr><td>34</td><td>导航</td><td>X</td></tr><tr><td>35</td><td>氧气</td><td>X</td></tr><tr><td>36</td><td>气动</td><td>X</td></tr><tr><td>37</td><td>真空</td><td>X</td></tr><tr><td>38</td><td>水/污物</td><td>X</td></tr><tr><td>41</td><td>压舱水</td><td>X</td></tr><tr><td>45</td><td>中央维修系统</td><td>X</td></tr><tr><td>46</td><td>信息系统</td><td></td></tr><tr><td>49</td><td>机载辅助动力</td><td></td></tr><tr><td></td><td>结构</td><td></td></tr><tr><td>51</td><td>标准实施和结构</td><td></td></tr><tr><td>52</td><td>舱门</td><td>X</td></tr><tr><td>53</td><td>机身</td><td></td></tr><tr><td>54</td><td>短舱/吊舱</td><td></td></tr><tr><td>55</td><td>安定面</td><td></td></tr><tr><td>56</td><td>窗</td><td></td></tr><tr><td>57</td><td>机翼</td><td></td></tr><tr><td></td><td></td><td></td></tr><tr><td></td><td></td><td>X</td></tr><tr><td></td><td>螺旋桨/旋翼</td><td></td></tr><tr><td>60</td><td>标准实施-螺旋桨/旋翼</td><td>X</td></tr><tr><td>61</td><td>螺旋桨</td><td>X</td></tr><tr><td>62</td><td>旋翼</td><td>X</td></tr><tr><td>63</td><td>旋翼驱动</td><td>X</td></tr><tr><td></td><td>说明</td><td>·索引舌</td></tr><tr><td>64</td><td>尾旋翼</td><td>X</td></tr><tr><td>65</td><td>尾旋翼驱动</td><td>X</td></tr><tr><td>66</td><td>可折叠桨叶/挂架</td><td>X</td></tr><tr><td>67</td><td>旋翼飞行控制</td><td>X</td></tr><tr><td></td><td>动力装置</td><td>X</td></tr><tr><td>70</td><td>标准实施-发动机</td><td>X</td></tr><tr><td>71</td><td>动力装置</td><td>X</td></tr><tr><td>72</td><td>发动机</td><td>X</td></tr><tr><td>73</td><td>发动机燃油及控制</td><td>X</td></tr><tr><td>74</td><td>点火</td><td>X</td></tr><tr><td>75</td><td>Air 引气</td><td>X</td></tr><tr><td>76</td><td>发动机控制</td><td>X</td></tr><tr><td>77</td><td>发动机指示</td><td>X</td></tr><tr><td>78</td><td>排气</td><td>X</td></tr><tr><td>79</td><td>滑油</td><td>X</td></tr><tr><td>80</td><td>起动</td><td>X</td></tr><tr><td>81</td><td>涡轮机</td><td>X</td></tr><tr><td>82</td><td>注水</td><td>X</td></tr><tr><td>83</td><td>附件齿轮箱</td><td>X</td></tr><tr><td>84</td><td>助推装置</td><td>X</td></tr><tr><td>94</td><td>图表</td><td>X</td></tr></table>

表 5-1-2.6 标准出版物中结构修理手册索引舌的要求  

<table><tr><td></td><td>说明</td><td>索引舌</td></tr><tr><td></td><td>标题页</td><td></td></tr><tr><td></td><td>更改记录</td><td></td></tr><tr><td></td><td>有效页目录</td><td></td></tr><tr><td></td><td>目录表</td><td></td></tr><tr><td></td><td>临时更改单记录</td><td></td></tr><tr><td></td><td>发送函</td><td></td></tr><tr><td></td><td>临时更改单有效目录</td><td></td></tr><tr><td></td><td>服务通报清单</td><td></td></tr><tr><td></td><td>引言</td><td></td></tr><tr><td></td><td>章目录</td><td></td></tr><tr><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td></tr><tr><td></td><td>飞机概述</td><td></td></tr><tr><td>05</td><td>时限/维护检查</td><td></td></tr><tr><td>06</td><td>尺寸和区域</td><td></td></tr><tr><td>07</td><td>顶起和支撑</td><td></td></tr><tr><td>08</td><td>调平和称重</td><td></td></tr><tr><td>09</td><td>牵引和滑行</td><td></td></tr><tr><td>10</td><td>停放和系留</td><td></td></tr><tr><td>11</td><td>标牌和标志</td><td></td></tr><tr><td>12</td><td>保养</td><td></td></tr><tr><td></td><td></td><td></td></tr><tr><td></td><td></td><td>X</td></tr><tr><td></td><td>机体系统</td><td></td></tr><tr><td>20</td><td>标准实施-机体</td><td>X</td></tr><tr><td>21</td><td>空调</td><td>X</td></tr><tr><td>22</td><td>自动飞行</td><td>X</td></tr><tr><td>23</td><td>通信</td><td>X</td></tr><tr><td>24</td><td>电源</td><td>X</td></tr><tr><td>25</td><td>设备/装备</td><td>X</td></tr><tr><td>26</td><td>防火</td><td>X</td></tr><tr><td>27</td><td>飞行控制</td><td>X</td></tr><tr><td>28</td><td>燃油</td><td>X</td></tr><tr><td>29</td><td>液压源</td><td>X</td></tr><tr><td>30</td><td>防冰和防雨</td><td>X</td></tr><tr><td>31</td><td>显示/记录系统</td><td>X</td></tr><tr><td>32</td><td>起落架</td><td>X</td></tr><tr><td>33</td><td>照明</td><td>X</td></tr><tr><td>34</td><td>导航</td><td>X</td></tr><tr><td>35</td><td>氧气</td><td>X</td></tr><tr><td>36</td><td>气动</td><td>X</td></tr><tr><td>37</td><td>真空</td><td>X</td></tr><tr><td>38</td><td>水/污物</td><td>X</td></tr><tr><td>41</td><td>压舱水</td><td>X</td></tr><tr><td>45</td><td>中央维修系统</td><td>X</td></tr><tr><td>46</td><td>信息系统</td><td></td></tr><tr><td>49</td><td>机载辅助动力</td><td></td></tr><tr><td></td><td></td><td></td></tr><tr><td></td><td>结构</td><td></td></tr><tr><td></td><td></td><td></td></tr><tr><td>51</td><td>标准实施一结构</td><td></td></tr><tr><td>52</td><td>舱门</td><td>X</td></tr><tr><td>53</td><td>机身</td><td></td></tr><tr><td>54</td><td>短舱/吊舱</td><td></td></tr><tr><td>55</td><td>安定面</td><td></td></tr><tr><td>56</td><td>窗</td><td></td></tr><tr><td>57</td><td>机翼</td><td></td></tr><tr><td></td><td></td><td></td></tr><tr><td></td><td></td><td>X</td></tr><tr><td></td><td>螺旋桨/旋翼</td><td></td></tr><tr><td>60</td><td>标准实施一螺旋桨/旋翼</td><td>X</td></tr><tr><td>61</td><td>螺旋桨</td><td>X</td></tr><tr><td>62</td><td>旋翼</td><td>X</td></tr><tr><td>63</td><td>旋翼驱动</td><td>X</td></tr><tr><td>64</td><td>尾旋翼</td><td>X</td></tr><tr><td>65</td><td>尾旋翼驱动</td><td>X</td></tr><tr><td>66</td><td>可折叠桨叶/挂架</td><td>X</td></tr><tr><td>67</td><td>旋翼飞行控制</td><td>X</td></tr><tr><td></td><td>动力装置</td><td>X</td></tr><tr><td>70</td><td>标准实施一发动机</td><td>X</td></tr><tr><td>71</td><td>动力装置</td><td>X</td></tr><tr><td>72</td><td>发动机</td><td>X</td></tr><tr><td>73</td><td>发动机燃油及控制</td><td>X</td></tr><tr><td>74</td><td>点火</td><td>X</td></tr><tr><td>75</td><td>引气</td><td>X</td></tr><tr><td>76</td><td>发动机控制</td><td>X</td></tr><tr><td>77</td><td>发动机指示</td><td>X</td></tr><tr><td>78</td><td>排气</td><td>X</td></tr><tr><td>79</td><td>滑油</td><td>X</td></tr><tr><td>80</td><td>起动</td><td>X</td></tr><tr><td>81</td><td>涡轮机</td><td>X</td></tr><tr><td>82</td><td>注水</td><td>X</td></tr><tr><td>83</td><td>附件齿轮箱</td><td>X</td></tr><tr><td>84</td><td>助推装置</td><td>X</td></tr><tr><td>94</td><td>图表</td><td>X</td></tr></table>

表 5-1-2.7 标准出版物中图解零件目录索引舌的要求  

<table><tr><td></td><td>说明</td><td>索引舌</td></tr><tr><td></td><td>标题页</td><td></td></tr><tr><td></td><td>更改记录</td><td></td></tr><tr><td></td><td>有效页目录</td><td></td></tr><tr><td></td><td>目录表</td><td></td></tr><tr><td></td><td>临时更改单记录</td><td></td></tr><tr><td></td><td>转送函</td><td></td></tr><tr><td></td><td>服务通报清单</td><td></td></tr><tr><td></td><td>引言</td><td></td></tr><tr><td></td><td>章目录</td><td></td></tr><tr><td></td><td>数字索引</td><td></td></tr><tr><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td></tr><tr><td></td><td>飞机概述</td><td></td></tr><tr><td>05</td><td>时限/维护检查</td><td></td></tr><tr><td>06</td><td>尺寸和区域</td><td></td></tr><tr><td>07</td><td>顶起和支撑</td><td></td></tr><tr><td>08</td><td>调平和称重</td><td></td></tr><tr><td>09</td><td>牵引和滑行</td><td></td></tr><tr><td>10</td><td>停放和系留</td><td></td></tr><tr><td>11</td><td>标牌和标志</td><td></td></tr><tr><td>12</td><td>保养</td><td></td></tr><tr><td></td><td></td><td></td></tr><tr><td></td><td></td><td>X</td></tr><tr><td></td><td>机体系统</td><td></td></tr><tr><td>20</td><td>标准实施-机体</td><td>X</td></tr><tr><td>21</td><td>空调</td><td>X</td></tr><tr><td>22</td><td>自动飞行</td><td>X</td></tr><tr><td>23</td><td>通信</td><td>X</td></tr><tr><td>24</td><td>电源</td><td>X</td></tr><tr><td>25</td><td>设备/装备</td><td>X</td></tr><tr><td>26</td><td>防火</td><td>X</td></tr><tr><td>27</td><td>飞行控制</td><td>X</td></tr><tr><td>28</td><td>燃料</td><td>X</td></tr><tr><td>29</td><td>液压源</td><td>X</td></tr><tr><td>30</td><td>防冰和防雨</td><td>X</td></tr><tr><td>31</td><td>显示/记录系统</td><td>X</td></tr><tr><td>32</td><td>起落架</td><td>X</td></tr><tr><td>33</td><td>照明</td><td>X</td></tr><tr><td>34</td><td>导航</td><td>X</td></tr><tr><td>35</td><td>氧气</td><td>X</td></tr><tr><td>36</td><td>气动</td><td>X</td></tr><tr><td>37</td><td>真空</td><td>X</td></tr><tr><td>38</td><td>水/污物</td><td>X</td></tr><tr><td>41</td><td>压舱水</td><td>X</td></tr><tr><td>45</td><td>中央维修系统</td><td>X</td></tr><tr><td>46</td><td>信息系统</td><td></td></tr><tr><td>49</td><td></td><td></td></tr><tr><td></td><td>机载辅助动力</td><td></td></tr><tr><td></td><td>结构</td><td></td></tr><tr><td></td><td></td><td></td></tr><tr><td>51</td><td>标准实施-结构</td><td></td></tr><tr><td>52</td><td>舱门</td><td>X</td></tr><tr><td>53</td><td>机身</td><td></td></tr><tr><td>54</td><td>短舱/吊舱</td><td></td></tr><tr><td>55</td><td>安定面</td><td></td></tr><tr><td>56</td><td>窗</td><td></td></tr><tr><td>57</td><td>机翼</td><td></td></tr><tr><td></td><td></td><td></td></tr><tr><td></td><td></td><td>X</td></tr><tr><td></td><td>螺旋桨/旋翼</td><td></td></tr><tr><td>60</td><td>标准实施一螺旋桨/旋翼</td><td>X</td></tr><tr><td>61</td><td>螺旋桨</td><td>X</td></tr><tr><td>62</td><td>旋翼</td><td>X</td></tr><tr><td>63</td><td>旋翼驱动</td><td>X</td></tr><tr><td>64</td><td>尾旋翼</td><td>X</td></tr><tr><td>65</td><td>尾旋翼驱动</td><td>X</td></tr><tr><td>66</td><td>可折叠桨叶/挂架</td><td>X</td></tr><tr><td>67</td><td>旋翼飞行控制</td><td>X</td></tr><tr><td></td><td></td><td></td></tr><tr><td></td><td></td><td>X</td></tr><tr><td></td><td>动力装置</td><td></td></tr><tr><td>70</td><td>标准实施-发动机</td><td>X</td></tr><tr><td>71</td><td>动力装置</td><td>X</td></tr><tr><td>72</td><td>发动机</td><td>X</td></tr><tr><td>73</td><td>发动机燃油及控制</td><td>X</td></tr><tr><td>74</td><td>点火</td><td>X</td></tr><tr><td>75</td><td>引气</td><td>X</td></tr><tr><td>76</td><td>发动机控制</td><td>X</td></tr><tr><td>77</td><td>发动机指示</td><td>X</td></tr><tr><td>78</td><td>排气</td><td>X</td></tr><tr><td>79</td><td>滑油</td><td>X</td></tr><tr><td>80</td><td>起动</td><td>X</td></tr><tr><td>81</td><td>涡轮机</td><td>X</td></tr><tr><td>82</td><td>注水</td><td>X</td></tr><tr><td>83</td><td>附件齿轮箱</td><td>X</td></tr><tr><td>84</td><td>助推装置</td><td>X</td></tr><tr><td>94</td><td>图表</td><td>X</td></tr></table>

表 5-1-2.8 标准出版物中机载设备维修手册索引舌的要求  

<table><tr><td></td><td>说明</td><td>索引舌</td></tr><tr><td></td><td>标题页</td><td></td></tr><tr><td></td><td>更改记录</td><td></td></tr><tr><td></td><td>有效页目录</td><td></td></tr><tr><td></td><td>目录表</td><td></td></tr><tr><td></td><td>临时更改单记录</td><td></td></tr><tr><td></td><td>转送函</td><td></td></tr><tr><td></td><td>临时更改单有效目录</td><td></td></tr><tr><td></td><td>服务通报清单</td><td></td></tr><tr><td></td><td>引言</td><td></td></tr><tr><td></td><td>章目录</td><td></td></tr><tr><td></td><td></td><td></td></tr><tr><td></td><td>字母/数字索引</td><td></td></tr><tr><td></td><td></td><td></td></tr><tr><td></td><td>飞机概述</td><td></td></tr><tr><td>05</td><td></td><td></td></tr><tr><td></td><td>时限/维护检查</td><td></td></tr><tr><td></td><td></td><td>X</td></tr><tr><td></td><td>机体系统</td><td></td></tr><tr><td>20</td><td>标准实施一机体</td><td>X</td></tr><tr><td>21</td><td>空调</td><td>X</td></tr><tr><td>22</td><td>自动飞行</td><td>X</td></tr><tr><td>23</td><td>通信</td><td>X</td></tr><tr><td>24</td><td>电源</td><td>X</td></tr><tr><td>25</td><td>设备/装备</td><td>X</td></tr><tr><td>26</td><td>防火</td><td>X</td></tr><tr><td>27</td><td>飞行控制</td><td>X</td></tr><tr><td>28</td><td>燃油</td><td>X</td></tr><tr><td>29</td><td>液压源</td><td>X</td></tr><tr><td>30</td><td>防冰和防雨</td><td>X</td></tr><tr><td>31</td><td>显示/记录系统</td><td>X</td></tr><tr><td>32</td><td>起落架</td><td>X</td></tr><tr><td>33</td><td>照明</td><td>X</td></tr><tr><td>34</td><td>导航</td><td>X</td></tr><tr><td>35</td><td>氧气</td><td>X</td></tr><tr><td>36</td><td>气动</td><td>X</td></tr><tr><td>37</td><td>真空</td><td>X</td></tr><tr><td>38</td><td>水/污物</td><td>X</td></tr><tr><td>41</td><td>压舱水</td><td>X</td></tr><tr><td>45</td><td>中央维修系统</td><td>X</td></tr><tr><td>46</td><td>信息系统</td><td></td></tr><tr><td>49</td><td>机载辅助动力</td><td></td></tr><tr><td></td><td></td><td></td></tr><tr><td></td><td>标准实施和结构</td><td>X</td></tr><tr><td></td><td></td><td></td></tr><tr><td>51</td><td>结构</td><td></td></tr><tr><td>52</td><td>舱门</td><td>X</td></tr><tr><td>53</td><td>机身</td><td>X</td></tr><tr><td>54</td><td>短舱/吊舱</td><td>X</td></tr><tr><td>55</td><td>安定面</td><td>X</td></tr><tr><td>56</td><td>窗</td><td>X</td></tr><tr><td>57</td><td>机翼</td><td>X</td></tr><tr><td></td><td></td><td></td></tr><tr><td></td><td></td><td>X</td></tr><tr><td></td><td>螺旋桨/旋翼</td><td></td></tr><tr><td>60</td><td>标准实施一螺旋桨/旋翼</td><td>X</td></tr><tr><td>61</td><td>螺旋桨</td><td>X</td></tr><tr><td>62</td><td>旋翼</td><td>X</td></tr><tr><td>63</td><td>旋翼驱动</td><td>X</td></tr><tr><td>64</td><td>尾旋翼</td><td>X</td></tr><tr><td>65</td><td>尾旋翼驱动</td><td>X</td></tr><tr><td>66</td><td>可折叠桨叶/挂架</td><td>X</td></tr><tr><td>67</td><td>旋翼飞行控制</td><td>X</td></tr><tr><td></td><td></td><td></td></tr><tr><td></td><td></td><td>X</td></tr><tr><td></td><td>动力装置</td><td></td></tr><tr><td>70</td><td>标准实施一发动机</td><td>X</td></tr><tr><td>71</td><td>动力装置</td><td>X</td></tr><tr><td>72</td><td>发动机</td><td>X</td></tr><tr><td></td><td>索引舌</td><td></td></tr><tr><td></td><td>有效页目录</td><td></td></tr><tr><td></td><td>临时更改单有效页目录</td><td></td></tr><tr><td></td><td>目录</td><td></td></tr><tr><td>73</td><td>发动机燃油及控制</td><td>X</td></tr><tr><td>74</td><td>点火</td><td>X</td></tr><tr><td>75</td><td>引气</td><td>X</td></tr><tr><td>76</td><td>发动机控制</td><td>X</td></tr><tr><td>77</td><td>发动机指示</td><td>X</td></tr><tr><td>78</td><td>排气</td><td>X</td></tr><tr><td>79</td><td>滑油</td><td>X</td></tr><tr><td>80</td><td>起动</td><td>X</td></tr><tr><td>81</td><td>涡轮机</td><td>X</td></tr><tr><td>82</td><td>注水</td><td>X</td></tr><tr><td>83</td><td>附件齿轮箱</td><td>X</td></tr><tr><td>84</td><td>助推装置</td><td>X</td></tr><tr><td>94</td><td>图表</td><td>X</td></tr></table>

表 5-1-2.9 标准出版物中图解工具和设备手册索引舌的要求  

<table><tr><td></td><td>说明</td><td>索引舌</td></tr><tr><td></td><td>标题页</td><td></td></tr><tr><td></td><td>更改记录</td><td></td></tr><tr><td></td><td>有效页目录</td><td></td></tr><tr><td></td><td>目录表</td><td></td></tr><tr><td></td><td>临时更改单记录</td><td></td></tr><tr><td></td><td>转送函</td><td></td></tr><tr><td></td><td>引言</td><td></td></tr><tr><td></td><td>章目录</td><td></td></tr><tr><td></td><td>数字索引</td><td></td></tr><tr><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td></tr><tr><td></td><td>飞机概述</td><td></td></tr><tr><td>05</td><td>时限/维护检查</td><td></td></tr><tr><td>06</td><td>尺寸和区域</td><td></td></tr><tr><td>07</td><td>顶起和支撑</td><td></td></tr><tr><td>08</td><td>调平和称重</td><td></td></tr><tr><td>09</td><td>牵引和滑行</td><td></td></tr><tr><td>10</td><td>停放和系留</td><td></td></tr><tr><td>11</td><td>标牌和标志</td><td></td></tr><tr><td>12</td><td>保养</td><td></td></tr><tr><td></td><td></td><td></td></tr><tr><td></td><td></td><td>X</td></tr><tr><td></td><td>机体系统</td><td></td></tr><tr><td>20</td><td>标准实施一机体</td><td>X</td></tr><tr><td>21</td><td>空调</td><td>X</td></tr><tr><td>22</td><td>自动飞行</td><td>X</td></tr><tr><td>23</td><td>通信</td><td>X</td></tr><tr><td>24</td><td>电源</td><td>X</td></tr><tr><td>25</td><td>设备/装备</td><td>X</td></tr><tr><td>26</td><td>防火</td><td>X</td></tr><tr><td>27</td><td>飞行控制</td><td>X</td></tr><tr><td>28</td><td>燃油</td><td>X</td></tr><tr><td>29</td><td>液压源</td><td>X</td></tr><tr><td>30</td><td>防冰和防雨</td><td>X</td></tr><tr><td>31</td><td>显示/记录系统</td><td>X</td></tr><tr><td>32</td><td>起落架</td><td>X</td></tr><tr><td>33</td><td>照明</td><td>X</td></tr><tr><td>34</td><td>导航</td><td>X</td></tr><tr><td>35</td><td>氧气</td><td>X</td></tr><tr><td>36</td><td>气动</td><td>X</td></tr><tr><td>37</td><td>真空</td><td>X</td></tr><tr><td>38</td><td>水/污物</td><td>X</td></tr><tr><td>41</td><td>压舱水</td><td>X</td></tr><tr><td>45</td><td>中央维修系统</td><td>X</td></tr><tr><td>46</td><td>信息系统</td><td></td></tr><tr><td>49</td><td>机载辅助动力</td><td></td></tr><tr><td></td><td></td><td></td></tr><tr><td></td><td>结构</td><td></td></tr><tr><td></td><td></td><td></td></tr><tr><td>51</td><td>标准实施-结构</td><td></td></tr><tr><td>52</td><td>舱门</td><td>X</td></tr><tr><td>53</td><td>机身</td><td></td></tr><tr><td>54</td><td>短舱/吊舱</td><td></td></tr><tr><td>55</td><td>安定面</td><td></td></tr><tr><td>56</td><td>窗</td><td></td></tr><tr><td>57</td><td>机翼</td><td></td></tr><tr><td></td><td></td><td></td></tr><tr><td></td><td></td><td>X</td></tr><tr><td></td><td>螺旋桨/旋翼</td><td></td></tr><tr><td>60</td><td>标准实施一螺旋桨/旋翼</td><td>X</td></tr><tr><td>61</td><td>螺旋桨</td><td>X</td></tr><tr><td>62</td><td>旋翼</td><td>X</td></tr><tr><td>63</td><td>旋翼驱动</td><td>X</td></tr><tr><td>64</td><td>尾旋翼</td><td>X</td></tr><tr><td>65</td><td>尾旋翼驱动</td><td>X</td></tr><tr><td>66</td><td>可折叠桨叶/挂架</td><td>X</td></tr><tr><td>67</td><td></td><td>X</td></tr><tr><td></td><td>旋翼飞行控制</td><td></td></tr><tr><td></td><td></td><td>X</td></tr><tr><td></td><td>动力装置</td><td></td></tr><tr><td>70</td><td>标准实施-发动机</td><td>X</td></tr><tr><td>71</td><td>动力装置</td><td>X</td></tr><tr><td>72</td><td>发动机</td><td>X</td></tr><tr><td>73</td><td>发动机燃油及控制</td><td>X</td></tr><tr><td>74</td><td>点火</td><td>X</td></tr><tr><td>75</td><td>引气</td><td>X</td></tr><tr><td>76</td><td>发动机控制</td><td>X</td></tr><tr><td>77</td><td>发动机指示</td><td>X</td></tr><tr><td>78</td><td>排气</td><td>X</td></tr><tr><td>79</td><td>滑油</td><td>X</td></tr><tr><td>80</td><td>起动</td><td>X</td></tr><tr><td>81</td><td>涡轮机</td><td>X</td></tr><tr><td>82</td><td>注水</td><td>X</td></tr><tr><td>83</td><td>附件齿轮箱</td><td>X</td></tr><tr><td>84</td><td>助推装置</td><td>X</td></tr><tr><td>94</td><td>图表</td><td>X</td></tr></table>

表 5-1-2.10 标准出版物中发动机手册索引舌的要求  

<table><tr><td></td><td>说明</td><td>索引舌</td></tr><tr><td></td><td>标题页</td><td></td></tr><tr><td></td><td>更改记录</td><td></td></tr><tr><td></td><td>有效页目录</td><td></td></tr><tr><td></td><td>目录表</td><td></td></tr><tr><td></td><td>转送函</td><td></td></tr><tr><td></td><td>引言</td><td>X</td></tr><tr><td></td><td>章目录</td><td></td></tr><tr><td></td><td>数字索引</td><td></td></tr><tr><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td></tr><tr><td></td><td>飞机概述</td><td></td></tr><tr><td>05</td><td>时限/维护检查</td><td>X</td></tr><tr><td>06</td><td>尺寸和区域</td><td></td></tr><tr><td>07</td><td>顶起和支撑</td><td></td></tr><tr><td>08</td><td>调平和称重</td><td></td></tr><tr><td>09</td><td>牵引和滑行</td><td></td></tr><tr><td>10</td><td>停放和系留</td><td></td></tr><tr><td>11</td><td>标牌和标志</td><td></td></tr><tr><td>12</td><td>保养</td><td></td></tr><tr><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td></tr><tr><td></td><td>机体系统</td><td></td></tr><tr><td>20</td><td>标准实施一机体</td><td></td></tr><tr><td>21</td><td>空调</td><td></td></tr><tr><td>22</td><td>自动飞行</td><td></td></tr><tr><td>23</td><td>通信</td><td></td></tr><tr><td>24</td><td>电源</td><td></td></tr><tr><td>25</td><td>设备/装备</td><td></td></tr><tr><td>26</td><td>防火</td><td></td></tr><tr><td>27</td><td>飞行控制</td><td></td></tr><tr><td>28</td><td>燃油</td><td></td></tr><tr><td>29</td><td>液压源</td><td></td></tr><tr><td>30</td><td>防冰和防雨</td><td></td></tr><tr><td>31</td><td>显示/记录系统</td><td></td></tr><tr><td>32</td><td>起落架</td><td></td></tr><tr><td>33</td><td>照明</td><td></td></tr><tr><td>34</td><td>导航</td><td></td></tr><tr><td>35</td><td>氧气</td><td></td></tr><tr><td>36</td><td>气动</td><td></td></tr><tr><td>37</td><td>真空</td><td></td></tr><tr><td>38</td><td>水/污物</td><td></td></tr><tr><td>41</td><td>压舱水</td><td></td></tr><tr><td>45</td><td>中央维修系统</td><td></td></tr><tr><td>46</td><td>信息系统</td><td></td></tr><tr><td>49</td><td></td><td></td></tr><tr><td></td><td>机载辅助动力</td><td></td></tr><tr><td></td><td>结构</td><td></td></tr><tr><td></td><td></td><td></td></tr><tr><td>51</td><td>标准实施一结构</td><td></td></tr><tr><td>52</td><td>舱门</td><td></td></tr><tr><td>53</td><td>机身</td><td></td></tr><tr><td>54</td><td>短舱/吊舱</td><td></td></tr><tr><td>55</td><td>安定面</td><td></td></tr><tr><td>56</td><td>窗</td><td></td></tr><tr><td>57</td><td>机翼</td><td></td></tr><tr><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td></tr><tr><td></td><td>螺旋桨/旋翼</td><td></td></tr><tr><td>60</td><td>标准实施一螺旋桨/旋翼</td><td></td></tr><tr><td>61</td><td>螺旋桨</td><td></td></tr><tr><td>62</td><td>旋翼</td><td></td></tr><tr><td>63</td><td>旋翼驱动</td><td></td></tr><tr><td>64</td><td>尾旋翼</td><td></td></tr><tr><td>65</td><td>尾旋翼驱动</td><td></td></tr><tr><td>66</td><td>可折叠桨叶/挂架</td><td></td></tr><tr><td>67</td><td>旋翼飞行控制</td><td></td></tr><tr><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td></tr><tr><td></td><td>动力装置</td><td></td></tr><tr><td>70</td><td>标准实施一发动机</td><td>X</td></tr><tr><td>71</td><td>动力装置</td><td>X</td></tr><tr><td>72</td><td>发动机</td><td>X</td></tr><tr><td>73</td><td>发动机燃油及控制</td><td></td></tr><tr><td>74</td><td>点火</td><td></td></tr><tr><td>75</td><td>引气</td><td></td></tr><tr><td>76</td><td>发动机控制</td><td></td></tr><tr><td>77</td><td>发动机指示</td><td></td></tr><tr><td>78</td><td>排气</td><td>X</td></tr><tr><td>79</td><td>滑油</td><td></td></tr><tr><td>80</td><td>起动</td><td></td></tr><tr><td>81</td><td>涡轮机</td><td></td></tr><tr><td>82</td><td>注水</td><td></td></tr><tr><td>83</td><td>附件齿轮箱</td><td></td></tr><tr><td>84</td><td>助推装置</td><td></td></tr><tr><td>94</td><td>图表</td><td></td></tr></table>

表 5-1-2.11 标准出版物中发动机零件目录手册索引舌的要求  

<table><tr><td></td><td>说明</td><td>索引舌</td></tr><tr><td></td><td>标题页</td><td></td></tr><tr><td></td><td>更改记录</td><td></td></tr><tr><td></td><td>有效页目录</td><td></td></tr><tr><td></td><td>目录表</td><td></td></tr><tr><td></td><td>临时更改单记录</td><td></td></tr><tr><td></td><td>转送函</td><td></td></tr><tr><td></td><td>服务通报清单</td><td></td></tr><tr><td></td><td>引言</td><td></td></tr><tr><td></td><td>章目录</td><td></td></tr><tr><td></td><td></td><td></td></tr><tr><td></td><td>字母数字索引</td><td></td></tr><tr><td></td><td></td><td></td></tr><tr><td></td><td>飞机概述</td><td></td></tr><tr><td>05</td><td>时限/维护检查</td><td></td></tr><tr><td>06</td><td>尺寸和区域</td><td></td></tr><tr><td>07</td><td>顶起和支撑</td><td></td></tr><tr><td>08</td><td>调平和称重</td><td></td></tr><tr><td>09</td><td>牵引和滑行</td><td></td></tr><tr><td>10</td><td>停放和系留</td><td></td></tr><tr><td>11</td><td>标牌和标志</td><td></td></tr><tr><td>12</td><td>保养</td><td></td></tr><tr><td></td><td></td><td></td></tr><tr><td></td><td>机体系统</td><td></td></tr><tr><td></td><td></td><td></td></tr><tr><td>20</td><td>标准实施一机体</td><td></td></tr><tr><td>21</td><td>空调</td><td></td></tr><tr><td>22</td><td>自动飞行</td><td></td></tr><tr><td>23</td><td>通信</td><td></td></tr><tr><td>24</td><td>电源</td><td rowspan="14">适用时,参见表2-1-1.2“防护”</td></tr><tr><td>25</td><td colspan="1">设备/装备</td></tr><tr><td>26</td><td colspan="1">防火</td></tr><tr><td>27</td><td colspan="1">飞行控制</td></tr><tr><td>28</td><td colspan="1">燃油</td></tr><tr><td>29</td><td colspan="1">液压源</td></tr><tr><td>30</td><td colspan="1">防冰和防雨</td></tr><tr><td>31</td><td colspan="1">显示/记录系统</td></tr><tr><td>32</td><td colspan="1">起落架</td></tr><tr><td>33</td><td colspan="1">照明</td></tr><tr><td>34</td><td colspan="1">导航</td></tr><tr><td>35</td><td colspan="1">氧气</td></tr><tr><td>36</td><td colspan="1">气动</td></tr><tr><td>37</td><td colspan="1">真空</td></tr><tr><td>38</td><td>水/污物</td><td></td></tr><tr><td>41</td><td>压舱水</td><td></td></tr><tr><td>45</td><td>中央维修系统</td><td></td></tr><tr><td>46</td><td>信息系统</td><td></td></tr><tr><td>49</td><td>机载辅助动力</td><td></td></tr><tr><td></td><td></td><td></td></tr><tr><td></td><td>结构</td><td></td></tr><tr><td></td><td></td><td></td></tr><tr><td>51</td><td>标准实施一结构</td><td></td></tr><tr><td>52</td><td>舱门</td><td></td></tr><tr><td>53</td><td>机身</td><td></td></tr><tr><td>54</td><td>短舱/吊舱</td><td></td></tr><tr><td>55</td><td>安定面</td><td></td></tr><tr><td>56</td><td>窗</td><td></td></tr><tr><td>57</td><td>机翼</td><td></td></tr><tr><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td></tr><tr><td></td><td>螺旋桨/旋翼</td><td></td></tr><tr><td>60</td><td>标准实施一螺旋桨/旋翼</td><td></td></tr><tr><td>61</td><td>螺旋桨</td><td></td></tr><tr><td>62</td><td>旋翼</td><td></td></tr><tr><td>63</td><td>旋翼驱动</td><td></td></tr><tr><td>64</td><td>尾旋翼</td><td></td></tr><tr><td>65</td><td>尾旋翼驱动</td><td></td></tr><tr><td>66</td><td>可折叠桨叶/挂架</td><td></td></tr><tr><td>67</td><td>旋翼飞行控制</td><td></td></tr><tr><td></td><td></td><td></td></tr><tr><td></td><td></td><td>X</td></tr><tr><td></td><td>动力装置</td><td></td></tr><tr><td>70</td><td>标准实施-发动机</td><td>X</td></tr><tr><td>71</td><td>动力装置</td><td>X</td></tr><tr><td>72</td><td>发动机</td><td>X</td></tr><tr><td>73</td><td>发动机燃油及控制</td><td>X</td></tr><tr><td>74</td><td>点火</td><td>X</td></tr><tr><td>75</td><td>引气</td><td>X</td></tr><tr><td>76</td><td>发动机控制</td><td>X</td></tr><tr><td>77</td><td>发动机指示</td><td>X</td></tr><tr><td>78</td><td>排气</td><td>X</td></tr><tr><td>79</td><td>滑油</td><td>X</td></tr><tr><td>80</td><td>起动</td><td>X</td></tr><tr><td>81</td><td>涡轮机</td><td>X</td></tr><tr><td>82</td><td>注水</td><td>X</td></tr><tr><td>83</td><td>附件齿轮箱</td><td>X</td></tr><tr><td>84</td><td>助推装置</td><td>X</td></tr><tr><td>94</td><td>图表</td><td></td></tr></table>

表 5-1-2.12 标准出版物中故障隔离手册索引舌的要求  

<table><tr><td></td><td>说明</td><td>索引舌</td></tr><tr><td></td><td>标题页</td><td></td></tr><tr><td></td><td>有效页目录</td><td></td></tr><tr><td></td><td>目录表</td><td></td></tr><tr><td></td><td>临时更改单记录</td><td></td></tr><tr><td></td><td>临时更改记录</td><td></td></tr><tr><td></td><td>服务通报记录</td><td></td></tr><tr><td></td><td>有效前页目录</td><td></td></tr><tr><td></td><td>引言</td><td></td></tr><tr><td></td><td>警告/状态信息清单</td><td></td></tr><tr><td></td><td>观测到的故障清单</td><td></td></tr><tr><td></td><td>驾驶舱故障代码索引</td><td></td></tr><tr><td></td><td>维修信息清单</td><td></td></tr><tr><td></td><td></td><td></td></tr><tr><td></td><td></td><td>X</td></tr><tr><td></td><td>机体系统</td><td></td></tr><tr><td>20</td><td>标准实施一机体</td><td>X</td></tr><tr><td>21</td><td>空调</td><td>X</td></tr><tr><td>22</td><td>自动飞行</td><td>X</td></tr><tr><td>23</td><td>通信</td><td>X</td></tr><tr><td>24</td><td>电源</td><td>X</td></tr><tr><td>25</td><td>设备/装备</td><td>X</td></tr><tr><td>26</td><td>防火</td><td>X</td></tr><tr><td>27</td><td>飞行控制</td><td>X</td></tr><tr><td>28</td><td>燃油</td><td>X</td></tr><tr><td>29</td><td>液压源</td><td>X</td></tr><tr><td>30</td><td>防冰和防雨</td><td>X</td></tr><tr><td>31</td><td>显示/记录系统</td><td>X</td></tr><tr><td>32</td><td>起落架</td><td>X</td></tr><tr><td>33</td><td>照明</td><td>X</td></tr><tr><td>34</td><td>导航</td><td>X</td></tr><tr><td>35</td><td>氧气</td><td>X</td></tr><tr><td>36</td><td>气动</td><td>X</td></tr><tr><td>37</td><td>真空</td><td>X</td></tr><tr><td>38</td><td>水/污物</td><td>X</td></tr><tr><td>41</td><td>压舱水</td><td>X</td></tr><tr><td>45</td><td>中央维修系统</td><td>X</td></tr><tr><td>46</td><td>信息系统</td><td></td></tr><tr><td>49</td><td>机载辅助动力</td><td></td></tr><tr><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td></tr><tr><td></td><td>结构</td><td></td></tr><tr><td>51</td><td>标准实施一结构</td><td></td></tr><tr><td>52</td><td>舱门</td><td>X</td></tr><tr><td>53</td><td>机身</td><td></td></tr><tr><td>54</td><td>短舱/吊舱</td><td></td></tr><tr><td>55</td><td>安定面</td><td></td></tr><tr><td>56</td><td>窗</td><td></td></tr><tr><td>57</td><td>机翼</td><td></td></tr><tr><td></td><td></td><td></td></tr><tr><td></td><td></td><td>X</td></tr><tr><td></td><td>螺旋桨/旋翼</td><td></td></tr><tr><td>60</td><td>标准实施一螺旋桨/旋翼</td><td>X</td></tr><tr><td>61</td><td>螺旋桨</td><td>X</td></tr><tr><td>62</td><td>旋翼</td><td>X</td></tr><tr><td>63</td><td>旋翼驱动</td><td>X</td></tr><tr><td>64</td><td>尾旋翼</td><td>X</td></tr><tr><td>65</td><td>尾旋翼驱动</td><td>X</td></tr><tr><td>66</td><td>可折叠桨叶/挂架</td><td>X</td></tr><tr><td>67</td><td>旋翼飞行控制</td><td>X</td></tr><tr><td></td><td></td><td></td></tr><tr><td></td><td></td><td>X</td></tr><tr><td></td><td>动力装置</td><td></td></tr><tr><td>70</td><td>标准实施一发动机</td><td>X</td></tr><tr><td>71</td><td>动力装置</td><td>X</td></tr><tr><td>72</td><td>发动机</td><td>X</td></tr><tr><td>73</td><td>发动机燃油及控制</td><td>X</td></tr><tr><td>74</td><td>点火</td><td>X</td></tr><tr><td>75</td><td>引气</td><td>X</td></tr><tr><td>76</td><td>发动机控制</td><td>X</td></tr><tr><td>77</td><td>发动机指示</td><td>X</td></tr><tr><td>78</td><td>排气</td><td>X</td></tr><tr><td>79</td><td>滑油</td><td>X</td></tr><tr><td>80</td><td>起动</td><td>X</td></tr><tr><td>81</td><td>涡轮机</td><td>X</td></tr><tr><td>82</td><td>注水</td><td>X</td></tr><tr><td>83</td><td>附件齿轮箱</td><td>X</td></tr><tr><td>84</td><td>助推装置</td><td>X</td></tr><tr><td colspan="3">*据飞机设备选择</td></tr></table>

对于出版物中不需要正文内容的各章，可与索引舌一起省略。结构《修理手册》要求中可以发现这样的例子。

应提供标题为“控制”和“飞机报告”的两个表。

为每种检查方法分配一个编号，每种检查方法都用写有分配编号和检查方法的索引舌来标记（参见图5-1-2.4）。

FRM应包含前置资料后的五部分，在每一部分的开始应有一个索引舌。这些部分如下所示：（参见图5-1-2.3)

1. 引言  
2.警告信息  
3.观测到的故障  
4. 状态信息  
5. 驾驶舱故障

故障报告手册中允许使用以上五个指定部分之外的其它标题，但是，每一部分的内容必须遵循故障报告手册详细规范(参见3-3-9)中描述的格式规则。

![](images/095da1066971a03333d9a85bcbba3b1bc431a72695f1a40999a1bf9ab7eecfef.jpg)  
图5-1-2.3 索引舌

每个手册的章、无损检测的检验方法、或包括手册引言部分的故障报告手册各部分，都应用一个塑封过的索引舌作标记。为了便于查找，这些索引舌应交错排列。

![](images/00ca3795ead9263d4333b1c5c35b9175912705fa6fe828856dd6b9722dbdd338.jpg)  
图5-1-2.4 索引舌(NDT)

# 5-1-3 缩微胶卷

# 1 物理介质规范一胶卷

制造商提供的胶卷应满足下列要求：

# 1.1 感光胶卷底片（第一代）

胶卷底片应由卤化银感光胶片生成。生胶片应是专门制造的无孔、消晕的安全胶卷，是专门按一些标准缩影复制而成，这些标准包括ANSI PH1.25-1974或ISO 543电影术一移动图像安全胶片一定义、测试及标记。

胶卷的宽度为  $16\mathrm{mm}$ ，其公差应在ANSI PH5.3—1967或者[ISO 69规定的误差范围以内为  $16\mathrm{mm}$ ，在加工卤化银感光胶片的过程中，残留的硫酸盐不应超过每平方厘米1微克。参见ANSI标准ANSI PH1.28—1973、ANSI PH1.41—1973以及ISO标准ISO4331:1977、ISO4332:1977。

# 2 物理介质规范一缩微胶片

制造商提供发行用的缩微胶片应符合美国的国家标准“文件的缩微胶片”(ANSI NMA MS5-1975、ANSI PH5.9-1975)以及“计算机输出缩微胶片的格式和编码标准”(ANSI NMA MS2-1978、ANSI PH5.18-1976)或这些文件后续修订版本。适用时，下列ISO标准可作为替代标准ISO 2707《缩微图形学一相同分区的透明A6尺寸缩微胶片一图像排列(方法)1号和2号》；ISO 2708《缩微图形学一不定分区的透明A6尺寸缩微胶片一图像排列(方法)A和B》；ISO 5126《缩微图形学一计算机输出缩微胶片(COM)-A6缩微胶片》。

# 5-1-4 磁带

# 1 格式标准

用磁带向一个用户或一组用户提供发动机零件构型管理数据时，应提供下列不同数据段：

1. 数字索引  
2. 发动机快速更换装置组——空档位置  
3. 发动机快速互换装置组  
4. 安装组  
5. 零件组  
6. 互换性组

列出零件号时，应同时给出它的数量。

# 1.1 磁带更改代码

更改记录磁带的部分内容时，应将整个记录磁带的全部内容重新发给用户或用户组。应按照如下注明的方式，在字段级别说明对磁带字段所作的单独更改：

<table><tr><td>记录的最初发送</td><td>N</td></tr><tr><td>更改记录</td><td>R</td></tr><tr><td>一个或多个记录的删除</td><td>D</td></tr><tr><td>上述内容的综合应用
(例：新增的零件号 CCO 取消)</td><td>M</td></tr></table>

检查其它文件类型的适用性。

# 5-1-5 CD-ROM

光盘

# 5-1-6 包装

# 1 介质外部标签

# 1.1 标签规范

所有介质的外部应使用自粘标签进行标记。标签应能反映所有便于接收者对介质进行操作和工作控制所需要的信息。不适合标注在标签上的信息，应包含在数据发送方提供的一张单独的发送单上，用介

质发送。下表给出了包括的推荐字段和适用的格式。

标签的形状应适合介质的大小。

供应商向用户发送的所有磁带，必须符合用户和供应商之间相互达成的关于密度、字区以及标题/标签的协议，以保证其在电子数据处理设备中连续使用。磁带标签应注明每盘磁带记录的全部内容以及发送的磁带盘数。

由于EDP设备的不同，供应商和用户之间应共同商定磁带的格式。

为了确保准确管理和迅速处理数据，所有要同这些程序之一一起使用的磁带应当用自粘标签粘在磁带盘的外面。这些标签应能反映磁带中包含的所有信息，且需要通过接收者的 EDP 工作控制器来传递这些信息。

由于使用的磁带类型不同，标签尺寸也可以不同，但必须满足以下要求是：

- 在任何情况下，标签尺寸都应与标准的直径为  $3\frac{11}{16}$  英寸的磁带轮毂相匹配，并且

应保持信息的顺序不变。

# 1.2 标签格式

下表中描述了标签上应给出的字段。

<table><tr><td>字段</td><td>ANSI/IBM格式</td><td>TAR 格式</td><td>目录格式</td><td>光盘格式</td></tr><tr><td>数据类型(9)</td><td>X</td><td>X</td><td>X</td><td>X</td></tr><tr><td>有效日期(10)</td><td>X</td><td>X</td><td>X</td><td>X</td></tr><tr><td>磁带序列号(11)</td><td>X</td><td></td><td></td><td></td></tr><tr><td>顺序号(12)</td><td>X</td><td>X</td><td>X</td><td>X</td></tr><tr><td>介质格式(13)</td><td>X</td><td>X</td><td>X</td><td></td></tr><tr><td>密度或容量(14)</td><td>X</td><td>X</td><td>X</td><td></td></tr><tr><td>字区大小(15)</td><td>X</td><td></td><td></td><td></td></tr><tr><td>块因子(16)</td><td></td><td>X</td><td></td><td></td></tr><tr><td>源(17)</td><td>X</td><td>X</td><td>X</td><td>X</td></tr><tr><td>用户名称(18)</td><td>X</td><td>X</td><td>X</td><td>X</td></tr><tr><td>创建日期(19)</td><td>X</td><td>X</td><td>X</td><td>X</td></tr><tr><td>ATA 引用(20)</td><td>X</td><td>X</td><td>X</td><td>X</td></tr></table>

# 1.2.1 标准打印文件

磁带标签应符合下列要求：

- 应保持下表列出的信息顺序不变。  
- 贴在每个磁带上的标签内容应包含字段 1 到 6,字段 1 到 24 应由发送文件提供。  
标签的形状应适合磁带盘的大小

以下描述了标签上应给出的字段：

<table><tr><td>字段</td><td>说明</td></tr><tr><td>1.数据类型</td><td>例如:维修数据采集、初始供应、消耗等</td></tr><tr><td>2.有效日期</td><td>对于采集的数据;如果存在多个日期的数据,应给出最新日期的或最新更改日期的数据</td></tr><tr><td>3.磁带序列号</td><td>显而易见</td></tr><tr><td>4.提供数据/磁带的公司名称</td><td>显而易见</td></tr><tr><td>5.供应商代码</td><td>对于提供数据的公司,该字段为其联邦或北约代码。若多于一个公司,应输入“若干”,并在“备注”栏列出所有公司</td></tr><tr><td>6.操作系统</td><td>输入“OS”、“DOS”，或如果为“其它”，应在“备注”栏中予以说明</td></tr><tr><td>7.标签</td><td>如果在磁带上有标签，则输入“YES”，否则输入“NO”</td></tr><tr><td>8.磁带标记</td><td>如果磁带上有标记，则输入“YES”，否则输入“NO”。如果为“NO”，应在“备注”栏说明磁带上数据的起始位置</td></tr><tr><td>9.执行日期</td><td>显而易见</td></tr><tr><td>10.操作系统</td><td>输入“OS”、“DOS”，如果为“OTHER”，应在“备注”栏中予以说明</td></tr><tr><td>11.轨道数</td><td>显而易见</td></tr><tr><td>12.密度</td><td>每英寸的存贮单元数(BPI)</td></tr><tr><td>13.奇偶性</td><td>显而易见</td></tr><tr><td>14.记录长度</td><td>显而易见</td></tr><tr><td>15.字区类型</td><td>固定的</td></tr><tr><td>16.字区大小</td><td>最大15,960字节</td></tr><tr><td>17.账号</td><td>供编制该磁带的供应商选择的数据</td></tr><tr><td>18.系统</td><td>供编制该磁带的供应商选择的数据</td></tr><tr><td>19.磁带驱动器号</td><td>供编制该磁带的供应商选择的数据</td></tr><tr><td>20.工作号</td><td>供编制该磁带的供应商选择的数据</td></tr><tr><td>21.运行时间</td><td>供编制该磁带的供应商选择的数据</td></tr><tr><td>22.备注</td><td>显而易见</td></tr><tr><td>23.记录类型</td><td>FBA(ANSI 固定字区)</td></tr><tr><td>24.记录长度</td><td>133字节</td></tr></table>

# 1.2.2 带标签的AMTOSS/JEMTOSS

磁带标签应符合下列要求：

- 应保持下表列出的信息顺序不变。  
- 贴在磁带上的标签内容应包括字段 1 到 6,字段 1 到 24 由发送文件提供。  
- 标签的形状应适合磁带盘的尺寸。

以下描述了标签上应给出的字段：

<table><tr><td>字 段</td><td>说 明</td></tr><tr><td>1.数据类型</td><td>飞机或发动机手册类型；例如：B767 AMM TEXT TAPE</td></tr><tr><td>2.有效日期</td><td>最新的更改日期</td></tr><tr><td>3.磁带序列号</td><td>显而易见</td></tr><tr><td>4.提供数据/磁带的公司名称</td><td>显而易见</td></tr><tr><td>5.供应商代码</td><td>对于提供数据的公司，该字段为其联邦或北约代码。若多于一个公司，应输入“若干”，并在“备注”栏列出所有公司。</td></tr><tr><td>6.共几盘，第几盘</td><td>显而易见</td></tr><tr><td>7.标签</td><td>如果在磁带上有标签，则输入“YES”，否则输入“NO”</td></tr><tr><td>8.磁带标记</td><td>如果磁带上有标记，则输入“YES”，否则输入“NO”。如果为“NO”，应在“备注”栏说明磁带上数据的起始位置。</td></tr><tr><td>9.运行日期</td><td>显而易见</td></tr><tr><td>10. 操作系统</td><td>输入“OS”、“DOS”，如果为“其它”，应在“备注”栏中予以说明。</td></tr><tr><td>11. 轨道数</td><td>显而易见</td></tr><tr><td>12. 密度</td><td>每英寸存贮单元数</td></tr><tr><td>13. 奇偶性</td><td>显而易见</td></tr><tr><td>14. 记录长度</td><td>显而易见</td></tr><tr><td>15. 字区类型</td><td>固定的</td></tr><tr><td>16. 字区大小</td><td>最大15，960字节</td></tr><tr><td>17. 账号</td><td>供编制该磁带的公司选择的数据</td></tr><tr><td>18. 系统</td><td>供编制该磁带的公司选择的数据</td></tr><tr><td>19. 磁带驱动器号</td><td>供编制该磁带的公司选择的数据</td></tr><tr><td>20. 工作号</td><td>供编制该磁带的公司选择的数据</td></tr><tr><td>21. 运行时间</td><td>供编制该磁带的公司选择的数据</td></tr><tr><td>22. 备注</td><td>显而易见</td></tr><tr><td>23. 记录类型</td><td>固定字区</td></tr><tr><td>24. 记录长度</td><td>133字节</td></tr></table>

图5-1-6.1 磁带标签格式  
![](images/209e85d44cd6871a0962c456fcc55cf50f8c0584ad75614850e0dde2080b4ad1.jpg)  
注：字段1到15为强制执行字段。  
标签的形状应与磁带尺寸相匹配。  
标签应是自粘性的并且贴在磁带盘上。

# 1.2.3 磁带标签字段定义

1. 数据类型——如零件构型数据。  
2. 有效日期——显而易见。

3. 磁带序列号——显而易见  
4. 提供数据/磁带的公司名称——显而易见  
5. 供应商代码一对于提供数据的公司，该字段为其联邦或北约代码。若多于一个公司，应输入“若干”，并在“备注”栏列出所有公司的代码。  
6. 操作系统——输入“OS”、“DOS”，如果为“其它”，应在“备注”栏中予以说明。  
7.标签——如果在磁带上有标签，则输入“有”否则输入“无”  
8. 磁带标记——如果磁带上有标记，则输入“YES”，否则输入“NO”。如果为“NO”，应在“备注”栏说明磁带上数据的起始位置。  
9.执行日期——显而易见  
10. 共几盘，第几盘——显而易见  
11.轨道数——显而易见  
12. 密度——(in BPI) 显而易见  
13. 奇偶校验——显而易见  
14. 记录长度——显而易见  
15. 字区大小——显而易见  
16. 账号——供编制该磁带的公司选择的数据  
17. 系统——供编制该磁带的公司选择的数据  
18. 记录总数——本次发送的记录总数  
19. 工作号——供编制该磁带的公司选择的数据  
20. 运行时间——供编制该磁带的公司选择的数据  
21. 备注——显而易见

# 5-2 交换

# 5-2-1 介质交换(介质V6.5)

# 1 概述

本文件描述了数字化资料、与文本和图形相关的辅助文件的包装，以及对于复杂技术资料的文本和图形进行交换的首选介质格式和文件布局。

# 2 介质和标签

由于资料发送者和接收者之间可能使用不同的电子数据处理设备，因而，应采用资料发送者和接收者经协商认可的介质类型。对于由 ATA 文本和图形数据组成的数字技术出版物在进行资料交换时，推荐使用下列介质格式类型：

ANSI/IBM的置标顺序格式  
UNIX tar 格式  
目录格式  
- CD-ROM 格式

除非经资料发送者和接收者协商认可，否则不应使用压缩文件。

# 2.1 ANSI/IBM 置标顺序格式

本格式对可能使用的介质没有限制。

# 2.2 UNIX Tar 格式

介质设备的配置差异很大。必须特别注意的是以该格式进行任何交换时所涉及的密度、字区记录数和压缩技术。当将文件和目录存放在tar格式磁带上时应使用相对路径名。

# 2.3 目录格式

本格式对可能使用的介质没有限制。

# 2.4 CD-ROM格式

光盘交付应按照ISO9660:1988对信息进行格式化。

# 2.5 标签

# 2.5.1 内部介质标签

由于资料发送者和接收者之间可能使用不同的数据处理设备，因而，应采用资料发送者和数据接收者经协商认可的内部磁带标签

- 对于以 IBM 格式写入的磁带，应使用标准的 IBM 内部标签。  
- 对于以ANSI格式写入的磁带，应按ANSIX3.27—1987使用标准的内部标签。  
- 对于 tar 格式，没有内部标签。  
- 格式化目录的介质不应包含内部标签。

对于CD-ROM，应按照ISO9660:1988描述并创建主卷描述符，下列主卷描述符的字段应自始至终存在：

卷集标识符(对于多卷集，多至128个字符)  
卷标识符(多至32个字符)  
出版商ID(多至128个字符)  
数据提供者(多至128个字符)  
应用程序ID(多至128个字符)  
- 版权文件名  
- 摘要文件名  
参考书目文件名  
卷创建日期  
卷修改日期  
卷终止日期  
卷有效日期

# 3 信息文件

SGML 实例和具有相关文件的图形都提供有关资料内容的信息。根据 ISO Latin 1 ASCII 字符集左侧的定义，这些文件中的字符代码值应限制在 32 到 126 之间。

在对 SGML 介质控制文件和图形声明文件理解的论述中，各字段中的文本应不随情况变化。每条记录的长度由介质决定。对于以 ANSI/IBM 磁带交付的数据，每条记录应为 80 个字符，不足部分需要用 ASCII 空格字符填补。对于以 TAR 或 DOS 格式交付的数据，每条记录必须以一个新行序来终止。操作系统之间记录的序列终止位置是不同的，因此，当在操作系统之间进行转换时，应特别注意对终止位置进行正确的转换。

# 3.1 SGML介质控制文件

介质控制文件(声明文件)是必需的。介质控制文件是一个单独的实体文件，它作为文件集的一部分交付。介质控制文件不能供后续卷使用，并且当需要后续的磁带或磁盘时，不能重复介质控制文件。该文件以人和机器都可读的形式，对介质中的数据文件给出了基本的说明。

介质控制文件的目的是对数字介质的内容提供容易理解的信息。这在介质的外部标签被损坏的情况下显得尤为重要。资料接收者能够利用介质控制文件可以找到数字文件的重要信息。

SGML 介质控制文件应包含以下记录。每条记录后出现的记录分隔符的样式取决于介质格式。前四条记录是必需的，后五条记录是可选的，并用一个关键短语来标识。

# 3.1.1 手册标题记录

下列手册信息是必需的：

<table><tr><td>字段名</td><td>字段长度</td><td>位置</td></tr><tr><td>模型</td><td>12</td><td>1-12</td></tr><tr><td>手册代码</td><td>4</td><td>13-16</td></tr><tr><td>用户代码</td><td>4</td><td>17-20</td></tr><tr><td>更改日期</td><td>8</td><td>21-28</td></tr><tr><td>手册</td><td>40</td><td>29-68</td></tr><tr><td>状态标记</td><td>8</td><td>69-76</td></tr></table>

# 3.1.2 用户标题记录

该记录给出了接收文件集的用户和被指定需该版本手册的用户的信息。这两者通常是相同的，但对于社团、租赁公司或转包维修而言可以不同。下列信息是必需的：

<table><tr><td>字段名</td><td>字段长度</td><td>位置</td></tr><tr><td>用户名</td><td>40</td><td>1-40</td></tr><tr><td>手册用户</td><td>40</td><td>41-80</td></tr></table>

# 3.1.3 SGML磁带指示符记录

下列信息是必需的：

<table><tr><td>字段名</td><td>字段长度</td><td>位置</td></tr><tr><td>SGML磁带指示符(23)</td><td>9</td><td>1-9</td></tr><tr><td>DTD标识(24)</td><td>71</td><td>10-80</td></tr></table>

# 3.1.4 数据用途和数据来源公司记录

下列信息是必需的：

<table><tr><td>字段名</td><td>字段长度</td><td>位置</td></tr><tr><td>数据用途(25)</td><td>4</td><td>1-4</td></tr><tr><td>数据来源(26)</td><td>76</td><td>5-80</td></tr></table>

# 3.1.5 数据类型

下列信息是可选的，并用一个关键短语来标识：

<table><tr><td>字段名</td><td>字段长度</td><td>位置</td></tr><tr><td>关键短语(27)</td><td>13</td><td>1-13</td></tr><tr><td>数据类型(28)</td><td>67</td><td>14-80</td></tr></table>

# 3.1.6 有效日期

下列信息是可选的，并用一个关键短语来标识：

<table><tr><td>字段名</td><td>字段长度</td><td>位置</td></tr><tr><td>关键短语(29)</td><td>15</td><td>1-15</td></tr><tr><td>有效日期(30)</td><td>8</td><td>16-23</td></tr></table>

# 3.1.7 磁带序列号

下列信息是可选的，并用一个短语来标识：

<table><tr><td>字段名</td><td>字段长度</td><td>位置</td></tr><tr><td>关键短语(31)</td><td>19</td><td>1-19</td></tr><tr><td>磁带序列号(32)</td><td>8</td><td>20-27</td></tr></table>

# 3.1.8 创建日期

下列信息是可选的，并用一个关键短语来标识：

<table><tr><td>字段名</td><td>字段长度</td><td>位置</td></tr><tr><td>关键短语(33)</td><td>9</td><td>1-9</td></tr><tr><td>创建日期(34)</td><td>8</td><td>10-17</td></tr></table>

# 3.1.9 注释记录

下列信息是可选的，并用一个关键短语来标识：

<table><tr><td>字段名</td><td>字段长度</td><td>位置</td></tr><tr><td>关键短语(35)</td><td>8</td><td>1-8</td></tr><tr><td>注释(36)</td><td>72</td><td>9-80</td></tr></table>

# 3.2 图形声明文件

图形声明文件是必需的。声明文件是一个单独的实体文件，它作为文件集的一部分交付。该文件的作用是存储示图的基本信息。对于一本手册和一种示图类型的每种组合应有一个单独的声明文件。如果同一手册中既包含TIFF文件又包含CGM文件，则该手册应有两个声明文件。

声明文件的作用是为数字介质的内容提供容易理解的信息。这在介质的外部标签被损坏的情况下显得尤为重要。数据接收者能够利用介质声明文件找到数字文件的重要信息。

该声明应包含以下记录。每条记录后出现的记录分隔符的样式取决于介质格式。

# 3.2.1 手册标题记录

下列手册信息是必需的：

<table><tr><td>字段名</td><td>字段长度</td><td>位置</td></tr><tr><td>模型(37)</td><td>12</td><td>1-12</td></tr><tr><td>手册代码(38)</td><td>4</td><td>13-16</td></tr><tr><td>用户代码(39)</td><td>4</td><td>17-20</td></tr><tr><td>更改日期(40)</td><td>8</td><td>21-28</td></tr><tr><td>手册(41)</td><td>40</td><td>29-68</td></tr><tr><td>状态标记(42)</td><td>8</td><td>69-76</td></tr></table>

# 3.2.2. 用户标题记录

该记录给出了接收文件集的用户和被指定需合并到该版本手册的用户的信息。这两者通常是相同的，但对于社团、租赁公司或转包维修而言可以不同。下列信息是必需的：

<table><tr><td>字段名</td><td>字段长度</td><td>位置</td></tr><tr><td>用户名(43)</td><td>40</td><td>1-40</td></tr><tr><td>手册用户(44)</td><td>40</td><td>41-80</td></tr></table>

# 3.2.3. 图形磁带类型指示符记录

数据应遵循的磁带类型(CGM or TIFF)和ATA规范的修订编号。  

<table><tr><td>字段名</td><td>字段长度</td><td>位置</td></tr><tr><td>图形类型指示符(45)</td><td>5</td><td>1-5</td></tr><tr><td>图形种类(46)</td><td>1</td><td>6</td></tr><tr><td>图形规范标识(47)</td><td>74</td><td>7-80</td></tr></table>

# 3.2.4 数据用途和数据来源公司记录

数据类型和数据来源公司  

<table><tr><td>字段名</td><td>字段长度</td><td>位置</td></tr><tr><td>数据用途(48)</td><td>4</td><td>1-4</td></tr><tr><td>数据来源(49)</td><td>76</td><td>5-80</td></tr></table>

# 3.2.5 注释记录

<table><tr><td>字段名</td><td>字段长度</td><td>位置</td></tr><tr><td>注释(50)</td><td>80</td><td>1-80</td></tr></table>

# 3.2.6 示图数记录

图形文件集中包含的示图数：  

<table><tr><td>字段名</td><td>字段长度</td><td>位置</td></tr><tr><td>图形数(51)</td><td>8</td><td>1-8</td></tr></table>

# 3.2.7 字体度量标准记录

仅在交换 CGM 数据时使用字体度量信息。应按下列规定单独记录，对每种字体的说明有必要用许多记录来说明全部字体信息。需要附加记录来描述 CGM 文件中使用的字体度量标准。规定的字体大小为单元格高度的几分之一的数值。所有字符在单元格高度和宽度定义的方框中处于居中位置。提供的数值完全适合于等宽字体。如果使用均衡字符，参见 GREXCHANGE 中 RESTRICTED TEXT 附加要求的有关说明。

<table><tr><td>字段位置</td><td>描 述</td></tr><tr><td>1-4</td><td>包含字母文本字符串“FONT”</td></tr><tr><td>5-7</td><td>字体ID, 包含 TEXT FONTINDEX 元素中存储的整数值, 数值范围必须在 1~256 之间</td></tr><tr><td>8</td><td>空白</td></tr><tr><td>9-13</td><td>单元格宽度是单元格高度几分之一的十进制实数值。对于等宽字体, 值为正数。对于均衡字符, 值为零</td></tr><tr><td>14-18</td><td>表示字符间距, 是单元格高度几分之一的十进制实数值值可以小于、大于或者等于零</td></tr><tr><td>19-23</td><td>表示基线到上行线的距离, 是单元格高度几分之一的十进制实数值值为正数</td></tr><tr><td>24-28</td><td>表示基线到下行线的距离, 是单元格高度几分之一的十进制实数值值为正数</td></tr><tr><td>29-33</td><td>表示单元格底端到下行线的距离, 是单元格高度几分之一的十进制实数值值大于或等于零</td></tr><tr><td>34-63</td><td>可选字段, 包含字母字符形式的字体名 (例如 “OCRB”)</td></tr><tr><td>64-80</td><td>可选字段, 包含字母字符形式的字体类型 (例如: “粗体”、“斜体”)</td></tr></table>

表中的后两个字段(34-63和64-80)可以合并，以便在字段34-80中提供字体类型的充分说明。在指定度量标准的模型中，单元格高度假定为1.0为单元格宽度、字符间距、基线到上行线、基线到下行线，以及单元格底部到下行线的值假定是单元格高度的几分之一。下图显示了字体描述坐标系，用于描述字体度量标准值。

![](images/6bd90f5c5dd96a105a86bf77825f0a41eaca5558ff94deaa8cbaf27ef9ea17c3.jpg)  
图5-2-1.1 字体度量标准的描述

# 4 文件集说明

该部分描述了SGML文件集和图形文件集的内容。

当使用 ANSI/IBM 格式化的介质时，通常情况下，应先考虑将文本和图形分别用单独磁带交付。当数据卷支持在单一 ANSI/IBM 格式化的介质上存贮图文混排的情况下，发送者和接收者之间可达成协议，以一套介质交付两个文件集。当使用任何其它格式化的介质时，文本和图形可以用同一介质或单独的介质进行交付。

# 4.1 SGML文件集

# 4.1.1 必需的SGML文件

下列文件是每次交付时SGML文件集中所必须包括的。

# 4.1.1.1 SGML介质控制文件

该文件给出了介质内容的标识。重复了许多在外部标签上可查到的信息。

# 4.1.1.2 SGML文件实例

该文件包含了公共 DTD 规定的文件结构和内容。

# 4.1.2 可选择的SGML文件

下列文件作为SGML文件集的一部分，可选择交付。

# 4.1.2.1 SGML文件实例DTD

该文件仅包括 DTD 公共标识符的一个索引，DTD 公共标识符的说明见 4-2-3。DTD 应包括任何（附加的实体索引）。

# 4.1.2.2 SGML声明文件

该文件是独立于手册之外的一个文件，只在变更时需要单独交付。它可作为该文件集的一部分交付，或以独立介质的形式单独交付。

# 4.1.2.3 SGML公共DTD

该文件是独立于手册示例之外的一个文件，只在变更时需要单独交付。它可作为该文件集的一部分交付，或以独立介质的形式单独交付。

# 4.1.2.4 有效更改标识位置 DTD 的 SGML 清单

该文件是独立于手册示例的一个文件，只在变更时需要单独交付。它可作为该文件集的一部分交付，或以独立介质的形式单独交付。

# 4.1.2.5 有效更改标识位置示例的SGML清单

该文件是对附加修订的一种整体控制手段，可根据发送者与接收者之间成的协议交付。

# 4.1.2.6 适用页面组DTD的SGML清单

该文件是一个与SDS相关联的特定文件。只在变更时需要单独交付。它可作为该文件集的一部分交付，或以独立介质的形式单独交付。

# 4.1.2.7 适用页面组示例的SGML清单

该文件是一个与SDS相关联的特定文件。它应作为包含SDS文件集的一部分交付。

# 4.1.2.8 SGML特殊实体文件

这些文件由ATA TXT.TECHREQ规范中4-2-3定义的图形实体集、带标记部分实体集、标准警告事项实体集、标准注意事项实体集以及供应商特定实体集组成。

# 4.2 图形文件集

# 4.2.1 必需的图形文件

当交付资料中包含图形时，图形文件集中必须包括下列文件。

# 4.2.1.1 图形声明文件

这些文件给出了介质内容的标识。它们重复了许多在外部标签上可查到的信息。如果交付内容中同时存在 CGM 和 TIFF 图形，那么对于每种格式都应有一个图形声明文件。

# 4.2.1.2 图形实例文件

这些文件包含了随 SGML 实例交付的独立图形。如果交付内容中存在 CGM 和 TIFF 图形，那么对于每种格式都应有图形实例。

# 4.2.2 可选的图形文件

下列文件作为图形文件集的一部分，可选择性地交付。

# 4.2.2.1 CGM图形符号库文件

该文件提供了 CGM 图形交付中使用的一组通用图形符号的一种交付形式。

# 5 介质文件设计

在格式化的介质上输入 SGML 文本数据集和相应的图形数据集放到，并对文件设计进行说明。要剪裁定期修订的文件，既可用于小文件，也可用于跨越多个磁带的大文件。

# 5.1 以ANSI/IBM格式交付的文件

介质上文件放置的顺序是有规定的。小文件放在磁带的最前面，以便提取。介质控制文件和图形声明文件通常放在前面，以人们易读的方式描述磁带的内容。它们提供了不宜放在外部标签上的附加详细信息。

对于以 ANSI/IBM 格式化介质交付的数据，文件是固定的字区记录。固定逻辑记录不被记录指示符的结束符所分隔。当物理记录跨越逻辑记录时，记录指示符的物理结束符嵌入在数据流中。对于 ANSI/IBM 格式化的介质，记录指示符的物理结束符应是一个 ASCII 换行符（十六进值：“OA”）。

# 5.1.1 SGML 文件格式

# 5.1.1.1 SGML介质控制文件

该文件为固定字区的记录类型。逻辑记录长度80个字节，字区大小800字节。每个物理记录的有

效字符不足80个字节时，必须用ASCII空格符填满。

# 5.1.1.2 SGML DTD 文件和 SGML 声明文件

这些文件不固定字区的记录类型。逻辑记录长度80个字节，字区大小800字节。每个物理记录的有效字符不足80个字节时，必须用ASCII空格符填满。

# 5.1.1.3 SGML实体文件

这些文件为固定字区的记录类型。逻辑记录长度80个字节，字区大小800字节。每个物理记录的有效字符不足80个字节时，必须用ASCII空格符填满。

# 5.1.1.4 SGML实例文件

这些文件为固定字区的记录类型。逻辑记录长度133个字节，字区大小32718字节。物理记录可跨越逻辑记录，并应包含记录指示符的结束符。

# 5.1.2 图形文件格式

# 5.1.2.1 图形声明文件

这些文件为固定字区的记录类型。逻辑记录长度80个字节，字区大小800字节。每个物理记录的有效字符不足80个字节时，必须用ASCII空格符填满。

# 5.1.2.2 图形实例文件(包括CGM符号库文件)

这些文件为固定字区的记录类型。逻辑记录长度512个字节，字区大小4096字节。不涉及物理记录的概念。

以 ANSI/IBM 格式化介质交付的图形实例文件应是一个物理文件。应将所有以一种特定图形格式编码的示图封装进一个物理文件中，并且每个单独的示图文件应从一个字区(512 字节)的边界处开始存放。

# 5.1.3 ANSI/IBM 格式的首选文件布局

# 5.1.3.1 单独的ANSI/IBM格式化介质上的SGML文件集

文件优先顺序如下：

SGML介质控制文件（必需）

SGML 声明文件 (可选)

SGMLLEADTD（可选）

SGMLLEA实例（可选）

SGML LAP DTD（可选）

SGML LAP 实例(可选)

SGML公共DTD（可选）

SGML特殊实体文件(可选)

SGML文件实例DTD(可选)

SGML 文件实例 (必需)

# 5.1.3.2 单独的ANSI/IBM格式化介质上的图形文件集

文件的优先顺序如下：

CGM 声明文件(当 CGM 实例存在时必需)

TIFF声明文件(当TIFF实例存在时必需)

CGM实例文件(当使用CGM图形时必需)

TIFF 实例文件（当使用TIFF图形时必需）

CGM符号库文件（可选）

# 5.1.3.3 在同一个磁带上的SGML和图形文件集

SGML介质控制文件(必需)

CGM 声明文件（当存在 CGM 实例时必需）

TIFF声明文件(当存在TIFF实例时必需)

SGML 声明文件 (可选)

SGMLLEADTD（可选）

SGMLLEA实例（可选）

SGML LAP DTD（可选）

SGML LAP 实例（可选）

SGML公共DTD（可选）

SGML特殊实体文件（可选）

SGML文件实例DTD（可选）

SGML文件实例（必需）

CGM实例文件(当使用CGM图形时必需)

CGM符号库文件（可选）

TIFF实例文件（当使用TIFF图形时必需）

5.2 以目录、UNIX Tar 或 CD-ROM 格式交付的文件

以目录、UNIX或CD-ROM格式化介质存放SGML和图形文件时，应按目录方式排列。当需要时，文本和图形以单个介质或者分离介质的形式交付。为便于访问，介质控制文件和图形声明文件应放在最高级目录。当以CD-ROM格式提交时，版权、摘要和参考书目文件应放在最高级目录。

对于以目录、UNIX tar 或者 CD-ROM 格式交付的数据，文件长度是可变的。每条物理记录用记录指示符的结束符界定。对于 PC 支持的数据，记录指示符的结束符应是两个 ASCII 字符，依次分别为回车符和换行符（十六进制数值：“OD”和“OA”）。对于 UNIX 支持的数据，记录指示符的结束符应为一个 ASCII 换行符（十六进制数值：“OA”）。对于以 CD-ROM 交付的数据，文件中的记录结构应按照 ISO 9660:1988 的规定构建。

5.2.1 SGML文件格式

5.2.1.1 SGML介质控制文件

该文件包含可变长度的记录。每条记录由记录指示符的结束符终止。

5.2.1.2 SGML DTD 文件和 SGML 声明文件

这些文件包含可变长度的记录。每条记录由记录指示符的结束符终止。

5.2.1.3 SGML实体文件

这些文件包含可变长度的记录。每条记录由记录指示符的结束符终止。

5.2.1.4 SGML实例文件

这些文件包含可变长度的记录。每条记录由记录指示符的结束符终止。

5.2.2 图形文件格式

5.2.2.1 图形声明文件

这些文件包含可变长度的记录。每条记录由记录指示符的结束符终止。

5.2.2.2 图形实例文件(包括CGM符号库文件)

这些文件包含可变长度的记录。不涉及物理记录的概念。

以 DOS 磁盘、UNIX tar 磁带或者 CD-ROM 交付的图形实例文件可以是一个物理文件，针对每幅示图的一个单独文件，或可以与任何通用 zip 兼容的 zip 格式交付。当图形实例作为一个物理文件交付时，应将所有以特定图形格式编码的示图封装进一个物理文件中，并且每个单独的示图文件应从一个字区 (512 字节) 的边界处开始存放。

5.2.3 首选的目录、UNIX Tar 或 CD-ROM 格式的文件布局

Dos 和 UNIX 系统的文件命名，采用基本名后跟扩展名 (base.ext) 的约定形式。文件的基本名由数据发送者定义。本规范简要介绍了推荐的扩展名。

5.2.3.1 推荐的SGML文件集扩展名

<table><tr><td>MCF</td><td>SGML 介质控制文件</td></tr><tr><td>SGM</td><td>SGM 文件实例</td></tr><tr><td>DTD</td><td>SGML 文件实例本 DTD</td></tr><tr><td>SDL</td><td>SGML 声明文件</td></tr><tr><td>DTD</td><td>SGML 公共 DTD</td></tr><tr><td>DTD</td><td>SGML LEA DTD</td></tr><tr><td>.LEA</td><td>SGML LEA 实例文件</td></tr><tr><td>DTD</td><td>SGML SDS LAP DTD</td></tr><tr><td>LAP</td><td>SGML SDS LAP 实例文件</td></tr><tr><td>SGE</td><td>SGML 图形实体集</td></tr><tr><td>SME</td><td>SGML 标记部分实体集</td></tr><tr><td>SWE</td><td>SGML 标准警告事项实体集</td></tr><tr><td>SCE</td><td>SGML 标准注意事项实体集</td></tr><tr><td>SPE</td><td>SGML 供应商特定实体集</td></tr></table>

# 5.2.3.2 推荐的图形文件集扩展名

<table><tr><td>CDL</td><td>CGM 声明文件</td></tr><tr><td>TDL</td><td>TIFF 声明文件</td></tr><tr><td>CGM</td><td>CGM 实例文件</td></tr><tr><td>TIF</td><td>TIFF 实例文件</td></tr><tr><td>SYM</td><td>CGM 图形符号库文件</td></tr></table>

# 5.2.3.3 推荐的CD-ROM主卷描述符文件扩展名

<table><tr><td>TXT</td><td>CD-ROM copyright file
CD-ROM 版权文件</td></tr><tr><td>TXT</td><td>CD-ROM abstract file
CD-ROM 摘要文件</td></tr><tr><td>TXT</td><td>CD-ROM bibliography file
CD-ROM 参考书目文件</td></tr></table>

存储在目录、UNIX Tar 和 CD-ROM 格式化介质中的目录结构应能反映每个目录中包含数据的类型。基本目录应包含介质信息文件，并应有与 SGML (SGML)、CGM (CGM) 和 TIFF (TIFF) 相关的目录。不规定目录中的文件顺序。当用 CD-ROM 提交时，基本目录中也应包含版权、摘要和参考书目文件。

5.2.3.4 采用目录、UNIX Tar或CD-ROM格式化介质存储的SGML和图形文件集

SGML 介质控制文件（必需）

CGM 声明文件(当存在 CGM 实例时必需)

TIFF声明文件(当存在TIFF实例时必需)

CD-ROM 版权文件（可选）

CD-ROM 摘要文件 (可选)

CD-ROM参考书目文件(可选)

SGML（目录）

SGML 声明文件(可选)

SGMLLEADTD（可选）

SGMLLEA实例（可选）

SGML LAP DTD（可选）

SGML LAP 实例(可选)

SGML公共DTD（可选）

SGML特殊实体文件（可选）

SGML文件实例DTD（可选）

SGML文件实例（必需）

CGM（目录一当使用 CGM 图形时提交）

CGM实例（当使用CGM图形时必需）

CGM符号库(可选)

TIFF（目录一当使用TIFF图形时提交）

TIFF实例（当使用TIFF图形时必需）

# 5-2-2 打印文件

# 1 标准打印文件的应用

# 1.1 概述

标准磁带格式应允许传输 iSpec 2200 所涵盖的技术手册和 PMDB 中包含的任何资料。设计的磁带格式被可使接收者能够直接用打印机进行打印，也可将资料加载到用于辅助处理的计算机文件中。接收者要使用磁带，必须安装应用程序。

有关磁带的规范包括标签、记录、磁带标记的开始和结束、每个记录的字符数以及表示数据开始和结束的字符。

由于可能使用不同的EDP设备(如选择BPI)，磁带格式应由发送者和接收者协商认可。

所有与这些程序一起使用的磁带应使用自粘标签在磁带盘外部进行标记。某详细程序和发送方式应能反应磁带中包含的所有信息，且需要通过接收者的 EDP 作业控制来传递磁带信息。

文本和图形应以单独的磁带交付。图形磁带按规定应与所有三种文本磁带一起使用。

# 1.2 打印磁带

有效页目录(LEPS)和提要与文本和图形文件应是逻辑上是相互独立的文件。

# 1.3 文本磁带一带标记的 AMTOSS 和 JEMTOSS

对于带标记的、一行一行定向打印的磁带，其格式将在后续章节中说明。

对于采用通用标记语言标准(SGML)制造商飞机支援手册，其磁带格式见《ATA介质交换规范》(5-2-1)规定。

# 1.4 图形磁带

图形磁带应包含用于表达技术手册中所涉及的示图、图表和原理图的数字化资料。

# 1.5 产品管理数据库(PMDB)内容磁带

索引一在PMDB每次出版和更改时应随其一起提供一个有效任务和分任务清单(LETS)，用以确认操作者数据库。它应是一个逻辑上与PMDB独立的文件，但应与PMDB在同一磁带上。

# 格式一PMDB磁带(格式)

- 标准格式允许传输符合 iSpec 2200 规定的 PMDB 中包括的任何资料。该部分的目的是描述包含 PMDM 的磁带布局和内容。磁带格式设计为可使接收者能够将资料加载到自身计算机的待处理文件中。接收者要使用磁带，必须安装应用程序。

磁带格式应包括标签和记录的规范、磁带标记的开始和结束、每条记录的字符数以及表示数据开始和结束的字符。

- 所有的磁带应使用自粘标签在磁带盘外部进行标记。

磁带的事务处理一PMDB数据控制应达到任务和分任务级别。PMDB数据的常规处理事务应包括首次发放、修订、删除以及对任务和分任务的附加处理事务。

首版磁带

在首次出版的磁带上，标题记录、任务和分任务记录类型、以及所有与任务和分任务相关的数据记录类型应在更改代码字段中包含一个“N”。

修订磁带

修订磁带应在更改代码字段中包含一个“R”的标题记录，并仅包含那些更改、删除或者增加的任务和分任务数据。

- 每个更改的任务或分任务记录应与和其相关的所有记录类型一起发送。

- 每条记录的更改代码应是：

R一将被更改的任务或分任务。

D一将被删除的任务或分任务。

N一将被增加的任务或分任务。

- 在任务号或分任务号将被更改之处，应使用更改代码“D”将整个任务或分任务记录类型连同与其相关的所有记录类型一起删除。

- 对于包含新任务或分任务号的已更改的任务或分任务记录类型，应使用更改代码“N”将其连同与新任务或分任务相关的所有记录类型一起嵌入。

- 在一个完整任务或分任务将被删除之处，只有 010 或者 020 记录类型在进行处理时，将分别使用更改代码“D”，删除所有与任务或分任务有关的记录类型。

- 当操作者要求 PMDB 再版时，虽然它是一个新的原始版本，但也应按以上所述方法处理。假设操作员删除了所有现存数据。再版数据应包括截至本次再版时积累的所有数据。

# 1.6 字符集、文本和图形一标准打印文件

引用规范一本规范的这一部分引用了下列国家标准和国际标准：

ISO4873-1986，信息处理一用于信息交换的8位编码字符集。  
ISO646—1983，信息处理一用于信息交换的ISO7位编码字符集。  
ISO8859-1:1987，1一9部分，信息处理用于8位单字节编码图形字符集。

该部分的范围（仅适于打印文件）

- 除发下文中 iSpec 2200 中有明确的不同于此的规定之外。为便于将来的修订和/或该字符集的扩充，推荐交换技术信息的作者和读者按照本规范编写他们的应用软件代码。  
- 指定的控制字符(十进制0-31)与ISO646、ISO4873和ISO8859-1:1987中列出的那些控制字符一致。  
- “Delete”字符在信息交换中没有意义。它不应包括在交换的数据中。

字符集的使用一本规范中没有定义的字符串应作为图形数据交换。如果图形是按照 CGM 矢量文件定义的，则未定义字符应当作笔划（图形）字符提供。

字符集的指定-iSpec 2200 这部分的图形字符组成了一个单一编码字符集。但当同时使用该字符集与 ISO 4873 中规定的编码标准时，本规范的代码表将由下列部分组成：

- 字符 SPACE 用十六进制 20 表示。  
- 94—字符 G0 图形字符集，用十六进制 21 到十六进制 7E 表示。  
- 96—字符 G1 图形字符集，用十六进制 A0 到十六进制 FF 表示。  
如果联合使用该字符集与其它字符集译码标准，则换码顺序‘ESC hex 28 hex 42’应表示G0图形字符集。  
- 如果联合使用该字符集与其它字符集译码标准，则换码顺序‘ESC hex 2C hex 51’应表示G1图形字符集。

# 编码字符集规范

- 后续页中，非打印字符用“一”表示。

1.7 字符定义  

<table><tr><td>十进制数</td><td>十六进制数</td><td>含义说明</td><td>图形</td></tr><tr><td>0</td><td>0</td><td>空字符</td><td>-</td></tr><tr><td>1</td><td>1</td><td>标题开始</td><td>-</td></tr><tr><td>2</td><td>2</td><td>文本开始</td><td>-</td></tr><tr><td>3</td><td>3</td><td>文本结束</td><td>-</td></tr><tr><td>4</td><td>4</td><td>发送结束</td><td>-</td></tr><tr><td>5</td><td>5</td><td>询问</td><td>-</td></tr><tr><td>6</td><td>6</td><td>应答</td><td>-</td></tr><tr><td>7</td><td>7</td><td>时钟</td><td>-</td></tr><tr><td>8</td><td>8</td><td>退格</td><td>-</td></tr><tr><td>9</td><td>9</td><td>横表</td><td>-</td></tr><tr><td>10</td><td>A</td><td>换行</td><td>-</td></tr><tr><td>11</td><td>B</td><td>竖表</td><td>-</td></tr><tr><td>12</td><td>C</td><td>续表</td><td>-</td></tr><tr><td>13</td><td>D</td><td>回车</td><td>-</td></tr><tr><td>14</td><td>E</td><td>移出</td><td>-</td></tr><tr><td>15</td><td>F</td><td>移入</td><td>-</td></tr><tr><td>16</td><td>10</td><td>数据通讯换码</td><td>-</td></tr><tr><td>17</td><td>11</td><td>设备控制1</td><td>-</td></tr><tr><td>18</td><td>12</td><td>设备控制2</td><td>-</td></tr><tr><td>19</td><td>13</td><td>设备控制3</td><td>-</td></tr><tr><td>20</td><td>14</td><td>设备控制4</td><td>-</td></tr><tr><td>21</td><td>15</td><td>否定应答</td><td>-</td></tr><tr><td>22</td><td>16</td><td>同步空闲</td><td>-</td></tr><tr><td>23</td><td>17</td><td>传输字区结束</td><td>-</td></tr><tr><td>24</td><td>18</td><td>取消</td><td>-</td></tr><tr><td>25</td><td>19</td><td>介质结束</td><td>-</td></tr><tr><td>26</td><td>1A</td><td>置换字符</td><td>-</td></tr><tr><td>27</td><td>1B</td><td>退出</td><td>-</td></tr><tr><td>28</td><td>1C</td><td>信息分隔符4</td><td>-</td></tr><tr><td>29</td><td>1D</td><td>信息分隔符3</td><td>-</td></tr><tr><td>30</td><td>1E</td><td>信息分隔符2</td><td>-</td></tr><tr><td>31</td><td>1F</td><td>信息分隔符1</td><td>-</td></tr><tr><td>32</td><td>20</td><td>空格</td><td>-</td></tr><tr><td>33</td><td>21</td><td>感叹号</td><td>!</td></tr><tr><td>34</td><td>22</td><td>引号</td><td>"</td></tr><tr><td>35</td><td>23</td><td>数字表示符</td><td>#</td></tr><tr><td>36</td><td>24</td><td>美元符号</td><td>$</td></tr><tr><td>37</td><td>25</td><td>百分比符号</td><td>%</td></tr><tr><td>38</td><td>26</td><td>“与”符号</td><td>&amp;</td></tr><tr><td>39</td><td>27</td><td>撇号</td><td>'</td></tr><tr><td>40</td><td>28</td><td>左括号</td><td>(</td></tr><tr><td>41</td><td>29</td><td>右括号</td><td>)</td></tr><tr><td>42</td><td>2A</td><td>星号</td><td>*</td></tr><tr><td>43</td><td>2B</td><td>加号</td><td>+</td></tr><tr><td>44</td><td>2C</td><td>逗号</td><td>,</td></tr><tr><td>45</td><td>2D</td><td>连字符、减号</td><td>-</td></tr><tr><td>46</td><td>2E</td><td>句号</td><td>。</td></tr><tr><td>47</td><td>2F</td><td>斜线分隔符号</td><td>/</td></tr><tr><td>48</td><td>30</td><td>数字0</td><td>0</td></tr><tr><td>49</td><td>31</td><td>数字1</td><td>1</td></tr><tr><td>50</td><td>32</td><td>数字2</td><td>2</td></tr><tr><td>51</td><td>33</td><td>数字3</td><td>3</td></tr><tr><td>52</td><td>34</td><td>数字4</td><td>4</td></tr><tr><td>53</td><td>35</td><td>数字5</td><td>5</td></tr><tr><td>54</td><td>36</td><td>数字6</td><td>6</td></tr><tr><td>55</td><td>37</td><td>数字7</td><td>7</td></tr><tr><td>56</td><td>38</td><td>数字8</td><td>8</td></tr><tr><td>57</td><td>39</td><td>数字9</td><td>9</td></tr><tr><td>58</td><td>3A</td><td>冒号</td><td>:</td></tr><tr><td>59</td><td>3B</td><td>分号</td><td>;</td></tr><tr><td>60</td><td>3C</td><td>小于号</td><td>&lt;</td></tr><tr><td>61</td><td>3D</td><td>等于号</td><td>=</td></tr><tr><td>62</td><td>3E</td><td>大于号</td><td>&gt;</td></tr><tr><td>63</td><td>3F</td><td>问号</td><td>?</td></tr><tr><td>64</td><td>40</td><td>位于符号</td><td>@</td></tr><tr><td>65</td><td>41</td><td>大写字母A</td><td>A</td></tr><tr><td>66</td><td>42</td><td>大写字母B</td><td>B</td></tr><tr><td>67</td><td>43</td><td>大写字母C</td><td>C</td></tr><tr><td>68</td><td>44</td><td>大写字母D</td><td>D</td></tr><tr><td>69</td><td>45</td><td>大写字母E</td><td>E</td></tr><tr><td>70</td><td>46</td><td>大写字母F</td><td>F</td></tr><tr><td>71</td><td>47</td><td>大写字母G</td><td>G</td></tr><tr><td>72</td><td>48</td><td>大写字母H</td><td>H</td></tr><tr><td>73</td><td>49</td><td>大写字母I</td><td>I</td></tr><tr><td>74</td><td>4A</td><td>大写字母J</td><td>J</td></tr><tr><td>75</td><td>4B</td><td>大写字母K</td><td>K</td></tr><tr><td>76</td><td>4C</td><td>大写字母L</td><td>L</td></tr><tr><td>77</td><td>4D</td><td>大写字母M</td><td>M</td></tr><tr><td>78</td><td>4E</td><td>大写字母N</td><td>N</td></tr><tr><td>79</td><td>4F</td><td>大写字母O</td><td>O</td></tr><tr><td>80</td><td>50</td><td>大写字母P</td><td>P</td></tr><tr><td>81</td><td>51</td><td>大写字母Q</td><td>Q</td></tr><tr><td>82</td><td>52</td><td>大写字母R</td><td>R</td></tr><tr><td>83</td><td>53</td><td>大写字母S</td><td>S</td></tr><tr><td>84</td><td>54</td><td>大写字母T</td><td>T</td></tr><tr><td>85</td><td>55</td><td>大写字母U</td><td>U</td></tr><tr><td>86</td><td>56</td><td>大写字母V</td><td>V</td></tr><tr><td>87</td><td>57</td><td>大写字母W</td><td>W</td></tr><tr><td>88</td><td>58</td><td>大写字母X</td><td>X</td></tr><tr><td>89</td><td>59</td><td>大写字母Y</td><td>Y</td></tr><tr><td>90</td><td>5A</td><td>大写字母Z</td><td>Z</td></tr><tr><td>91</td><td>5B</td><td>左方括号</td><td>[</td></tr><tr><td>92</td><td>5C</td><td>反斜线分隔符号</td><td>\</td></tr><tr><td>93</td><td>5D</td><td>右方括号</td><td>]</td></tr><tr><td>94</td><td>5E</td><td>抑扬音符</td><td>^</td></tr><tr><td>95</td><td>5F</td><td>字下线、下划线</td><td>-</td></tr><tr><td>96</td><td>60</td><td>重音符</td><td>i</td></tr><tr><td>97</td><td>61</td><td>小写字母a</td><td>a</td></tr><tr><td>98</td><td>62</td><td>小写字母b</td><td>b</td></tr><tr><td>99</td><td>63</td><td>小写字母c</td><td>c</td></tr><tr><td>100</td><td>64</td><td>小写字母d</td><td>d</td></tr><tr><td>101</td><td>65</td><td>小写字母e</td><td>e</td></tr><tr><td>102</td><td>66</td><td>小写字母f</td><td>f</td></tr><tr><td>103</td><td>67</td><td>小写字母g</td><td>g</td></tr><tr><td>104</td><td>68</td><td>小写字母h</td><td>h</td></tr><tr><td>105</td><td>69</td><td>小写字母i</td><td>i</td></tr><tr><td>106</td><td>6A</td><td>小写字母j</td><td>j</td></tr><tr><td>107</td><td>6B</td><td>小写字母k</td><td>k</td></tr><tr><td>108</td><td>6C</td><td>小写字母l</td><td>l</td></tr><tr><td>109</td><td>6D</td><td>小写字母m</td><td>m</td></tr><tr><td>110</td><td>6E</td><td>小写字母n</td><td>n</td></tr><tr><td>111</td><td>6F</td><td>小写字母o</td><td>o</td></tr><tr><td>112</td><td>70</td><td>小写字母p</td><td>p</td></tr><tr><td>113</td><td>71</td><td>小写字母q</td><td>q</td></tr><tr><td>114</td><td>72</td><td>小写字母r</td><td>r</td></tr><tr><td>115</td><td>73</td><td>小写字母s</td><td>s</td></tr><tr><td>116</td><td>74</td><td>小写字母t</td><td>t</td></tr><tr><td>117</td><td>75</td><td>小写字母u</td><td>u</td></tr><tr><td>118</td><td>76</td><td>小写字母v</td><td>v</td></tr><tr><td>119</td><td>77</td><td>小写字母w</td><td>w</td></tr><tr><td>120</td><td>78</td><td>小写字母x</td><td>x</td></tr><tr><td>121</td><td>79</td><td>小写字母y</td><td>y</td></tr><tr><td>122</td><td>7A</td><td>小写字母z</td><td>z</td></tr><tr><td>123</td><td>7B</td><td>左波形括号</td><td>{</td></tr><tr><td>124</td><td>7C</td><td>垂直线</td><td>|</td></tr><tr><td>125</td><td>7D</td><td>右波形括号</td><td>}</td></tr><tr><td>126</td><td>7E</td><td>代字号</td><td>~</td></tr><tr><td>127</td><td>7F</td><td></td><td></td></tr><tr><td>128</td><td>80</td><td></td><td></td></tr><tr><td>129</td><td>81</td><td></td><td></td></tr><tr><td>130</td><td>82</td><td></td><td></td></tr><tr><td>131</td><td>83</td><td></td><td></td></tr><tr><td>132</td><td>84</td><td></td><td></td></tr><tr><td>133</td><td>85</td><td></td><td></td></tr><tr><td>134</td><td>86</td><td></td><td></td></tr><tr><td>135</td><td>87</td><td></td><td></td></tr><tr><td>136</td><td>88</td><td></td><td></td></tr><tr><td>137</td><td>89</td><td></td><td></td></tr><tr><td>138</td><td>8A</td><td></td><td></td></tr><tr><td>139</td><td>8B</td><td></td><td></td></tr><tr><td>140</td><td>8C</td><td></td><td></td></tr><tr><td>141</td><td>8D</td><td></td><td></td></tr><tr><td>142</td><td>8E</td><td></td><td></td></tr><tr><td>143</td><td>8F</td><td></td><td></td></tr><tr><td>144</td><td>90</td><td></td><td></td></tr><tr><td>145</td><td>91</td><td></td><td></td></tr><tr><td>146</td><td>92</td><td></td><td></td></tr><tr><td>147</td><td>93</td><td></td><td></td></tr><tr><td>148</td><td>94</td><td></td><td></td></tr><tr><td>149</td><td>95</td><td></td><td></td></tr><tr><td>150</td><td>96</td><td></td><td></td></tr><tr><td>151</td><td>97</td><td></td><td></td></tr><tr><td>152</td><td>98</td><td></td><td></td></tr><tr><td>153</td><td>99</td><td></td><td></td></tr><tr><td>154</td><td>9A</td><td></td><td></td></tr><tr><td>155</td><td>9B</td><td></td><td></td></tr><tr><td>156</td><td>9C</td><td></td><td></td></tr><tr><td>157</td><td>9D</td><td></td><td></td></tr><tr><td>158</td><td>9E</td><td></td><td></td></tr><tr><td>159</td><td>9F</td><td></td><td></td></tr><tr><td>160</td><td>A0</td><td></td><td></td></tr><tr><td>161</td><td>A1</td><td></td><td></td></tr><tr><td>162</td><td>A2</td><td>分币符号</td><td>Φ</td></tr><tr><td>163</td><td>A3</td><td></td><td></td></tr><tr><td>164</td><td>A4</td><td>通货符号</td><td>Ω</td></tr><tr><td>165</td><td>A5</td><td>尖括号</td><td>∠</td></tr><tr><td>166</td><td>A6</td><td>小圆点</td><td></td></tr><tr><td>167</td><td>A7</td><td>大圆点</td><td>·</td></tr><tr><td>168</td><td>A8</td><td>平方根号</td><td>✓</td></tr><tr><td>169</td><td>A9</td><td>小于等于号</td><td>≤</td></tr><tr><td>170</td><td>AA</td><td>大于等于号</td><td>≥</td></tr><tr><td>171</td><td>AB</td><td>左引用号</td><td>《</td></tr><tr><td>172</td><td>AC</td><td>“非”符号</td><td>-</td></tr><tr><td>173</td><td>AD</td><td>不等于号</td><td>≠</td></tr><tr><td>174</td><td>AE</td><td>0次幂</td><td>0</td></tr><tr><td>175</td><td>AF</td><td>1次幂</td><td>1</td></tr><tr><td>176</td><td>B0</td><td>度数符号</td><td>°</td></tr><tr><td>177</td><td>B1</td><td>正负号</td><td>±</td></tr><tr><td>178</td><td>B2</td><td>2次幂</td><td>2</td></tr><tr><td>179</td><td>B3</td><td>3次幂</td><td>3</td></tr><tr><td>180</td><td>B4</td><td>锐角符号</td><td></td></tr><tr><td>181</td><td>B5</td><td>4次幂</td><td>4</td></tr><tr><td>182</td><td>B6</td><td>5次幂</td><td>5</td></tr><tr><td>183</td><td>B7</td><td>6次幂</td><td>6</td></tr><tr><td>184</td><td>B8</td><td>7次幂</td><td>7</td></tr><tr><td>185</td><td>B9</td><td>8次幂</td><td>8</td></tr><tr><td>186</td><td>BA</td><td>9次幂</td><td>9</td></tr><tr><td>187</td><td>BB</td><td>右引号</td><td>》</td></tr><tr><td>188</td><td>BC</td><td>四分之一</td><td>¼</td></tr><tr><td>189</td><td>BD</td><td>二分之一</td><td>½</td></tr><tr><td>190</td><td>BE</td><td>四分之三</td><td>¾</td></tr><tr><td>191</td><td>BF</td><td>无穷大符号</td><td>∞</td></tr><tr><td>192</td><td>CO</td><td>约等于号</td><td>≈</td></tr><tr><td>193</td><td>C1</td><td>正交</td><td>⊥</td></tr><tr><td>194</td><td>C2</td><td>差分</td><td>～</td></tr><tr><td>195</td><td>C3</td><td>中间线</td><td>-</td></tr><tr><td>196</td><td>C4</td><td>大写的德耳塔</td><td>△</td></tr><tr><td>197</td><td>C5</td><td>下标0</td><td>0</td></tr><tr><td>198</td><td>C6</td><td>下标1</td><td>1</td></tr><tr><td>199</td><td>C7</td><td>下标2</td><td>2</td></tr><tr><td>200</td><td>C8</td><td>下标3</td><td>3</td></tr><tr><td>201</td><td>C9</td><td>下标4</td><td>4</td></tr><tr><td>202</td><td>CA</td><td>下标5</td><td>5</td></tr><tr><td>203</td><td>CB</td><td>下标6</td><td>6</td></tr><tr><td>204</td><td>CC</td><td>下标7</td><td>7</td></tr><tr><td>205</td><td>CD</td><td>下标8</td><td>8</td></tr><tr><td>206</td><td>CE</td><td>下标9</td><td>9</td></tr><tr><td>207</td><td>CF</td><td>中心线</td><td>CL</td></tr><tr><td>208</td><td>D0</td><td>方框左上</td><td>厂</td></tr><tr><td>209</td><td>D1</td><td>方框中间</td><td>│</td></tr><tr><td>210</td><td>D2</td><td>方框左下</td><td>L</td></tr><tr><td>211</td><td>D3</td><td>大写的 Sigma</td><td>Σ</td></tr><tr><td>212</td><td>D4</td><td>方框右上</td><td>7</td></tr><tr><td>213</td><td>D5</td><td>方框十字</td><td>+</td></tr><tr><td>214</td><td>D6</td><td>方框右下</td><td>」</td></tr><tr><td>215</td><td>D7</td><td>乘号</td><td>X</td></tr><tr><td>216</td><td>D8</td><td></td><td></td></tr><tr><td>217</td><td>D9</td><td>大写的 Omega</td><td>Ω</td></tr><tr><td>218</td><td>DA</td><td></td><td></td></tr><tr><td>219</td><td>DB</td><td></td><td></td></tr><tr><td>220</td><td>DC</td><td>有分音符的大写字母U</td><td>ü</td></tr><tr><td>221</td><td>DD</td><td></td><td></td></tr><tr><td>222</td><td>DE</td><td></td><td></td></tr><tr><td>223</td><td>DF</td><td></td><td></td></tr><tr><td>224</td><td>E0</td><td></td><td></td></tr><tr><td>225</td><td>E1</td><td>小写的 Alpha</td><td>α</td></tr><tr><td>226</td><td>E2</td><td>小写的 Beta</td><td>β</td></tr><tr><td>227</td><td>E3</td><td>小写的 Gamma</td><td>γ</td></tr><tr><td>228</td><td>E4</td><td>小写的 Delta</td><td>δ</td></tr><tr><td>229</td><td>E5</td><td>小写的 Epsilon</td><td>ε</td></tr><tr><td>230</td><td>E6</td><td></td><td></td></tr><tr><td>231</td><td>E7</td><td>有变音符的小写c</td><td>ζ</td></tr><tr><td>232</td><td>E8</td><td>小写的 Theta</td><td>θ</td></tr><tr><td>233</td><td>E9</td><td>有重音符的小写e</td><td>é</td></tr><tr><td>234</td><td>EA</td><td></td><td></td></tr><tr><td>245</td><td>EB</td><td>小写的 Lambda</td><td>λ</td></tr><tr><td>246</td><td>EC</td><td>小写的 Mu</td><td>μ</td></tr><tr><td>247</td><td>ED</td><td></td><td></td></tr><tr><td>248</td><td>EE</td><td></td><td></td></tr><tr><td>239</td><td>EF</td><td></td><td></td></tr><tr><td>240</td><td>F0</td><td>小写的 Pi</td><td>π</td></tr><tr><td>241</td><td>F1</td><td></td><td></td></tr><tr><td>242</td><td>F2</td><td></td><td></td></tr><tr><td>243</td><td>F3</td><td>小写的 Sigma</td><td>σ</td></tr><tr><td>244</td><td>F4</td><td></td><td></td></tr><tr><td>245</td><td>F5</td><td></td><td></td></tr><tr><td>246</td><td>F6</td><td>小写的 Phi</td><td>φ</td></tr><tr><td>247</td><td>F7</td><td>除号</td><td>÷</td></tr><tr><td>248</td><td>F8</td><td>小写的 Psi</td><td>ψ</td></tr><tr><td>249</td><td>F9</td><td>小写的 Omega</td><td>ω</td></tr><tr><td>250</td><td>FA</td><td></td><td></td></tr><tr><td>251</td><td>FB</td><td></td><td></td></tr><tr><td>252</td><td>FC</td><td></td><td></td></tr><tr><td>253</td><td>FD</td><td></td><td></td></tr><tr><td>254</td><td>FE</td><td></td><td></td></tr><tr><td>255</td><td>FF</td><td></td><td></td></tr></table>

![](images/8dd1669c5364a4bacbb9fb858f70a5aa28eb72fb13ec46daee687edb835acc5c.jpg)  
图5-2-2.1 字符图

图5-2-2.1 字符图(续)

<table><tr><td>b8</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td></tr><tr><td>b7</td><td>0</td><td>0</td><td>0</td><td>0</td><td>1</td><td>1</td><td>1</td><td>1</td></tr><tr><td>b6</td><td>0</td><td>0</td><td>1</td><td>1</td><td>0</td><td>0</td><td>1</td><td>1</td></tr><tr><td>b5</td><td>0</td><td>1</td><td>0</td><td>1</td><td>0</td><td>1</td><td>0</td><td>1</td></tr></table>

<table><tr><td>b4</td><td>b3</td><td>b2</td><td>b1</td></tr><tr><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>0</td><td>0</td><td>0</td><td>1</td></tr><tr><td>0</td><td>0</td><td>1</td><td>0</td></tr><tr><td>0</td><td>0</td><td>1</td><td>1</td></tr><tr><td>0</td><td>1</td><td>0</td><td>0</td></tr><tr><td>0</td><td>1</td><td>0</td><td>1</td></tr><tr><td>0</td><td>1</td><td>1</td><td>0</td></tr><tr><td>0</td><td>1</td><td>1</td><td>1</td></tr><tr><td>1</td><td>0</td><td>0</td><td>0</td></tr><tr><td>1</td><td>0</td><td>0</td><td>1</td></tr><tr><td>1</td><td>0</td><td>1</td><td>0</td></tr><tr><td>1</td><td>0</td><td>1</td><td>1</td></tr><tr><td>1</td><td>1</td><td>0</td><td>0</td></tr><tr><td>1</td><td>1</td><td>0</td><td>1</td></tr><tr><td>1</td><td>1</td><td>1</td><td>0</td></tr><tr><td>1</td><td>1</td><td>1</td><td>1</td></tr></table>

<table><tr><td></td><td>8</td><td>9</td><td>10</td><td>11</td><td>12</td><td>13</td><td>14</td><td>15</td></tr><tr><td>0</td><td></td><td></td><td></td><td>0</td><td>∞</td><td>Γ</td><td></td><td>π</td></tr><tr><td>1</td><td></td><td></td><td></td><td>±</td><td>⊥</td><td>|</td><td>α</td><td></td></tr><tr><td>2</td><td></td><td></td><td>∅</td><td>2</td><td>~</td><td>L</td><td>β</td><td></td></tr><tr><td>3</td><td></td><td></td><td></td><td>3</td><td>△</td><td>Σ</td><td>γ</td><td>σ</td></tr><tr><td>4</td><td></td><td></td><td>∅</td><td>&#x27;</td><td></td><td>¬</td><td>δ</td><td></td></tr><tr><td>5</td><td></td><td></td><td>∠</td><td>4</td><td>0</td><td>+</td><td>ε</td><td></td></tr><tr><td>6</td><td></td><td></td><td>•</td><td>5</td><td>1</td><td>」</td><td></td><td>φ</td></tr><tr><td>7</td><td></td><td></td><td>•</td><td>6</td><td>2</td><td></td><td>L</td><td>÷</td></tr><tr><td>8</td><td></td><td></td><td>√</td><td>7</td><td>3</td><td></td><td>θ</td><td>ψ</td></tr><tr><td>9</td><td></td><td></td><td>≤</td><td>8</td><td>4</td><td>Ω</td><td>é</td><td>ω</td></tr><tr><td>10</td><td></td><td></td><td>≥</td><td>9</td><td>5</td><td></td><td></td><td></td></tr><tr><td>11</td><td></td><td></td><td>《》</td><td></td><td>6</td><td></td><td>λ</td><td></td></tr><tr><td>12</td><td></td><td></td><td>-</td><td>1/4</td><td>7</td><td>U</td><td>μ</td><td></td></tr><tr><td>13</td><td></td><td></td><td>≠</td><td>1/2</td><td>8</td><td></td><td></td><td></td></tr><tr><td>14</td><td></td><td></td><td>0</td><td>3/4</td><td>9</td><td></td><td></td><td></td></tr><tr><td>15</td><td></td><td></td><td>1</td><td>∞</td><td>E</td><td></td><td></td><td></td></tr></table>

# 2 表达方式

# 2.1 磁带字符标准

应使用扩充的二进制编码的十进制交换代码[EBCDIC]字符：

- 在每个文件文本资料的开头与末尾应使用标准的磁带标签。  
- 应使用美国国家标准化学学会(ANSI)的打印机走纸控制标准，提供了下列十六进制数值，并有操作注解：

<table><tr><td>十六进制</td><td>操作</td></tr><tr><td>4E</td><td>打印前控制空格</td></tr><tr><td>40</td><td>打印前的空格1</td></tr><tr><td>F0</td><td>打印前的空格2</td></tr><tr><td>60</td><td>打印前的空格3</td></tr><tr><td>F1</td><td>在新页上跳到第一行</td></tr><tr><td></td><td></td></tr><tr><td colspan="2">十六进制操作</td></tr><tr><td>01</td><td>打印前控制空格</td></tr><tr><td>09</td><td>打印后的空格1</td></tr><tr><td>11</td><td>打印后的空格2</td></tr><tr><td>19</td><td>打印后的空格3</td></tr><tr><td>9B</td><td>不打印时空行1</td></tr><tr><td>8B</td><td>不打印时跳向通道1</td></tr></table>

# 2.2 磁带记录类型

文本磁带应包括手册文本页的数据。该磁带不包括图形。但带示图的页可以包含描述示图的文本信息，这样的文本数据应包含在文本主题中。该磁带有4种记录类型：手册标题、文件标题、页眉和数据记录。手册标题应是磁带上的第一条记录。手册标题应包含与特定的型号/手册及接收磁带的客户有关的信息。每个ATA章一节一题目一页码组一构型应以一个文件标题开始，该文件标题应给出手册信息。文件中的每一页应有一个页眉来详细说明该页的特定信息。页眉后应跟随页面上文本或插图编号的每行数据记录。一个典型的磁带可包含下列内容：

<table><tr><td>手册标题</td><td>用于 XYZ MM 用户 03</td></tr><tr><td>文件标题</td><td>用于21-00-00-0</td></tr><tr><td>页眉</td><td>用于第1页</td></tr><tr><td>数据记录</td><td>用于第2行</td></tr><tr><td>数据记录</td><td>用于第3行</td></tr><tr><td>数据记录</td><td>用于第4行</td></tr><tr><td>数据记录</td><td>用于第5行</td></tr><tr><td>数据记录</td><td>用于第6行</td></tr><tr><td>页眉</td><td>适用于第2页</td></tr><tr><td>数据记录</td><td>用于第1行</td></tr><tr><td>数据记录</td><td>用于第2行</td></tr><tr><td>数据记录</td><td>用于第3行</td></tr><tr><td>文件标题</td><td>用于21-00-00-1</td></tr><tr><td>页眉</td><td>用于第101页</td></tr><tr><td>数据记录</td><td>用于第1行</td></tr><tr><td>数据记录</td><td>用于第2行</td></tr><tr><td>数据记录</td><td>用于第3行</td></tr><tr><td>页眉</td><td>用于第102页</td></tr><tr><td>数据记录</td><td>用于第1行</td></tr><tr><td>数据记录</td><td>用于第2行</td></tr><tr><td>数据记录</td><td>用于第3行</td></tr><tr><td>页眉</td><td>用于第103页</td></tr><tr><td>数据记录·</td><td>用于第1行</td></tr><tr><td>数据记录</td><td>用于第2行</td></tr><tr><td>数据记录</td><td>用于第3行</td></tr></table>

每个磁带应有一个包含下列信息的手册标题记录：

<table><tr><td>字段名</td><td>字符数</td><td>字段格式</td><td>值/描述</td></tr><tr><td>记录类型</td><td>1</td><td>N</td><td>手册标题用数值1表示</td></tr><tr><td>型号</td><td>9</td><td>AN</td><td>型号名称</td></tr><tr><td>手册代码</td><td>4</td><td>A</td><td>例如:MM或者CMM</td></tr><tr><td>用户代码</td><td>4</td><td>AN</td><td>给用户分配的代码</td></tr><tr><td>更改日期</td><td>8</td><td>AN</td><td>格式为mm/dd/yy,其中mm=月,dd=日,yy=年</td></tr><tr><td>手册标题</td><td>40</td><td>AN</td><td>手册全称,如维修手册</td></tr><tr><td>用户名</td><td>40</td><td>AN</td><td>用户全称</td></tr><tr><td>用户名</td><td>3</td><td>AN</td><td>用户原始资料代码</td></tr><tr><td>ANSI标记</td><td>1</td><td>A</td><td>S=标准,V=可变</td></tr><tr><td>活页</td><td>23</td><td></td><td>空白</td></tr></table>

对于章一节一题目一页码组一构型的每次更改，应有一个文件标题。在文件标题中应提供以下信息：

<table><tr><td>字段名</td><td>字符数</td><td>字段格式</td><td>值/描述</td></tr><tr><td>记录类型</td><td>1</td><td>N</td><td>文件标题用数值2表示</td></tr><tr><td>文件标识(ID)</td><td>16</td><td>AN</td><td>ATA文件号</td></tr><tr><td></td><td></td><td></td><td>所有字段右对齐一两端对齐,用空格填充</td></tr><tr><td></td><td></td><td></td><td>位置说明</td></tr><tr><td></td><td></td><td></td><td>1发动机前缀</td></tr><tr><td></td><td></td><td></td><td>2-4章</td></tr><tr><td></td><td></td><td></td><td>5-6节</td></tr><tr><td></td><td></td><td></td><td>8-10题目</td></tr><tr><td></td><td></td><td></td><td>11-13页号组</td></tr><tr><td></td><td></td><td></td><td>14-16构型</td></tr><tr><td>文件标题</td><td>40</td><td>AN</td><td>文件名,位于手册页脚</td></tr><tr><td>书号</td><td>1</td><td>N</td><td>1或2</td></tr><tr><td>开始页号</td><td>5</td><td>AN</td><td>文件中第一页的页码</td></tr><tr><td></td><td></td><td></td><td>位置描述</td></tr><tr><td></td><td></td><td></td><td>1-4页码</td></tr><tr><td></td><td></td><td></td><td>5(0001-9999)</td></tr><tr><td></td><td></td><td></td><td>字母后缀(A-Z)</td></tr><tr><td>增加日期</td><td>8</td><td>AN</td><td>用户接收该文件的第一个更改日期(月/日/年)</td></tr><tr><td>更改</td><td>8</td><td>AN</td><td>该文件为用户更改的最新更改日期(mm/dd/yy)</td></tr><tr><td>活页</td><td>54</td><td></td><td>空白</td></tr></table>

$\mathrm{N}=$  数字；AN=字母数字  
每页应有一个页眉，包含下列信息：

<table><tr><td>字段名</td><td>字符数</td><td>字段格式</td><td>值/描述</td></tr><tr><td>记录类型</td><td>1</td><td>N</td><td>页眉用数值3表示</td></tr><tr><td>页</td><td>1</td><td>N</td><td>1=文本页2=示图页3=文本/示图4=空白页</td></tr><tr><td></td><td></td><td></td><td>5=专用空白页</td></tr><tr><td></td><td></td><td></td><td>注:空白页和专用空白页没有与其相关的数据记录</td></tr><tr><td>页面大小</td><td>1</td><td>N</td><td>1=81/2×11页面2=11×17页面的左边3=11×17页面的右边4=全尺寸的11×17示图手册页脚</td></tr><tr><td>页编号</td><td>5</td><td>AN</td><td>页面的页码位置描述1-4页码(0001-8888)5字母后缀(A-Z)</td></tr><tr><td>页码</td><td>25</td><td>AN</td><td>位于手册页脚中的页码</td></tr><tr><td>页日期</td><td>8</td><td>AN</td><td>该页最后更改的汇编日期(月/日/年)</td></tr><tr><td>增加日期</td><td>8</td><td>AN</td><td>(月/日/年)
该用户首次接收该页的汇编日期(月/日/
年)</td></tr><tr><td>活页</td><td>84</td><td></td><td>空白</td></tr></table>

$\mathrm{N} =$  数字；AN=字母数字

页面上的每行文本应有一个数据记录。每幅示图应有一个描述它的数据记录。这些记录字段的磁带标题应提供下列信息：

<table><tr><td>字段名</td><td>字符数</td><td>字段格式</td><td>值/描述</td></tr><tr><td>记录类型</td><td>1</td><td>N</td><td>数据记录用数值4表示</td></tr><tr><td>行类型</td><td>1</td><td>N</td><td>1=汇编基本编号</td></tr><tr><td></td><td></td><td></td><td>这些行出现在CMM页的标识区域中。它们在页面上应是起始行。</td></tr><tr><td></td><td></td><td></td><td>2=文本行</td></tr><tr><td></td><td></td><td></td><td>3=示图编号</td></tr><tr><td></td><td></td><td></td><td>4=有效性行</td></tr><tr><td></td><td></td><td></td><td>这些行在页脚的有效区域内</td></tr></table>

\*AN=字母数字  
可以提供一个可选的记录布局，由下列部分组成：

<table><tr><td>字段名</td><td>字符数</td><td>字段格式</td><td>值/描述</td></tr><tr><td>数据行(对于行类型1、2和4)</td><td>102</td><td>AN</td><td>数据行分类</td></tr><tr><td></td><td></td><td></td><td>1走纸控制</td></tr><tr><td></td><td></td><td></td><td>2-6左页边距</td></tr><tr><td></td><td></td><td></td><td>7-9用户原始资料代码</td></tr><tr><td></td><td></td><td></td><td>10更改条</td></tr><tr><td></td><td></td><td></td><td>11空白</td></tr><tr><td></td><td></td><td></td><td>12-92文本行</td></tr><tr><td></td><td></td><td></td><td>93-102右页边距</td></tr><tr><td>数据行(对于示图行)</td><td>102</td><td>AN</td><td>数据行分类</td></tr><tr><td></td><td></td><td></td><td>1-32示图</td></tr><tr><td></td><td></td><td></td><td>33-35示图占用的行数</td></tr><tr><td></td><td></td><td></td><td>36-38示图起始行号</td></tr><tr><td></td><td></td><td></td><td>39-43图形编号</td></tr><tr><td></td><td></td><td></td><td>44-45图表编号</td></tr><tr><td></td><td></td><td></td><td>46-53更改周期(月/日/年)</td></tr><tr><td></td><td></td><td></td><td>54-102活页(位置)</td></tr><tr><td>活页</td><td>29</td><td></td><td>空白</td></tr></table>

\*AN=字母数字

可选的记录布局是：

<table><tr><td>位置</td><td>功能</td></tr><tr><td>1</td><td>走纸控制</td></tr><tr><td>2</td><td>更改条位置</td></tr><tr><td>2-3</td><td>左边距</td></tr><tr><td>4</td><td>如果是十六进制值“FF”，则后跟字符是½英寸高的标题。如果后跟字符是空格，则空两行。如果不是十六进制“FF”，则它是一个数据行。</td></tr><tr><td>4-72</td><td>文本行，最多有69个字符。</td></tr><tr><td>58</td><td>页脚行：如果是十六进制值“FF”，则跟在章一节一题目后为½英寸高度的编号。在58行中可以只有一个包含十六进制“FF”的行/页。字符位置21处有效性起始行。用户代码将在该行的第18和第19字符位置中。下一行包含页码，并在字符位置72处结束。</td></tr><tr><td>73-74</td><td>用户代码该行之后的第二行(无构型)或第三行(如果构型存在)应有该页日期。日期起始于字符位置64-72。</td></tr></table>

相位符号是叠印字符，通过打印一行并加上无空格走纸控制(01)，然后再打印其它行形成的。十六进制FO叠印十六进制61形成的符号就是相位符号。

一个示图编号用“.”标识。当建立该编号时，前三个字符应是样式类型（HPU、HPL、FPA、RHF），后面的字符组成了样式标识编号。

HPU是上半页

HPL是下半页

FPA是整页

RHF是右手页的前部

# 2.3 格式一打印数据

利用数字传输技术提供的出版物要求以下内容：

- 字符集可用 147 个符号和标记。  
- 每页最多由60行组成，包括头部和尾部行。  
- 每行最多由 80 个字符位置组成，包括更改符号。  
不允许用水平布局方式(横向方式)书写文本。  
- 如果需要，临时更改单可用硬拷贝或摄影即用拷贝(CRC)的形式来生成。

# 3 表达方式一文本磁带一带标记的 AMTOSS/JEMTOSS

# 3.1 磁带字符标准

应使用本部分规定的字符集。

标准磁带标签应在每个文件的开始和结束使用。

# 3.2 磁带记录类型

文本磁带应包含手册的数字化资料。该磁带上不包括图形。有三种记录类型：手册标题、文件标题和数据记录。手册标题应是磁带上的第一个记录。每个ATA章一节一题目一页码组一构型应以一个文件标题开始，该文件标题应提供文件的相关信息。对于每个文本行或示图编号应有一个数据记录。

每个文件应有一个手册标题记录。一个文件可以包含一个或多个物理磁带。手册标题记录包含以下信息：

<table><tr><td>字段名</td><td>值/大小</td><td>位置</td><td>描述</td></tr><tr><td>记录类型</td><td>9(1)</td><td>1</td><td>I=手册标题</td></tr><tr><td>型号</td><td>X(9)</td><td>2-10</td><td>型号名称</td></tr><tr><td>手册代码</td><td>A(4)</td><td>11-14</td><td>如:AMM或者CMM或者EM</td></tr><tr><td>用户代码</td><td>X(4)</td><td>15-18</td><td>分配给用户的代码</td></tr><tr><td>修订日期</td><td>X(8)</td><td>19-26</td><td>格式为mm/dd/yy其中:mm=月;dd=天;yy=年。</td></tr><tr><td>手册标题</td><td>X(40)</td><td>27-66</td><td>手册全称,如《飞机维修手册》</td></tr><tr><td>用户名称</td><td>X(40)</td><td>67-106</td><td>用户全称</td></tr><tr><td>COC标记名称</td><td>X(3)</td><td>107-109</td><td>用户原始资料代码</td></tr><tr><td>ANSI标记</td><td>A(1)</td><td>110</td><td>S=标准,V=可变</td></tr><tr><td>语言</td><td>A(1)</td><td>111</td><td>E=英语,F=法语 D=德语 I=意大利语S=西班牙语</td></tr><tr><td>活页纸</td><td>X(22)</td><td>112-133</td><td>空白</td></tr></table>

*9=数字；X=字母数字；A=字母

这是一个文件标题记录的例子：

1 2 3 4 5 6 7 1234567890123456789012345678901234567890123456789012345678901

1ALL EM ABC.10/01/88ENGINE MANUAL.ABC.A

1 1 1 8 9 0 1 2 3

23456789012345678901234567890123456789012345678901234567890123

IRLINES. ABCSEFILLER

对于章一节一题目一页码组一构型的每次更改应有一个文件标题。应在文件标题中提供以下信息：

<table><tr><td>字段名</td><td>值/大小</td><td>位置</td><td>描述</td></tr><tr><td>记录类型</td><td>9(1)</td><td>1</td><td>2=文件标题</td></tr><tr><td>文件 ID</td><td>X(17)</td><td>2</td><td>发动机/飞机前缀3-4 章,6-7 节,9-10 题目,12-15 页号组,17-18 构型。注:位置5、8、11和16中的字符为破折号。</td></tr><tr><td>页号组标题</td><td>X(40)</td><td>19-58</td><td>文件类型,如拆卸/安装</td></tr><tr><td>原始发行日期</td><td>X(8)</td><td>59-66</td><td>月/日/年</td></tr><tr><td>更改日期</td><td>X(8)</td><td>67-74</td><td>月/日/年</td></tr><tr><td>更新代码</td><td>X(1)</td><td>75</td><td>N=新文件 R=更改文件 D=删除文件B=未更改文件 T=临时更改</td></tr><tr><td>活页</td><td>X(58)</td><td>76-133</td><td>空白</td></tr></table>

*9=数字，X=字母数字，A=字母 **b=空白

这是一个文件标题记录的例子：

1 2 3 4 5 6 7 1234567890123456789012345678901234567890123456789012345678901

2E99-99-99-9999-99PAGEBLOCK TITLE

01/23/8610/01

<table><tr><td></td><td>1</td><td>1</td><td>1</td><td>1</td></tr><tr><td>8</td><td>9</td><td>0</td><td>1</td><td>2</td></tr></table>

2345678901234567890123456789012345678901234567890123

/88RFILLER

数据记录应提供以下内容：

表 5-2-2.1.表 3-a 适用于数据记录 4、行类型 2 的字段  

<table><tr><td>字段名</td><td>值/大小</td><td>位置</td><td>描述</td></tr><tr><td>记录类型</td><td>9(1)</td><td>1</td><td>4=数据记录</td></tr><tr><td>行类型</td><td>9(1)</td><td>2</td><td>2=文本数据行</td></tr><tr><td>走纸控制符</td><td>X(1)</td><td>3</td><td>+=打印之前控制空格β=打印前到下一行</td></tr><tr><td>修订代码</td><td>X(1)</td><td>4</td><td>R=以前修订版的数据已经被更改β=数据没有被更改</td></tr><tr><td>标记</td><td>X(4)</td><td>5-8</td><td>参见TAG定义的说明</td></tr><tr><td>文本数据</td><td>X(79)</td><td>9-87</td><td>显而易见</td></tr><tr><td>COC 标记</td><td>X(3)</td><td>88-90</td><td>用户原始数据代码</td></tr><tr><td>活页</td><td>X(43)</td><td>91-133</td><td>除了特定标记外,其余为空白</td></tr></table>

*9=数字，X=文字数字，A=字母

\*\*β=空白；

这是一个行类型2的数据记录的例子：

<table><tr><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td></tr><tr><td colspan="7">1234567890123456789012345678901234567890123456789012345678901</td></tr></table>

42+RTAN.THIS LINE OF TEXT CONTAINS THE TASK

NUMBER

<table><tr><td></td><td>1</td><td>1</td><td>1</td><td>1</td></tr><tr><td>8</td><td>9</td><td>0</td><td>1</td><td>2</td></tr></table>

2345678901234567890123456789012345678901234567890123

COCFFILLER

表 5-2-2.2.表 3-b 适用于行类型 3、数据记录 4 的字段  

<table><tr><td>字段名</td><td>值/大小</td><td>位置</td><td>描述</td></tr><tr><td>记录类型</td><td>9(1)</td><td>1</td><td>4=数据记录</td></tr><tr><td>行类型</td><td>9(1)</td><td>2</td><td>3=示图编号</td></tr><tr><td>走纸控制符</td><td>X(1)</td><td>3</td><td>+=打印之前控制空格β=打印前转到下一行</td></tr><tr><td>更改代码</td><td>X(1)</td><td>4</td><td></td></tr><tr><td></td><td></td><td></td><td>R=以前修订版的数据已经被更改</td></tr><tr><td></td><td></td><td></td><td>N=新数据</td></tr><tr><td></td><td></td><td></td><td>β=数据未被更改</td></tr><tr><td></td><td></td><td></td><td>D=数据已被删除</td></tr><tr><td>TAG标记</td><td>X(4)</td><td>5-8</td><td>ILLILL</td></tr><tr><td>示图</td><td>X(76)</td><td>9-32</td><td>任务号注:在适用的情况下,位置11、14、17、21、29的字符为破折号。</td></tr><tr><td></td><td></td><td>33-64</td><td>图形标识(ID)号</td></tr><tr><td></td><td></td><td>65-72</td><td>空白</td></tr><tr><td></td><td></td><td>73-78</td><td>宽度在一百个打印点之内</td></tr><tr><td></td><td></td><td>79-84</td><td>深度在一百个打印点之内</td></tr><tr><td>活页</td><td>X(49)</td><td>85-133</td><td>空白</td></tr></table>

*9=数字，X=字母数字，A=字母

$\text{水水}$ $\beta =$  空白

这是行类型3的数据记录的一个例子：

<table><tr><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td></tr><tr><td>12345678901</td><td>12345678901</td><td>12345678901</td><td>12345678901</td><td>12345678901</td><td>12345678901</td><td>12345678901</td></tr><tr><td colspan="7">43+RILL.72-22-00-990-902.........GRAPHIC-ID-NUMBER.........</td></tr><tr><td></td><td></td><td></td><td>1</td><td>1</td><td>1</td><td>1</td></tr><tr><td>8</td><td>9</td><td>0</td><td>1</td><td>2</td><td>3</td><td>3</td></tr></table>

23456789012345678901234567890123456789012345678901234567890123

WIDTH.MAXDepth.FILLER

表 5-2-2.3.表 3-c 适用于行类型 4、数据记录 4 的字段(允许多记录)  

<table><tr><td>字段名</td><td>值/大小</td><td>位置</td><td>描述</td></tr><tr><td>记录类型</td><td>9(1)</td><td>1</td><td>4=数据记录</td></tr><tr><td>行类型</td><td>9(1)</td><td>2</td><td>4=示图属性</td></tr><tr><td>走纸控制符</td><td>X(1)</td><td>3</td><td>+=打印之前控制空格β=打印前转到下一行</td></tr><tr><td>更改代码</td><td>X(1)</td><td>4</td><td>R=以前修订版的数据已经被更改N=新数据β=数据未被修改D=数据已被删除</td></tr><tr><td>标记</td><td>X(4)</td><td>5-8</td><td>ILL</td></tr><tr><td>标题</td><td>X(79)</td><td>9-87</td><td>示图标题</td></tr><tr><td>图形</td><td>X(5)</td><td>88-92</td><td>图号</td></tr><tr><td>图表</td><td>X(3)</td><td>93-95</td><td>图表编号</td></tr><tr><td>活页</td><td>X(38)</td><td>96-133</td><td>空白</td></tr></table>

*9 数字，X=字母数字，A=字母

\*\*β=空白

这是行类型4的数据记录的一个例子：

<table><tr><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td></tr><tr><td colspan="7">1234567890123456789012345678901234567890123456789012345678901</td></tr><tr><td colspan="7">44+RILL.THIS LINE.CONTAINS.THE-ILLUSTRATION-TITLE</td></tr><tr><td colspan="3">1</td><td>1</td><td>1</td><td>1</td><td>1</td></tr><tr><td>8</td><td>9</td><td>0</td><td>1</td><td>2</td><td>3</td><td>3</td></tr><tr><td colspan="7">2345678901234567890123456789012345678901234567890123</td></tr><tr><td colspan="7">WIDTH.depth.FILL</td></tr></table>

# 3.3 标签

下列TAG描述(内容)表述了记忆类型符号列表，这些符号用于标识发动机手册(参见3-3-10和飞机维修手册(参见3-3-1)电子传输的数据单元。这些标记应用于数据记录的“TAGS”字段。

<table><tr><td>标记</td><td>元素</td><td>描 述</td></tr><tr><td>BODN BODN</td><td>数据字区编号</td><td>唯一的数字标识符,用于将一个数据字区标识为一个单元。该数据块是一个或多个句子的任意组合</td></tr><tr><td>CAUT</td><td>注意</td><td>标识与“注意事项”相关的数据</td></tr><tr><td>CBD</td><td>电路断路器名称</td><td>标识一个电路断路器</td></tr><tr><td>CNSM</td><td>消耗性材料</td><td>标识用于特定程序的消耗性材料</td></tr><tr><td>CNSW</td><td>非特殊消耗性材料</td><td>标识用于特定程序的非特定消耗性材料(对此不分配代码)</td></tr><tr><td>EFF</td><td>有效性</td><td>标识特定数据对于发动机序列号、飞机序列号、型号命名或服务通报的适用性</td></tr><tr><td>ENDX</td><td>表示结束</td><td>用于对特殊条件下的结束信号代码</td></tr><tr><td></td><td></td><td>X=</td></tr><tr><td></td><td></td><td>C=注意</td></tr><tr><td></td><td></td><td>E=有效性</td></tr><tr><td></td><td></td><td>Q=等式Q=平衡</td></tr><tr><td></td><td></td><td>N=注</td></tr><tr><td></td><td></td><td>S=服务通报号</td></tr><tr><td></td><td></td><td>H=表头</td></tr><tr><td></td><td></td><td>T=表内容</td></tr><tr><td></td><td></td><td>W=警告</td></tr><tr><td></td><td></td><td>K=保持</td></tr><tr><td>EQU</td><td>等式</td><td>标识表达式(等式、公式等)</td></tr><tr><td>EXPM</td><td>消耗性材料</td><td>标识消耗性材料</td></tr><tr><td>EXPW</td><td>非特定消耗性材料</td><td>标识非特定消耗性材料</td></tr><tr><td>ILL</td><td>示图</td><td>标识一幅示图(面向任务或页)</td></tr><tr><td>IX</td><td>维修变更</td><td>从列开始的随后文本与以前的行不同。‘X'标识维修级别(1到6或-)</td></tr><tr><td>NOT</td><td>注</td><td>标识与“注”相关的数据</td></tr><tr><td>PAN</td><td>维修口盖</td><td>标识一个维修口盖</td></tr><tr><td>REF</td><td>引用</td><td>标识一个在随后文本中的引用</td></tr><tr><td>SBN</td><td>服务通报号</td><td>对文件中纳入特定服务通报所引起的影响进行标识。可以有多个 SBN 记录。对服务通报引用后的文本行数没有限制</td></tr><tr><td>SKP</td><td>保留起始位置</td><td>标识随后一起作为一个实体保存的数据。如果要打印或显示,则不能在页面或者屏幕上被断开</td></tr><tr><td>STN</td><td>分任务号</td><td>标识 AMTOSS 或 JEMTOSS 分任务号,用于标识一个将要执行的功能</td></tr><tr><td>TAN</td><td>任务号</td><td>标识 AMTOSS 或 JEMTOSS 任务号,用于标识一个将要执行的功能</td></tr><tr><td>TBLC</td><td>表内容</td><td>将随后的数据标识为表内容。内容是格式化的,并在表中居中排列</td></tr><tr><td>TBLH</td><td>表头</td><td>将随后的数据标识为表头。表头内容是格式化的,并在表头居中排列</td></tr><tr><td>TDS</td><td>标题</td><td>字区标题。标题可包含在一个或两个记录内</td></tr><tr><td>TED</td><td>工具、设备、描述</td><td>将随后的数据标识为任务中使用的工具/地面支持设备</td></tr><tr><td>TR</td><td>临时更改</td><td>表示随后的是临时更改</td></tr><tr><td>WARN</td><td>警告</td><td>标识与警告相关的数据</td></tr></table>

# 5-2-3 直接存取一文件传输协议

# 1 概述

文件传输组编写的这份报告作为直接存储工作组所做工作的的一部分。该文件反映了方案设计报告的一个最初的结果。

该文件于1997年九月的TICC工作周提交给DAWG成员获得认可，并且DAWG成员与文件传输组成员一起合作完善了该文件。但由于下列工作还未完成，因此它仍处于发展状态：

开始重新搜集支持文件传输过程中必要和充足的信息。

确保文件传输过程具有开放性和通用性；将设计局限性减至最小修订主要示图

![](images/d2ddf8e8649fb654544404c808b89499dd60d86c332a23c6da0c88f02dad217b.jpg)  
图5-2-3.1 文件传输概念

# 2 文件传输概述

# 2.1 前言

文件传输是通过电子交换信息。该规范定义了文件传输应用模型和协议。

# 2.2 文件传输概念

# 2.2.1 目的

文件传输应用协议必须支持从发送者环境到接收者环境的自动数据传输。

应用协议应使发送者能够利用其应用程序发送数据，使接收者能够自动执行应用程序接收数据。

# 2.2.2 概念

# 2.2.3 描述

每次传输时，一条消息可以包含一种或多种数据类型(工作包)，并可能涉及到一个或多个应用程序。规定单条消息的合理长度。

仅管理文件的有效版本(根据有存档管理的需求)。

在数据传输期间数据不能发生变化。

以批处理模式或交互式处理模式完成文件传输。

批处理模式应管理某些单机性能，例如：

通过在线协议下载目录表(TOC)。  
- 接收者做出以单机模式接收文件的选择。接收者通过下载目录表完成选择。  
根据对数据源的选择传输TOC。  
根据对TOC的选择进行数据传输。

批处理模式负责管理重复性请求。

批处理模式也负责管理选则准则。

# 2.2.4 规范结构

规范提出了下列主题：

目的与目标  
消息定义  
功能定义  
控制信息定义  
现行标准调查/评估  
控制信息结构  
验证  
- 术语表

# 2.3 一般要求

# 2.3.1. 描述

能支持多种文件传输方法，包括：

- 客户端启动的文件传输(浏览)  
- 过程启动的文件传输(入栈)  
- 请求启动的文件传输(出栈)

多种“方法”允许在航空公司、制造商及其合作伙伴内部启动自动化程序，也允许从多个服务器到单个客户端进行直接文件传输。

# 2.3.2 功能要求

元数据中应包括下列定义的信息

寻址信息  
加密信息  
触发处理信息(例如通知、应答、应用程序运行等)

·批处理和交互式能力  
数据完整性  
- 双向跟踪和日志  
标准加密法/软件的应用  
- 输入/输出规则的一致性  
跟踪/日志信息的管理

# 2.3.3 执行要求

TCP/IP是推荐的文件传输通信协议。

FTP是推荐的文件传输协议。

# 2.4 详细要求

# 2.4.1 目的与目标

建立基本的功能要求，以使技术信息交换(交互式或批处理式)，保证可接受的系统安全级别和数据完整性。

建立体系结构的概念和协议，以使发送者和接收者能够开发他们自己的传输应用程序。

![](images/54350b0440b8ae1fbf7757072386c5438575117bfe2215fc4381fd4ad62c2066.jpg)  
图5-2-3.2 消息结构

# 2.4.2 消息结构

消息由一个标题（“消息信息控制”）和一个主体部分组成，主体则由一组事务组成。每个事务包含一个标题（“事务信息控制”）和一个作为终端用户资料的主体部分。消息标题用于发送管理信息，事务头部用于进行过程管理。

# 2.4.3 消息定义

标识发送者与接收者之间交换的各种类型的消息。

![](images/1cc2079dff0d4fbff1856e86317dcefcf4d2b4e701e654ee784419a6a9a71716.jpg)  
图5-2-3.3 消息定义

# 过程触发参数

预定义参数可触发接收者的应用程序处理过程。这些参数存储在发送者环境中取决于数据类型。

数字化资料请求/数字数据请求 ACK/NACK

在发送者与接收者之间交换的消息序列，用来启动和接收信息传输。

消息传输/消息传输 ACK/NACK

在发送者与接收者之间交换的消息序列，用以传输并验证信息。

通知触发参数

描述数据的可用性。

# 2.4.4 功能定义

应用程序启动

触发接收消息时应用程序的处理过程。这种触发功能基于封装在接收消息内的过程触发参数。

压缩/解压缩

数据和所有必要信息进行压缩/解压缩的过程是将数据量减到最小，以便于通过网络进行数据交换。应采用直接存储工作组框架(在线访问分组)中定义的压缩标准。

数据接收

应答数据接收的过程。数据经过接收并验证后，被合并在应用程序处理过程中。合并的级别将取决于文件类型和接收者/发送者的要求。

加密/解密

数据和所有必要信息进行加密/解密的过程用来保证数据的安全性。应采用直接存储工作组框架(安全分组)中定义的加密标准。

错误控制

在数据传输的各种处理过程中，对检测到的错误进行管理的过程。

完整性管理

保证数据传输的完整性控制。管理的完整性级别取决于文件的重要性。

日志

跟踪并记录所有必要信息的过程用来保证良好的跟踪性级别。

消息应答

确保利用观察点进行通信控制的过程。该过程可控制数据流。

消息分析

对接收的消息进行分析的过程，以标识接收消息的各组成部分(数据信息控制)。

消息生成

封装数据和所有必要信息的过程，用来驱动接收者的应用程序传输过程。

通知

管理与资料可用性相关的通知的过程。该过程也应对没有按预期完成数据传输的异常事件处理进行管理。

请求管理

根据下述内容建立接收者/发送者的请求：

- 发送类型(文件类型)  
发送进度表  
接收者标识  
选择准则  
- 过程触发参数

![](images/d439e2696bd0848711ab5b34eb6b4009596ab989f148ddc796a0d8a609df39e2.jpg)  
图5-2-3.4 请求管理过程描述

交互式过程应是对符合选择准则的数据进行显示的公共切入点，或建立一个同样基于选择准则的重复请求。

第一步是访问文件传输请求管理形式。该形式建立了选择准则和请求模式。

在第二步中：

- 如果选择了在线模式，则执行查询过程并显示查询结果集。此时，将出现下列可能：

作为后台进程，启动文件传输  
下载  
基于当前参数，建立重复请求。

- 如果选择了批处理模式，则接收者可选择建立包括选择准则的重复请求。

# 3 功能性体系结构报告

# 3.1 范围

# 3.1.1 文件传输范围

ATA 文件传输规范的目标是，规定文件传输的应用模式和协议，使得航空公司、销售商、制造商和网络服务供应商能够开发兼容的传输软件。

# 3.1.2 文件目的

该文件描述了网络服务和相关的网络接口应用程序必须满足的最小功能体系结构，以满足ATA2200规范中规定的文件传输要求。

# 3.2 文件传输模型

# 3.2.1 体系结构概念

文件传输功能可以是通用的或特定的。

因此，对于每个组织，其文件传输由下列内容组成：

- 对于网络接口等每个组织均是相同的通用过程。

通用过程提供数据交换机制。

交换的数据是根据文件传输消息结构来编排格式的。

- 取决于特定的航空公司、销售商、制造商的应用程序的特定过程。  
- 允许采用通用过程机制的应用程序，以便与合作伙伴进行通信。

# 3.2.2 通用功能

通用功能分为三类：

数据处理(数据完整性、加密、压缩、格式化等)  
管理  
控制/监控

# 3.2.2.1 数据处理

消息生成

封装事务

可选的：一条消息可以封装多个事务。所有链接到消息的事务有相同的信息类型、相同的发送地址，到了发送日期时必须立即或根据预定计划发送。

数据传输

根据向接收者发送的特定指令集和相关信息类型，由发送者向接收者传输消息。

消息分析

分析接收到的消息以便于标识各个部分，并且从消息中提取事务。

事务分析

从事务中提取数据

加密/解密

对数据和所有必要的信息进行加密/解密，以保证数据安全性。

![](images/12a9ed8335d9b671d8bf19cfed2997209a5b5a30ddd799ec52528c1cacd26f1c.jpg)  
图5-2-3.5 体系结构概念

压缩/解压缩

对数据和所有必要的信息进行压缩/解压缩，使需要通过网络交换的数据量最少。

消息分段/组合（可选的）

保证量大的消息能够通过网络正确交换。在发送站点，这样的消息被分割成若干可接收的部分。在接收站点，再把各段重新组合成原始消息。

# 3.2.2.2 管理

用户访问管理

- 在发送站点，验证发送者是否具有向接收者提供该类信息的必要授权。  
- 在接收站点，验证接收者是否具有接受由特定发送者提供的该类信息的必要授权。

# 3.2.2.3 控制/监控

进度程序管理(可选)

- 当接收者希望按预定发送(每周或每月)或因其站点无效而希望变周期发送时(通过接收者建立的特定发送指令来详细说明)，应建立事务处理保持区域。  
在上次发送试验失败后重新安排消息发送。  
- 应定期检查保持区域内的事务，保证发送的事物得到及时处理。

数据传输的重新计划（可选）

- 数据传输失败后，依靠向接收者发送特定指令集和相关信息类型，按同一地址或备用地址重新计划数据传输。

消息应答

- 在成功完成物理接收和完整性检查的基础上应答消息。

接收者响应控制

- 消息传输后，从接收站点检测无响应的消息。

接收者通知

- 将数据发送的成败结果通知接收者。依据该类型信息的特定发送指令集来发出通知。

发送者通知

- 将数据发送的成败结果通知发送者。依据该类型信息的特定发送指令集来发出通知。

异常事件管理

- 对包括传输或提示程序的不同各过程中检测到的错误进行管理。异常程序基于向接收者发送特定指令集和相关信息类型。

计时器管理

- 如果有必要，可启动计时器，对接收者发出的数据接收应答指令进行控制。确认收到接收应答时停止计时。

网络故障控制

- 检测消息传输时的网络故障。

数据完整性检查

- 保证传输数据的完整性控制，以及检测可能的数据完整性错误。

数据接收/不接收

- 向发送者报告接收/不接收数据的应答处理过程。数据一经验证且合并到应用程序后，接收者将接收数据。

提示信息的生成

- 特定发送指令在规定的时间内未给出应答，有必要通知接收者对数据接收进行应答。

日志与跟踪

在发送者和接收者站点进行跟踪并记录传输的消息以及保证良好跟踪能力的所有必要信息。通信建立

- 获取接收器建立的特定发送指令的参数，它适合于每种信息类型。

版本管理

- 检查正在进行通信的文件传输模块是否标识为相同的版本。

# 3.2.3 特殊功能

# 3.2.3.1 数据处理

应用程序处理器

在发送模式中：处理应用程序发出的请求

该请求相当于：

- 一个汇集数据的请求  
- 一个集的发送  
- 一个对于数据接收的应答

在接收模式中：保证(立即或延时)执行应用程序

事务分析和处理

- 依据事务特性，对执行一个应用程序提供必要的信息。

事务生成

- 生成与待传输数据相关的标题信息。

本地分发

- 以向接收者发送的特定指令参数集和相关信息类型（“分发目录”参数）为依据，将消息通过文件传输地区的网络集线器分发到一系列的本地实体。

# 3.2.4 通用/特殊机载设备

基于发送者与接收者之间的数据传输，下表示出了通用与特定机载设备之间的分配情况。

# 3.2.5 发送特定指令 (DSI) 参数

每个接收器必须有自己的DSI参数。这意味着每个接收器必须对每个传输信息类型给出一些参数值。

此外，为每个接收器授权读取与每个实体相关联的DSI参数。

当接收器要更新其DSI参数时，必须给该DSI相关联的实体分配新值。

当任何实体接收新的DSI参数时，必须运行一个特定程序，以更新DSI本地数据库。

对于每个出现的事项(接收器、信息类型)，必须设置下列参数。

![](images/48d5e92cdcc656b84bd1ab7355270e4281e1b06ad2850a8fe8db3005e12b718c.jpg)  
图5-2-3.6 文件传输机载设备

# 3.2.5.1 发送方法

数据传输程序发送以下类型信息的方法：点对点连接、互联网、专用网络、传真、电报、电子邮件等。

# 3.2.5.2 发送地址

数据传输程序发送一种信息类型的地址：IP 地址、电话号码、电子邮件地址等。

# 3.2.5.3 数据传输参数

当数据传输程序中止时，文件传输应用程序根据下列参数再进行传输试验：

- 试验时间：数据传输试验应持续六小时。  
- 试验频率：数据传输试验应在六小时内每小时测试一次。  
- 在(一次有效的)试验之后交替发送方法和地址。

- 接收应答延迟时间

# 3.2.5.4 通知参数

在数据传输的同时，当接收应答为OK时，可向发送站点和/或接收站点发送通知消息。

对于每个站点，与通知参数有关的内容：

- 通知方法：传真、电子邮件  
通知地址  
默认通知消息

# 3.2.5.5 接收应答要求

对于每种信息类型和每个接收器，该参数表明接收应答是否需要。

如果需要，必须指明接收应答的最大延迟时间。

![](images/ae88779d3f1c4102d6b6e4a1e07a50aa66490243a100fa64d3bf7369828df9f3.jpg)  
图5-2-3.7 提示/异常程序机制

ACK 代表 ACKNOWLEDGMENT(应答)

# 3.2.5.6 提示和异常参数

限定时间内，没有必需的数据接受应答时，文件传输过程可执行一些提示程序选项。

触发异常程序的事件可能是网络故障、数据完整性故障、提示过程故障等。

每种程序规定了三种选项。

如果调用一个提示/异常程序，文件传输过程运行第一个选项。

如果第一选项失败，文件传输过程应运行第二选项。

如果第二选项失败，文件传输过程应运行第三选项。

如果第三项选失败，文件传输过程应通知发送者。

每个选项应设置下列参数：

- 发送方法(传真、电子邮件)  
发送地址  
传真或电子邮件发送的默认消息  
数据传输失败时的试验频率(例每小时)  
- 试验时间(例在六个小时内的每个小时)

用传真发送，传输失败表明线路忙，或通讯状况不好，或接到传真的人在试验时间后没有执行操作。用电子邮件发送，传输失败表明接到“不能发送”消息，或接到电子邮件的人在试验时间后没有执行操作。在这种情况下，试验次数设置为零，因为邮件服务器此时正进行迭代试验。

对于发送者通知，文件传输过程根据信息类型来判断发送者。

# 3.2.5.7 过程触发参数

这些参数根据运行时间参数清单来执行任意过程(数据转换过程、加密等)，它们特定事件(数据传输、特定要求等)触发。

在收到信息类型符合‘DSI参数’的消息时，应更新DSI本地数据库。

# 3.2.5.8 接收者访问控制要求

在发送者站点，必须检查发送者，以确认是否授权给他向接收者提供该类型信息。

然而，对于接收站点的访问控制是可选的(检查接收者是否期望从该发送者处获取该类型信息)。

# 3.2.5.9 分发列表

为将网络通讯成本减到最小，数据可从A传输到B，然后从B到C和D和E，而不是直接从A到C、从A到D和从A到E。

建立一个分发列表(C、D 和 E)，以确保当数据发送到 B 时，再被发送到 C 和 D 和 E。

# 3.2.5.10 发送数据参数

这些参数使接收器能够显示被发送信息类型的每个发送特性：

- 发送模式：立即、定期、不定期。  
- 对于立即发送，不需要更多信息描述。  
- 对于定期发送，文件传输过程需要频率(星期或月)，每星期几(按星期)或每几号(按月)以及次数。  
- 对于不定期发送，文件传输过程需要一个精确的日期和时间。

# 3.3 文件传输功能规范

# 3.3.1 主要特征

文件传输应用程序基于下列特征：

通信介质

文件传输规范是一个应用程序协议级别的协议。

基本通信协议是TCP/IP协议组或Internet协议。

通信介质是：

- Internet、专用线、基于Internet协议的专用网(ARINC、SITA Aeronet等)。

文件传输规范可和支持传输机制的技术或工具一起执行，这些技术和工具将在以后规定，详细说明如下：

- 任何包括网络编程接口(Internet应用插件，CORBA ORBs等)的工具箱  
- 消息(X400、SMTP等)  
- EDI(电子数据交换)类的XML(可扩展标记语言)  
传输机制

对于数据传输，文件传输应用程序管理下列机制：

- 入栈机制：文件传输应用程序(在发送站点)将数据直接送入接收者环境。发送者在这里启动文件传输。

![](images/4e9c0b8e02155cba389b96f61eecf0deac4a0503d22145ccbfdbccf6fc5d06bf.jpg)  
图5-2-3.8 入栈机制

- 出栈机制：文件传输应用程序(在接收站点)直接从发送者环境取出数据。接收者在这里启动文件传输。

![](images/d135fe5e3454613b038a0d5bdd390b93ad5f71e2fed98783bd33e84256e120e6.jpg)  
图5-2-3.9 出栈机制

- 入栈一出栈机制：发送者无权将数据送入接收者环境。所以，文件传输应用程序(在发送站点)将数据发送进一个邮箱，然后，文件传输应用程序(在接收站点)从代理服务器中取出数据。

![](images/67848e8ce9c00586f2156968c55e899b4ac51a8b6f6b0e4108991299bdf22e73.jpg)  
图5-2-3.10 入栈/出栈机制

传输模式

当开始传输数据时，文件传输应用程序承认下列模式：

- 请求模式：文件传输执行交互式过程。  
- 预定模式：文件传输以批处理模式执行。  
数据长度

被传输的数据没有长度限制。其长度可以在1K字节到100M字节之间变化。

- 可将一条消息分发给若干不同的接收者。此时，接收器信息显示一个接收器列表。

为保证在发送中包括所有必要的功能，文件传输组件需要一些称为发送特定指令 (DSI) 参数的特定参数，它们在标题为“发送特定指令 (DSI) 参数”的章中列出。

# 3.3.2 文件传输协议定义

# 3.3.2.1 基本传输协议

![](images/8e17af758144fe15a08deb3f55fe4324cb3246f9ef437ad34dce95535179146e.jpg)  
图5-2-3.11 基本传输协议

基于基本传输协议有三种数据传输方式：init_session(底层会话)

数字资料请求(DDR)  
资料  
- 接收/不接收资料的应答

# 3.3.2.2 发送者到接收者(入栈)

![](images/80dc73cc215ce1a8b3f199cb299c38419a4ed9c1b841496d9ffbd6c03a60fb36.jpg)  
图5-2-3.12 入栈流程

# 3.3.2.3 接收者从发送者获取资料(出栈)

![](images/d63d703c74b959d3f67d587dd5d15439723ba8c70909996f5349781a25711b13.jpg)  
图5-2-3.13 出栈流程

# 3.4 文件传输详细功能规范

# 3.4.1 功能结构图

![](images/d66f6eaa2bf9229e272c804198f51befe5425ec8bee6035934438181f16ecad0.jpg)  
图5-2-3.14 功能结构图

# 3.4.2 文件传输的组织过程和数据

3.4.2.1 文件传输组件

AH一应用程序处理器  
TB-事务生成器  
- OMB一输出消息生成器  
DT—数据传输  
NEH一网络事件处理器  
CHK-检查器  
EH一异常处理器  
TIM一计时器  
- REM一提示信息  
- IMP一输入消息处理  
TP一事务处理

LOG一日志记录器

# 3.4.2.2 详细的组件描述

# 3.4.2.2.1 应用程序处理器(AH)

AH 组件是文件传输应用程序与任何外部应用程序之间、发送器与接收器之间的唯一接口。

在发送站点，外部应用程序通过调用应用程序处理器组件，将数据传输到文件传输应用程序。

在接收站点，文件传输应用程序通过应用程序处理器组件调用外部应用程序，将数据传输到外部应用程序。

应用程序处理器组件可执行以下软件：

- 任何特定应用程序(在发送站点)。  
- 事务处理(TP)组件(在接收站点)。

![](images/92f9d43f0c52c8f986765e53640277d5daa1a12296296b216ea831caf4044f3f.jpg)  
图5-2-3.15 应用程序处理器原理

# 发送站点

1. 发送站点，应用程序用下列“输入参数”调用AH组件。

- 请求类型(发送、信息请求、数据接收应答)  
信息类型  
接收者  
发送者  
数据(待传输)

2. 如果请求类型是发送数据集，则AH组件读取访问授权表。AH组件以发送模式查找接收者和信息类型值。  
3. 如果发送者没有被授以向接收者传输该请求类型和信息类型的权限，应立即通知发送者。  
4. 如果该请求类型和信息类型可以发送给该接收者，则 AH 组件应与事务生成器 (TB) 进行同步通信。

AH组件按一定格式生成并传输一个称为<<事务生成请求>>的消息  
TB组件立即发回事务ID  
AH组件以向应用程序返回事务ID告终，以便被应用程序存储。

# 接收站点

1. 当收到消息时，TP 组件用下列<<输出参数 >>调用 AH 组件：

- 用DSI参数及其运行参数建立特定过程。  
- 访问控制标记：表示在接收站点是否需要显示访问控制。  
事务 ID

- 发送者  
- 请求类型  
信息类型  
数据（待发送）

2. 如果请求类型是发送数据集，且访问控制标记是“Yes”，则AH组件读取访问授权表，并在接收模式中查找发送者和信息类型值。  
3. 如果发送者没有被授以向该接收者传输该请求类型和信息类型的权限，应立即通知发送者。  
4. 如果可以从该发送者处收到该请求类型和信息类型，则AH组件应检查触发该过程的参数。

如果没有提供触发过程的参数，AH组件将消息存储到收件箱内。  
- 如果存在一个特定过程名称，则AH组件用下列<<过程参数>>调用特定过程：  
运行参数  
- 事务ID  
- 请求类型  
息类型  
- 发送者  
数据(待发送)

# 管理功能

应用程序请求管理  
用户访问管理  
应用程序启动  
- 发送者通知

# 3.4.2.2.2 事务生成器(TB)

TB组件管理来自发送站点上的应用程序处理器组件的请求，并生成事务标识符。

![](images/624d2908350b6c0cfac0ccc808828d13d7b182ed4dd4ccb53cb621b8d534dc26.jpg)  
图5-2-3.16 事务生成器原理

在收到<<事务生成请求>>消息时，TB组件：

将<<事务ID>>返回给AH组件  
- 按一定格式生成一条<<事务>>消息，并将<<事务>>消息传输到输出消息生成器组件。

# 管理功能

# - 事务建立

# 3.4.2.2.3 输出消息生成器(OMB)

OMB 组件接收并安排事务或先前传输失败的消息。这时，它发送重新预定的消息或必须同时传输的相似事务集。

输出消息生成器组件负责：

- 调度表检查：调度表包含预定的事务和重新预定的消息。  
-  $<<$  事务>>消息处理，来自于事务生成器组件。  
- <消息重新预定>>消息处理，来自于数据传输组件。

![](images/e571a8d8d579e36c7a2de57731c622a188a448d9e95b78d1182a645a121c0d93.jpg)  
图5-2-3.17 输出消息生成器原理

# a) 高度表检查

调度表检查是查找已存储在调度表中的事务或消息的一个后台过程，到发送日期时就准备发送。

因此，OMB组件定期读取调度表，并且

1. 如果找到准备发送的消息(到发送日期)，它就按一定格式生成名为<<消息开始>>的消息。

若提取的消息与其它消息或事物无链接，总是被单独传输。

如果找到准备发送的一个或多个事务（到发送日期），对于相同的接收者和信息类型，这些事务都被链接到名为<<消息启动>>的同一传输单元。

2. 然后，<<消息启动>>必须被传输到数据传输组件。

# b)  $<<$  事务>>消息处理

1. 收到<<事务>>消息时，OMB组件首先读取DSI参数。然后，对于用事务特性标识的信息类型和接收者，按照其建立方式，OMB组件获取发送日期参数。  
2. 然后，OMB 组件安排一次新的数据传输。这意味着将一条新记录用基于相应 DSI 参数的发送日期插入到调度表里，该记录的来源为事务。

# c) <<消息重新预定>>消息处理

在收到<<消息重新预定>>消息时，OMB组件完全能够安排一次新的数据传输。

这意味着在调度表中插入一条新记录，该记录具有新的发送日期并由数据传输组件（包括在消息中）提供数据来源。

d) 管理功能

- 进度管理  
通信建立  
消息生成

# 3.4.2.2.4 数据传输(DT)

DT组件代表了文件传输应用程序的主要组件。因为它接收所有类型的消息(数据请求、数据、异常事件、提示信息、通知等)在通过网络发送之前，它是能够跟踪所有被发送消息的唯一组件。数据传输组件也完全能够管理应答状态，如果必要，它也可以管理数据传输失败时进行的迭代试验。

数据传输组件负责：

- <<消息启动>>、<<消息异常>>或<<消息提示>>消息处理，它们分别来自输出消息生成器组件、或异常处理器组件或提示信息组件  
- <<ACK/NACK>>消息处理来自网络事件处理器组件  
使用跟踪表跟踪发送的消息

![](images/52e506870227cb3ee1167adb608b6194c00f83266e971abb3470383b90dd52c7.jpg)  
图5-2-3.18 数据传输原理

a) “<<消息启动>>、<<消息异常>>或<<消息提示>>”消息处理

在收到<<消息启动>>、<<消息异常>>或<<消息提示>>消息时，DT组件首先检查消息ID是否已经存储在跟踪表中。

A. 收到的消息是一个新消息。消息 ID 在跟踪表中不存在; 新消息表示对该消息传输的第一次试验。

(1) 根据消息来源, DT 组件读取 DSI 参数, 以建立用消息特性标识的信息类型和接收器:

如果来源是“事务”，参数包括：

发送方法  
发送地址  
数据传输参数

如果来源是“异常”或“提示”，则：

- 异常或提示参数基于包括在消息中的选项编号。

(2) 然后, DT 组件在跟踪表里插入一条新记录: 处于激活状态的、符合 [(试验时间除以试验次数) -1] 的再试验次数, 接收应答的限制日期以发送日期和相应的延迟时间为基准。重新安排和备用地址标记被设置到 “No” 状态为 “None”。

(3）最后，DT组件按一定格式生成名为<<消息结束>>的消息，并将消息传输到网络事件处理器组件。  
B. 收到的消息已经存在。消息ID被置于跟踪表中，并且重新安排标记为“Yes”。这意味着消息已经被重新安排并将立刻被重新发送。

(1) 如果状态仍与 ACK 不同，依据消息来源，DT 组件将读取 DSI 参数，以建立用消息特性标识的信息类型和接收器：

如果来源是“事务”，参数是：

发送方法  
若备用地址标记为“No”则发送地址  
- 若备用地址标记为“Yes”则更改地址(包括在数据传输参数中)  
数据传输参数

如果来源是“异常”或“提示”

- 异常或提示参数以跟踪表中存储的选项编号为准。

(2) 然后，DT组件更新跟踪表中的现存记录：

- 减少处于激活状态的再试次数  
基于重新发送的日期和相应的延迟时间，设置接收应答的限制日期  
将重新安排标记设置为“No”  
设置状态为 None

(3）最后，DT组件按一定格式生成名为<<消息结束>>的消息，并且将消息传输到网络事件处理器组件。

b)  $<<$  ACK/NACK>>消息处理

DT 组件应管理来自网络事件处理器组件的  $<<$  ACK/NACK >> 消息。

1. 如果  $<<$  ACK/NACK>>消息与ACK值一起被收到，则DT组件检查跟踪表中的相应来源。

如果来源是“事务”，则DT组件通过消息ID读取基于跟踪表信息的DSI参数：  
通知参数  
数据接收应答要求

如果必须在发送站点和/或在接收站点发送一个通知消息，则DT组件按一定格式生成名为<<消息结束>>的消息，并且将消息传输到网络事务处理器组件。

如果需要必须对数据接收进行应答，则DT组件首先从跟踪表的数据字段中查找各个事务ID。然后，按一定格式生成名为<<计时器启动>>的消息，并将消息传输到计时器组件。

- 如果来源是“异常”，则DT组件按一定格式生成<<异常状态>>消息并(与ACK值一起)将其传输到异常处理器组件。  
- 如果来源是“提示”，则DT组件按一定格式生成<<提示状态>>消息并(与ACK值一起)将其传输到提示信息组件。

2. 然后，DT 组件更新跟踪表中相应的记录。状态设置为 ACK 或 NACK。

c) 发送消息跟踪

跟踪发送的消息是一个后台过程，用以检测跟踪表中具有下列特性的消息：

- 还未应答(状态为 None)并且超过了接收应答的限定日期，或拒绝应答(状态为 NACK)  
- 重新安排的消息未置于调度表中。重新安排标记为“No”

当DT组件找到这样一条消息时，如果必要，应检查处于激活状态的再试次数和备用地址标记：

A. 仍然处于激活状态的再试次数大于零:

(1) 如果来源是“事务”，DT 组件首先读取 DSI 参数以获取发送日期参数，从而建立用消息特性标识的信息类型和接收器。然后，基于这些 DSI 参数，DT 组件确定新的发送日期。如果模式是“不同”（见发送日期参数），则发送日期相应于实际的发送日期，或在其它情况下，发送日期相应于上次发送日

期+试验次数。接收者不改变。

(2) 如果来源是“异常”或“提示”，则新的发送日期相应于上次发送日期+试验次数

(3) 最后, DT 组件按一定格式生成  $<<$  消息重新安排>>消息, 并将其传输到输出消息生成器组件。重新安排标记设置为 “Yes”。

B. 处于激活状态的再试次数为零:

(1) 如果来源是“事务”并且备用地址标记为“No”，则DT组件首先读取DSI参数。DT组件捕获数据传输和发送日期参数，从而建立用消息特性标识的信息类型和接收器。

然后，基于这些DSI参数，DT组件确定新的发送日期。如果模式为“不同”（见发送日期参数），则发送日期相应于实际的发送日期，或在其它情况下，发送日期相应于当前日期和时间+试验次数。接收器(地址)被设置为备用地址(见数据传输参数)。

最后，DT组件按一定格式生成<<消息重新安排>>消息，并将其传输到输出消息生成器组件。重新安排标记和备用地址标记设置为“Yes”。

(2) 如果来源是“事务”并且备用地址标记“Yes”，DT组件按一定格式生成<<数据传输失败>>消息，并将其传输到异常处理器组件。状态设置为EXCP。  
(3) 如果来源是“异常”，DT 组件按一定格式生成<<异常状态>>消息（与 NACK 值一起），并将消息传输到异常处理器组件。状态设置为 EXCP。  
(4) 如果来源是“提示”，则DT组件按一定格式生成<<提示状态>>消息（与NACK值一起），并将消息传输到提示信息组件。

d) 管理功能

通信建立  
数据传输  
数据传输重新安排  
- 消息应答  
- 接收者响应控制  
接收者通知  
- 发送者通知  
异常管理  
计时器管理

# 3.4.2.2.5 网络事件处理器(NEH)

接收站点和发送站点都使用网络事件处理器组件。它给出标准通信机制的唯一接口。

![](images/4009cde7a206d72774404109d5c486ae78769fe92ac94cc8e112465795289865.jpg)  
图5-2-3.19 网络事件处理器原理

# a) 发送站点

在发送站点，NEH 组件收到<<消息结束>>消息。如果发送方法并非传真、电报或电子邮件，则它调用检查器组件并且返回<<消息完成>>，包括：

- 在接收站点对数据完整性进行检查所使用的完整性元素。  
- 文件传输应用程序版本号

如果数据传输为 OK，则 NEH 组件从接收站点的 NEH 组件接收<< ACK/NACK>>消息，并将它返回给数据传输组件。

如果出现网络故障，则 NEH 组件接收一份物理的未收到通知，并且完全能够将它自己的 <<ACK/NACK>> 消息 (与 NACK 值一起) 发送给数据传输组件。

最后，根据发送方法和地址，NEH组件负责建立通信和消息路线。

# b) 接收站点

在接收站点，NEH 组件接收<<消息完成>>消息。首先，它检查文件传输应用程序的版本号，并确保文件传输模块与同一版本标识(的应用程序)正在通信。随后，一旦发送物理接收通知，它将调用检查器组件并且返回：

包括数据完整性检查结果的<<消息发送>>消息  
- <完整性状态>>消息

如果完整性检查结果是 OK，则 NEH 组件：

- 按一定格式生成  $<<$  ACK/NACK >> 消息 (与 ACK 值一起), 并将其传输到发送站点的网络事件处理器组件 (在同一通信会话期间)  
- 将<<消息发送>>消息传输到输入消息处理组件。

如果完整性检查结果不是 OK，则 NEH 组件按一定格式生成一个<<ACK/NACK>>消息（与 NACK 值一起），并将其传输到发送站点的网络事件处理器组件（在同一通信会话期间）。

如果能将<<消息完成>>发送给它的接收器，则传输时将不会通知接收站点的NEH组件。因此

<<ACK/NACK>>消息不会被传输到发送站点的NEH组件，从而不会被传输到DT组件。由于有接收应答的限制日期，该问题可被检测到。

c) 管理功能

数据传输  
- 消息应答  
- 接收者响应控制  
网络故障控制  
版本管理

# 3.4.2.2.6 查器（CHK）

在发送站点和接收站点都使用检查器组件，并且被网络事件处理器组件调用。

它负责数据处理和控制，例如数据加密/解密、数据压缩/解压缩、数据完整性检查等。

a) 发送站点

在发送站点，网络事件处理器组件用<<消息结束>>消息调用CHK组件。基于数字签名机制，CHK组件返回<<消息完成>>消息，该消息包括在接收站点用于进行数据完整性检查的数据字符串和当前文件传输(组件)版本号。

然后，依据信息类型，CHK组件：

- 加密或不加密消息  
压缩或不压缩消息

b) 接收站点

在接收站点，网络事件处理器组件用<<消息完成>>消息调用CHK组件。

首先，依据信息类型，CHK组件：

解密或不解密消息  
- 解压缩或不解压缩消息

然后，基于同一数字签名机制，CHK组件返回<<消息发送>>消息和表示数据完整性检查结果的<<完整性状态>>消息：“OK”或“not OK”。

c) 管理功能

数据完整性检查  
- 加密/解密  
压缩/解压缩

# 3.4.2.2.7 异常处理器(EH)

EH组件管理数据传输和提示错误：它并不能通过网络传输数据消息或提示消息。

该组件负责：

- <数据传输失败>>或<<提示失败>>消息处理，这些消息来自于数据传输组件或提示信息组件  
- <特殊状态>>消息处理，该消息来自于数据传输组件

![](images/ac7dcccff50bde67395e254a14ab7b96e12ba021b3d78c44dc196440e5fbe9b6.jpg)  
图5-2-3.20 常处理器原理

a) <<数据传输失败>>或<<提示失败>>消息处理

1. 在收到<<数据传输失败>>或<<提示失败>>消息时，EH组件首先在通知表里插入一条新记录，将通知选项设置为可接受的最大试验次数(3次试验)。  
2. 然后，EH组件按一定格式生成名为  $<<$  消息异常>>的消息(来源是“异常”并且选项编号是3)，并将消息传输到数据传输组件。

b)  $<<$  异常状态>>消息处理

在收到<<异常状态>>消息时，EH组件检查状态：

如果状态是应答，则异常程序以成功代码终止。  
如果状态是NACK，EH组件查找相应的记录放到通知表里。

如果(通知选项一1)大于或等于零，则EH组件首先插入一条新记录，包括同一拒绝消息的ID、信息类型和接收器、一个新的通知消息ID和减少的通知选项，然后按一定格式生成<<消息异常>>消息(来源是“异常”并且选项编号为新的通知选项)并将其传输到数据传输组件。

如果(通知选项一1)小于零，异常程序以错误代码终止。

c) 管理功能

异常管理

# 3.4.2.2.8 计时器(TIM)

计时器组件在一个物理消息应答之后被启动，在规定的延迟期满之前，仅在必须进行数据接收应答时需要。

当必须触发一个提示程序时，计时器开始启动计时。如果数据接收被应答，它可以在任何时间终止。计时器组件负责：

• <<计时器启动>>消息处理，该消息来自于数据传输组件  
计时器表的检查  
- <<数据接收>>消息处理，该消息来自于事务处理组件

![](images/969cc9ff80ed93ee4065cf6709a3f504b2dac65e53bd00b05427b303c6c43e8e.jpg)  
图5-2-3.21 计时器原理

a)  $<<$  计时器启动>>消息处理

对于每个包括在<<计时器启动>>消息中的事务ID，计时器组件将一条新记录插入到计时器表中，并将停止时间设置为开始时间+相应的延迟时间。激活标记设置为“Yes”。提示激活标记设置为“No”。

b）计时器表检查

计时器表检查是在计时器表中查找存储事务的一个后台过程。激活标记设置为“Yes”，并且数据接收的延迟时间(设置为)超过(达到的停止时间)。

当计时器组件发现这样一个事务时，它首先必须更新计时器表（将提示激活标记设置为“Yes”，活动标记设置为“No”）。然后将<<暂停>>消息传输到提示信息组件。

c) <<数据接收>>消息处理

当接收到<<数据接收>>消息时，计时器组件在计时器表中查找相应的触发计时器，并且更新记录，将激活标记设置为“No”。

d) 管理功能

计时器管理  
数据接收/未接收  
提示信息生成

# 3.4.2.2.9 提示信息(REM)

当数据接收没按预期的(在相应的计时器结束之前)那样被应答时，提示信息组件说明了被触发的程序。它向一些预定义的接收者反复地发布通知。如果在所有试验之后还没有响应，则调用异常程序。

提示信息组件负责：

- < $\ll$ 暂停>>消息处理，该消息来自于计时器组件  
- <提示状态>>消息处理，该消息来自于数据传输组件

![](images/26066867062ee7f046138ffada670e7db83f635b1d9ba3f89d62fe50533faa5a.jpg)  
图5-2-3.22 提示信息原理

a)  $<<$  暂停>>消息处理

在收到<<暂停>>消息时，EH组件首先检查事务ID是否已经被拒绝：

A. 如果在通知表中不存在被拒绝的事务 ID，则提示信息组件插入一条新记录，将通知选项设置为最大可接受的试验次数(3 次试验)。  
然后，提示信息组件按一定格式生成名为<<消息提示>>的消息(来源是提示信息组件，选项编号是3)，并且将消息传输到数据传输组件。  
B. 如果被拒绝的事务 ID 已经存储在通知表中, 则提示信息组件在通知表里查找相应的记录。

如果(通知选项一1)大于零，则提示信息组件首先插入一条新记录，记录包含同样被拒绝的事备ID、信息类型和接收者、一个新的通知消息ID。它使通知选项减少。然后它按一定格式生成<<消息异常>>消息(来源是“提示信息组件”并且选项编号为新的通知选项)，并将其传输到数据传输组件。

如果(通知选项一1)等于零，则提示信息组件按一定格式生成<<提示故障>>消息，并将其传输到异常处理器组件。

b)  $<<$  提示状态>>消息处理

在收到<<提示状态>>消息时，提示信息组件检查状态：

如果状态是应答，则提示程序以成功代码终止。  
如果状态是NACK，提示信息组件在通知表里查找相应的记录。

如果(通知选项一1)大于零，提示信息组件首先插入一条新的记录，记录包括同样被拒绝的事务ID、信息类型和接收者以及一个新的通知消息ID。通知选项被减小。然后按一定格式生成<<消息“提示”>>消息(来源是提示信息组件，选项数字是新的通知选项)，并将其传输到数据传输组件。

如果(通知选项一1)等于零，提示信息组件按一定格式生成<<提示故障>>消息，并将其传输到异常处理器组件。

c) 管理功能

提示信息生成

3.4.2.2.10 输入消息处理(IMP)

输入消息处理组件接收输入消息并从消息中选取不同的事务。

输入消息处理组件负责<<消息“发送”>>消息的处理，该消息来自于接收站点上的网络事件处理器组件。

![](images/03cc1215879bdb73166d5251dcacc67c689a58fb20d43e54182624c6ee5a31b7.jpg)  
图5-2-3.23 输入消息处理原理

a）在收到<<消息“发送”>>消息时，IMP组件：

- 读取DSI参数以获取过程触发参数(执行过程和它的运行参数)和接收访问控制要求，以建立用消息特性标识的信息类型和接收者。  
从消息中选取事务。  
- 按一定格式生成一个或多个名为<<已发送事务>>的消息。  
- 将每个<<已发送事务>>消息传输到事务处理组件。

b) 管理功能

- 消息分析

# 3.4.2.2.11 事务处理(TP)

- TP组件负责<<已发送事务>>消息处理，该消息来自于输入消息处理组件。

![](images/867a8d54a165a79f15c106490007fffe6815c114f16f0caf4982ce34add7da80.jpg)  
图5-2-3.24 事务处理原理

在收到<<已发送事务>>消息时，TP组件首先检查请求类型。如果请求类型是对数据接收应答，它按一定格式生成<<数据接收>>消息，并将其传输到计时器组件。

然后，TP组件用下列<<输出参数>>调用应用程序处理器组件(在接收站点)：

用相应的运行时间参数调用的特定过程  
- 访问控制标记  
- 事务ID  
- 发送者  
- 请求类型  
信息类型  
数据(待发送).  
管理功能  
事务分析  
数据接收/未接收

# 3.4.2.2.12 记录器(LOG)

日志LOG组件负责：

- 记录文件传输时所有文件传输的外部信息。这就是说，它记录了来自于两个站点(发送者和接收者)上的应用程序处理器组件和网络事件处理器组件的所有输入和输出数据。  
- 跟踪所有文件传输的内部信息(时间、地点、责任人和方式)

# a) 日志记录机制

应存储下列信息：

在发送站点：

- <<输入参数>>消息和它相关的事务ID，它们来自于应用程序处理器组件  
- <<消息完成>>输出消息和<< ACK/NACK >>输入消息，这些消息来自于网络事件处理器

在接收站点：

- <消息完成>输入消息和<ACK/NACK>>输出消息，这些消息来自于网络事件处理器  
- <<过程参数>>消息来自于应用程序处理器组件。

每条消息在传输时与日期和时间、发送者和接收者标识、通信介质等一起被存储。

所有日志记录机制将在技术设计阶段被详细说明(存储格式，访问存储系统中数据的方式等)

# b) 跟踪机制

跟踪机制将在技术设计阶段被详细说明。

它们将基于文件传输的内部表，例如调度表、跟踪表、通知表、计时器表、访问授权表等，以确定被传输的数据量和信息类型，例如传输时间、提示信息和被触发的异常程序、通知等。

# c) 管理功能

日志记录与跟踪

# 3.4.2.3 数据模型

下面的消息结构不是IP数据包的结构；消息结构只包含发送者与接收者之间需要交换的信息。

# 3.4.2.3.1 消息结构

a）事务生成请求

数据/发送者/接收者/信息类型/请求类型

b）事务ID

$\mathbf{ID}_{\mathbf{TR}}$

c） 事务

数据/发送者/接收者/信息类型/请求类型/  $\mathrm{ID}_{\mathrm{TR}}$

d) 已发送的事务

数据/发送者/接收者/信息类型/请求类型/  $\mathrm{ID}_{\mathrm{TR}}$  过程名称/过程参数或

默认通知消息/接收者/信息类型/过程名称/过程参数e）消息“启动”

消息ID/接收者/信息类型/来源

数据/发送者/接收者/信息类型/请求类型/事务1的ID

数据/发送者/接收者/信息类型/请求类型/事务2的ID

数据/发送者/接收者/信息类型/请求类型/事务3的ID或

消息ID/接收者/信息类型/来源

默认通知消息/选项编号

f) 消息“重新安排”

消息ID/接收者/信息类型/发送日期/来源

数据/发送者/接收者/信息类型/请求类型/事务1的ID

数据/发送者/接收者/信息类型/请求类型/事务2的ID

数据/发送者/接收者/信息类型/请求类型/事务3的ID或

消息ID/接收者/信息类型/发送日期/来源

默认通知消息

g) 消息“结束”

消息ID/接收者/信息类型/地址/方法

数据/发送者/接收者/信息类型/请求类型/事务1的ID

数据/发送者/接收者/信息类型/请求类型/事务2的ID

数据/发送者/接收者/信息类型/请求类型/事务3的ID或

消息ID/接收者/信息类型/地址/方法

默认通知消息。

h）消息“完成”

消息ID/接收者/信息类型/地址/方法/完整性元素/版本号

数据/发送者/接收者/信息类型/请求类型/事务1的ID

数据/发送者/接收者/信息类型/请求类型/事务2的ID

数据/发送者/接收者/信息类型/请求类型/事务3的ID或

消息ID/接收者/信息类型/地址/方法/完整性元素/版本号默认通知消息

i）消息“发送”

消息ID/接收者/信息类型

数据/发送者/接收者/信息类型/请求类型/事务1的ID

数据/发送者/接收者/信息类型/请求类型/事务2的ID

数据/发送者/接收者/信息类型/请求类型/事务3的ID或

消息ID/接收者/信息类型

默认通知消息

j） 消息“异常”

消息ID/接收者/信息类型/选项号/来源

k) 消息“提示”

消息ID/接收者/信息类型/选项号/来源

1) 异常状态

接收者/信息类型/消息ID/状态

m） 提示状态

接收者/信息类型/消息ID/状态

n) ACK/NACK

接收者/信息类型/消息ID/ACK/NACK

o）数据传输故障

接收者/信息类型/消息ID

p) 提示故障

接收者/信息类型/消息ID

q）计时器启动

发送者/接收者/信息类型/延迟/事务1的ID/事务2的ID/事务3的ID

r） 整性状态

接收者/信息类型/消息ID/状态

s）暂停

发送者接收者/信息类型/事务ID

t）数据接收

发送者/接收者/信息类型/事务ID

u) 输入参数

数据/发送者/接收者/信息类型/请求类型

v) 输出参数

数据/发送者/信息类型/请求类型/事务ID/访问控制标记/过程名称/过程参数

w) 过程参数

数据/发送者/信息类型/请求类型/事务ID/过程参数

# 3.4.2.3.2 表结构

a) 调度表

每条要发送的事务或消息，即使被立即发送，也要先存储在调度表里。这样就保存了事务和消息，也表述了数据发送的进度安排：

ID(消息ID或事务ID)  
接收者  
- 消息类型  
数据

对于预定的事务，该栏相当于数据、发送者和请求类型子区。

对于重新安排的消息(事务集)，该栏相当于整个附加事务。

对于重新安排的异常或提示消息，该栏相当于默认的通知消息。

发送数据  
来源(事务或异常或提示)

b）跟踪表

每条发送的消息系统地存储在跟踪表里。主要的是，它允许跟踪消息的应答状态：

消息ID  
发送日期  
试验次数  
- 接收应答(ACK/NACK)的限定日期

- 重新安排标记：Yes或No  
- 备用地址标记：Yes 或 No  
- 状态：ACK或NACK或EXCP或None  
- 处于激活状态的再试次数  
信息类型  
接收者  
来源(事务或异常或提示)  
- 通知选项(只用于异常或提示消息)  
数据

对于异常或提示消息，该栏相当于默认通知消息。

对于其它消息，该栏相当于整个附加事务。

# c) 通知表

通知表允许对提示信息和异常事件进行跟踪：与其相应程序的当前选项，启动程序的拒绝消息或事务等。

- 通知类型(提示或异常)  
通知消息ID  
通知选项  
拒绝ID(信息或事务)  
信息类型  
接收者

# d) 计时器表

计时器表包含不同的触发计时器和它们的相应状态：

事务ID  
信息类型  
接收者  
- 发送者  
- 激活标记  
- 启动时间  
- 终止时间  
提示激活标记

# e) 访问授权表

对于获得该表的当前用户，访问授权表列出他/她被授以发送权限的所有实体，和他/她被授以接收权限的所有实体：

信息类型  
公司(发送者或接收者)  
系统管理员标识  
- 访问类型(发送或接收)

# f) 发送特定指令表

下列DSI表列出所有的发送特定指令：

信息类型  
公司  
发送方法  
- 发送地址  
- 试验时间

试验次数  
- 接收应答延迟时间  
备选发送方法  
备选发送地址  
发送者通知方法  
发送者通知地址  
- 发送者通知默认消息  
接收者通知方法  
接收者通知地址  
- 接收者通知默认消息  
- 第一异常发送方法  
- 第一异常发送地址  
- 第一异常试验时间  
- 第一异常试验频率  
- 第二异常发送方法  
- 第二异常发送地址  
第二异常试验时间  
第二异常试验频率  
第三异常发送方法  
第三异常发送地址  
第三异常试验时间  
第三异常试验频率  
- 第一提示发送方法  
- 第一提示发送地址  
- 第一提示试验时间  
第一提示试验频率  
第二提示发送方法  
- 第二提示发送地址  
- 第二提示试验时间  
第二提示试验频率  
第三提示发送方法  
第三提示发送地址  
第三提示试验时间  
第三提示试验频率  
- 过程名称  
运行时间过程参数  
数据接收要求  
数据接收应答延迟时间  
接收者访问控制  
- 发送模式(立即、定期或不定期)  
发送次数(只用于定期模式)  
- 发送日（只用于定期模式）  
- 发送日期(只用于不定期模式)  
发送时间

# 3.4.3 功能/组件矩阵

表 5-2-3.1 功能/组件矩阵  

<table><tr><td></td><td>AH</td><td>TB</td><td>OMB</td><td>DT</td><td>NEH</td><td>CHK</td><td>EH</td><td>TIM</td><td>REM</td><td>IMP</td><td>TP</td><td>LOG</td></tr><tr><td>用户访问管理</td><td>X</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>应用程序请求管理</td><td>X</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>应用程序启动</td><td>X</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>事务生成</td><td></td><td>X</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>进度管理</td><td></td><td></td><td>X</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>通信建立</td><td></td><td></td><td>X</td><td>X</td><td></td><td></td><td></td><td></td><td></td><td>X</td><td></td><td></td></tr><tr><td>消息生成</td><td></td><td></td><td>X</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>数据传输</td><td></td><td></td><td></td><td>X</td><td>X</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>数据传输重新安排</td><td></td><td></td><td></td><td>X</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>消息应答</td><td></td><td></td><td></td><td>X</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>接收者响应控制</td><td></td><td></td><td></td><td>X</td><td>X</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>接收者通知</td><td></td><td></td><td></td><td>X</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>发送者通知</td><td>X</td><td></td><td></td><td>X</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>异常管理</td><td></td><td></td><td></td><td>X</td><td></td><td></td><td>X</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>计时器管理</td><td></td><td></td><td></td><td>X</td><td></td><td></td><td></td><td>X</td><td></td><td></td><td></td><td></td></tr><tr><td>网络故障管理</td><td></td><td></td><td></td><td></td><td>X</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>数据完整性检查</td><td></td><td></td><td></td><td></td><td></td><td>X</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>消息分析</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>X</td><td></td><td></td></tr><tr><td>事务分析</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>X</td><td></td></tr><tr><td>数据接收/未接收</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>X</td><td></td><td></td><td>X</td><td></td></tr><tr><td>提示信息生成</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>X</td><td>X</td><td></td><td></td><td></td></tr><tr><td>加密/解密</td><td></td><td></td><td></td><td></td><td></td><td>X</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>压缩/解压缩</td><td></td><td></td><td></td><td></td><td></td><td>X</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>消息分段/组合</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>版本管理</td><td></td><td></td><td></td><td></td><td>X</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>日志记录与跟踪</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>X</td></tr><tr><td>本地分发</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr></table>

AH：应用程序处理器  
TB：事务生成器  
- OMB：输出消息生成器  
DT：数据传输  
CHK: 检查器  
NEH：网络事件处理器  
EH: 异常处理器  
TIM：计时器

- REM: 提示信息  
- IMP：输入消息处理  
- TP：事务处理  
LOG：日志

# 5-2-4 图形交换

# 1 引用规范

本规范中引用了下列标准和规范：

- 第4组传真机一般特性[CCITT VII.3]  
- 关于图像描述信息存储和传输的计算机图元文件(CGM), [ISO/IEC 8632:1999](1、3部分)  
- 标签图像文件格式规范[TIFF 5.0修订版]

# 2 介质

由于可用数据处理设备的多样性，介质类型应经过资料供应方和资料接收方共同协商。关于数字交换中所使用的推荐介质格式的论述，请参考ATA TICC.MEDIA规范(参见5-2-1)。

# 3 字符标准

# 3.1 声明文件

声明文件中的字符代码，根据[ISO Latin 1 ASCII]字符集左手页上的定义，其值应限制为32到126；根据ISO Latin1字符集右手页的定义，其值应限制为161到255。

# 3.2 标签图像格式文件

对于ASCII类型的TIFF标记，根据[ISO Latin 1 ASCII]字符集左手页的定义，字符代码值应限制为32到126。

# 3.3 计算机图元文件

CGM 文件中认可的字符集在本文件的矢量图形部分中被定义。图形和非图形的文本元素都是可寻址的。

# 4 方向

示图应按照允许在垂直方向直接浏览图形而不必旋转的坐标系统来提供。

# 5 声明文件

声明文件是必需的。声明文件作为文件集的一部分，是一个单独交付的物理文件。该文件用来存储示图的基本信息。对于手册和图形类型的每种组合，应有一个单独的声明文件。如果同一手册既包含TIFF文件又包含CGM文件，那么该手册应有两个声明文件。

图形声明文件的内容和格式要求包含在ATA TICC.MEDIA规范中(参见[5-2-1])

# 6 光栅图形

根据[ISO/IEC 8632:1992]的介绍，利用CCITT组4算法压缩而成的光栅图像可被计算机图元文件(CGM)标准所支持。CGM是光栅数据交换的首选方法，但采用TIFF文件格式可与该规范的早期版本保持兼容性。这里介绍的TIFF规范并不期望在将来被扩展，以包含更多的功能。

# 6.1 标签图像文件格式

以标签图像文件格式(TIFF)来进行交换的示图应采用CCITT组4压缩算法。并非所有的TIFF文件都采用CCITT组4压缩；因而TIFF and CCITT组4都是必需的。

# 6.1.1 规范

本规范基于标签图像文件格式规范，修订版5.0。

# 6.1.2 应用

本规范既适用于资料提供者(称为TIFF作者)，也适用于资料接收者(称为TIFF读者)。定义了下列TIFF图像分类，以允许TIFF读者和作者更有效地通信。作者应告知读者他们所提供的TIFF图像类型。其类型在声明文件中的第3个记录中指定。

1类：每英寸300像素的黑白图像。

2类：每英寸400像素的黑白图像。  
3类：每英寸600像素的黑白图像。  
- 4类：每英寸1200像素的黑白图像。

# 6.2TIFF格式

下列格式定义了TIFF文件的ATA应用简述文件。在[TIFF修订版5.0]规范的附录G中定义的TIFF类B-Bi级别规范只是出于引用目的而被转述。如果ATA的简述文件中包括TIFFB规范的部分或全部内容，则它应被明确地叙述。

# 6.2.1TIFF规则

<table><tr><td>功能</td><td>规范-ATA 简述文件</td><td>规范-TIFF B</td></tr><tr><td>6.2.1.1 默认标记值</td><td>TIFF 作者应写出一个有默认值的字段,即使该默认值即期望值。</td><td>如果该默认值即为期望值,那么 TIFF 作者可以但不要求写出一个有默认值的字段。TIFF 读者应准备好处理任何一种情况。</td></tr><tr><td>6.2.1.2 信息标记处理</td><td>TIFF 作者应编写图像说明标记。其它信息标记是可选的。</td><td>TIFF 作者应准备遇到除 TIFF 文件 Tiff 中字段以外的字段。允许 TIFF 作者编写诸如:制作、模型、日期时间等字段,并且如果它们存在,TIFF 读者当然能够利用这些字段。但如果这些可选字段不存在,TIFF 读者也不应拒绝阅读该文件。</td></tr><tr><td>6.2.1.3 数据类型 ASCII 处理</td><td>所有 ASC II 字符串应以 null(空字符)结束</td><td>未提及</td></tr><tr><td>6.2.1.4 图像分辨率</td><td>对于完全分辨率的图形,可接受的分辨率是每英寸300、400、600和1200 象素。TIFF 作者应以最低每英寸300 象素提供完全清晰的图象。TIFF 读者应声明他们支持的分辨率。</td><td>未提及</td></tr><tr><td>6.2.1.5 多个子文件</td><td>Same as TIFF class B与TIFF 的B 类相同</td><td>TIFF 读者应为每个 TIFF 文件准备多个图像(如子文件),尽管针对第一个(子)文件之后的其它任何图像对他们没有任何要求。按照TIFF 规范的说明,TIFF 作者应确保在最后的 IFD(这是信息传输的标准方式,该 IFD 是最后一个字符串)之后写一个长字0。如果TIFF 作者编写多个子文件,则第一个文件应是完全分辨率的图像。随后的子图像,例如降低分辨率的图像和透明蒙版的图像,且在TIFF 文件中可以按任意顺序。如果一个读者想要使用这样的子图像,在决定如何进行之前应搜索 IFD 的内容。</td></tr></table>

# 6.2.2TIFF图像文件标题

<table><tr><td>功能</td><td>规范—ATA简述文件</td><td>规范—TIFF B</td></tr><tr><td>6.2.2.1 字节指令</td><td>同TIFF B类</td><td>TIFF读者应能处理双方字节指令。TIFF作者可选择最方便或最有效的任何一种进行处理。</td></tr><tr><td>6.2.2.2 版本号</td><td>同TIFF B类</td><td>必需的数字值是42</td></tr><tr><td>6.2.2.3 偏移量</td><td>值应为8</td><td>到第一个图像文件目录的偏移量。目录可出现在文件头部之后的任何位置，但应从一个字的边界开始。</td></tr></table>

6.2.3 基本标记  

<table><tr><td>标记名称(值)</td><td>规范-ATA 简述文件</td><td>规范-TIFF B</td></tr><tr><td>6.2.3.1 每个样本的位数(258)</td><td>同TIFF B类</td><td>必需-值应为1</td></tr><tr><td>6.2.3.2 彩色图像(320)</td><td>禁止</td><td>未提及</td></tr><tr><td>6.2.3.3 色彩感应曲线(301)</td><td>禁止</td><td>未提及</td></tr><tr><td>6.2.3.4 压缩(259)</td><td>必需-值应为4</td><td>必需-值应为1、2、或32773</td></tr><tr><td>6.2.3.5 灰度感应曲线(291)</td><td>禁止</td><td>未提及</td></tr><tr><td>6.2.3.6 灰度感应单元(290)</td><td>禁止</td><td>未提及</td></tr><tr><td>6.2.3.7 图像长度(257)</td><td>必需</td><td>必需-建议长型</td></tr><tr><td>6.2.3.8 图像宽度(256)</td><td>必需</td><td>必需-建议为长型</td></tr><tr><td>6.2.3.9 方向(274)</td><td>必需-值应为1或4</td><td>未提及</td></tr><tr><td>6.2.3.10 新的子文件类型(254)</td><td>必需-只有允许的单页图象和第一个IFD应有该标记,用于将所有位设置为零。对于后续的子文件,0位和2位的任何组合可设置为1。</td><td>推荐,但不是必需的</td></tr><tr><td>6.2.3.11 光度解析(262)</td><td>必需-值应是0、1或4。值4不允许在第一个IFD中。</td><td>必需-值应是0或1</td></tr><tr><td>6.2.3.12 平面结构(284)</td><td>禁止</td><td>未提及</td></tr><tr><td>6.2.3.13 预报装置(317)</td><td>禁止</td><td>未提及</td></tr><tr><td>6.2.3.14 分辨率单位(296)</td><td>必需-值应为2</td><td>必需-TIFF 读者应准备处理分辨率单位的所有3个值</td></tr><tr><td>6.2.3.15 每条的行数(278)</td><td>必需-类型应为长型</td><td>必需-建议长型,并将该值设置为每条长度大约8K字节。</td></tr><tr><td>6.2.3.16 每象素样本(277)</td><td>必需-值应为1</td><td>因为1为默认值,该标记不是必需的</td></tr><tr><td>6.2.3.17 条字节数(279)</td><td>必需</td><td>必需-建议为短型</td></tr><tr><td>6.2.3.18 条偏移(273)</td><td>必需</td><td>必需-建议为长型</td></tr><tr><td>6.2.3.19 X分辨率(282)</td><td>必需-完全分辨率图像的值应为300、400、600或1200</td><td>必需</td></tr><tr><td>6.2.3.20 Y分辨率(283)</td><td>必需-完全分辨率图像的值应为300、400、600或1200</td><td>必需</td></tr></table>

# 6.2.4 信息标记

<table><tr><td>标记名称(值)</td><td>规范-ATA 简述文件</td><td>规范-TIFF B</td></tr><tr><td>6.2.4.1 家(315)</td><td>允许</td><td>允许</td></tr><tr><td>6.2.4.2 日期时间(306)</td><td>允许-如果存在,该值应和图形声明文件中的修订日期匹配。</td><td>允许</td></tr><tr><td>6.2.4.3 主机(316)</td><td>允许</td><td>允许</td></tr><tr><td>6.2.4.4 图像说明(270)</td><td>必需-该字段的前32个字节应包含图形描述符,并且应符合ATA 文本规范(4-2)中定义的图形编号(gnbr)。如果必须要填满所有32个字节,应用 ASC II 码空格来填补。第33字节应是一个 ASC II 码空格(以与本规范的早期版本保持兼容性)。</td><td>允许</td></tr><tr><td>6.2.4.5 制作(271)</td><td>允许</td><td>允许</td></tr><tr><td>6.2.4.6 模型(272)</td><td>允许</td><td>允许</td></tr><tr><td>6.2.4.7 软件(305)</td><td>允许</td><td>允许</td></tr></table>

# 6.2.5 传真标记

<table><tr><td>标记名称(值)</td><td>规范—ATA 简述文件</td><td>规范—TIFF B</td></tr><tr><td>6.2.5.1 组3选项(292)</td><td>禁止</td><td>禁止</td></tr><tr><td>6.2.5.2 组4选项(293)</td><td>必需</td><td>禁止</td></tr></table>

# 6.2.6 文件存储和检索标记

<table><tr><td>标记名称(值)</td><td>规范-ATA 简述文件</td><td>规范-TIFF B</td></tr><tr><td>6.2.6.1 文件名(269)</td><td>允许</td><td>允许</td></tr><tr><td>6.2.6.2 页名(285)</td><td>允许</td><td>允许</td></tr><tr><td>6.2.6.3 页码 (297)</td><td>允许-如果该标记存在,值应为0或1。0表示左手(背面)页,1表示右手(正面)页。</td><td>允许</td></tr><tr><td>6.2.6.4 X位置(286)</td><td>禁止</td><td>允许</td></tr><tr><td>6.2.6.5 Y位置(287)</td><td>禁止</td><td>允许</td></tr></table>

# 6.2.7 不再推荐的标记

<table><tr><td>标记名称(值)</td><td>规范一ATA 简述文件</td><td>规范一TIFF B</td></tr><tr><td>6.2.7.1 单元格长度(265)</td><td>禁止</td><td>未提及</td></tr><tr><td>6.2.7.2 单元格宽度(264)</td><td>禁止</td><td>未提及</td></tr><tr><td>6.2.7.3 填充顺序(266)</td><td>禁止</td><td>未提及</td></tr><tr><td></td><td>注:应首先填充一个字节的最左边位。</td><td></td></tr><tr><td>6.2.7.4 空字节数(289)</td><td>禁止</td><td>未提及</td></tr><tr><td>6.2.7.5 自由偏移(288)</td><td>禁止</td><td>未提及</td></tr><tr><td>6.2.7.6 最大样本值(281)</td><td>禁止</td><td>未提及</td></tr><tr><td>标记名称(值)</td><td>规范—ATA 简述文件</td><td>规范—TIFF B</td></tr><tr><td>6.2.7.7 最小样本值(280)</td><td>禁止</td><td>未提及</td></tr><tr><td>6.2.7.8 子文件类型(255)</td><td>禁止</td><td>未提及</td></tr><tr><td>6.2.7.9 阈值(门限值)(263)</td><td>禁止</td><td>未提及</td></tr></table>

# 6.2.8 应用标记

<table><tr><td>标记名称(值)</td><td>规范—ATA 简述文件</td><td>规范—TIFF B</td></tr><tr><td>6.2.8.1 图像内容 X 偏移 (34326)</td><td>允许—从图像边界的左边界到信息内容的左 边界的偏移量，以像素为度量单位</td><td>未提及</td></tr><tr><td>6.2.8.2 图像内容 Y 偏移 (34327)</td><td>允许—从图像边界的上边界到信息内容的上 边界的偏移量，以像素为度量单位</td><td>未提及</td></tr><tr><td>6.2.8.3 图像内容宽度 (34328)</td><td>允许—以像素来度量的信息内容矩形区域的 宽度—该值应小于或等于图像宽度。</td><td>未提及</td></tr><tr><td>6.2.8.4 图形内容长度 (34329)</td><td>允许—以像素来度量的信息内容矩形区域的 长度—该值应小于或等于图像长度。</td><td>未提及</td></tr></table>

# 6.3TIFF范例

以下是一个符合ATA2200规范的TIFF标记集合的实例。所有的偏移量和大多数值都用十六进制表示。有一个分辨率为300DPI的  $7.5\times 10.5$  图像，使用应用标记以标识相对于图像的左边界和上边界一个半英寸的偏移量，以及相对于图像的右边界和下边界一个1英寸的偏移量。这里没有列出CCITT组4的数据。

# 6.3.1 IFH

<table><tr><td>偏移量</td><td>值</td><td>名称</td></tr><tr><td>000</td><td>4D4D</td><td>字节顺序</td></tr><tr><td>002</td><td>002A</td><td>TIFF 版本</td></tr><tr><td>004</td><td>00000008</td><td>第一个 IFD 的位置指针</td></tr></table>

# 6.3.2 IFD

<table><tr><td>偏移量</td><td>标记</td><td>类型</td><td>长度</td><td>值/偏移量</td><td>说明</td></tr><tr><td>008</td><td>0014</td><td>IFD</td><td>计数</td><td></td><td></td></tr><tr><td>00A</td><td>00FE</td><td>0004</td><td>00000001</td><td>00000000</td><td>新子文件类型</td></tr><tr><td>016</td><td>0100</td><td>0003</td><td>00000001</td><td>08CA0000</td><td>图像宽度</td></tr><tr><td>022</td><td>0101</td><td>0003</td><td>00000001</td><td>0C4E0000</td><td>图像长度</td></tr><tr><td>02E</td><td>0102</td><td>0003</td><td>00000001</td><td>00010000</td><td>每样本的字节数</td></tr><tr><td>03A</td><td>0103</td><td>0003</td><td>00000001</td><td>0004000Q</td><td>压缩</td></tr><tr><td>046</td><td>0106</td><td>0003</td><td>00000001</td><td>00000000</td><td>光度解析</td></tr><tr><td>052</td><td>010E</td><td>0002</td><td>00000022</td><td>00000100</td><td>图像说明</td></tr><tr><td>05E</td><td>0111</td><td>0004</td><td>000000C5</td><td>00000122</td><td>条偏移量</td></tr><tr><td>06A</td><td>0112</td><td>0003</td><td>00000001</td><td>00010000</td><td>方向</td></tr><tr><td>076</td><td>0115</td><td>0003</td><td>00000001</td><td>00010000</td><td>每象素样本</td></tr><tr><td>082</td><td>0116</td><td>0004</td><td>00000001</td><td>00000010</td><td>每条行数</td></tr><tr><td>08E</td><td>0117</td><td>0004</td><td>000000C5</td><td>00000436</td><td>条字节数</td></tr><tr><td>09A</td><td>011A</td><td>0005</td><td>00000001</td><td>0000074A</td><td>X分辨率</td></tr><tr><td>0A6</td><td>011B</td><td>0005</td><td>00000001</td><td>00000752</td><td>Y分辨率</td></tr><tr><td>0B2</td><td>0125</td><td>0003</td><td>00000001</td><td>00000000</td><td>组4选项</td></tr><tr><td>0BE</td><td>0128</td><td>0003</td><td>00000001</td><td>00020000</td><td>分辨率单位</td></tr><tr><td>0CA</td><td>8616</td><td>0003</td><td>00000001</td><td>00960000</td><td>图像内容X偏移</td></tr><tr><td>0D6</td><td>8617</td><td>0003</td><td>00000001</td><td>00960000</td><td>图像内容Y偏移</td></tr><tr><td>0E2</td><td>8618</td><td>0003</td><td>00000001</td><td>07080000</td><td>图像内容的宽度</td></tr><tr><td>0EE</td><td>8619</td><td>0003</td><td>00000001</td><td>07080000</td><td>图像内容的长度</td></tr><tr><td>0FA</td><td>000000</td><td></td><td></td><td></td><td>结束</td></tr></table>

# 6.3.3 IFD显示的标记数据

<table><tr><td>偏移量</td><td>值</td></tr><tr><td>100</td><td>图形的标识编号 1001001</td></tr><tr><td>122</td><td>(偏移 0、偏移 1、偏移 196)</td></tr><tr><td>436</td><td>(计数 0、计数 1、计数 196)</td></tr><tr><td>74A</td><td>0000012C00000001</td></tr><tr><td>752</td><td>0000012C00000001</td></tr></table>

# 7 矢量图形

# 7.1 CGM

使用矢量数据和文本字符进行交换的示图应符合计算机图形元文件(CGM)格式[ISO/IEC 8632:1999]。该ISO标准标识了图元文件的4个版本。关于这些版本的论述，请查阅标准。

# 7.1.1 应用

本规范既适用于资料提供者(称为 CGM 生成程序), 也适用于资料接收者(称为 CGM 解释程序)。下文中定义了两类 CGM 文件, 以便 CGM 生成程序和解释程序可以更有效地进行通信。生成程序应告知解释程序它们将提供的图像类型。该类型在声明文件的记录 3 中进行了规定, 并通过图元文件描述符元素部分所描述的 METAFILE DESCRIPTION(图元文件描述) 元素的色彩类别参数值反映出来。

# 7.1.1.1 单色图元文件

1 类数据应由单色图元文件组成。该类基于黑白线条艺术的概念。定义特殊类别的主要原因是提高本规范的兼容性。CGM 生成程序和解释程序可证明它们本身对 ATA 的 1 类数据是兼容的。

# 7.1.1.2 灰度和彩色图元文件

2类数据应由灰度或彩色图元文件组成。灰度图元文件被认为是彩色图元文件的一个特例。

# 7.2 CGM格式(版本1、2和3)

以下格式对照[ISO/IEC 8632:1999]中定义的 ISO 模型简述文件，对包含 1、2 和 3 版本元素的 CGM 文件的 ATA 应用程序简述文件进行了定义。格式表中的编号方式与 ISO CGM 标准中的编号方式相同。ISO 模型简述文件的规范作为引用而被提出，并应当是准确的。（两个文件）如果存在差异，应首先选用[ISO/IEC 8632:1999]中的模型简述文件。该格式的目的就是当该规范进行修订时能保持向上的兼容性。

可通过ATA对供应商产品进行认证测试维护。推荐使用已认证的ATA应用程序简述文件的CGM工具。使用认证的工具可确保一个CGM产品正确地执行标准和应用程序简述文件。它给用户提供了较高的信誉度级别和产品质量，它能生成正确的图片，并与其它认证产品具有互用性。目前，CGM解释程序的认证维护对ATA简述文件而言是有效的。生成程序的测试维护目前尚处于开发阶段。即使生成程序目前还无法使用，利用已认证的解释程序工具也可以改进其可靠性。可以根据本规范起始部分列出的出版商地址直接与ATA联系以获取更多的信息。

# 7.2.1 图元文件规则

<table><tr><td>功能</td><td>规范-ATA 简述文件</td><td>规范-模型简述文件</td></tr><tr><td>T.13.1 编码</td><td>有无</td><td>选择 1 或更多编码二进制:有明码:有</td></tr><tr><td>T.13.2 图片数目</td><td>1无限制每个图元文件最少有一个图像每个图元文件最多有一个图像,除了符号库图元文件中的图像外(参见符号库的论述),还包括降低分辨率的光栅图像。</td><td>在一个图元文件中允许有多少图像:最小(0)?1最大(0或“无限制”)?无限制其它:无</td></tr><tr><td>T.13.3 空图像</td><td>同模型简述文件有其它:无</td><td>允许图片没有图像图元?(是/否)</td></tr><tr><td>T.13.4 图元文件大小</td><td>同模型简述文件</td><td>对图元文件大小上有限制吗?无其它:无</td></tr></table>

# 7.2.2 多元素规则

<table><tr><td>功能</td><td>规范—ATA 简述文件</td><td>规范—模型简述文件</td></tr><tr><td rowspan="4">T.14.1 颜色</td><td></td><td>选择哪个适用于每个图元文件的规则(选择1):应定义所有颜色还是不定义任何颜色?</td></tr><tr><td>是</td><td>是</td></tr><tr><td>否</td><td>应定义所有颜色吗?否</td></tr><tr><td>否</td><td>不定义任何颜色吗?否</td></tr><tr><td>功能</td><td>规范-ATA 简述文件</td><td>规范-模型简述文件</td></tr><tr><td></td><td>是无是单色和彩色灰度被认为是彩色的一个特例。这类颜色在图形声明文件的记录3中被定义,并通过必需的METAFILE DESCRIPTION(图元文件说明)元素的彩色类别参数反映出来。</td><td>允许重新定义一个图片或图元文件的颜色索引吗?(是/否)否对一个图片或图元文件中使用不同颜色的数目限制。(单色图元文件应最多使用两种不同的颜色。)无定义兼容性类别了吗?(是/否)是如果是,详细说明单色、灰度和彩色其它:无</td></tr><tr><td>T.14.2 线型图元一几何简化度</td><td>同模型简述文件</td><td>几何简化度是:允许如果允许,简化的图形含意是:一个线型图元元素,其整个轨迹是一个孤立点,表示一个图形点,该点是一个以直径等于当前线宽,颜色等于当前线颜色填充的圆。Other:none 其它:无</td></tr><tr><td>T.14.3 填充区域图元一几何简化度</td><td>同模型简述文件</td><td>几何简化度是:允许如果允许,简化的图形含意是:一个填充区域图元,其整个轨迹是以下说明中的一个点或一条线:如果填充区域图元的轨迹是一个单点,则意味着它是一个圆点(是一个填充圆)。如果填充区域图元的轨迹是一条非简化线段,那么意味着它是一条线。如果EDGE VISIBILITY(边可见度)为禁止,那么点或线用填充颜色来显示,除非在INTERIOR STYLE(内部样式)为空的情况下,它不被填色。EDGE VISIBILITY(边可见</td></tr><tr><td></td><td></td><td>度)为允许,内部处理方式是用填充颜色来显示点或线,于是圆点或线与当前边界属性相叠加。其它:无</td></tr><tr><td>T.14.4 图形的文本字符串</td><td>0254通过CHARACTER CODE ANNOUNCER(字符码表示器)的基本值来选择。允许CO字符为NUL(代码值),且该字符没有实际的作用。图形文本的字符串参数应不包括控制字符。(7/8位代码:1-31和128-159)无</td><td>最小字符串长度(字节)0最大字符串长度(字节)254使用[ISO/IEC2022]转换控制有限制吗?图元文件中使用的任何字符集通过[ISO/IEC2022]转换技术可被存取,这些字符集应在字符集列表中(在本简述文件中定义)其它:无</td></tr><tr><td>T.14.5 非图形的文本字符串</td><td>2541024允许的字符集是: [ISO 8859-1:1987]LHS No.1和 [ISO 8859-1:1987]RHS No.1通过[ISO/IEC 2022]转换技术可被存取的任何字符集应包含在字符集列表中(在本简述文件中定义)</td><td>最小字符串长度(字节)对于SF类型:254对于D类型中的SF类型1024格式控制符和ESCAPE字符允许其它CO控制码被禁止(除了[ISO/IEC2022]转换控制的NUL字符)对可接受的字符集有限制吗?允许的字符集是:[ISO 8859-1:1987]LHS No.1和[ISO 8859-1:1987]RHS No.1对使用[ISO/IEC 2022]转换控制的限制:可通过[ISO/IEC 2022]转换技术存取的图元文件中使用的任何字符集应包含在字符集列表中(在本简述文件中定义)</td></tr><tr><td></td><td>非图形的文本字符串大小写皆可。</td><td>其它:无</td></tr><tr><td>T.14.6 数据记录字符串</td><td>同模型简述文件</td><td>最大字符串长度(字节)或无限制状态:32767应使用SDR编码技术。其它:无</td></tr></table>

7.2.3 分隔符元素  

<table><tr><td>功能</td><td>规范-ATA 简述文件</td><td>规范-模型简述文件</td></tr><tr><td>T.15.0空操作版本:1</td><td>同模型简述文件</td><td>元素是:允许的注:这个元素只适用于使用二进制编码的图元文件。</td></tr><tr><td>T.15.1 图元文件开始图元文件结束CGM 版本:1</td><td>必需的对于示图,图元文件标识字段的前32个字节应包含图形描述符,并与ATA 文本规范(4-2)中定义的gnbr相匹配。如果必须填满所有32个字节,应用 ASC II 码空格来填补。第33个字节应是一个 ASC II 码空格(与本规范的早期版本保持兼容)。对于符号库,1 至6 字节应包含SYMLIB 字符串,7 至32 字节应包含符号库名称,该名称包含在参考图元文件的 SYMBOL LIBRARY LIST(符号库列表)元素中。其它:无</td><td>元素是:必需的</td></tr><tr><td>T.15.2 图片开始图片主体开始图片结束CGM 版本:1</td><td>必需的每个图元文件应有一幅示图。对于第一幅图片中降低分辨率的光栅图像,允许具有附加的图片。降低分辨率的光栅图像应具有第一幅图片的图片标识符,该标识符与字符串RRn 连接,其中n 是降低分辨率的图像编号。对于符号库图元文件,则允许不限定图片数目。</td><td>元素是:允许的图元文件中所允许这些元素出现的次数。未限定</td></tr><tr><td></td><td>无</td><td>其它:无</td></tr><tr><td>T.15.3 图段开始图段结束CGM 版本:2</td><td>禁止</td><td>元素是:允许的在图元文件的任何位置,同时定义的图段(全部和局部)的最大数目1024对元素数目的限制以及对组成图段的元素的约束:无图段标识符参数有何含义?(有/没有)没有如果有,详细说明。(意味着应没有图形结果)其它:当全部图段在图元文件描述符中被指定时,所有全部图段的定义都应遵循所有其它图元文件描述符。当图段在图片描述符中被指定时,所有图段的定义都应遵循所有其它图片描述符元素。</td></tr><tr><td>T.15.4 图形开始图形结束CGM 版本:2</td><td>同模型简述文件</td><td>元素是:允许的对元素数目的限制,以及对构成一个图形定义的元素的约束:元素最大数目=128对可被包括在内的合格元素无限制。其它:无。</td></tr><tr><td>T.15.5 REGION 保护区域开始保护区域结束CGM 版本:3</td><td>同模型简述文件</td><td>元素是:允许的同时被定义的保护区域的最大数目:32每个保护区域内的元素的最大数目:128区域的索引参数有含义吗?(有/没有)没有如果有,详细说明。(意味着应没有图形结果)其它:无</td></tr><tr><td>T.15.6 混合行开始</td><td>同模型简述文件</td><td>元素是:允许的</td></tr><tr><td>E混合行结束CGM版本:3</td><td></td><td>对元素的数目和构成一个路径定义的元素等同性的限制:元素最大数目=128。对可被包括在内的合格元素无限制。其它:无</td></tr><tr><td>T.15.7 混合文本路径开始混合文本路径结束CGM 版本:3</td><td>同模型简述文件</td><td>元素是:允许的对元素数目和构成一个路径定义的元素等同性的限制:元素最大数目=128。对可被包括的合格元素无限制。其它:无</td></tr><tr><td>T.15.8 图象块阵列开始图象块阵列结束CGM 版本:3</td><td>允许64641024,对于图像块光栅图象1024,对于图像块光栅图象应为0无.无允许两种光栅图像。一种单一(非块式图像)图像,最大有67,320,000个单元格(以600dpi 扫描的11X17英寸图像)。一个非块式图像可以超过针对块式图像所指定的1024个单元格/图像块的限制。块式光栅图像被限定为64X64个图像块,每个图</td><td>元素是:允许的在路径方向上图像块的最大数目:16在行方向上图像块的最大数目:16在路径方向上单元格/图像块的最大数目:1024在行方向上单元格/图像块的最大数目1024对像素走向有限制吗?无对行的级数有限制吗?无对图像偏移量有限制吗?无其它:无</td></tr><tr><td></td><td>像块最多有1024X1024个单元格。块式图像限定总共有2.5亿个单元格。(图像块和每个图像的单元格的可调节最大值应满足该要求。)</td><td></td></tr><tr><td rowspan="2">T.15.9 应用程序结构开始应用程序结构主体开始应用程序结构结束CGM 版本: 4</td><td>禁止</td><td rowspan="2">元素是:允许的对一个图片中定义的结构的最大数目的限制:无对组成一个结构的元素的数目和等同性的限制:无如果应用程序的含义被分配给应用程序结构标识符参数,规定其含义为:除了为应用程序结构分配一个唯一标识符外,没有其它含义。限制继承标记参数吗?否其它:无</td></tr><tr><td colspan="1">对于在 GREXCHANGE(图形交换)中允许的版本4的功能描述,可参见 CGM 格式的相关部分(版本4)。</td></tr></table>

# 7.2.4 图元文件描述符元素

<table><tr><td>功能</td><td>规范—ATA 简述文件</td><td>规范—模型简述文件</td></tr><tr><td>T.16.1 图元文件版本 CGM 版本: 1</td><td>必需的1、2、3对于 GREXCHANGE(图形交换)中允许的版本4的功能描述, 参见CGM 格式的相关部分。(版本4)</td><td>元素是: 必需的该简述文件允许的图元文件版本。1、2、3、4其它: 无</td></tr><tr><td>T.16.2 图元文件说明 CGM 版本: 1</td><td>元素是: 必需的注: SF 参数中的子字符串应具有格式: “关键词: 项”, 其中双引号是子字符串的一部分。</td><td>元素是: 必需的注: SF 参数中的子字符串应具有格式: “关键词: 项?”, 其中双引号是子字符串的一部分。</td></tr><tr><td>功能</td><td>规范-ATA 简述文件</td><td>规范-模型简述文件</td></tr><tr><td></td><td>不限制“简述文件 ATA 图形交换”注:在 ATA 字符串之后的简述文件 ID字符串中有一个 ASCII 空格符。参考适用于该图形的规范的认证版本和修订版本。与关键词 ProfileEd 相关的项目应是 n.m,其中 n 是规范的版本号,m 是修订版号,它们被规定注在本规范的封面或页眉中:例如:“ProfileEd:2.4”“ColourClass 是:单色”或“ColourClass 是:彩色”附加的可选信息内容:“来源:供应商”“日期:yyyymmdd”提倡多次使用该元素,以便当一个CGM 文件通过应用程序被移动时,能保存其历史记录。</td><td>该元素出现的最大次数:不限制简述文件标识(使用关键词,“ProfileID(简述文件标识):”“简述文件:模型一简述文件”简述文件版本,(使用关键字ProfileEd: )“ProfileEd:1”如果简述文件的版次没有给出,那么版次的缺省值为 1。彩色类别:(使用关键词ColourClass:)彩色、灰度或单色之一附加的必需信息内容:来源:(使用关键词 “Source:"销售商、产品和版本日期,(使用关键词 “Date:”)图元文件的生成日期。格式和内容应按照[ISO 8601:1988]的规定。其它:无</td></tr><tr><td>T.16.3 VDC 类型CGM 版本:1</td><td>同模型简述文件</td><td>元素是:允许的对参数值有限制吗?无其它:无</td></tr><tr><td>T.16.4 整数精度CGM 版本:1</td><td>允许16n/a</td><td>元素是:允许的对参数值有限制吗?二进制编码:8、16 或 32明码文本编码[-256,255],[-32767,32767],[-32768,32767],或[-2147483648,2147483647]</td></tr><tr><td></td><td>无</td><td>其它:无</td></tr><tr><td>T.16.5 实数精度CGM 版本:1</td><td>允许[1,1,16]或 [0,9,23]n/a无</td><td>元素是:允许的对参数值有限制吗?二进制编码:[1,1,16]或 [0,9,23]明码文本编码[-32767,32767,4],[-32768,32767,10],或[-3.4028235E38,3.4028235E38,8]其它:无</td></tr><tr><td>T.16.6 索引精度CGM 版本:1</td><td>允许16n/a无</td><td>元素是:允许的对参数值有限制吗?二进制编码:8、16或32明码文本编码[0,127],[-256,255],[-32767,32767],[-32768,32767],或[-2147483648],2147483647]其它:无</td></tr><tr><td>T.16.7 颜色精度CGM 版本:1</td><td>允许8或16n/a无</td><td>元素是:允许的对参数值有限制吗?二进制编码:8或16明码文本编码255或65535其它:无</td></tr><tr><td>T.16.8 颜色索引精度CGM 版本:1</td><td>允许8或16n/a无</td><td>元素是:允许的对参数值有限制吗?二进制编码:8或16明码文本编码127,255,或32767其它:无</td></tr><tr><td>T.16.9 颜色索引最大值</td><td>允许</td><td>元素是:允许的</td></tr><tr><td>CGM 版本:1</td><td>否0、1,对于单色图元文件0-255,对于彩色图元文件灰度被认为是彩色的一个特例</td><td>这个必需的元素是最小上限吗?(是/否)否对参数值有限制吗?0、1,对于单色图元文件0-63,对于灰度图元文件0-255,对于彩色图元文件其它:无</td></tr><tr><td>T.16.10 颜色值范围CGM 版本:1</td><td>同模型简述文件</td><td>元素是:允许的对参数值有限制吗?无其它:无</td></tr><tr><td>T.16.11 图元文件元素列表CGM 版本:1</td><td>同模型简述文件</td><td>元素是:必需的其它:无</td></tr><tr><td>T.16.12 图元文件默认代替值CGM 版本:1</td><td>同模型简述文件</td><td>元素是:允许的对于每次出现的MDR是否限制为只定义一个默认值?(是/否)注:关于使用MDR的简述文件规范应与其它简述文件规范相一致。例如,如果简述文件将图元文件限制为一幅单个的图片,那么简述文件要求图元文件中MDR元素就没有太大的意义了。其它:无</td></tr><tr><td>T.16.13 字体列表CGM 版本:1</td><td>允许对于包含图形文本的所有图元文件,该元素是必需的。256图元文件中引用的所有字体,包括默认字体应在字体列表元素中被指定,字体名称的组成形式应符合[ISO 9541]规则。推荐的字体列表:Times-RomanTimes-BoldTimes-ItalicTimes-BoldItalic</td><td>元素是:允许的对于包含图形文本的所有图元文件,该元素是必需的。在字体列表中的字体的最多数目:64图元文件中引用的所有字体,包括默认字体应在字体列表元素中被指定,字体名称的组成形式应符合[ISO9541]规则。推荐的字体列表:Times-RomanTimes-BoldTimes-ItalicTimes-BoldItalic</td></tr></table>

<table><tr><td>功能</td><td>规范-ATA 简述文件</td><td>规范-模型简述文件</td><td></td></tr><tr><td rowspan="10"></td><td>Helvetica</td><td>Helvetica</td><td></td></tr><tr><td>Helvetica-Bold</td><td>Helvetica-Bold</td><td></td></tr><tr><td>Helvetica-Oblique</td><td>Helvetica-Oblique</td><td></td></tr><tr><td>Helvetica-BoldOblique</td><td>Helvetica-BoldOblique</td><td></td></tr><tr><td>Courier</td><td>Courier</td><td></td></tr><tr><td>Courier-Bold</td><td>Courier-Bold</td><td></td></tr><tr><td>Courier-Oblique</td><td>Courier-Oblique</td><td></td></tr><tr><td>Courier-BoldOblique</td><td>Courier-BoldOblique</td><td></td></tr><tr><td>Symbol</td><td>Symbol</td><td></td></tr><tr><td>OCRB</td><td>注:这些字体是经过商标注册的,并且一些是有专利权和版权的。Times 和 Helvetica 是 Allied 联合公司的注册商标,他们是那些字体名称的版权所有者。与命名字体等效的规格字体可利用解释程序进行替换。如果使用其它字体,FONT PROPERTIES(字体属性)和RESTRICTED TEXT(受限文本)元素是必需的。OCRB 字体被编码到 ISO Latin1 字符集,假设字符高度为 1.0 个度量单位,那么相比较而言,其宽度则为 1.06 度量单位。OCRB 字体中的空格字符与所有其它字符的宽度相同。对于将来的新技术,除 OCRB 以外的字体都应该被考虑。</td><td>注:这些字体是经商标注册,并且一些是有专利权和版权的。Times 和 Helvetica 是 Allied 公司的注册商标,他们是那些字体名称的版权所有者。与命名字体等效的规格字体可利用解释程序进行替换。其它:无</td></tr><tr><td>T.16.14 T 字符集列表CGM 版本:1</td><td>同模型简述文件</td><td>元素是:允许的对于包含图形文本的所有图元文件,该元素是必需的。对于字符集列表中的字符集限制的最大数目:4列出被使用的字符集:4-character G-set? 4/2 (ISO 8859 -1:1987 LH)6-character G-set? 4/1 (ISO 8859 -1:1987 RH)4-character G-set? 2/10 3/10 (Symbol LH)</td><td></td></tr></table>

<table><tr><td>功能</td><td>规范-ATA 简述文件</td><td>规范-模型简述文件</td></tr><tr><td></td><td></td><td>4 - character G - set? 2/6 3/10(Symbol RH)如果这些字符集是完全编码类型,应指定完全编码的内容和该编码相关序列的后面内容:不适用其它:无</td></tr><tr><td>T.16.15 字符编码表示器CGM 版本:1</td><td>必需值应是:“基本8-bit”无</td><td>元素是:允许的对参数值有限制吗?值应是:“基本的7位”和“基本的8位”其它:无</td></tr><tr><td>T.16.16 命名精度CGM 版本:2</td><td>禁止</td><td>元素是:允许的对参数值有限制吗?二进制编码16或32明码文本编码[-256,255],[-32767,32767],[-32768,32767],或[-2147483648,2147483647]Other:none 其它:无</td></tr><tr><td>T.16.17 最大VDC 范围CGM 版本:2</td><td>同模型简述文件</td><td>元素是:允许的对参数值有限制吗?无其它:无</td></tr><tr><td>T.16.18 图段优先级范围CGM 版本:2</td><td>禁止</td><td>元素是:允许的对参数值有限制吗?无其它:无</td></tr><tr><td>T.16.19 色彩模型CGM 版本:2</td><td>允许应是1无</td><td>元素是:允许的对参数值有限制吗?无其它:无</td></tr><tr><td>T.16.20 颜色校准CGM 版本:3</td><td>禁止</td><td>元素是:允许的允许的校准选择值应按照允许的模型:1..6、9如果允许CMYK,应规定栅格区域的最小数目:3</td></tr><tr><td></td><td></td><td>对查找表的条目n(使用)的颜色数目有限制吗?无对栅格区域m的数目有限制吗?无如果允许CMYK,栅格区域之间是否有插值算法?无其它:无</td></tr><tr><td>T.16.21 字体属性CGM 版本:3</td><td>允许使用时所必需的参数有INDEX(索引)、FONT FAMILY(字体库)、POSTURE(形态)、WEIGHT(重量)、PROPORTION ATE WIDTH(ATE 宽度比例)、DESIGNGROUP(设计组)和STRUCTURE(结构)当使用一个不在被推荐字体列表中的字体时,该元素是必需的。</td><td>元素是:允许的对参数值有限制吗?应许可所有定义的索引和所有参数的列举值。其它:无</td></tr><tr><td>T.16.22 符号映射CGM 版本:3</td><td>禁止</td><td>元素是:允许的可被引用的AFII注册符号的子集:没有可被定义的符号的最大数目为:8192其它:无</td></tr><tr><td>T.16.23 符号库列表CGM 版本:3</td><td>允许对于存取机制,参见文本中的符号库的论述。参见符号库的论述。8无</td><td>元素是:禁止的可被存取的符号库以及它们的编码规则:符号库的明确命名程序。可被存取的符号库的最大数目:其它:无</td></tr><tr><td>T.16.24 图片目录CGM 版本:4</td><td>禁止</td><td>元素是:允许的其它:无</td></tr></table>

# 7.2.5 图片描述符元素

<table><tr><td>功能</td><td>规范-ATA 简述文件</td><td>规范-模型简述文件</td></tr><tr><td>T.17.1 缩放模式CGM 版本:1</td><td>必需比例缩放模型)应按度量单位计算。无</td><td>元素是:允许的对参数值有限制吗?如果 SCALING MODE 按度量单位计算,那么度量单位的比例因子应是正数。其它:无</td></tr><tr><td>T.17.2 颜色选择模式CGM 版本:1</td><td>同模型简述文件</td><td>元素是:允许的对参数值有限制吗?无其它:无</td></tr><tr><td>T.17.3 线宽规范模式CGM 版本:1</td><td>同模型简述文件</td><td>元素是:允许的对参数值有限制吗?无其它:无</td></tr><tr><td>T.17.4 标记尺寸规范模式CGM 版本:1</td><td>同模型简述文件</td><td>元素是:允许的对参数值有限制吗?无其它:无</td></tr><tr><td>T.17.5 边界宽度规范模式CGM 版本:1</td><td>同模型简述文件</td><td>元素是:允许的对参数值有限制吗?无其它:无</td></tr><tr><td>T.17.6 VDC 范围CGM 版本:1</td><td>同模型简述文件</td><td>元素是:允许的对 VDC 空间的认知和方向的限制:无允许零区域 VDC 范围吗?(是/否)否如果是,详细说明它的含义:其它:无</td></tr><tr><td>T.17.7 背景颜色CGM 版本:1</td><td>同模型简述文件</td><td>元素是:允许的其它:无</td></tr><tr><td>T.17.8 设备观察区CGM 版本:2</td><td>同模型简述文件</td><td>元素是:禁止的该元素与周围环境显示指令的相互作用:如果规定值与显示设备不一致,该元素的含义是:其它:无</td></tr><tr><td></td><td></td><td>注:由于该元素具有设备依赖性,因此该元素被禁止。</td></tr><tr><td>T.17.9 设备观察区规范模式CGM 版本:2</td><td>同模型简述文件</td><td>元素是:禁止的合法值的集合其它:无注:由于该元素具有设备依赖性,因此该元素被禁止。</td></tr><tr><td>T.17.10 设备观察区映射CGM 版本:2</td><td>同模型简述文件</td><td>元素是:禁止的合法值的集合:其它:无注:由于该元素具有设备依赖性,因此该元素被禁止。</td></tr><tr><td>T.17.11 线的表示法CGM 版本:2</td><td>禁止</td><td>元素是:允许的同时(进行线束)定义的最大数目:20其它:无</td></tr><tr><td>T.17.12 标记表示法CGM 版本:2</td><td>禁止</td><td>元素是:允许的同时(进行线束)定义的最大数目:20其它:无</td></tr><tr><td>T.17.13 文本表示法CGM 版本:2</td><td>禁止</td><td>元素是:允许的同时(进行线束)定义的最大数目:20其它:无</td></tr><tr><td>T.17.14 填充表示法CGM 版本:2</td><td>禁止</td><td>元素是:允许的同时(进行线束)定义的最大数目:20其它:无</td></tr><tr><td>T.17.15 边界表示法CGM 版本:2</td><td>禁止</td><td>元素是:允许的同时(进行线束)定义的最大数目:20其它:无</td></tr><tr><td>T.17.16 内部样式规范模式CGM 版本:3</td><td>同模型简述文件</td><td>元素是:允许的对参数值有限制吗?无其它:无</td></tr><tr><td>T.17.17 线型和边界类型定义CGM 版本:3</td><td>同模型简述文件</td><td>元素是:允许的对定义的数目有限制吗?最多同时定义32种线类型。</td></tr><tr><td></td><td></td><td>对给定定义中的元素数目有限制吗?虚线间距列表中的数值个数应不超过8。对虚线循环重复长度有限制吗?无为防止退变,对定义的复杂性有限制吗?无其它:无</td></tr><tr><td>T.17.18阴影样式定义CGM 版本:3</td><td>同模型简述文件</td><td>元素是:允许的对阴影样式的数目有限制吗?应同时定义最多32种阴影样式。对一个给定定义中的间隙个数有限制吗?间隙宽度列表的(各)条目(中)的个数将不超过8对填充区段长度有限制吗?无对用于防止简化的复杂定义有限制吗?无对样式指示方式有限制吗?无其它:无</td></tr><tr><td>T.17.19 几何图形定义CGM 版本:3</td><td>禁止</td><td>元素是:允许的对定义的几何图形的数目有限制吗?几何图形的最大数目是64.对图元的类别有限制吗?无其它:无</td></tr><tr><td>T.17.20 应用程序结构目录CGM 版本:4</td><td>禁止</td><td>元素是:允许的其它:无</td></tr></table>

# 7.2.6 控制元素

<table><tr><td>功能</td><td>规范-ATA 简述文件</td><td>规范-模型简述文件</td></tr><tr><td>T.18.1 VDC整型精度</td><td>允许</td><td>元素是:允许的</td></tr><tr><td>CGM 版本:1</td><td>16或32n/a无</td><td>对参数值有限制吗?二进制编码16或32明码文本编码[-32767,32767],[-32768,32767],或[-2147483648,2147483647]其它:无</td></tr><tr><td>T.18.2 VDC实数型精度CGM 版本:1</td><td>允许[1,16,16]或 [0,9,23]n/a无</td><td>元素是:允许的对参数值有限制吗?二进制编码[1,16,16]或[0,9,23]明码文本编码[0.,1.,4],[-32767,32767,4],[-32768,32767,10],或[-3.4028235E38,3.4028235E28,8]其它:无</td></tr><tr><td>T.18.3 辅助颜色CGM 版本:1</td><td>同模型简述文件</td><td>元素是:允许的其它:无</td></tr><tr><td>T.18.4 透明性CGM 版本:1</td><td>允许对该元素的解释程序不能依靠ISO/IEC 8632:1999中的注释内容来执行。解释程序应按照标准中元素说明的规定要求执行。</td><td>元素是:允许的其它:无</td></tr><tr><td>T.18.5 裁剪矩形CGM 版本:1</td><td>同模型简述文件</td><td>元素是:允许的边界情况?的含义是:零区域:禁止比VDC范围大的区域:应在裁剪矩形和VDC范围的相交处进行裁剪。其它情况:无其它:无</td></tr><tr><td>T.18.6 裁剪指示符CGM 版本:1</td><td>同模型简述文件</td><td>元素是:允许的对参数值有限制吗?无其它:无元素是:允许的</td></tr><tr><td>T.18.7 线裁剪模式</td><td>禁止</td><td>元素是:允许的</td></tr><tr><td>CGM 版本:2</td><td>解释程序应使用形态参数</td><td>对参数值有限制吗?无其它:无</td></tr><tr><td>T.18.8 标记载剪模式CGM 版本:2</td><td>禁止解释程序应使用形态参数</td><td>元素是:允许的对参数值有限制吗?无其它:无</td></tr><tr><td>T.18.9 边裁剪模式CGM 版本:2</td><td>禁止解释程序应使用形态参数</td><td>元素是:允许的对参数值有限制吗?无其它:无</td></tr><tr><td>T.18.10 新区域CGM 版本:2</td><td>同模型简述文件</td><td>元素是:允许的对出现的次数有限制吗?没有其它:无</td></tr><tr><td>T.18.11 保存图元上下文CGM 版本:2</td><td>禁止</td><td>元素是:允许的可同时保存上下文的最大数目是:1024其它:无</td></tr><tr><td>T.18.12 恢复图元上下文CGM 版本:2</td><td>禁止</td><td>元素是:允许的其它:无</td></tr><tr><td>T.18.13 保护区域指示符CGM 版本:3</td><td>同模型简述文件</td><td>元素是:允许的其它:无</td></tr><tr><td>T.18.14 通用的文本路径模式CGM 版本:3</td><td>同模型简述文件</td><td>元素是:允许的对参数值有限制吗?无其它:无</td></tr><tr><td>T.18.15 斜接面限制CGM 版本:3</td><td>同模型简述文件</td><td>元素是:允许的对参数值有限制吗?无其它:无</td></tr><tr><td>T.18.16 透明的单元格颜色CGM 版本:3</td><td>同模型简述文件</td><td>元素是:允许的对参数值有限制吗?无其它:无</td></tr></table>

# 7.2.7 图元元素

<table><tr><td>功能</td><td>规范-ATA 简述文件</td><td>规范-模型简述文件</td></tr><tr><td>T.19.1 多段线(折线)CGM 版本:1</td><td>同模型简述文件</td><td>元素是:允许的点或无限制形态的最大数目:4096其它:无</td></tr><tr><td>T.19.2 相交多段线CGM 版本:1</td><td>同模型简述文件</td><td>元素是:允许的点或无限制形态的最大数目:4096其它:无</td></tr><tr><td>T.19.3 多点标记CGM 版本:1</td><td>同模型简述文件</td><td>元素是:允许的点或无限制形态的最大数目:4096其它:无</td></tr><tr><td>T.19.4 文本CGM 版本:1</td><td>禁止图形化文本应由本简述文件中受限文本元素来表述。</td><td>元素是:允许的允许存在未终止标记吗?(是/否)是其它:无</td></tr><tr><td>T.19.5 受限文本CGM 版本:1</td><td>允许是是框式标记?v3 图元文件:如果使用该元素,应使用受限文本类型。对于v3 图元文件,应将受限文本类型框起来</td><td>元素是:允许的允许存在未终止标记吗?(是/否)是v1/v2 图元文件:受限文本是根据受限文本类型的一个标准或注册值实现的吗?如果是,详细说明框式标记v3 图元文件:如果使用该元素,应使用受限文本类型。其它:无</td></tr><tr><td>T.19.6 附加文本CGM 版本:1</td><td>同模型简述文件</td><td>元素是:允许的其它:无</td></tr><tr><td>T.19.7 多边形CGM 版本:1</td><td>同模型简述文件</td><td>元素是:允许的点的最大数目:4096</td></tr><tr><td></td><td></td><td>其它:无</td></tr><tr><td>T.19.8 多边形集合CGM 版本:1</td><td>同模型简述文件</td><td>元素是:允许的点的最大数目:4096在一个集合中允许的多边形数量:-无限制其它:一个集合中的每个多边形应至少有3个点。</td></tr><tr><td>T.19.9 单元格排列CGM 版本:1</td><td>允许4096409616777216否禁止排列零区域单元格</td><td>元素是:允许的nx的限制:2048ny的限制:2048nx*ny的限制:4194304允许单元格矩阵旋转和/或倾斜吗?(是/否)否如果是,详细说明(多边形旋转)图形的含义:其它:禁止排列零区域单元格</td></tr><tr><td>T.19.10 通用的绘图图元CGM 版本:1</td><td>同模型简述文件</td><td>元素是:禁止的列出允许的所有已注册的 GDP:列出所有允许的简述文件定义的GDP并附上完整的描述:其它:无</td></tr><tr><td>T.19.11 矩形CGM 版本:1</td><td>同模型简述文件</td><td>元素是:允许的其它:无</td></tr><tr><td>T.19.12 圆CGM 版本:1</td><td>同模型简述文件</td><td>元素是:允许的其它:无</td></tr><tr><td>T.19.13 圆弧3点CGM 版本:1</td><td>同模型简述文件</td><td>元素是:允许的其它:无</td></tr><tr><td>T.19.14 圆弧3点闭合CGM 版本:1</td><td>同模型简述文件</td><td>元素是:允许的其它:无</td></tr><tr><td>T.19.15 圆弧中心CGM 版本:1</td><td>同模型简述文件</td><td>元素是:允许的其它:无</td></tr><tr><td>T.19.16 圆弧中心闭合</td><td>同模型简述文件</td><td>元素是:允许的</td></tr><tr><td>CGM 版本:1</td><td></td><td>其它:无</td></tr><tr><td>T.19.17 椭圆</td><td>同模型简述文件</td><td>元素是:允许的</td></tr><tr><td>CGM 版本:1</td><td></td><td>其它:无</td></tr><tr><td>T.19.18 椭圆弧</td><td>同模型简述文件</td><td>元素是:允许的</td></tr><tr><td>CGM 版本:1</td><td></td><td>其它:无</td></tr><tr><td>T.19.19 椭圆弧闭合</td><td>同模型简述文件</td><td>元素是:允许的</td></tr><tr><td>CGM 版本:1</td><td></td><td>其它:无</td></tr><tr><td>T.19.20 圆弧中心反向?</td><td>同模型简述文件</td><td>元素是:允许的</td></tr><tr><td>CGM 版本:2</td><td></td><td>其它:无</td></tr><tr><td>T.19.21 连接边</td><td>同模型简述文件</td><td>元素是:允许的</td></tr><tr><td>CGM 版本:2</td><td></td><td>其它:无</td></tr><tr><td>T.19.22 双曲线弧</td><td>同模型简述文件</td><td>元素是:允许的</td></tr><tr><td>CGM 版本:3</td><td></td><td>其它:无</td></tr><tr><td>T.19.23 抛物线弧</td><td>同模型简述文件</td><td>元素是:允许的</td></tr><tr><td>CGM 版本:3</td><td></td><td>其它:无</td></tr><tr><td>T.19.24 非均匀B一样条</td><td>同模型简述文件</td><td>元素是:允许的</td></tr><tr><td>CGM 版本:3</td><td></td><td>样条阶次集合:三次曲线样条控制点的最大数目4096其它:无</td></tr><tr><td>T.19.25 非均匀有理B一样条</td><td>同模型简述文件</td><td>元素是:允许的</td></tr><tr><td>CGM 版本:3</td><td></td><td>样条阶次集合:三次样条控制点的最大数目4096其它:无</td></tr><tr><td>T.19.26 贝塞尔多段拟合曲线</td><td>同模型简述文件</td><td>元素是:允许的</td></tr><tr><td>CGM 版本:3</td><td></td><td>点的最大数目4096对连续性指示符有限制吗?无其它:无</td></tr><tr><td>T.19.27 多符号</td><td>允许</td><td>元素是:禁止的</td></tr><tr><td>CGM 版本:3</td><td>4096符号被忽略根据符号索引可参见符号库图元文件中相应位置处的一个图片,这与符号库部分的论述相同。</td><td>点的最大数目引用不在符号库中的一个符号索引参数的影响:其它:无注:因为禁止符号库列表,因此该元素被禁止.</td></tr><tr><td>T.19.28 双调图象块CGM 版本:3</td><td>允许2 (T6)无无</td><td>元素是:允许的列出许可的压缩类型:0..6对填充行的要求:无其它:无</td></tr><tr><td>T.19.29 图像块CGM 版本:3</td><td>允许2 (T6), 6 (运行长度), 7 (JPEG),或 9 (PNG)无.值 9 是针对 PNG 的压缩方法 0 的ISO 注册值。值 7 是针对 JPEG 压缩方法的 ISO 注册值。本简述文件可使用受 TILE(图象块)元素限制的 JPEG 压缩方法。这个方法限于基线JPEG 压缩方法。基线 JPEG 压缩方法遵循所有基于 DCT 的译码器所必需的过程。 TILE 元素的色彩选择模式应总是直接的,效果上独立于 CGM 中采用的色彩选择模式。对于基线 JPEG 压缩方法,TILE 单元格色彩精密参数应总是8 位。 TILE 元素的色彩模型应按</td><td>元素是:允许的列出许可的压缩类型:0..6对填充行的要求:无其它:无注:JPEG 的注册工作正在进行中。如果 JPEG 被注册,它将被添加到本简述文件允许的压缩类型值中。</td></tr><tr><td>功能</td><td>规范-ATA 简述文件</td><td>规范一模型简述文件</td></tr><tr><td></td><td>照 TILE 元素的特定参数方法来定义。它可能是相同的,或独立于 CGM 的色彩模型。基线 JPEG 压缩方法应假定光谱的次序与特定参数方法中定义的色彩模型所给出的次序相同。例如,如果色彩模型是 RGB ,每次扫描将先压缩红色部分,随后是绿色部分,随后是蓝色部分。对于色彩模型是 “RGB 相关” 这种情况,特定的色彩模型按照 TILE 元素的特定参数方法来定义。对于使用基线 JPEG 压缩的每幅图象,应提交方法特定参数。参数应作为一个SDR 被编码。TJPEG 色彩模型参数是必需的,并且根据索引精度元素的规则被指定。有效值是:0-JPEG 色彩模型与 CGM 的色彩模型相同1-RGB2-CIELAB3-CIELUV4-CMYK5-RGB related相关的 5-RGB0-5 范围以外的值是不允许的。JPEG 色彩子模型仅当 JPEG 色彩模型是“RGB 相关”时是必需的,并且根据索引精度元素的规则被指定。有效值是:0-YCbCr1-YCrCb2-YUV3-YIQ4-YES5-ADT不允许给出其它值。</td><td>注:JPEG 的注册工作正在进行中。如果 JPEG 被注册,它将被添加到本简述文件允许的压缩类型值中。</td></tr></table>

7.2.8 属性元素  

<table><tr><td>元素</td><td>规范-ATA 简述文件</td><td>规范-模型简述文件</td></tr><tr><td>T.20.1 线束索引CGM 版本:1</td><td>禁止</td><td>元素是:允许的。对于v1图元文件,允许的索引值:1...51:类型(1)宽度(1.0)颜色(1)2:类型(2)宽度(1.0)颜色(1)3:类型(3)宽度(1.0)颜色(1)4:类型(4)宽度(1.0)颜色(1)5:类型(5)宽度(1.0)颜色(1)对于v2/v3图元文件,任何引用的线束应有一个明确的表达定义。其它:无</td></tr><tr><td>T.20.2 线型CGM 版本:1</td><td>允许1...56...15无负值应由线和边类型定义元素指定线型6--15包括在图形对象的注册记录中。该注册记录可从ISO SC24 委员会中获得。</td><td>元素是:允许的指出下列所有限制:值:1...5注册值的子集:无简述文件定义值(附带完整说明):无v3 图元文件负值应由线和边类型定义元素指定。其它:无</td></tr><tr><td>T.20.3 线宽CGM 版本:1</td><td>同模型简述文件</td><td>元素是:允许的允许值为零吗?(是/否)是如果是,详细说明它的含义:可用的最小线宽对参数值有限制吗?无其它:无</td></tr><tr><td>T.20.4 线色CGM 版本:1</td><td>同模型简述文件</td><td>元素是:允许的对参数值有限制吗?</td></tr><tr><td></td><td></td><td>无其它:无</td></tr><tr><td>T.20.5标记束索引CGM 版本:1</td><td>禁止</td><td>元素是:允许的对于v1图元文件,允许的索引值:1...51:类型(1)大小(1.0)颜色(1)2:类型(2)大小(1.0)颜色(1)3:类型(3)大小(1.0)颜色(1)4:类型(4)大小(1.0)颜色(1)5:类型(5)大小(1.0)颜色(1)对于v2/v3图元文件,任何引用的束应有一个明确的表达定义。其它:无</td></tr><tr><td>T.20.6标记类型CGM 版本:1</td><td>同模型简述文件</td><td>元素是:允许的指出下列所有限制:值:1...5其它:无</td></tr><tr><td>T.20.7标记尺寸CGM 版本:1</td><td>同模型简述文件</td><td>元素是:允许的允许值为零吗?(是/否)是如果是,详细说明它的含义:最小可用尺寸。对参数值有限制吗?无其它:无</td></tr><tr><td>T.20.8标记颜色CGM 版本:1</td><td>同模型简述文件</td><td>元素是:允许的对参数值有限制吗?无其它:无</td></tr><tr><td>T.20.9文本束索引CGM 版本:1</td><td>禁止</td><td>元素是:允许的对于v1图元文件,允许的索引值:1...21:字体(1)精度(笔划)放大因子(1.0)间距(0.0)颜色(1)</td></tr><tr><td></td><td></td><td>2:字体(1)精度(笔划)放大因子(0.7)间距(0.0)颜色(1)对于v2/v3图元文件,任何引用的束应有一个明确的表达定义。其它:无</td></tr><tr><td>T.20.10 文本字体索引CGM 版本:1</td><td>同模型简述文件</td><td>元素是:允许的注:每个引用的字体索引应对应于字体列表中定义的一个条目其它:无</td></tr><tr><td>T.20.11 文本精度CGM 版本:1</td><td>允许值应是‘笔划’无</td><td>元素是:允许的对参数值有限制吗?无其它:无</td></tr><tr><td>T.20.12 字符放大因子CGM 版本:1</td><td>同模型简述文件</td><td>元素是:允许的允许值为零吗?(是/否)否如果是,详细说明它的含义:对参数值有限制吗?值应被限制在.1到10的范围内。其它:无</td></tr><tr><td>T.20.13 字符间距CGM 版本:1</td><td>同模型简述文件</td><td>元素是:允许的对参数值有限制吗?值应被限制为-1.0到5.0的范围。其它:无</td></tr><tr><td>T.20.14 文本颜色CGM 版本:1</td><td>同模型简述文件</td><td>元素是:允许的对参数值有限制吗?无其它:无</td></tr><tr><td>T.20.15 字符高度CGM 版本:1</td><td>同模型简述文件</td><td>元素是:允许的允许值为零吗?(是/否)是如果是,详细说明它的含义:最小可用的高度。对参数值有限制吗?无其它:无</td></tr><tr><td>T.20.16 字符方向</td><td>同模型简述文件</td><td>元素是:允许的</td></tr><tr><td>CGM 版本:1</td><td></td><td>对下列变形方式有限制吗?旋转:无倾斜无镜像:无纵横比:无其它:无</td></tr><tr><td>T.20.17 文本路径CGM 版本:1</td><td>同模型简述文件</td><td>元素是:允许的对参数值有限制吗?无其它:无</td></tr><tr><td>T.20.18 T 文本对齐CGM 版本:1</td><td>同模型简述文件</td><td>元素是:允许的对水平和垂直对齐值有限制吗?无对连续的水平和垂直对齐值有限制吗?无其它:无</td></tr><tr><td>T.20.19 字符集索引CGM 版本:1</td><td>允许注:每个引用的索引应对应字符集列表中定义的一个条目。这包括对默认索引值的隐含引用。无</td><td>元素是:允许的注:每个引用的索引应对应字符集列表或字形映像中定义的一个条目。这包括对默认索引值的隐含引用。其它:无</td></tr><tr><td>T.20.20 备用字符集索引CGM 版本:1</td><td>允许注:每个引用的索引应对应字符集列表或字形映像中定义的一个条目。这包括对默认索引值的隐含引用。无</td><td>元素是:允许的注:每个引用的索引应对应字符集列表或字形映像中定义的一个条目。这包括对默认索引值的隐含引用。其它:无</td></tr><tr><td>T.20.21 填充束索引CGM 版本:1</td><td>禁止</td><td>元素是:允许的对于v1图元文件,允许的索引值:1...51:样式(阴影线)颜色(1)阴影线(1)图形(1)</td></tr><tr><td></td><td></td><td>2:样式(阴影线)颜色(1)阴影线(2)图形(1)3:样式(阴影线)颜色(1)阴影线(3)图形(1)4:样式(阴影线)颜色(1)阴影线(4)图形(1)5:样式(阴影线)颜色(1)阴影线(5)图形(1)对于v2/v3图元文件,任何引用的束应有一个明确的表达定义。其它:无</td></tr><tr><td>T.20.22 内部样式CGM 版本:1</td><td>同模型简述文件</td><td>元素是:允许的对于下列内部样式,边界线的线型和宽度:实线类型和默认线宽对参数值有限制吗?无其它:无</td></tr><tr><td>T.20.23 填充颜色CGM 版本:1</td><td>同模型简述文件</td><td>元素是:允许的对参数值有限制吗?无其它:无</td></tr><tr><td>T.20.24 阴影线索引CGM 版本:1</td><td>同模型简述文件</td><td>元素是:允许的指出下列所有限制:值:1...6v3图元文件负值应由阴影线样式定义元素来赋值其它:无</td></tr><tr><td>T.20.25 图案索引CGM 版本:1</td><td>同模型简述文件</td><td>元素是:允许的对参数值有限制吗?无其它:无</td></tr><tr><td>T.20.26 边线束索引CGM 版本:1</td><td>禁止</td><td>元素是:允许的对于v1图元文件,允许的索引值:1...51:类型(1)宽度(1.0)颜色(1).</td></tr><tr><td></td><td></td><td>2:类型(2)宽度(1.0)颜色(1)3:类型(3)宽度(1.0)颜色(1)4:类型(4)宽度(1.0)颜色(1)5:类型(5)宽度(1.0)颜色(1)对于v2/v3图元文件,任何引用的束应有一个明确的表达定义。其它:无</td></tr><tr><td>T.20.27 边类型CGM 版本:1</td><td>同模型简述文件</td><td>元素是:允许的指出下列所有限制:值:1...5v3 图元文件:负值应由线和边类型定义元素来赋值其它:无</td></tr><tr><td>T.20.28 边宽CGM 版本:1</td><td>同模型简述文件</td><td>元素是:允许的允许值为零吗?(是/否)是如果是,详细说明它的含义:可用的最小宽度。对参数值有限制吗?无其它:无</td></tr><tr><td>T.20.29 边颜色CGM 版本:1</td><td>同模型简述文件</td><td>元素是:允许的对参数值有限制吗?无其它:无</td></tr><tr><td>T.20.30 边可见性CGM 版本:1</td><td>同模型简述文件</td><td>元素是:允许的对参数值有限制吗?无其它:无</td></tr><tr><td>T.20.31 填充引用点CGM 版本:1</td><td>同模型简述文件</td><td>元素是:允许的对参数值有限制吗?无其它:无</td></tr><tr><td>T.20.32 图案表CGM 版本:1</td><td>同模型简述文件</td><td>元素是:允许的nx的最大尺寸32nx的允许尺寸:</td></tr><tr><td></td><td></td><td>8、16、或32nx的允许尺寸:32ny的允许尺寸:8、16、或32对图案定义的数目有限制吗?64对允许的nx和ny组合有限制吗?无对颜色数目有限制吗?没有其它:无</td></tr><tr><td>T.20.33 图案尺寸CGM 版本:1</td><td>同模型简述文件</td><td>元素是:允许的图案向量应平行于坐标轴吗?(是/否)否如果否,说明倾斜或非对齐的图案的含义。其它:无</td></tr><tr><td>T.20.34 颜色表CGM 版本:1</td><td>禁止单色:2彩色:256索引值不应超过颜色索引最大值。灰度图元文件被认为是彩色图元文件的特例。</td><td>元素是:允许的对颜色列表的长度有限制吗?单色:2灰度:64彩色:256对索引值有限制吗?索引值不应超过颜色索引最大值。其它:无</td></tr><tr><td>T.20.35 信号方式标记CGM 版本:1</td><td>禁止</td><td>元素是:允许的对于下述项目,所有ASF值都相同吗:图元文件?(是/否)否每个类别(展开、标记、文本填充、边)或图元?(是/否)是其它:无</td></tr><tr><td>T.20.36 选取标识符 CGM 版本:2</td><td>禁止</td><td>元素是:允许的对参数值有限制吗?无其它:无</td></tr><tr><td>T.20.37 线端 CGM 版本:3</td><td>允许1...41...3None 无</td><td>元素是:允许的对线端指示符的值集合有限制吗?1...5对虚线端指示符的值集合有限制吗?1...3其它:无</td></tr><tr><td>T.20.38 线的连接 CGM 版本:3</td><td>同模型简述文件</td><td>元素是:允许的对数值集合有限制吗?1...4其它:无</td></tr><tr><td>T.20.39 线型扩充 CGM 版本:3</td><td>同模型简述文件</td><td>元素是:允许的对数值集合有限制吗?1...4其它:无</td></tr><tr><td>T.20.40 线型初始偏移 CGM 版本:3</td><td>同模型简述文件</td><td>元素是:允许的对参数值有限制吗?无其它:无</td></tr><tr><td>T.20.41 文本划线类型 CGM 版本:3</td><td>同模型简述文件</td><td>元素是:允许的对参数值有限制吗?1...4其它:无</td></tr><tr><td>T.20.42受限文本类型 CGM 版本:3</td><td>允许2无规定在 v3 文件中,应使用该元素</td><td>元素是:允许的对参数值有限制吗?1...6实现限制类型的算法(附带):无规定其它:无</td></tr><tr><td>T.20.43 内部插值 CGM 版本:3</td><td>同模型简述文件</td><td>元素是:允许的对插值区段数目有限制吗?</td></tr><tr><td></td><td></td><td>区段的最大数目是8 对数值集合有限制吗? 1...3 其它:无</td></tr><tr><td>T.20.44 边的端点 CGM 版本:3</td><td>同模型简述文件</td><td>元素是:允许的 对数值集合有限制吗? 1...5 对虚线端点指示符的数值集合有限制吗? 1...3 其它:无</td></tr><tr><td>T.20.45 边的连接 CGM 版本:3</td><td>同模型简述文件</td><td>元素是:允许的 对数值集合有限制吗? 1...4 其它:无</td></tr><tr><td>T.20.46 边类型扩充 CGM 版本:3</td><td>同模型简述文件</td><td>元素是:允许的 对数值集合有限制吗?</td></tr><tr><td></td><td></td><td>1...4 其它:无</td></tr><tr><td>T.20.47 边类型初始偏移 CGM 版本:3</td><td>同模型简述文件</td><td>元素是:允许的 对参数值有限制吗? 无 其它:无</td></tr><tr><td>T.20.48 符号库索引 CGM 版本:3</td><td>允许 参考符号库的论述</td><td>元素是:禁止的 其它:无 注:因为禁止符号库列表,因此该元素被禁止。</td></tr><tr><td>T.20.49 符号颜色 CGM 版本:3</td><td>允许 无 无</td><td>元素是:禁止的 对参数值有限制吗? 其它 注:因为禁止符号库列表,因此该元素被禁止。</td></tr><tr><td>T.20.50 符号尺寸 CGM 版本:3</td><td>允许 是</td><td>元素是:禁止的 允许值为零吗?(是/否) 如果是,详细说明它的意思:</td></tr><tr><td></td><td>最小可用尺寸无无</td><td>对参数值有限制吗?其它: 无注: 因为禁止符号库列表,因此该元素被禁止。</td></tr><tr><td>T.20.51 符号方向 CGM 版本:3</td><td>允许无无无无无</td><td>元素是: 禁止的对旋转有限制吗?对倾斜有限制吗?对镜像有限制吗?对纵横比失真有限制吗?其它: 无注: 因为禁止符号库列表,因此该元素被禁止。</td></tr></table>

# 7.2.9 ESCAPE元素

<table><tr><td>元素</td><td>规范-ATA 简述文件</td><td>规范-模型简述文件</td></tr><tr><td>T.21.1 换码 CGM 版本: 1</td><td>允许 ESCAPE 22, 透明彩色单元格: 只用于 v1 和 v2 图元文件。 ESCAPE 45: α 透明度。SDR 参数被编码为 0.0 和 1.0 之间的一个实数值, 且适用于所有后续的图元。 ESCAPE 46: 符号背景透明度。SDR 参数被编码为一个整数值 0 (透明) 或 1 (不透明), 且控制一个符号的背景是否透明。这个换码用于图元文件中, 且引用了实例符号的处理。默认值是 0。</td><td>元素是: 允许的 列出所有允许的已注册 ESCAPE 元素: ESCAPE 22, 透明彩色单元格: 只用于 v1 和 v2 图元文件。</td></tr><tr><td></td><td>ESCAPE 47: 符号引用点。该点作为符号图元文件中的符号图片在 VDC 空间中的 X 和 Y 值。如果指定了该引用点, 则 ESCAPE 元素应出现在定义符号的符号库图片的图片描述符区域内。</td><td></td></tr><tr><td></td><td>ESCAPE 48: 设计高度和宽度。高度和宽度在符号空间的 VDC 单元中被指定。如果指定了设计参数,则 ESCAPE 元素应出现在定义符号的符号库图片的图片描述符区域内。值-4000 用来定义图层。图层定义应数值化,最大值应限制为 256。对于图层内容的含义没有定义,对于图片的正确显示而言,该 ESCAPE 的解释不是必需的。ESCAPE 元素参数应作为一个 SDR 被编码.</td><td>列出所有允许的简述文件所定义的 ESCAPE,并附带其完整描述:无。其它:无</td></tr></table>

# 7.2.10 外部元素

<table><tr><td>元素</td><td>规范-ATA 简述文件</td><td>规范-模型简述文件</td></tr><tr><td>T.22.1 消息CGM 版本: 1</td><td>禁止</td><td>元素是: 允许的‘操作必需标记’参数值。操作标记应被设置为 ‘无操作’对消息字符串长度有限制吗?无其它: 无</td></tr><tr><td>T.22.2 应用程序数据CGM 版本: 1</td><td>禁止</td><td>元素是: 允许的对于所有与本简述文件相关的应用程序数据元素, 附带一个语法和语义说明:无其它: 无</td></tr></table>

# 7.2.11 图段元素

<table><tr><td>元素</td><td>规范—ATA 简述文件</td><td>规范—模型简述文件</td></tr><tr><td>T.23.1 拷贝图段 CGM 版本: 2</td><td>禁止</td><td>元素是: 允许的 对图段转换应用程序值有限制吗? 无 对转换性质有限制吗(如只允许各向同性的转换)? 非奇异 其它: 无</td></tr><tr><td>T.23.2 继承性过滤</td><td>禁止</td><td>元素是: 允许的</td></tr><tr><td>元素</td><td>规范-ATA 简述文件</td><td>规范-模型简述文件</td></tr><tr><td>CGM 版本:2</td><td></td><td>对过滤选择列表有限制吗?无对选择设置有限制吗?无其它:无</td></tr><tr><td>T.23.3 裁剪继承CGM 版本:2</td><td>禁止</td><td>元素是:允许的对参数值有限制吗?无其它:无</td></tr><tr><td>T.23.4 图段转换CGM 版本:2</td><td>禁止</td><td>元素是:允许的对转换性质有限制吗?非奇异其它:无</td></tr><tr><td>T.23.5 图段增亮CGM 版本:2</td><td>禁止</td><td>元素是:允许的对参数值有限制吗?无其它:无</td></tr><tr><td>T.23.6 图段显示优先权CGM 版本:2</td><td>禁止</td><td>元素是:允许的对参数值有限制吗?无其它:无</td></tr><tr><td>T.23.7 图段选取优先权CGM 版本:2</td><td>禁止</td><td>元素是:允许的对参数值有限制吗?无其它:无</td></tr></table>

7.2.12 应用结构描述符元素  

<table><tr><td>元素</td><td>规范—ATA 简述文件</td><td>规范—模型简述文件</td></tr><tr><td>T.24.1 应用程序结构属性 CGM 版本: 4</td><td>禁止 对于GREXCHANGE(图形交换)中允许的版本 4 功能描述, 参见 CGM 格式(版本 4)处理部分</td><td>元素是: 允许的 为了在应用程序结构内部使用,应定义结构属性元素的集合,并附带完整的语法和语义说明。 无 其它: 无</td></tr></table>

7.2.13 生成程序执行要求  

<table><tr><td>元素</td><td>规范-ATA 简述文件</td><td>规范-模型简述文件</td></tr><tr><td>T.25.1 颜色要求</td><td>同模型简述文件</td><td>颜色映像是:允许的颜色的种类是否会减少?无说明注:如果必须将应用程序的颜色映射到图元文件颜色规范,那么推荐映像中的颜色距离应使用 CIEXYZ空间中的欧几里得几何度量单位来计算。映射算法、度量单位和颜色空间的定义?没有定义特定的颜色映射技术或选择图元文件颜色集合。对于v1/v2图元文件,具有隐含的颜色校准规范吗?没有定义规范</td></tr><tr><td>T.25.2 几何精度和范围</td><td>同模型简述文件</td><td>将应用程序图形映射到 CGM 图形元素的精度和范围。生成程序应生成一个图元文件,它的图元素与应用程序图元的匹配精度应为 VDC 范围框中的相对位置的±0.1%之内,或是期望(误差)尺寸的±0.5象素,无论哪一个更大一些。生成程序生成基本元素的几何尺寸(例如:文本尺寸、线宽、边宽),精度应在期望尺寸±1%范围以内,或在期望尺寸±0.5象素范围内。</td></tr><tr><td>T.25.3 文本精度和范围</td><td>同模型简述文件</td><td>文本精度和范围可寻址吗?(是/或否)是如果是,详细说明对于每个文本字符串的布局和范围而言,图元文件文本规范应符合应用程序图像的文本,精度应在预计尺寸±1%范围以内,或在预计尺寸±0.5象素范围以内,无论哪一个更大。</td></tr><tr><td>T.25.4 字体替换</td><td>允许替换的字体应在规格上相当,或被受限文本元素所控制。图形声明文件的记录7</td><td>字体替换是:允许的字体视觉特征的相似性?替换的字体应有相似的视觉特征(例如形态、粗细度、成比例的宽度)。字体规格ISO/IEC 8632:1992 Amd.1:1994附件H中的规定。</td></tr><tr><td></td><td>[ISO/IEC 8632:1999 附件 I]中对于13种核心字体的规定，以及字体列表的说明中对于OCRB 的规定。无</td><td>单个字型的规格[ISO/IEC 8632:1999 附件 I]中的规定其它：无</td></tr><tr><td>T.25.5 图元保存</td><td>同模型简述文件</td><td>图元元素的保存可寻址吗?(是/否)否如果是，说明许可的替换法。</td></tr><tr><td>T.25.6 语义范围</td><td>优先级应与图元文件次序一致(即在文件中较后出现的图元应覆盖文件中较早出现的图元)。模式应是“替换”模式。裁剪应在裁剪矩形、VDC 范围、设备观察区和设备视图界面限定的交集中进行。边应在按理论数学定义的区域边界居中。该简述文件既支持普通的但不精确的线型，也支持特殊的精确的线型。线型1...5 的实现方法在CGM 标准的通用术语中描述。(例如"双点划线")，已注册线型6...15 的实现方法和约束条件在ISO 图形项目注册文件中说明。(例如在某个工程线型中对于墨线顶点的要求)。另外，对于隐含线型1...15 的确切线模型没有进行约束。在期望和需要准确体现线型的地方，应使用线和边类型定义元素。</td><td>绘图的优先级和模式优先级应与图元文件次序一致(即在文件中较后出现的图元应覆盖文件中较早出现的图元)。模式应是“替换”模式。裁剪裁剪应在裁剪矩形、VDC 范围、设备观察区和设备视图界面限定的交集中进行。边中心边应在按理论数学定义的区域边界居中。预定义的线类型和边类型的含义:对于预定义线类型和边类型的确切的允许/禁止定义，无规定。预定义的阴影线型的含义:</td></tr><tr><td>元素</td><td>规范-ATA 简述文件</td><td>规范一模型简述文件</td></tr><tr><td></td><td>该简述文件既支持普通的但不精确的阴影线型,也支持特殊的精确的阴影线型。阴影线型 1...6 的实现方法在 CGM标准的通用术语中进行了描述。))另外,对于隐含阴影线型 1...6 的确切线模型没有进行约束。在期望和需要准确体现线型的地方,应使用阴影线型定义元素。无</td><td>未规定内部线距。对于角方向,使用[ISO/IEC 8632:1999 附件 D]的相关条款。其它:无</td></tr><tr><td>T.25.7 误差处理</td><td>同模型简述文件</td><td>误差处理可被寻址吗?(是/否)否如果是,说明采取的操作:误差严重性的等级?对误差恢复的要求?对误差报告的要求?其它方面?其它:无</td></tr><tr><td>T.25.8 报告</td><td>同模型简述文件</td><td>需要报告吗?(是/否)否如果是,说明采取的操作:报告的方法和格式?对于报告的替换、误差、撤销行为、映射或其它行为的要求?其它方面?其它:无</td></tr><tr><td>T.25.9 简化</td><td>同模型简述文件</td><td>简化图元的生成可被寻址吗?(是/否)否如果是,附带详细说明其它:无</td></tr></table>

7.2.14 解释程序执行要求  

<table><tr><td>元素</td><td>规范-ATA 简述文件</td><td>规范-模型简述文件</td></tr><tr><td>T.26.1 图片数量</td><td>同模型简述文件</td><td>如果允许0幅图片一解释程序执行动作:禁止</td></tr><tr><td>T.26.2 空图片</td><td>同模型简述文件</td><td>如果允许一解释程序执行动作</td></tr><tr><td></td><td></td><td>图形效果应是在背景色上的一幅图片。</td></tr><tr><td>T.26.3 颜色要求</td><td>同模型简述文件</td><td>解释程序应是单色、灰度或全彩色的解释程序的其中之一,这由解释程序的颜色性能而决定,并应符合ISO/IEC 8632:1999.附件26.3中定义的标准。不同色彩模型之间的转换应依据 ISO/IEC8632:1999 附件G .中规定的转换方法。图元文件的颜色映射到设备组件吗?如果 RGB 图元文件映射(成为较少颜色、灰度或单色)是必需的,宜采用 ISO/IEC8632:1999 附件D 规定的方法。对于v1/v2 图元文件一存在隐含的颜色校准规范?无已定义的规范。其它:无</td></tr><tr><td>T.26.4 几何精度和范围</td><td>同模型简述文件</td><td>在描绘几何图元时,其布局和几何样式实现的精度和范围。解释程序应精确地描绘图元元素,精度在VDC 范围框中的相对位置±0.1%的范围内,或在输出设备分辨率±0.5 象素的范围内,无论哪一个更大。解释程序应描绘图元的几何尺寸的样式(例如文本尺寸、线宽、边宽),精度应在期望误差尺寸±1%以内,或在输出设备分辨率±0.5 象素的范围内,无论哪一个更大。该要求应适用于所有图元元素,除非被该项目中的特定元素要求所代替。</td></tr><tr><td>T.26.5 文本描绘</td><td>同模型简述文件</td><td>文本的精度和范围是否可寻址?(是/否)是如果是,详细说明对于每个文本字符串的布局和范围而言,描绘文本的解释程序应符合图元文件的文本规范,其精度应在相应预定尺寸±0.1%的范围内,或输出设备分辨率±0.5 象素的范围内,无论哪一个更大。文本描绘的精度是否可寻址?(是/否)是如果是,说明解释程序操作动作:解释程序应使用‘笔划’精度描绘文本,而不管图元文件的文本精度的实际值。</td></tr><tr><td>T.26.6 字体替换</td><td>允许</td><td>字体替换是:允许的</td></tr><tr><td></td><td>见字体列表元素和 ISO/IEC 8632:1999 附件 I。替代方法、范围和约束条件是否可寻址:(是/否)是如果是:详细说明字体视觉特征具有相似性?被替换的字体应与图元文件中规定的字体有相似的视觉特征。字体规格被替换的字体应与图元文件中规定的字体有相似的规格。具有单个的字形规格?对于核心 13 种字体的规定以及字体列表的说明中对于 OCRB 的规定,参见[ISO/IEC 8632:1999 附件 I]。其它方面?无无</td><td>若允许,包括一个字体引用和字形规格,这与替换字体的典型实例相一致。见字体列表元素和 ISO/IEC 8632:1999 附件 I。替代方法、范围和约束条件是否可寻址:(是/否)是如果是:详细说明字体视觉特征具有相似性?被替换的字体应与图元文件中规定的字体有相似的视觉特征。字体规格被替换的字体应与图元文件中规定的字体有相似的规格。具有单个的字形规格?按照[ISO/IEC 8632:1999 附件 I]中的规定。其它方面?无其它:无</td></tr><tr><td>T.26.7 语义的范围</td><td>优先级应与图元文件次序一致(即在文件中较后出现的图元应覆盖文件中较早出现的图元)。模式应是“替换”模式。界面将在 BEGIN PICTURE BODY(图片主体开始)出现时被刷新。当 CLIP INDICATOR (裁剪指示符)为“off(关)”时,裁剪应在设备观察区和设备浏览界面限定的交集中进行。当 CLIP INDICATOR 为“on(开)”时,裁剪应在裁剪矩形、VDC 范围、设备观察区和设备浏览界面限定的范围进行。</td><td>绘图的优先级和模式:优先级应与图元文件次序一致(即在文件中较后出现的图元应覆盖文件中较早出现的图元)。模式应是“替换”模式。在图片开始时刷新视图界面。界面将在 BEGIN PICTURE BODY(图片主体开始)出现时被刷新。裁剪当 CLIP INDICATOR (裁剪指示符)为“off(关)”时,裁剪应在设备观察区和设备浏览界面限定的交集中进行。当 CLIP INDICATOR 为“on(开)”时,裁剪应在裁剪矩形、VDC 范围、设备观察区和设备浏览界面限定的范围进行。</td></tr><tr><td></td><td>边应在按理论数学定义的边区域中居中。未规定预定义线类型和边类型的确切的允许/禁止定义。未规定内部线距。对于角方向,使用[ISO/IEC 8632:1999 附件D]的相关部分。以 SHAPE(形状)参数值的样式。值=2以来自 LINE CAP(线端)元素的标准集合和注册值中(除值1外)的任何一对参数值的样式。来自 EDGE CAP(边线端)元素的标准集合和注册值(除值1外)的任何一对参数值的样式。以来自 LINE JOIN(线连接)元素的标准集合和注册值(除值1外)的任何参数值的样式以及自 EDGE JOIN(边连接)元素的标准集合和注册值(除值1外)的任何参数值的样式。</td><td>边中心边应在按理论数学定义的边区域中居中。预定义的线类型和边类型的含义:未规定预定义线类型和边类型的确切的允许/禁止定义。预定义的阴影线型的含义:未规定内部线距。对于角方向,使用[ISO/IEC 8632:1999 附件D]的相关部分。在没有线/文本/裁剪模式标记元素的情况下,解释程序处理线/标记/文本裁剪模式。以特定参数值的任何样式,来自标准值集合。对于v1/v2图元文件,受限文本元素的文本限制方法,选自受限文本类型元素的标准集合和注册样式。值=2对于v1/v2图元文件,解释程序处理线端的两种样式:以来自 LINE CAP(线端)元素的标准集合和注册值中(除值1外)的任何一对参数值的样式。对于v1/v2图元文件,解释程序处理边线端的两种样式:来自EDGE CAP(边线端)元素的标准集合和注册值(除值1外)的任何一对参数值的样式。对于v1/v2图元文件,解释程序处理线连接:以来自LINE JOIN(线连接)元素的标准集合和注册值(除值1外)的任何参数值的样式。对于v1/v2图元文件,解释程序处理边连接:以及自EDGE JOIN(边连接)元素的标准集合和注册值(除值1外)的任何参数值的样式</td></tr><tr><td></td><td>以 来 自 LINE TYPE CONTINUATION(线型扩充)元素的标准集合和注册值(除值1外)的任何参数值的样式。以来 自 EDGE TYPE CONTINUATION(边线型扩充)元素的标准集合和注册值(除值1外)的任何参数值的样式。无</td><td>对于v1/v2图元文件,解释程序处理线型连续:以来自INE TYPE CONTINUATION(线型扩充)元素的标准集合和注册值(除值1外)的任何参数值的样式。对于v1/v2图元文件,解释程序处理连续边型:以来自EDGE TYPE CONTINUATION(边线型扩充)元素的标准集合和注册值(除值1外)的任何参数值的样式。其它:无</td></tr><tr><td>T.26.8 误差处理</td><td>同模型简述文件</td><td>误差处理可被寻址吗?(是/否)否如果是,说明采取的操作:误差严重性的分级?对误差恢复的要求?对误差报告的要求?其它方面?其它:无</td></tr><tr><td>T.26.9 报告</td><td>同模型简述文件</td><td>需要报告吗?(是/否)否如果是,说明采取的操作:报告的方法和格式?对于报告的替换、误差、撤销行为、映射或其它行为的要求?其它方面?其它:无</td></tr><tr><td>T.26.10 简化</td><td>同模型简述文件</td><td>生成的简化图元可被寻址吗?(是/否)是如果是,对于每个图元,规定简化度及其来源(即固有的或计算的):固有的简化图元应按[ISO/IEC 8632:1999附录D]中的规定来描绘。解释程序不必检测计算的简化度。如果解释程序检测了计算的简化度,则它们应按[ISO/IEC 8632:1999附录D]中的规定来描述。</td></tr><tr><td></td><td></td><td>其它:无</td></tr><tr><td>T.26.11 透明性</td><td>同模型简述文件</td><td>如果透明性被允许,应详细说明解释程序应执行的动作:解释程序应按照[ISO/IEC 8632:1999] 7.5.4说明部分的第2和第3段所述,执行AUXILIARY COLOUR(辅助颜色)和TRANSPARENCY(透明性)元素。</td></tr><tr><td>T.26.12 应用程序结构的解释</td><td>不适用于版本1、2、3的格式对于 GREXCHANGE(图形交换)中允许的版本4功能的描述,参见CGM格式(版本4)的处理部分。</td><td>对应用程序结构的解释有何要求?解释程序应生成正确的图形结果。应用程序含义与应用程序结构相关吗?否如果是,详细说明解释程序的操作或对于每个结构类型的操作。其它:无</td></tr></table>

# 7.3 CGM格式(版本4)

对照[ISO/IEC 8632:1999]中定义的 ISO 模型简述文件，以下格式对包含版本 4 元素的 CGM 文件的 ATA 应用程序简述文件进行了定义。这里只列出了那些与版本 1、2 和 3 格式不同的元素和要求。格式表中的编号方式与 ISO CGM 标准中的编号方式相同。ISO 模型简述文件的规范作为引用文件被提交，并应当是准确的。（两个文件）如果存在差异，应首先选用 [ISO/IEC 8632:1999] 中的模型简述文件。该格式的目的就是当该规范进行修订时能保持向上的兼容性。

这些简述文件都由GREXCHANGE(图形交换)用适当的版本号来标识。一个包含METAFILE VERSION(图元文件版本)元素值4的CGM文件应符合本格式包含的规则。

# 7.3.1 图元文件规则

版本1、2和3的格式无变化。

# 7.3.2 多元素规则

版本1、2和3的格式无变化

# 7.3.3 分隔符元素

<table><tr><td>元素</td><td>规范-ATA 简述文件</td><td>规范-模型简述文件</td></tr><tr><td>T.15.9 应用程序结构开始应用程序结构主体开始应用程序结构结束</td><td>允许无无</td><td>元素是: 允许的一个图片中所定义结构的最大数目限制:无对组成一个结构的元素的数目和等同性的限制:无</td></tr><tr><td>元素</td><td>规范—ATA 简述文件</td><td>规范一模型简述文件</td></tr><tr><td></td><td>除了为应用程序结构分配一个唯一标识符外,没有其它含义。是的,继承标记参数的值被限制为与“状态列表”相应的值。应用程序结构类型参数被限制为一个值为“grobject”的字符串。</td><td>如果应用程序结构标识符参数被分配了一定的实际应用意义,那么,说明其含义:除了为应用程序结构分配一个唯一标识符外,没有其它含义。存在关于继承标记参数的限制吗?没有其它:无</td></tr></table>

# 7.3.4 图元文件描述符元素

<table><tr><td>元素</td><td>规范-ATA 简述文件</td><td>规范-模型简述文件</td></tr><tr><td>T.16.1 图元文件版本 CGM 版本 1</td><td>必需 4 V4 元素的识别不是必需的,但解释程序应能忽略它们,并且生成正确的图形图像。</td><td>元素是:必需的 该简述文件允许的图元文件版本。 1、2、3、4 其它:无</td></tr></table>

# 7.3.5 图片描述符元素

版本1、2和3的格式无变化。

# 7.3.6 控制元素

版本1、2和3的格式无变化。

# 7.3.7 图元元素

版本1、2和3的格式无变化。

# 7.3.8 属性元素

版本1、2和3的格式无变化。

# 7.3.9 ESCAPE元素

版本1、2和3的格式无变化。

# 7.3.10 外部元素

版本1、2和3的格式无变化。

# 7.3.11 图段元素

版本1、2和3的格式无变化。

# 7.3.12 应用结构描述符元素

<table><tr><td>元素</td><td>规范-ATA 简述文件</td><td>规范-模型简述文件</td></tr><tr><td>T.24.1 应用程序结构属性CGM 版本: 4</td><td>允许</td><td>元素是: 允许的在应用程序结构内部使用时,应定义结构属性元素的集合,并附带完整的语法和语义说明。</td></tr><tr><td></td><td>应用程序结构属性类型参数被限制为以下字符串值:“name(名称)”、“region(区域)”、“refloc(参考位置)”、“viewcontext(浏览上下文)”、“screentip(屏幕提示)”和“content(内容)”。名称属性的含义是将一个通用的名称和一个类型为“grobjec”的应用程序结构联系起来。名称属性值是一个与对象联系的标识符(不必唯一)。对于一个在应用程序中的名称属性,这里没有给出更多的关于其如何使用的语义说明。该属性在APS内最多可出现一次。定义数据记录参数的SDR由一个固定字段的字符串组成。区域属性的含义是将一个区域和一个类型为“grobjec”的应用程序结构联系起来。“区域”APS 属性在APS 内最多可出现一次,但是由简单区域的集合所组成的复杂区域,可以通过允许定义不相交的子区域、中空的区域等方法来建立。它们的语义(子区域和内部/外部定义)与CGM的CLOSED FIGURE(闭合图形)元素的那些语义相同。定义数据记录参数的SDR 由定义一个索引和一个点列表的一对或多对的参数组成。点列表对应于等价 CGM 元素的参数数据。定义了四个索引:矩形:索引=1,点列表=2点椭圆:索引=2,点列表=3点多边形:索引=3,点列表=n点连续多贝塞尔曲线:索引=4,点列表(基于连续指示符2)=3n+1点。对于分段贝塞尔曲线,如果闭合不是显式的,那么区域将隐含为封闭。refloc 属性的含义规定了与另一对象(图形或文本)相关的一个ID。目的是通过由该属性指定的对象ID 导航到该对象。在一个单独APS 内可以包含多重 refloc 属性。定义数据记录的SDR由一个固定类型字符串的成员组成。viewcontext 属性的含义是,当将浏览器直接导航到包含该属性的图形对象时,该属性为使用浏览器开始浏览一个对象提供了详细说明。另外,viewcontext 属性可以包含在一个空APS 内,在此情况下,APS 只提供一个观察区的说明。该属性在一个APS 内至多可出现一次。定义数据记录的SDR 由一个定义矩形的两个对角顶点的VDC 类型的成员组成</td><td>None无</td></tr><tr><td></td><td>screentip 属性的含义是，提供了一个与图形对象相关的可选字符串，当图形光标经过图形对象时，浏览器可显示该字符串。(该属性)在任何特定的 APS 内至多可出现一次。定义数据记录的 SDR 由一个固定类型字符串的成员组成。
content 属性的含义是，对可查找的 APS 的文本内容，提供了一种相关的方法(以进行查找)。该属性只能出现在一个 APS 中。定义数据记录参数的 SDR 由一个固定字段的字符串组成。</td><td>其它:无</td></tr></table>

# 7.3.13 生成程序执行要求

对于版本1、2和3的格式无变化

# 7.3.14 解释程序执行要求

<table><tr><td>元素</td><td>规范-ATA 简述文件</td><td>规范-模型简述文件</td></tr><tr><td>T.26.12 应用程序结构的解释</td><td>解释程序应生成正确的图形结果是针对与 grobject(图形对象) 应用程序结构相关的下列属性, 定义了解释程序行为:</td><td>对应用程序结构的解释有要求吗?解释程序应生成正确的图形结果应用程序结构具有相关的实际意义吗?否如果是, 说明解释程序的执行动作或每个结构类型的执行动作。</td></tr><tr><td></td><td>name(名称): 名称属性给出了应用程序的一种将对象和通用名称联系起来的方法。该对象可通过名称属性值进行寻址。Region(区域): 若不出现 region 属性, 那么由APS 的应用程序结构主体中的图元范围定义一个隐含的区域。region 属性是为了在应用程序进行选取而使用的。当嵌套 APS 的结果为多重区域时, 选取优先权属于最低级嵌套的 APS 所包含的区域。当重叠区域不是由嵌套 APS 产生时,选取优先权属于最近出现的 APS 所包含区域。浏览器应为用户给出一个视觉反馈信息, 已完成一次成功的挑选, 并指示特定对象 (或区域)已被选取。</td><td></td></tr><tr><td></td><td>refloc: 如果有一个 refloc 属性与一个 APS 相关联,那么浏览器应导航到被标识的应用程序结构,以证明其行为可通过目标应用程序结构的 viewcontext 属性来指示。当目标不是一个应用程序结构时,浏览器应与所指出的用于显示的过程相通信。如果有多个 refloc 属性与一个 APS 相关联,浏览器应给用户提供导航选项以供选择,并列出上述行为。viewcontext: 如果导航目标对象包含一个 view context(浏览上下文)属性,浏览器应使浏览内容“置于” 浏览器的显示矩形框中,并在这个矩形框内建立一个新的显示画面。如果对象没有包含 “view context(浏览上下文)” 属性,但包含一个 “区域” 属性,那么浏览器应将对象移动到视图中,并应直观地指出该区域是链接的目标。浏览器建立新显示画面的方式由浏览器决定。如果对象既不包含 view context(浏览上下文)属性也不包含区域属性,那么浏览器应将对象移动到视图中,并应直观地指出 gproject 的图元是链接的目标。浏览器建立新的显示画面的方式由浏览器决定。screentip: 浏览器应能显示屏幕提示,若为一个图形对象定义了一个 screentip,那么当光标经过图形对象时,用户应能看到该屏幕提示。content: content 属性字符串应能用于查询,其方式与 CGM 版本 4 的文件内容中任何图形文本的查询方式相同。</td><td>其它:无</td></tr></table>

# 7.4 符号库

[ISO/IEC 8632:1999] 定义了外部符号库，这样，一个符号库列表可在一个图元文件中被定义，符号可以从任意库中被提取，在一个图片中被缩放、倾斜、旋转和放置。标准未提及结构、语义、语法或符号库本身的编码。本规范定义了一个与包含一个或多个图片的图元文件兼容的外部符号库。符号库图元文件中的每个符号都作为一个图片被储存。通常来说，符合本规范的符号库图元文件可与参考它们的图元文件独立地交换。

# 7.4.1 说明

一个符号库图元文件中的元素和它们的参数之间的一致性，以及参考图元文件中的元素和它们的参数之间的一致性如下：

# 7.4.1.1 开始图元文件标识符

符号库图元文件中BEGIN METAFILE(开始图元文件)元素中的字符7到32的内容是引用图元文件中SYMBOL LIBRARY LIST(符号库列表)元素的符号库名称参数。字符1到6包含字符串SYMLIB。

# 7.4.1.2 开始图片标识符

符号库图元文件中的每个BEGIN PICTURE(开始图片)元素的标识符参数是包含在该图片中的图元

元素定义的符号名称。

# 7.4.1.3 符号引用

引用图元文件中的POLYSYMBOL元素的符号索引参数是一个正整数，引用了符号库图元文件中的图片顺序。例如：一个为3的符号索引将提取当前SYMBOL LIBRARY INDEX(符号库索引)中指定的库中的第3个图片(作为符号)，其尺寸依据SYMBOL SIZE(符号尺寸)，其方向依据SYMBOL ORIENTATION(符号方向)，其显示依据当前的SYMBOL COLOUR(符号颜色)。

# 7.4.1.4 符号背景透明度

除非用一个标识符参数为46的ESCAPE元素进行规定，否则符号背景应是透明的。规定用一个参数值为1的ESCAPE元素46可产生不透明的符号背景。这个换码用于样例图元文件，并且参考了样例符号的处理方式。

# 7.4.1.5 符号引用处

除非用一个标识符参数为47的ESCAPE元素规定，否则符号库图元文件中被引用图片的VDC空间的位置被放置在引用图元文件中的POLYSYMBOL元素的位置列表参数中的各位置处。如果位置列表中有多处位置，那么各处将会放置一个样例符号。

# 7.4.1.6 符号设计高度和宽度

除非用一个标识符参数为48的ESCAPE元素规定，否则一个符号的设计宽度和设计高度参数是VDCEXTENT空间的宽度和高度。

# 7.4.2 裁剪

一个符号的裁剪不应发生在设计宽度和高度形成的矩形框上。如果CLIP INDICATOR(裁剪指示符)为ON(允许)，裁剪应在包含符号定义和其它裁剪要求的图片的VDC范围中进行。

# 7.4.3 继承

上下文和属性的继承行为分为两种，语法上下文关系和图形上下文关系。

# 7.4.3.1 图形上下文关系

解释程序应遵从符号库图元文件的语法上下文关系。这表明解释程序应保存引用图元文件的当前语法上下文关系，设定符号图元文件的上下文关系描述符号并还原已保存的引用图元文件的上下文关系。

# 7.4.3.2 继承性

图形上下文继承性规则由3个因素决定：[ISO/IEC8632:1999]中存在一个默认行为，引用图元文件中的一个明确定义，以及符号图元文件中的一个明确定义。下表定义了这些规则：

<table><tr><td>存在一个 CGM 默认行为</td><td>引用图元文件中存在一个 明确定义</td><td>符号图元文件中存在一个明 确定义</td><td>在确定图形上下文中规 定的权限</td></tr><tr><td>是</td><td>是</td><td>是</td><td>符号图元文件</td></tr><tr><td>是</td><td>是</td><td>否</td><td>CGM 默认行为</td></tr><tr><td>是</td><td>否</td><td>是</td><td>符号图元文件</td></tr><tr><td>是</td><td>否</td><td>否</td><td>CGM 默认行为</td></tr><tr><td>否</td><td>是</td><td>是</td><td>符号图元文件</td></tr><tr><td>否</td><td>是</td><td>否</td><td>引用的图元文件</td></tr><tr><td>否</td><td>否</td><td>是</td><td>符号图元文件</td></tr><tr><td>否</td><td>否</td><td>否</td><td>相关的解释程序</td></tr></table>

# 5—2—5 智能图形交换(IGEXCHANGE V2.6)

# 1 概述

智能图形不仅包含相应的可见影像，还包含关于图解说明的附加信息。该附加信息为应用程序提供

了解图形构造和内容的能力。该信息可按导航、查询、数据提取和分析四个主要功能区域进行分组。

# 1.1 用途

智能图形的数字交付包括应用程序的特定用途的数据。

智能图形基本构建模块是包含该数据的图形对象。一个智能化图形的实例是由对象组成的一幅示图，这些对象已经作为图形信息的逻辑单元被标识。这些对象可同其它对象(图形或者SGML)相关连，并可包含与这些对象相关的描述性或特性信息。同这些对象相关的信息允许功能性地使用示图。

# 1.2 范围

本文件主要集中在二维静态图形(的描述)上。本规范是对GREXCHANGE[5-2-4]的一个扩展，以支持与图形数据相关的智能化(信息)的传输。本规范的版本号与它适用的GREXCHANGE版本号相同。GREXCHANGE包含所有CGM元素的格式，其中包括版本4的元素。包含在本规范中的任何格式元素都将替代GREXCHANGE中的相应的格式元素。本规范定义了支持IGFUNCREQ[2-2-2]中要求的语法和机制。本规范的附录A中的信息与ATA通用数据词典[ATA CSDD]共同定义了图形对象类型和属性名，以支持与图形对象相关联的智能化交换。本规范预期可支持附录B[5-2-5.6]中描述的图形交换模型。

本版本的IGEXCHANGE(智能图形交换)主要目的是定义尽可能少的一组图形对象类型，来支持结构化的标识和导航、查询的功能。在将来本规范还会被扩充，以完全支持IGFUNCREQ中定义的要求。

# 1.3 术语

在本文件中，词“图形”与词“示图”是可以互换使用的。

# 1.3.1 智能图形

智能图形被定义为以一种交换格式传送一幅图形信息的方法，这种格式允许功能性的使用这些信息。

# 1.3.2 图形对象

图形对象被唯一地命名，是图元、其它图形对象及图形对象属性的集合。

# 1.3.3 图形对象属性

图形对象属性是与图形对象相关联的一个信息块。

# 1.3.4 图元

图元是在一个图形格式中最底层的可寻址元素。

# 1.3.5 应用程序结构

一个应用程序结构相当于一个图形对象。

# 1.3.6 应用程序结构属性

一个应用程序结构属性相当于一个图形对象属性。

# 1.3.7 应用程序结构类型

应用程序结构类型是一个结构参数，用于将应用程序结构分成相似的组。

# 1.3.8 应用程序结构属性类型

应用程序结构属性类型是一个结构属性参数，用于将应用程序结构属性分类成相似的组。

# 1.3.9 图片目录

图片目录是在一个图元文件中直接存取图片的一种机制。

# 1.3.10 应用程序结构目录

应用程序结构目录是一个图片图元文件中直接存取应用程序结构的一种机制。

# 2 应用程序结构

通过对不同类型的示图的分析，对适用于任何示图的通用图形对象属性以及一幅特定示图中的唯一图形对象属性进行标识。被标识的示图类型是决断图(故障隔离和故障报告树)、详细功能图(布线图和系统原理图)，定位图(导航图)、组件和布局的二维投影图(典型的MM示图和分解视图)和分析图表(图形表和功能图)。

附录A中所包括的信息是一个SGML DTD片段以及结构类型和属性名表格。该信息包括可适用于许多技术出版应用软件的结构类型和属性。

# 3 交换机制

智能图形的交换机制需要使用 CGM V4 元素。CGM V4 应用程序结构用来定义图元分组，以描述一个图形对象。这可以通过使用嵌入的应用程序结构，或通过使用定义图形对象的覆盖区域的应用程序结构来完成。使用嵌入的应用程序结构意味着应用程序结构的内容是构成对象的图元。智能图形覆盖模型是用具有一个相关区域属性的一个应用程序结构来实现的，该区域属性由覆盖对象对应的图形图片的空间范围来定义。其余应用程序结构属性可被编码到 CGM 应用程序结构语法中，也可在相关文件的 SGML 内容模型中被交换。在 SGML 元素和图形应用程序结构类型之间，以及在 SGML 属性和图形应用程序结构属性之间存在一个简单的映射。

对于GERXCHANGE中定义的每个图形交换格式，都存在一个隐含的图形对象。该图形对象是指整个图形，并有一个隐含的属性：StructId(结构标识)。该属性的定义针对于TECHREQ规范(参见[4一3-2])中定义的SHEET元素的SGMLgnbr(图形编号)属性中的整个示图，以及CGM简述文件中的BEGINMETAFILEDESCRIPTION(图元文件描述开始)元素中的整个示图。如果需要其它属性，就应将整个示图明确地定义为一个图形对象，并使用一种适当的交换格式语法来分配需要的属性。

支持智能图形的图形语法需要在交换格式中引入两类附加元素。第一个是标识图形对象的方法。第二个是对来自数据词典的属性标识符及其相关值进行定义的通用方法。

# 3.1 SGML语法

SGML可用于交换与一幅示图有关的智能信息。SGML文件类型定义(DTD)包含在附录A中，它定义了智能图形的结构组织规则。该DTD是定义一个SGML实例文件结构的一个片段，该SGML实例可用作图形文件的伴随实例，作为SGML文本实例中的一个子文件，或嵌入在相关SGML文本DTD中。通过使用应用程序结构ID，SGML语法能将属性同用一个智能图形定义的应用程序结构联系起来。

# 3.2TIFF语法

为了将智能化应用于TIFF示图，根据GREXCJANGE版本3格式和CGM版本V4中定义的规则，智能化信息应被转换为CGM中的双色图象块元素，根据本简述文件中的规则，应用程序结构应用于定义智能化图形。

# 3.3 CGM语法

ISO/IEC 8632:1999 定义的概念包括：图形结构、与这些结构相关的非图形属性，以及辅助检索包含图片和结构开始偏移地址的可选目录。

# 3.4 CGM格式

以下格式是对GREXCHANGE规范[5-2-4]中所包含的CGM格式的一个扩展。它定义了在CGM文件中嵌入的智能图形的ATA应用程序简述文件。本规范中再次给出的元素替代了GREXCHANGE规范[5-2-4]中规定的相应要求。在这里，对照[ISO/IEC8623:1990]定义的ISO模型简述文件，给出ATA简述文件。格式表中的编号方式与ISO CGM标准中的编号方式相同。ISO模型简述文件规范是作为引用而给出的，并应是正确的。在两者存在差异的情况下，应以[ISO/IEC8632:1999]中的模型简述文件为准。

# 3.4.1 分隔符元素

<table><tr><td>元素</td><td>规范-ATA 简述文件</td><td>规范-模型简述文件</td></tr><tr><td>T.15.9 应用程序结构开始</td><td>允许</td><td>元素是: 允许的</td></tr><tr><td>应用程序结构主体开始</td><td></td><td></td></tr><tr><td>应用程序结构结束</td><td></td><td></td></tr><tr><td>CGM 版本: 4</td><td></td><td>对一幅图片内所定义结构的最大数目限制:</td></tr><tr><td></td><td>无</td><td>无</td></tr><tr><td></td><td></td><td>对组成一个结构的元素的数目及等同性的限制</td></tr><tr><td></td><td>无</td><td>无</td></tr><tr><td></td><td></td><td>如果给应用程序结构标识符参数指定实际意义,规定的含义为:</td></tr><tr><td></td><td>除了为应用程序结构分配一个唯一标识符外,没有其它含义。</td><td>除了为应用程序结构分配一个唯一标识符外,没有其它含义。</td></tr><tr><td></td><td></td><td>限制继承标记参数吗?是/否</td></tr><tr><td></td><td>结构类型参数应从附录A中列出的有效结构类型列表中选择。</td><td>否</td></tr><tr><td></td><td>根据附录A中定义的规则,结构对布局的变化是敏感并且是许可的。根据SGML DTD定义的规则,nd放置在图元文件中。</td><td>其它:无</td></tr><tr><td></td><td>应用程序结构类型的定义包含在ATA通用数据词典中。</td><td></td></tr></table>

3.4.2 图元文件描述符元素  

<table><tr><td>元素</td><td>描述-ATA简述文件</td><td>描述-模型简述文件</td></tr><tr><td>T.16.1 图元文件版本 CGM 版本:1</td><td>必需的4无</td><td>元素是:必需的本简述文件允许的图元文件版本:1、2、3、4其它:无</td></tr><tr><td>T.16.2 图元文件描述 CGM 版本:1</td><td>必需的注:SF 参数中的子字符串应按格式:"keyword:item(关键词:项)",其中双引号是子字符串的一部分。不限制“简述文件ID:ATA GRAPHICS.IGEXCHANGE”注:简述文件ID中,在ATA字符串之后有一个ASCII空格符。</td><td>元素是:必需的注:SF参数中的子字符串应具有格式:"keyword:item(关键词:项)",其中双引号是子字符串的一部分。该元素出现的最大次数:不限制简述文件标识,(使用关键词,"ProfileID(简述文件标识):")“简述文件标识:模型一简述文件”</td></tr><tr><td>元素</td><td>描述-ATA 简述文件</td><td>描述一模型简述文件</td></tr><tr><td></td><td>参考适用于该图形的规范的认证版本和修订版本</td><td>简述文件版本，（使用关键字ProfileEd:）“ProfileEd:1”</td></tr><tr><td></td><td>与关键词 ProfileEd 相关的项目应是 n.m, 其中 n 是规范的版本号, m 是修订版号, 它们应标注在本规范的封面或页眉中: 例如: “ProfileEd:2.4”。‘‘ColourClass 是: 单色”或‘‘ColourClass 是: 彩色”附加可选的信息内容‘‘来源: 供应商”‘‘日期: yyyyMMdd”当一个 CGM 文件通过应用程序被移动时, 提倡使用元素多次出现的方法, 以保存历史记录。</td><td>若简述文件版本没有给出，那么版本缺省值为 1。彩色类别：（使用关键词 ColourClass:）彩色、灰度或者单色之一附加的必需信息内容来源：（使用关键词“Source:”销售商、产品和版本日期，（使用关键词“Date:”）图元文件的生成日期。格式和内容应按照[ISO 8601:1988]的规定。其它:无</td></tr><tr><td>T.16.24 图片目录CGM 版本: 4</td><td>同模型简述文件</td><td>元素是: 允许的其它:无</td></tr></table>

# 3.4.3 图片描述符元素

<table><tr><td>元素</td><td>描述-ATA 简述文件</td><td>描述一模型简述文件</td></tr><tr><td>T.17.20 应用程序结构目录 CGM 版本: 4</td><td>同模型简述文件</td><td>元素是: 允许的</td></tr><tr><td></td><td></td><td>其它: 无</td></tr></table>

# 3.4.4 应用程序结构描述符元素

<table><tr><td>元素</td><td>描述-ATA 简述文件</td><td>描述一模型简述文件</td></tr><tr><td>T.24.1 应用程序结构属性 CGM 版本: 4</td><td>允许</td><td>元素是: 允许的定义应用程序结构中使用的结构属性元素集合, 并附带完整的语法和语义说明:</td></tr><tr><td></td><td>允许的属性组在附录 A 中列出, 并且</td><td>无</td></tr><tr><td></td><td>根据应用程序结构类型定义。</td><td></td></tr><tr><td></td><td>应用程序结构属性的定义包含在 ATA 通用数据词典中。 应用程序结构属性的语义在附录 A 中进行了解释。</td><td>其它:无</td></tr></table>

# 3.4.5 解释程序执行要求

<table><tr><td>元素</td><td>描述-ATA 简述文件</td><td>描述-模型简述文件</td></tr><tr><td>3.4.5.1 结构解释</td><td>解释程序应生成正确的图形结果。</td><td>对应用程序结构的解释有要求吗?解释程序应生成正确的图形结果。实际意义与应用程序结构相关吗?是/否</td></tr><tr><td></td><td>是结构类型列表及其含义在附录A中给出。应用程序结构的解释程序语义在附录A中列出。</td><td>否如果是,详细说明解释程序的操作或对于每个结构类型的操作。无其它:无</td></tr></table>

# 4 附录A

# 4.1 描述

本附录中的包含的信息由结构类型和属性组成，这些结构类型和属性已经通过对飞机工业相关手册中所存在的示图类型进行评估而被标识过了。关于结构类型和属性类型的定义，参见ATA通用数据词典[ATA CSDD]。本附录也包含一个描述智能图形结构的SGML DTD片段。

# 4.1.1 应用结构类型

<table><tr><td>类型</td><td>允许来源</td><td>属性</td></tr><tr><td>(智能图形图页)</td><td>不适用</td><td>gnbr(图形编号)一必需sheetnbr(图页编号)一必需</td></tr><tr><td>(定位符)</td><td></td><td>id 一必需region(区域)一可选name(名称)一可选revdate(修订日期)一可选text(文本)一可选</td></tr><tr><td>(详图)</td><td>(智能图形图页)(定位符)(详图)</td><td>id-必需region(区域)一可选name(名称)一可选revdate(修订日期)一可选text(文本)一可选</td></tr><tr><td></td><td></td><td>assembly(组件)-可选sys(系统)-可选分子系统-可选subsys(分分系统)-可选</td></tr><tr><td>(示图编号)</td><td>(定位符)(详图)(段落)</td><td>id-必需region(区域)-可选text(文本)-可选</td></tr><tr><td>(段落)</td><td>(智能图形图页)(定位符)(详图)</td><td>id-必需region(区域)-可选content(内容)-可选</td></tr><tr><td>(内部引用)</td><td>(示图编号)(引用条件)</td><td>id-必需refid(引用标识)-必需reftype(引用类型)-可选</td></tr><tr><td>(外部引用)</td><td>(示图编号)(引用条件)</td><td>id-必需refloc(被引用位置)-可选refman(被引用手册)-可选refmodel(被引用模型)-可选refspl(引用的供应商)-可选docnbr(文件编号)-可选</td></tr><tr><td>(应用程序引用)</td><td>(示图编号)(引用条件)</td><td>id-必需refid(引用标识)-必需sheetnbr(图页编号)-可选structid(结构标识)-可选Shownow(即时显示)-可选</td></tr><tr><td>(引用条件)</td><td>(示图编号)</td><td>id-必需text(文本)-可选condition(条件)-可选</td></tr><tr><td>(有效性)</td><td>(智能图形图页)(定位符)(详图)(示图编号)</td><td>标识-必需effrg(有效区域)-可选efftext(有效文本)-可选</td></tr><tr><td>(服务通报有效性)</td><td>(有效性)</td><td>标识-必需effrg(有效区域)-可选efftext(有效文本)-可选sbnbr(服务通报编号)-必需sbcond(服务通报条件)-必需</td></tr><tr><td></td><td></td><td>sbrev(服务通报修订)-可选</td></tr><tr><td>(COC有效性)</td><td>(有效性)</td><td>id-必需effrg(有效区域)-可选efftext(有效文本)-可选cocnbr(COC编号)-必需</td></tr><tr><td>(修订)</td><td>(段落)(内部引用)(外部引用)(应用程序引用)(用户提出的更改)</td><td>id-必需</td></tr><tr><td>(用户提出的更改)</td><td>(段落)(内部引用)(外部引用)(应用程序引用)</td><td>id-必需</td></tr></table>

# 4.1.2 应用程序结构属性

属性ID对应于[ISO/IEC8632:1999]中定义的BEGINAPPLICATIONSTRUCTURE(应用程序结构开始)元素中的结构标识符参数。

<table><tr><td>属性</td><td>应用程序结构类型</td><td>属性类型</td></tr><tr><td>(图形编号)</td><td>(智能图形图页)</td><td>标识符</td></tr><tr><td>(图页编号)</td><td>(智能图形图页)</td><td>字母数字</td></tr><tr><td></td><td>(应用程序引用)</td><td></td></tr><tr><td>标识</td><td>(定位符)</td><td>标识符</td></tr><tr><td></td><td>(详图)</td><td></td></tr><tr><td></td><td>(示图编号)</td><td></td></tr><tr><td></td><td>(段落)</td><td></td></tr><tr><td></td><td>(内部引用)</td><td></td></tr><tr><td></td><td>(外部引用)</td><td></td></tr><tr><td></td><td>(应用程序引用)</td><td></td></tr><tr><td></td><td>(参考引用)</td><td></td></tr><tr><td></td><td>(有效性)</td><td></td></tr><tr><td></td><td>(服务通报有效性)</td><td></td></tr><tr><td></td><td>(COC 有效性)</td><td></td></tr><tr><td></td><td>(修订)</td><td></td></tr><tr><td></td><td>(用户提出的更改)</td><td></td></tr><tr><td>名称</td><td>(定位符)</td><td>字母数字</td></tr><tr><td></td><td>(详图)</td><td></td></tr><tr><td>(修订日期)</td><td>(定位符)</td><td>数字</td></tr><tr><td></td><td>(详图)</td><td></td></tr><tr><td>(文本)</td><td>(定位符)</td><td>字母数字</td></tr><tr><td></td><td>(详图)</td><td></td></tr><tr><td></td><td>(示图编号)</td><td></td></tr><tr><td></td><td>(引用条件)</td><td></td></tr><tr><td>(组件)</td><td>(详图)</td><td>字母数字</td></tr><tr><td>(系统)</td><td>(详图)</td><td>字母数字</td></tr><tr><td>(子系统)</td><td>(详图)</td><td>字母数字</td></tr><tr><td>(二级子系统)</td><td>(详图)</td><td>字母数字</td></tr><tr><td>(区域)</td><td>(定位符)</td><td></td></tr><tr><td></td><td>(详图)</td><td></td></tr><tr><td></td><td>(段落)</td><td></td></tr><tr><td></td><td>(示图编号)</td><td></td></tr><tr><td>(内容)</td><td>段落</td><td>字母数字</td></tr><tr><td>(引用标识)</td><td>(内部引用)</td><td>引用标识符</td></tr><tr><td></td><td>(应用程序引用)</td><td></td></tr><tr><td>(引用类型)</td><td>(内部引用)</td><td>字母数字</td></tr><tr><td>(引用位置)</td><td>(外部引用)</td><td>字母数字</td></tr><tr><td>(引用手册)</td><td>(外部引用)</td><td>字母数字</td></tr><tr><td>(引用模型)</td><td>(外部引用)</td><td>字母数字</td></tr><tr><td>(特殊引用)</td><td>(外部引用)</td><td>字母数字</td></tr><tr><td>(文件编号)</td><td>(外部引用)</td><td>字母数字</td></tr><tr><td>(结构标识)</td><td>(应用程序引用)</td><td>字母数字</td></tr><tr><td>(即时显示)</td><td>(应用程序引用)</td><td>数字(0或1)</td></tr><tr><td>(条件)</td><td>(引用条件)</td><td>字母数字</td></tr><tr><td>(有效区域)</td><td>(有效性)</td><td>字母数字</td></tr><tr><td></td><td>(服务通报有效性)</td><td></td></tr><tr><td></td><td>(COC有效性)</td><td></td></tr><tr><td>(有效文本)</td><td>(有效性)</td><td>字母数字</td></tr><tr><td></td><td>(服务通报有效性)</td><td></td></tr><tr><td></td><td>(COC有效性)</td><td></td></tr><tr><td>(服务通报编号)</td><td>(服务通报有效性)</td><td>字母数字</td></tr><tr><td>(服务通报条件)</td><td>(服务通报有效性)</td><td>字母数字</td></tr><tr><td>(服务通报修订)</td><td>(服务通报有效性)</td><td>字母数字</td></tr><tr><td>(COC 编号)</td><td>(COC 有效性)</td><td>字母数字</td></tr></table>

# 4.1.3 应用程序结构属性的语义特性

在所有情况中，一个浏览器必须能够根据用户的要求来显示与一个应用程序结构相关的所有属性。（图形编号）

gnbr属性可作为CGM文件的标识符，它在图元文件开始元素中被编码。该标识符能被浏览器识别，与gnbr值相对应的参考标识符能使浏览器显示被参考的CGM文件。该属性不在应用程序结构内编码。

（图页编号）

sheetnbr属性相当于一个SGML文本实例中的SGML SHEET标记的sheetnbr属性，当refaps结构指定了一个sheetnbr时，浏览器将打开与引用图页相关的CGM文件。该属性不在应用程序结构中编码。

（标识）

当一个特定的ID属性作为一个图形对象的引用标识符显示时，浏览器将显示该图形对象。在ID属性是文本对象的引用标识符的情况下，浏览器将对正在执行文本浏览功能的内容进行扫描控制。该属性作为应用程序结构的一个参数给出。

（名称）

name属性在浏览器(执行)任何查找功能期间应是可用的。该属性在应用程序结构中最可多出现一次，并且其SDR参数按照固定字符串被编码。

（修订日期）

不需要更多的特性。该属性在应用程序结构中最多可出现一次，并且其SDR参数按照固定字符串被编码。

(文本)

text 属性在浏览器(执行)任何查找功能期间应是可用的。该属性在应用程序结构中最多可出现一次，并且其SDR参数按照固定字符串被编码。

(组件)

不需要更多的特性。该属性在应用程序结构中最多可出现一次，并且其SDR参数按照固定字符串被编码。

（系统）

不需要更多的特性。该属性在应用程序结构中最多可出现一次，并且其SDR参数按照固定字符串被编码。

(子系统)

不需要更多的特性。该属性在应用程序结构中最多可出现一次，并且其SDR参数按照固定字符串被编码。

# （二级子系统）

不需要更多的特性。该属性在应用程序结构中最多可出现一次，并且其SDR参数按照固定字符串被编码。

（区域）

如果不存在 region 属性，那么由 APS 应用程序结构主体中的图元范围来定义一个隐含的区域。region 属性是为了由应用程序进行选取而使用的。当嵌套 APS 的结果为多重区域时，选取优先权属于包含该区域的最低级嵌套的 APS。当重叠区域不是由嵌套 APS 产生时，选取优先权属于包含该区

域的最后生成的APS。浏览器应给用户一个视觉反馈信息，以成功地完成一次选取动作，并应指示出特定对象(或区域)已被选取。区域属性的意义是将一个区域和一个类型为“grobjec”的应用程序结构联系起来。region属性在一个APS内最多能出现一次，但在允许定义不相交的子区域、中空区域等情况下，复杂区域可由所建立的简单区域的集合组成。它们的语义(子区域和内部/外部定义)与CGM的CLOSEDFIGURE(闭合图形)元素的那些语义相同。定义数据记录参数的SDR由定义索引和点列表的一对或多对的参数组成。点列表对应于等价CGM元素的参数数据。定义了四个索引：矩形：索引=1，点列表=2点，椭圆：索引=2，点列表=3点，多边形：索引=3，点列表=n点，连续的分段贝塞尔曲线：索引=4，点列表(基于2的连续指示符)=3n+1点。如果闭合不是显式的，区域将隐含为封闭。

(内容)

Content属性在浏览器(执行)任何查找功能期间应是可用的。该属性在应用程序结构中最多可出现一次，并且其SDR参数按照固定字符串被编码。

(参考标识)

当选取包含refid属性的对象时，或从一个条件性的引用列表中选择对象时，浏览器应导航到由refid标识的被引用对象。该属性在应用程序结构中最多可出现一次，并且其SDR参数按照固定字符串被编码。

（引用类型）

不需要更多的特性。该属性在应用程序结构中最多可出现一次，并且其SDR参数按照固定字符串被编码。

（引用位置）

当选取包含refloc属性的对象时，或从一个条件性的引用列表中选择对象时，浏览器应导航到由被引用手册中的refloc标识的被引用对象，被引用手册由refman属性标识。该属性在应用程序结构中最多可出现一次，并且其SDR参数按照固定字符串被编码。

（引用手册）

不需要更多的特性。该属性在应用程序结构中最多可出现一次，并且其SDR参数按照固定字符串被编码。

（引用模型）

不需要更多的特性。该属性在应用程序结构中最多可出现一次，并且其SDR参数按照固定字符串被编码。

（引用的供应商）

不需要更多的特性。该属性在应用程序结构中最多可出现一次，并且其SDR参数按照固定字符串被编码。

(文件编号)

不需要更多的特性。该属性在应用程序结构中最多可出现一次，并且其SDR参数按照固定字符串被编码。

（结构标识）

在一个 refaps 应用程序结构内，refid 可指向同一文档中的其它 CGM 文件的 gnbr。如果 structid 属性给出了 refaps 应用程序结构，则浏览器应导航到一个具有与 structid 相同 ID 值的应用程序结构。该属性在应用程序结构中最多可出现一次，并且其 SDR 参数按照固定字符串被编码。

（即时显示）

当 shownnow 属性设置为 “0” 时(默认状况), 浏览器应显示被引用应用程序结构的一个视图。否则, 显示器将导航到对象, 并显示一个表示图形视图存在的图标。该属性在应用程序结构中最多可出现一次, 并且其 SDR 参数按照固定字符串被编码。

（条件）

当遇到该属性时，浏览器应给用户一些参考条件以供选择。该属性在应用程序结构中最多可出现一次，并且其SDR参数按照重复出现的固定字符串被编码。

# (有效性区域)

当指定一个外部有效性条款时，浏览器应限制应用程序结构的智能图形功能，以满足基于effrg属性的有效性条款。该属性在应用程序结构中最多可出现一次，并且其SDR参数按照固定字符串被编码。

# (有效性文本)

不需要更多的特性。该属性在应用程序结构中最多可出现一次，并且其SDR参数按照固定字符串被编码。

# （服务通报编号）

不需要更多的特性。该属性在应用程序结构中最多可出现一次，并且其SDR参数按照固定字符串被编码。

# (服务通报条件)

不需要更多的特性。该属性在应用程序结构中最多可出现一次，并且其SDR参数按照固定字符串被编码。

# （服务通报修订）

不需要更多的特性。该属性在应用程序结构中最多可出现一次，并且其SDR参数按照固定字符串被编码。

# (COC编号)

不需要更多的特性。该属性在应用程序结构中最多可出现一次，并且其SDR参数按照固定字符串被编码。

# 4.1.4 智能图形的SGML DTD

```txt
<!ENTITY % yesorno 'NUMBER'  
<!ELEMENT igsheet - -(effect?, (locator | detail | para) *) >  
<!ATTLIST igsheet  
gnbr ENTITY #REQUIRED  
sheetnbr CDATA #REQUIRED  
<!ELEMENT locator - -(effect?, (detail | callout | para) *) >  
<!ATTLIST locator  
id ID #REQUIRED  
region NUMBERS #IMPLIED  
name CDATA #IMPLIED  
revdate NUMBER #IMPLIED  
text CDATA #IMPLIED  
<!ELEMENT detail - -(effect?, (detail | callout | para) *) >  
<!ATTLIST detail  
id ID #REQUIRED  
region NUMBERS #IMPLIED  
name CDATA #IMPLIED  
revdate NUMBER #IMPLIED  
text CDATA #IMPLIED
```

```shell
assembly CDATA #IMPLIED
sys CDATA #IMPLIED
subsys NUMBER #IMPLIED
subsubsys NUMBER #IMPLIED
<!ELEMENT callout -- (effect?, (refint | refext | refaps | refcond+)) > <!ATTLIST callout
id ID #REQUIRED
region NUMBERS #IMPLIED
text CDATA #IMPLIED
<!ELEMENT para -- (#PCDATA | rev | coc | callout) +
<!ATTLIST para
id ID #REQUIRED
region NUMBERS #IMPLIED
content CDATA #IMPLIED
<!ELEMENT refint -- (#PCDATA | rev | coc) +
<!ATTLIST refint
id ID #REQUIRED
refid IDREF #REQUIRED
reftype CDATA #IMPLIED
<!ELEMENT refext -- (#PCDATA | rev | coc) +
<!ATTLIST refext
id ID #REQUIRED
refloc CDATA #IMPLIED
refman CDATA #IMPLIED
refmodel CDATA #IMPLIED
refspl CDATA #IMPLIED
docnbr CDATA #IMPLIED
<!ELEMENT refaps -- (#PCDATA | rev | coc) +
<!ATTLIST refaps
id ID #REQUIRED
refid IDREF #REQUIRED
sheetnbr CDATA #IMPLIED
structid IDREF #IMPLIED
shownow %yesorno; "0"
<!ELEMENT refcond -- (refint | refext | refaps+) > <!ATTLIST refcond
id ID #REQUIRED
text CDATA #IMPLIED
condition CDATA #REQUIRED
```

```shell
<!ELEMENT effect -- (sbeff|coceff)*  
<!ATTLIST effect  
id ID #REQUIRED  
effrg CDATA #IMPLIED  
efftext CDATA #IMPLIED  
<!ELEMENT sbeff-o EMPTY  
<!ATTLIST sbeff  
id ID #REQUIRED  
effrg CDATA #IMPLIED  
efftext CDATA #IMPLIED  
sbinbr CDATA #REQUIRED  
sbcond CDATA #REQUIRED  
sbrev CDATA #IMPLIED  
<!ELEMENT coceff-o EMPTY  
<!ATTLIST coceff  
id ID #REQUIRED  
effrg CDATA #IMPLIED  
efftext CDATA #IMPLIED  
cocnbr CDATA #REQUIRED  
<!ELEMENT rev - - (#PCDATA)  
<!ATTLIST rev  
id ID #REQUIRED  
<!ELEMENT coc - - (#PCDATA|rev)+  
<!ATTLIST coc  
id ID #REQUIRED
```

# 4.1.5 智能图形模型结构图

下列图形集给出了该DTD的直观视图。

![](images/be2dd838e1b4428801f682e326d71c0d9525dc4ea7881741b1f1b3279eef16d5.jpg)  
图5-2-5.1 智能图形结构(第一部分)

![](images/cb614f6c692e61ab3e741cc1c821317fe8212a38072b7b4f2c71a5e33a472cd4.jpg)  
图5-2-5.1 智能图形结构（第二部分）

![](images/06692f0bb177b184c89a16e1bfa1b138be4315847066bea811ddc8f2b79e66dc.jpg)  
图5-2-5.1 智能图形结构(第三部分)

# 5 附录B.交换模型

包含图形对象的智能示图的交换可采用不同方式实现。对于交换的三个级别，这里介绍一个概念模型。在图B-1中，数据生成程序将从该示图的上部所示的一个“样式”数据库中理想化地生成示图。在这个简单的例子中，数据库包含四种图形样式，分别为abcd、bcde、cdef和defg。该示图中所示的xxxx和yyyy两个图形是从数据库中选择对象，并对它们进行各种变形之后所组成的。

![](images/9a95ed32722c9cafe2e8d89e515d3c592f15c730a5ee9e9726386c10da30e02a.jpg)  
图5-2-5.2 交换模型

数据接收者可以分成三类。第一类接收者将每幅示图当作其本地数据库中的一个实体，这些实体包含与每个对象和示图相关的智能化信息。该类接收者在它的数据库中有两个记录：xxxx 和 yyyy。

第二类数据接收者可将示图分解为示图的对象，将每个对象和与该对象相关的智能信息作为一个唯一的实体。该类接收者的数据库应由相应的xxxx.abcd、xxxx.defg、xxxx.cdef1、xxxx.cdef2、yyyy.bcde、yyyy.abcd和yyyy.defg记录组成。这时，必须具有重新构建每幅示图的方法。

第三类接收者可能将试图通过捕获每个对象的各种变形以及逆向变换以生成原始对象的方式来重

新构建数据生成器数据库，从而能够象数据生成器那样再利用原始对象。这种类型接收者的数据库由四种原始的对象组成：abcd、bcde、cdef和defg。每个对象的智能信息必须在实例级别被捕获，并应保存重建示图的方法。

每一种方法论的交换策略稍有不同，在交换格式上要求具有不同的结构。对于无论是在全局级别还是局部级别分配图形对象属性，应考虑周全，以适应各种类型的用户。本规范的目标就是定义一个支持所有这三种交换方法的语法。交换文件实例在附录C中介绍。

# 6 附录C.文件交换示例

本附录给出了关于交换文件的几个范例。[图5-2-5.3]是一幅被作为智能图形来表现的实例示图。以下示例示范了CGM版本4文件的使用、版本4覆盖模型的使用和一个SGML伴随文件的使用。

![](images/fc49683ff776848b594d3f6033c9535465047232a5444e70c805f1f157508493.jpg)  
图5-2-5.3 智能图形图例

# 6.1 CGM V4 文件

下列实例是一个定义了智能示图结构和属性的自包含的版本4CGM文件。

BegMF“ME_628493 ZGSR 5510092 2011”；

MFVersion4;

MFElemList "VERSION4";

MFDesc“ProfileID:ATA GRAPHICS.IGEXCHANGE”“ProfileEd:2.4”“ColourClass:monochrome”；

RealPrec -1000000000.0 1000000000.07;

ColrPrec 65535;

ColrIndexPrec 65535;

MaxColrIndex 1;

CharCoding basic8bit;

FontList“OCRB”“Symbol”;

CharSetList std94 "4/2 (ISO 8859-1 LH)" std94 "4/2 (ISO 8859-1 RH)" std94 "2/10 3/10 (Symbol LH)" std94 "2/6 3/10 (Symbol RH)";

BegMFDetails;

TextPrec stroke;

IntStyle empty;

EdgeVis on;

EndMFDefaults;

BegPic "Intelligence Graphics Example for IGEXCHANGE V2.4";

ScaleMode metric 0.0254;

LineWidthMode abs;

EdgeWidthMode abs;

VDCExt 0 0 7650 10050;

BegPicBody;

BegAPS "S_001" "igsheet" "APS"; *igsheet *

BegAPSBody;

LineWidth 32;

Line 750 2884 750 2154;

BegAPS“S_002”“para”“APS”； *para*

APSAAttr "content" "14 1 "Horizontal Stabilizer Rib Repairs";

BegAPSBody;

TextFontIndex 1;

CharHeight 97;

RestrText 2605 97 2949 1525 final "Horizontal Stabilizer Rib Repairs"

"RestrText 1569 97 3466 1357 final "Figure 201 (Sheet 1)";

EndAPS; \*end para \*

BegAPS "S_003" "Locator" "APS"; * locator *

BegAPSBody:

LineWidth 8;

Line 2303 9969 2144 9887 2126 9874 2112 9857 1535 8819;

\*

* Line primitives deleted *

\*

3027 8612 2956 8553 2949 8547 2929 8537 2907 8534 2228 8491;

BegAPS "S_004" "callout" "APS"; *callout *

BegAPSBody;

FontIndex 1;

CharHeight 69;

BegAPS "S_005" "refaps" "StateList"; * refaps *

APSAtrr“Structid”“141‘S_006”；

BegAPSBody;

RestrText 742 69 2412 8249 final "SEE DETAIL I";

EndAPS; *end refaps *

LineWidth 8;

EdgeWidth 12;

IntStyle solid;

Line 2356 8306 2164 8541;

Polygon 2164 8541 2217 8468 2223 8473;

EndAPS;  $\%$  end callout \%

EndAPS;  $\%$  end locator  $\%$

BegAPS "S_006" "detail" "APS"; % detail %

BegAPSBody;

LineWidth 8;

Line 1738 3870 1738 3844;

\*

* Line primitives deleted *

\*

Line 6237 6895 6237 6903;

BegAPS“S_007”“para”“APS”; % para %

BegAPSBody;

FontIndex 1;

CharHeight 97;

RestrText 1169 97 3682 3754 final "LEFT SIDE SHOWN";

RestrText 1489 97 3523 3586 final "RIGHT SIDE OPPOSITE";

RestrText 611 97 3965 3418 final "DETAIL I";

EndAPS; *end para *

BegAPS“S_008”“para”“APS”; \%*para *

BegAPSBody;

FontIndex 1;

CharHeight 69;

RestrText 230 69 992 4951 final "HSBL";

RestText 424 69 897 4823 final "357.442";

LineWidth 8;

Line 1154 4763 1287 4547;

EndAPS; % end para %

BegAPS "S_009" "para" "APS"; % para %

BegAPSBody:

FontIndex 1;

CharHeight 69;

RestrText 678 69 2480 4134 final "RIBS AFT OF";

RestrText 550 69 2480 4006 final "REAR SPAR";

LineWidth 8;

EdgeWidth 12;

IntStyle solid;

Line 2682 4257 2686 4551;

Polygon 2686 4551 2702 4452 2668 4452;

EndAPS; \*endpara\*

BegAPS "S_010" "para" "APS"; * para *

BegAPSBody;

TextFontIndex 1;

CharHeight 69;

RestrText 296 69 2548 6372 final "CHORD";

RestrText 552 69 2548 6244 final “(TYPICAL)”;

LineWidth 8:

EdgeWidth 12;

IntStyle solid;

Line 2974 6383 3885 6338;

Polygon 3885 6338 3785 6326 3787 6360;

EndAPS; \*end para \*

BegAPS "S_011" "para" "APS"; * para *

APSAttr "content" "14 1 'RIBS BETWEEN AUXILIARY SPAR AND FRONT SPAR SEE FIG. 204";

BegAPSBody;

TextFontIndex 1;

CharHeight 69;

RestrText 744 69 2519 7426 final "RIBS BETWEEN";

RestrText 870 69 2519 7290 final "AUXILIARY SPAR";

RestrText 934 69 2519 7154 final "AND FRONT SPAR";

BegAPS "S_012" "callout" "APS"; * callout *

BegAPSBody;

FontIndex 1;

CharHeight 69;

BegAPS "S_013" "refaps" "StateList"; * refaps *

APSAtr "refid" "14 1 'ME_628496";

BegAPSBody;

RestrText 744 69 2519 7026 final "SEE FIG. 204";

EndAPS; \*end refaps

EndAPS; *end shout *

BegAPS "S_014" "callout" "APS"; *callout *

BegAPSBody;

FontIndex 1;

CharHeight 69;

BegAPS "S_015" "refaps" "stateList"; * refaps *

APSAtr "structid" "14 1 's_040";

BegAPSBody;

RestrText 40 69 3330 7025 final “A”;

EndAPS; \*end refaps\*

LineWidth 8;

Line 3299 7004 3424 7004 3424 7129 3299 7129 3299 7004;

EndAPS; \*end callout\*

LineWidth 8;

EdgeWidth 12;

IntStyle solid;

Line 3480 7057 4323 6787;

Polygon 4323 6787 4224 6801 4234 6833;

EndAPS; \*endpara\*

BegAPS "S_016" "para" "APS"; *para *

APSAtr "content" "14 1 'FOR WEBS (TYPICAL) SEE FIG.202 AND 203";

BegAPSBody;

FontIndex 1;

CharHeight 69;

"RestrText 1128 69 3661 4724 final "FOR WEBS (TYPICAL)";

BegAPS "S_017" "callout" "APS"; * callout *

BegAPSBody;

TextFontIndex 1;

CharHeight 69;

BegAPS "S_018" "refcond" "StateList"; * refcond *

APSAttr "condition" "14 2 '202' '203";

BegAPSBody;

BegAPS "S_019" "refaps" "StateList";

APSAtr "refid" "14 1 'ME_628494";

BegAPSBody;

RestrText 816 69 3661 4588 final "SEE FIG. 202";

EndAPS; \*end refaps \*

BegAPS "S_020" "refaps" "StateList"; * refaps *

APSAAttr "refid" "14 1 'ME_628495";

BegAPSBody:

RestrText 440 69 4477 4588 final "AND 203";

EndAPS; \* end refaps \*

EndAPS; \*end refcond \*

EndAPS; * end shout *

LineWidth 8;

EdgeWidth 12;

ntStyle solid;

Line 4010 4846 4121 5292;

Polygon 4121 5292 4114 5192 4081 5200;

Line 4010 4846 3726 5544;

Polygon 3726 5544 3756 5459 3764 5462;

Line 4010 4846 3289 5854;

Polygon 3289 5854 3360 5783 3333 5764;

EndAPS; \*endpara\*

BegAPS "S_021" "para" "APS"; * para *

APSAttr "content" "14 1 'RIBS BETWEEN FRONT SPAR AND REAR SPAR. SEE FIG. 204";

BegAPSBody;

TextFontIndex 1;

CharHeight 69;

RestrText 744 69 5416 5427 final "RIBS BETWEEN";

RestrText 870 69 5416 5291 final "FRONT SPAR AND";

RestrText 614 69 5416 5155 final "REAR SPAR."

BegAPS "S_022" "callout" "APS"; * callout *

BegAPSBody;

FontIndex 1;

CharHeight 69;

BegAPS "S_023" "refaps" "StateList";

APSAAttr "refid" "14 1 'ME_628496";

BegAPSBody;

RestrText 744 69 5416 5027 final "SEE FIG. 204";

EndAPS; \*end refaps \*

EndAPS; \*end callout\*

BegAPS "S_024" "callout" "APS"; * callout *

BegAPSBody;

TextFontIndex 1;

CharHeight 69;

BegAPS "S_025" "refaps" "StateList"; * refaps *

APSAtr "Structid" "14 1 'S_040";

BegAPSBody;

RestrText 406962345026 final“A”；

EndAPS; \* end refaps \*

LineWidth 8;

Line 6203 5005 6328 5005 6328 5130 6203 5130 6203 5005;

EndAPS; \*end callout\*

LineWidth 8;

EdgeWidth 12;

IntStyle solid;

Line 5368 5471 4886 6119;

Polygon 4886 6119 4959 6050 4931 6028;

EndAPS; \*endpara\*

BegAPS "S_026" "para" "APS"; * para *

BegAPSBody;

FontIndex 1;

CharHeight 69;

RestrText 552 69 5672 8074 final "AUXILIARY";

RestrText 230 69 5672 7938 final "SPAR";

LineWidth 8;

EdgeWidth 12;

IntStyle solid;

Line 5812 7902 5360 7622;

Polygon 5360 7622 5454 7660 5436 7690;

EndAPS; \*endpara\*

BegAPS“S_027”“para”“APS”； *para*

BegAPSBody;

FontIndex 1;

CharHeight 69;

RestrText 296 69 6324 7748 final "FRONT";

RestrText 230 69 6324 7612 final "SPAR";

LineWidth 8;

Line 6123 7654 6291 7750;

EndAPS; \*endpara\*

BegAPS“S_028”“para”“APS”； *para*

BegAPSBody;

FontIndex 1;

CharHeight 69;

RestrText 616 69 6773 7518 final "FOR CENTER";

RestrText 422 69 6773 7390 final "SECTION";

BegAPS "S_029" "callout" "APS"; * callout *

BegAPSBody;

TextFontIndex 1;

CharHeight 69;

BegAPS "S_030" "refaps" "StateList"; * refaps *

APSAtr "sheetnbr" "14 1 '2";

APSAtrr“structid”“141“s_003”；

BegAPSBody;

RestrText 806 69 6773 7257 final "SEE DETAIL II";

EndAPS; \*end refaps \*

EndAPS; \*end callout \*

LineWidth 8;

EdgeWidth 12;

IntStyle solid;

Line 6742 7540 6405 7146;

Polygon 6405 7146 6456 7232 6482 7210;

EndAPS; *end para *

BegAPS "S_031" "para" "APS"; *para*

BegAPSBody;

FontIndex 1;

CharHeight 69;

RestrText 232 69 6741 7018 final "REAR";

RestrText 230 69 6741 6882 final "SPAR";

LineWidth 8;

Line 6544 6938 6686 7020;

EndAPS; \*endpara\*

BegAPS "S_032" "para" "APS"; * para *

BegAPSBody;

TextFontIndex 1;

CharHeight 69;

RestrText 170 69 6682 6320 final "RIB";

RestrText 232 69 6682 6184 final "NO.3";

LineWidth 8;

Line 6591 6570 6725 6447;

EndAPS; \*endpara\*

LineWidth 12;

DisjtLine 6550 4240 6578 4224 6578 4224 6634 4338 6634 4338 6578 4386 6578 4386

6578 4354 6578 4354 6437 4273 6437 4273 6437 4175 6437 4175 6578 4257 6578 4257

6578 4224 6578 4386 6550 4403 6550 4403 6550 4371 6550 4371 6410 4289 6410 4289

6410 4192 6410 4192 6437 4175 6410 4289 6437 4273 6550 4371 6578 4354;

RestrText 232 69 6676 4346 final "INBD";

DisjtLine 6203 4228 6175 4212 6175 4212 6119 4326 6119 4326 6175 4374 6175 4374

6175 4342 6175 4342 6316 4261 6316 4261 6316 4163 6316 4163 6175 4245 6175 4245

6175 4212 6175 4374 6203 4391 6203 4391 6203 4359 6203 4359 6343 4277 6343 4277

6343 4180 6343 4180 6316 4163 6343 4277 6316 4261 6203 4359 6175 4342;

RestrText 298 69 5773 4332 final " FWD?

EndAPS; \*end detail\*

BegAPS "S_033" "para" "APS"; * para *

BegAPSBody;

TextFontIndex 1;

CharHeight 97;

RestrText 369 97 882 2987 final "NOTES";

EndAPS; \*endpara\*

BegAPS "S_034" "para" "APS"; * para *

APSAttr "content" "14 1 'CALL THE BOEING COMPANY FOR REPAIRS TO HORIZONTAL

STABILIZER CENTER SECTION RIB WEBS, CHORDS, AND SPLICES";

BegAPSBody:

FontIndex 2;

AltCharSetIndex 4;

CharHeight 69;

RestrText 40 69 999 2793 final “:”;

FontIndex 1;

BegAPS "S_035" "rev" "StateList"; * rev *

BegAPSBody;

RestrText 2474 69 1127 2793 final "CALL THE BOEING COMPANY FOR REPAIRS TO";

RestrText 2534 69 1127 2665 final "HORIZONTAL STABILIZER CENTER SECTION RIB";

RestrText 1574 69 1127 2537 final "WEBS, CHORDS, AND SPLICES";

EndAPS; \*end rev\*

EndAPS; \* end para \*

BegAPS "S_036" "para" "APS"; * para *

APSAtr "content" "14 1 'REFER TO SRM 51-70-12 FOR TYPICAL EXTRUDED SECTION REPAIRS TO STIFFENERS";

BegAPSBody;

FontIndex 2;

AltCharSetIndex 4;

CharHeight 69;

RestrText 40 69 999 2345 final ".

FontIndex 1;

BegAPS "S_037" "callout" "APS"; *argout *

BegAPSBody:

FontIndex 1;

CharHeight 69;

BegAPS "S_038" "refint" "StateList"; * refint *

APSAtr "refid" "14 1 'T-51-70-12";

BegAPSBody;

BegAPS "S_039" "rev" "StateList"; * rev *

BegAPSBody;

RestrText 13956911272345 final "REFER TO SRM 51-70-12";

EndAPS; \*end rev\*

EndAPS; \*end refint\*

EndAPS; \*end callout\*

BegAPS "S_040" "rev" "StateList"; * rev *

BegAPSBody:

RestrText 1269 69 2522 2345 final "FOR TYPICAL EXTRUDED";

RestrText 1824 69 1127 2217 final "SECTION REPAIRS TO STIFFENERS";

EndAPS; \*end rev\*

EndAPS; \*endpara\*

BegAPS "S_041" "para" "APS"; * para *

APSAtr "content" "14 1 'REFER TO SRM 51-70-12 (TYPICAL EXTRUDED SECTION REPAIRS) FOR AN ALTERNATIVE REPAIR TO RIB CHORDS";

BegAPSBody:

FontIndex 1;

CharHeight 69;

RestrText 406946842803 final "A";

LineWidth 8;

Line 4653 2782 4778 2782 4778 2907 4653 2907 4653 2782;

BegAPS "S_042" "callout" "APS"; *callout *

BegAPSBody;

TextFontIndex 1;

CharHeight 69;

BegAPS "S_043" "Refint" "StateList"; *refint *

APSAtr "refid" "14 1 'T-51-70-12";

BegAPSBody;

BegAPS "S_044" "rev" "StateList"; * rev *

BegAPSBody;

RestrText 1431 69 4877 2793 final “REFER TO SRM 51-70-12”；

EndAPS; \*end rev\*

EndAPS; * end refint *

EndAPS; \*end callout\*

BegAPS "S_045" "rev" "StateList"; * rev *

BegAPSBody;

RestrText 1105 69 6308 2793 final “(TYPICAL EXTRUDED”;

RestrText 2660 69 4877 2665 final "SECTION REPAIRS) FOR AN ALTERNATIVE REPAIR";

RestrText 806 69 4877 2537 final "TO RIB CHORDS";

EndAPS; *end rev *

EndAPS; \*endpara\*

EndAPS; * end igsheet*

EndPic;

EndMF;

6.2 CGM V4 覆盖图文件

下列实例是一个应用覆盖模型的版本4CGM文件，该模型使用区域属性来定义应用程序结构。

BegMF "ME_628493_OVERLAY

ZGSR 5510092 2011

MFVersion 4;

MFElemList "VERSION4";

MFDesc 'ProfileID:ATA GRAPHICS.IGEXCHANGE ProfileEd:2.4';

RealPrec -1000000000.0 10000000000.07;

ColrPrec 65535;

ColrIndexPrec 65535;

MaxColrIndex 1;

CharCoding basic8bit;

FontList“OCRB”“Symbol”;

CharSetList std94 "4/2 (ISO 8859-1 LH)" std94 "4/2 (ISO 8859-1 RH)" std94 "2/10 3/10 (Symbol LH)"std94 "2/6 3/10 (Symbol RH)";

BegMFDefaults;

TextPrec stroke;

IntStyle empty;

EdgeVis on;

EndMFDefaults;

BegPic "Intelligence Graphics Overlay Example for IGEXCHANGE V2.4";

ScaleMode metric 0.0254;

LineWidthMode abs;

EdgeWidthMode abs;

VDCExt 0 0 7650 10050;

BegPicBody;

\*  
* Picture primitives deleted *  
\*in example only  
\*

BegAPS "S_001" "igsheet" "APS"; *igsheet *

BegAPSBody;

BegAPS "S_002" "para" "APS"; *para*

APSAAttr "content" "14 1 Horizontal Stabilizer Rib Repairs";

APSAAttr "region" "11 1 1 16 4 2949 1357 5540 1622";

BegAPSBody;

BegAPS "S_003" "locator" "APS"; * locator *

APSAtr "region" "11 1 1 16 4 950 7730 2950 9970";

BegAPSBody;

BegAPS "S_004" "callout" "APS"; * callout *

APSAAttr "region" "11 1 1 16 4 2412 8249 3154 8318";

BegAPSBody;

BegAPS "S_005" "refaps" "StateList"; * refaps *

APSAtr "structid" "14 1 's_006";

BegAPSBody;

EndAPS; \*end refaps\*

EndAPS; \*end callout\*

EndAPS: \*end locator\*

BegAPS "S_006" "detail" "APS"; *detail *

APSAAttr "region" "11 1 3 16 10 897 3418 897 4951 2519 8143 7579 8143 7579 3418";

BegAPSBody;

BegAPS“S_007”“para”“APS”； *para*

APSAtr "region" "11 1 1 16 4 3523 3418 5012 3851";

BegAPSBody;

EndAPS; \*endpara\*

BegAPS "S_008" "para" "APS"; *para*

APSAtr "region" 11 1 1 16 4 897 4823 1321 5020";

BegAPSBody;

EndAPS; \*endpara\*

BegAPS "S_009" "para" "APS"; * para *

APSAtr "region" "11 1 1 16 4 2480 4006 3158 4203";

BegAPSBody;

EndAPS; \*endpara\*

BegAPS "S_010" "para" "APS"; *para*

APSAtr "region" "11 1 1 16 4 2548 6244 3100 6441";

BegAPSBody;

EndAPS; \*endpara\*

BegAPS "S_011" "para" "APS"; * para *

APSAtr "content" "14 1 'RIBS BETWEEN AUXILIARY SPAR AND FRONT SPAR SEE FIG.204";

APSAtr "region" "11 1 1 16 4 2519 7004 3453 7495";

BegAPSBody;

BegAPS "S_012"callout"“APS”; *logout *

APSAtr "region" "11 1 1 16 4 2519 7026 3263 7095";

BegAPSBody;

BegAPS "S_013" "refaps" "StateList"; * refaps *

APSAtrr“refid”“14 1‘ME_628496”；

BegAPSBody;

EndAPS; \*end refaps\*

EndAPS; \*end callout\*

BegAPS "S_014" "callout" "APS"; * callout *

APSAtr "region"11111643299700434247129";

BegAPSBody;

BegAPS "S_015" "refaps" "StateList"; * refaps *

APSAtr "structid" "14 1 's_040";

BegAPSBody;

EndAPS; \*end refaps\*

EndAPS; \*end callout\*

EndAPS; \*endpara\*

BegAPS "S_016" "para" "APS"; *para*

APSAtr "content" "14 1 'FOR WEBS (TYPICAL) SEE FIG.202 AND 203";

APSAAttr "region" "11 1 1 16 4 3661 4588 4917 4793";

BegAPSBody;

BegAPS "S_017" "callout" "APS"; * callout *

APSAtr "region" "11 1 1 16 4 3661 4588 4917 4657";

BegAPSBody;

BegAPS "S_018" "refcond" "StateList"; * refcond *

APSAtr "condition" "14 2 '202' '203";

BegAPSBody;

BegAPS "S_019" "refaps" "StateList"; * refaps *

APSAtr "refid" "14 1 'ME_628494";

BegAPSBody;

EndAPS; \*end refaps \*

BegAPS "S_020" "refaps" "StateList"; *refs *

APSAtrr "refid" "14 1 'ME_628495";

BegAPSBody;

EndAPS; \*end refaps\*

EndAPS; *end refcond *

EndAPS; \*end callout\*

EndAPS; \*endpara\*

BegAPS "S_021" "para" "APS"; * para *

APSAAttr "content" "14 1 'RIBS BETWEEN FRONT SPAR AND REAR SPAR. SEE FIG. 204";

APSAtr "region" "11 1 1 16 4 5416 5005 6328 5496";

BegAPSBody;

BegAPS "S_022" "callout" "APS"; * callout *

APSAtr "region" "11 1 1 16 4 5416 5027 6160 5096";

BegAPSBody;

BegAPS "S_023" "refaps" "StateList"; * refaps *

APSAtr "refid" "14 1 'ME-628496";

BegAPSBody;

EndAPS; \*end refaps\*

EndAPS; \*end callout\*

BegAPS "S 024" "callout" "APS"; *argout *

APSAttr "region" "11 1 1 16 4 6203 5005 6328 5130";

BegAPSBody;

BegAPS "S_025" "refaps" "StateList"; * refaps *

APSAtr "structid" "14 1 's_040";

BegAPSBody;

EndAPS; \*end refaps\*

EndAPS; \*end callout\*

EndAPS; \*endpara\*

BegAPS "S_026" "para" "APS"; * para *

APSAttr "region" "11 1 1 16 4 5672 7938 6224 8143";

BegAPSBody;

EndAPS; \*endpara\*

BegAPS "S_027" "para" "APS"; * para *

APSAttr "region" "11 1 1 16 6324 7612 6620 7817";

BegAPSBody;

EndAPS; \*endpara\*

BegAPS "S_028" "para" "APS"; * para *

APSAAttr "region" "11 1 1 16 6773 7257 7579 7886";

BegAPSBody;

BegAPS "S_029" "callout" "APS"; * callout *

APSAAttr "region" "11 1 1 16 6773 7257 7579 7326";

BegAPSBody;

BegAPS "S_030" "refaps" "StateList"; * refaps *

APSAtr "sheetnbr" "14 1 '2";

APSAAttr "structid" "14 1 's_003";

BegAPSBody;

EndAPS; \*end refaps\*

EndAPS; \*end callout\*

EndAPS; \*endpara\*

BegAPS "S_031" "para" "APS"; * para *

APSAAttr "region" "11 1 1 16 6741 6882 6973 6951";

BegAPSBody;

EndAPS; \*endpara\*

BegAPS "S_032" "para" "APS"; * para *

APSAtr "region" "11 1 1 16 6682 6184 6914 6389";

BegAPSBody;

EndAPS; \*endpara\*

EndAPS; \*end detail \*

BegAPS“S_033”“para”“APS”； *para*

APSAAttr "region" "11 1 1 16 882 2987 1251 3056";

BegAPSBody;

EndAPS; \*endpara\*

BegAPS“S_034”“para”“APS”；*para*

APSAtr "content" "14 1 'CALL THE BOEING COMPANY FOR REPAIRS TO HORIZONTAL STABILIZER CENTER SECTION RIB WEBS, CHORDS, AND SPLICES";

APSAtr“region”11116999253736612862”;

BegAPSBody;

BegAPS "S_035" "rev" "StateList"; *rev*

BegAPSBody;

EndAPS; * end rev *

EndAPS; \*endpara\*

BegAPS“S_036”“para”“APS”； *para*

APSAtr "content" "14 1 'REFER TO SRM 51-70-12 FOR TYPICAL EXTRUDED SECTION REPAIRS TO STIFFENERS";

APSAtr "region"11116999221737912414";

BegAPSBody;

BegAPS "S_037" "callout" "APS"; * callout *

APSAtr "region"1111161127234525082414";

BegAPSBody;

BegAPS "S_038" "refint" "StateList"; * refint *

APSAtr "refid" "14 1 'T-51-70-12";

BegAPSBody;

BegAPS "S_039" "rev" "StateList"; * rev *

BegAPSBody;

EndAPS; * end rev *

EndAPS; * end refint *

EndAPS; \*end callout \*

BegAPS "S_040" "rev" "StateList"; * rev *

BegAPSBody;

EndAPS; * end rev *

EndAPS; \*endpara\*

BegAPS "S_041" "para" "APS"; * para *

APSAtr "content" "14 1 'REFER TO SRM 51-70-12 (TYPICAL EXTRUDED SECTION REPAIRS) FOR AN ALTERNATIVE REPAIR TO RIB CHORDS";

APSAtr "region" "11 1 1 16 4653 2537 7537 2907";

BegAPSBody;

BegAPS "S_042" "callout" "APS"; * callout *

APSAtr "region" "11 1 1 16 4877 2793 6258 2862";

```txt
BegAPSBody;   
BegAPS "S_043" "refint" "StateList"; * refint *   
APSAtr "refid" "14 1 'T-51-70-12";   
BegAPSBody;   
BegAPS "S_044" "rev" "StateList"; * rev *   
BegAPSBody;   
EndAPS; * end rev*   
EndAPS; * end refint *   
EndAPS; * end callout *   
BegAPS "S_045" "rev" "StateList"; * rev *   
BegAPSBody;   
EndAPS; * end rev *   
EndAPS; * end para *   
EndAPS; * end igsheet*   
EndPic;   
EndMF;
```

# 6.3 SGML伴随文件

以下的例子示范了一个伴随版本4 CGM文件的SGML实例。结构的定义包含在CGM文件中，并且相关属性标识在SGML实例中。该实例依赖于DTD技术要求所定义的SGML声明文件的使用。

```txt
<IGSHEET gnbr="S_001"> <PARALD  $id =$  "S_002"content  $\coloneqq$  "Horizontal Stabilizer Rib Repairs"> Horizontal Stabilizer Rib Repairs Figure 201 (Sheet 1) </PARA> <LOCATOR id="S_003"> <CALLOUT id="S_004"> <REFAPS id="S_005" structid="S_006">SEE DETAIL I</REFAPS></CALLOUT></LOCATOR> <DETAIL id="S_006">; <PARALD  $id =$  "S_007">LEFT SIDE SHOWN RIGHT SIDE OPPOSITE DETAIL I</PARA> <PARALD  $id =$  "S_008">HSBL 357.442</PARA> <PARALD  $id =$  "S_009">RIBSAFT OF REAR SPAR</PARA> <PARALD  $id =$  "S_010">CHORD (TYPICAL) </PARA> <PARALD  $id =$  "S_011"content  $\coloneqq$  "RIBSBETWEEN AUXILIARY SPAR AND FRONT SPAR.SEE FIG. 204"RIBSBETWEEN AUXILIARY SPAR AND FRONT SPAR." <CALLOUT id="S_012"> <REFAPS id="S_013"refid="ME_628496">SEE FIG. 204</REFAPS></CALLOUT> <CALLOUT id="S_014"> <REFAPS id="S_015"structid="S_040">A</REFAPS></CALLOUT></PARALD> <PARALD  $id =$  "S_016"content  $\coloneqq$  "FOR WEBS (TYPICAL) SEE FIG. 203 and 203">FOR WEBS (TYPICAL) <CALLOUT id="S_017"> <REFCOND id="S_0018"condition  $\coloneqq$  "202 203"> <REFAPS id="S_019"refid="ME_628494"SEE FIG. 202"></REFAPS> <REFAPSD  $id =$  "S_020"refid="ME_628495">AND   
203</REFAPS></REFCOND></CALLOUT></PARALD> <PARALD  $id =$  "S_021"content  $\coloneqq$  "RIBSBETWEEN FRONT SPAR AND REAR SPAR.SEE FIG. 204">
```

```xml
<CALLOUT id="S_022">
    <REFAPS id="S_023"refid="ME_628496">SEE FIG. 204</REFAPS></CALLOUT>
    <CALLOUT id="S_024">
        <REFAPS id="S_025"structid="S_040">A</REFAPS></CALLOUT></PARAPARAPARAPARAPARAPARAPARAPARAPARAPARAPARAPARAPARAPARAPARAPARAPARAPARAPARAPARAPARAPARAPARAPARAPARAPARAPARAPARAPARAPARAPARAPARAPARAPARAPARAPARAPARAPARAPARAPARAPARAPARAPARAPARAPARAPARAPARAPARAPARAPARAPARAPPARAPARAPARAPARAPARAPARAPARAPARAPARAPARAPARAPARAPARAPARAPARAPARAPARAPARAPARAPARAPARAPARAPARAPARAPARAPARAPARAPARAPARAPARAPARAPARAPARAPARAPARAPARAPARAPARAPARAPARAPARAPARAPARAPARAPARAPARAPARAPARAPARAPARIPRAS TO HORIZONTAL
        <PARAMID="S_031">REAR SPARCNOTES</PARAMID>
    <PARAMID="S_032">RIB NO. 3</PARAMID>
    <PARAMID="S_033">NOTES</PARAMID>
    <PARAMID="S_034">CALL THE BOEING COMPANY FOR REAPIRS TO HORIZONTAL
        CENTER SECTION RIB WEBS, CHORDS, AND SPLICES">
        <REV id="S_035">CALL THE BOEING COMPANY FOR REAPIRS TO HORIZONTAL
        CENTER SECTION RIB WEBS, CHORDS, AND SPLICES</REV></PARALD
        <PARAMID="S_036">REFER TO SRM 51-70-12 FOR TYPICAL EXTRUDED SECTION
            REPAIRS TO STIFFENERS">
            <CALLOUT id="S_037">
                <REFINT id="S_038"refid="T-51-70-12">
                    <REV id="S_039">
                        REFER TO SRM 51-70-12</REV></REFINT></CALLOUT>
            <REV id="S_040">
                FOR TYPICAL EXTRUDED SECTION REPAIRS TO STIFFENERS</REV></PARALD
            <PARAMID="S_041">REFER TO SRM 51-70-12 (TYPICAL EXTRUDED SECTION
            REPAIRS) FOR AN ALTERNATIVE REPAIR TO RIB CHORDS">
            <CALLOUT id="S_042">
                REVINT id="S_043"refid="T-51-70-12">
                <REV id="S_044">
                    REFER TO SRM 51-70-12</REV>
            </REFINT></CALLOUT>
            <REV id="S_045">(TYPICAL EXTRUDED SECTION REPAIRS) FOR AN ALTERNATIVE REPAIR
TO RIB CHORDS</REV></PARALD</IGSHEET>
```

# 5-3 表达方式

# 5-3-1 纸

除按特定详细要求修改的部分之外，下列信息应为制造商出版物采用所有介质的表达方式的格式、样式以及方法提供指南。

# 1 表达方式一纸

# 1.1 文本表达方式

应使用适于由静电印刷、照片翻拍或缩微胶卷等方法生成的黑色图像的打印形式。字符、线等的打印质量应在同一页内、页与页之间以及修订页与修订页之间是统一的。

# 1.1.1 打印尺寸

# 1.1.1.1 字符

对于所有的文本、图表、表等包含的字符应为10或12pitch无衬线(无上划线和下划线)字符，每英寸6行，首选[ECMA-11][ISO推荐1073]标准中关于10pitch字符形式的字母数字字符集OCR-B。

# 1.1.1.2 字符尺寸

对于不符合计算机输出的缩微胶卷(COM)或照片排版的示图、图表、表格、布线图等，标准页面(8.5"×11")和特大型页面(11"x16")上的字符高度应不低于0.075英寸，其大写无衬线字符的线条粗细度应不小于0.009"，且任何字符间距应能够包含直径不小于0.018"的圆。

所有故障描述和故障代码的文本，它的字符高度不应小于0.090英寸。

制造商原始实际尺寸的布线图中的字符或数字的最终打印形式应清晰易读，因此，在缩小到手册尺寸后，它们的最小高度应与本节相关规定相一致。字体应无衬线。

字符间距应不小于0.022", 行间距不应小于0.030英寸。对于由计算机输出的缩微胶卷(COM)所产生的或符合照片排版的示图、图表、表格、布线图等, 其最终放大尺寸的无衬线字符高度不应小于0.060"。

章/节/目题编号应以不小于0.25"高度的字符显示。

# 1.1.1.3 原图

如果文本和/或包括标题和日期的图像的标称高度为20，则提供的用于更新的示图、图表、表格、布线图等的页和它们的字符应是实际标准尺寸或特大型页面尺寸的两倍。

# 1.1.2 表达方法

布线图的布局应安排为从特大型页面的底部开始浏览，在这种情况下，左边对应于飞机的前方。当布线图限制在一个标准尺寸页面中，应从它的右边界来浏览，页面的底部对应于飞机的前方。数字和字符应安排为从页面底部和/或右边界来阅读。

布线图[第91章(系统)]的位置图布局应安排为从特大型页面的底部来浏览，左边对应于飞机的前方。当(布线图的)位置图限制在一个标准尺寸页面中，应从它的右边界来浏览，页面的底部应对于飞机的前方。数字和字符应安排为从页面底部和/或右边界来阅读。

打印的电气和电子设备清单应包括《布线手册》[3-4-7]要求部分中陈述的，按图示(参见[图5-3-1.1])顺序和格式编排的所有信息。另外，打印的手册应在制造商零件号的旁边有一个一英寸宽的空白栏，这是为航空公司的使用而保留的。

图5-3-1.1 样例一设备清单

<table><tr><td>设备</td><td>零件</td><td>航空公司库存号</td><td>零件说明</td><td>销售商位置</td><td>图表</td><td>有效性</td></tr><tr><td>K1</td><td>9274-6686</td><td></td><td>继电器-L跳闸装置组件</td><td>V35344面板PL15</td><td>21-54-01</td><td>全部</td></tr><tr><td>K2</td><td>9274-6686</td><td></td><td>继电器-R跳闸装置组件</td><td>V35344370 358 L14</td><td>21-54-01</td><td>全部</td></tr><tr><td>K3</td><td>6042H92</td><td></td><td>继电器-主舱导管过热</td><td>V15605面板PL15</td><td>21-61-01</td><td>001-015</td></tr><tr><td>K3</td><td>9128-1Z-C7C4-001</td><td></td><td>继电器-主舱导管过热</td><td>V35344面板PL15</td><td>21-61-01</td><td>016-999</td></tr><tr><td>K4</td><td>6041-H169A</td><td></td><td>继电器一直流电子开关无线电总线</td><td>V15605440 158 R26</td><td>24-58-01</td><td>全部</td></tr><tr><td>K5</td><td>BACR-13CD2</td><td></td><td>继电器-左盥洗室后面呼叫</td><td>V812051522 206 L44</td><td>33-27-01</td><td>001-006</td></tr><tr><td>K5</td><td>BACR-13CD3</td><td></td><td>继电器-左盥洗室后面呼叫</td><td>V812051522 206 L44</td><td>33-27-01</td><td>007-999</td></tr><tr><td>K6</td><td>9220-4407</td><td></td><td>继电器-过热试验</td><td>V353442264 180 L85</td><td>26-14-01</td><td>全部</td></tr><tr><td>K7</td><td>9227-6686</td><td></td><td>继电器-高度指示襟翼上升</td><td>V35344430 164 R84</td><td>27-51-01</td><td>全部</td></tr><tr><td>K8</td><td>9227-6686</td><td></td><td>继电器-高度指示襟翼下</td><td>V35344430 164 R84</td><td>27-51-01</td><td>全部</td></tr><tr><td>K9</td><td>6042H92</td><td></td><td>继电器-主电气稳定调整继续</td><td>V15605面板PL15</td><td>27-41-01</td><td>001-011</td></tr><tr><td>K9</td><td>6042H93</td><td></td><td>继电器-主电气稳定调整继续</td><td>V15605面板PL15</td><td>27-41-01</td><td>012-999</td></tr><tr><td>K10</td><td>6041h169A</td><td></td><td>继电器-窗户加温继续左高</td><td>V15605面板PL22</td><td>30-41-01</td><td>001-021</td></tr><tr><td>K10</td><td>DR-18E-1</td><td></td><td>继电器-窗户加温继续左高</td><td>V74063面板PL22</td><td>30-41-01</td><td>022-999</td></tr><tr><td>机型号用户××</td><td>MFRS×××</td><td>修改日期</td><td>手册×××</td><td>设备清单</td><td>节页</td><td>K00001</td></tr></table>

打印的电气导线和接线清单应包含《布线手册》要求部分中陈述的，按图示(参见[图5-3-1.2]和[图5-3-1.3])顺序和格式编排的所有信息。

图5-3-1.2 样例一接线图

<table><tr><td>起始项目</td><td>插针</td><td>导线识别号</td><td>图表</td><td>接至项目</td><td>插针</td><td>有效性</td></tr><tr><td rowspan="47">PO122</td><td>1</td><td>BLA0294</td><td>33-11-51</td><td>P2443</td><td>W</td><td>全部</td></tr><tr><td>2</td><td>BLA0295</td><td>33-11-51</td><td>P2443</td><td>E</td><td>全部</td></tr><tr><td>3</td><td>ARA3017</td><td>27-32-11</td><td>P1483</td><td>1</td><td>全部</td></tr><tr><td>4</td><td>ARA3020</td><td>27-32-11</td><td>TB257</td><td>H15</td><td>001-008</td></tr><tr><td>4</td><td>ARA3026</td><td>27-32-11</td><td>TB248</td><td>H12</td><td>009-999</td></tr><tr><td>5</td><td>BLA0534</td><td>33-11-73</td><td>SP2694</td><td></td><td>全部</td></tr><tr><td>6</td><td>BLA0535</td><td>33-11-73</td><td>SP6296</td><td></td><td>全部</td></tr><tr><td>7</td><td>ARA3021</td><td>27-32-11</td><td>TB220</td><td>H11</td><td>全部</td></tr><tr><td>8</td><td>ARA0101</td><td>27-32-11</td><td>TB220</td><td>G1</td><td>全部</td></tr><tr><td>9</td><td>ARA3023</td><td>27-32-11</td><td>P1525</td><td>6</td><td>全部</td></tr><tr><td>10</td><td>ARA3024</td><td>27-32-11</td><td>P1525</td><td>1</td><td>全部</td></tr><tr><td>11</td><td>ARA3025</td><td>27-32-11</td><td>P1525</td><td>2</td><td>全部</td></tr><tr><td>12</td><td>ARA3004</td><td>27-32-11</td><td>P1480</td><td>7</td><td>全部</td></tr><tr><td>13</td><td>ARA3005</td><td>27-32-11</td><td>P1480</td><td>8</td><td>全部</td></tr><tr><td>14</td><td>ARA3006</td><td>27-32-11</td><td>P1480</td><td>9</td><td>全部</td></tr><tr><td>15</td><td>ARA3007</td><td>27-32-11</td><td>P1480</td><td>10</td><td>全部</td></tr><tr><td>16</td><td>ARA3001</td><td>27-32-11</td><td>P1480</td><td>4</td><td>全部</td></tr><tr><td>17</td><td>ARA3002</td><td>27-32-11</td><td>P1480</td><td>5</td><td>全部</td></tr><tr><td>18</td><td>ARA3003</td><td>27-32-11</td><td>P1480</td><td>6</td><td>全部</td></tr><tr><td>19</td><td>UNUSED</td><td></td><td></td><td></td><td>全部</td></tr><tr><td>20</td><td>UNUSED</td><td></td><td></td><td></td><td>全部</td></tr><tr><td>21</td><td>ARA3018</td><td>27-32-11</td><td>P1483</td><td>2</td><td>全部</td></tr><tr><td>22</td><td>ARA3019</td><td>27-32-11</td><td>P1483</td><td>3</td><td>全部</td></tr><tr><td>23</td><td>ARC1051</td><td>27-35-11</td><td>SP7082</td><td></td><td>全部</td></tr><tr><td>24</td><td>ARC1005</td><td>27-35-11</td><td>P1517</td><td>1</td><td>全部</td></tr><tr><td>25</td><td>ARA3026</td><td>备用</td><td>P1480</td><td>12</td><td>001-003</td></tr><tr><td>26</td><td>UNUSED</td><td></td><td></td><td></td><td>全部</td></tr><tr><td>27</td><td>UNUSED</td><td></td><td></td><td></td><td>-001-012</td></tr><tr><td>27</td><td>DBC232</td><td>31-35-21</td><td>TB145</td><td>G4</td><td>013-999</td></tr><tr><td>28</td><td>UNUSED</td><td></td><td></td><td></td><td>全部</td></tr><tr><td>29</td><td>UNUSED</td><td></td><td></td><td></td><td>全部</td></tr><tr><td>30</td><td>UNUSED</td><td></td><td></td><td></td><td>全部</td></tr><tr><td>31</td><td>ARA3013</td><td>27-32-11</td><td>P1495</td><td>9</td><td>全部</td></tr><tr><td>32</td><td>ARA3012</td><td>27-32-11</td><td>P1495</td><td>8</td><td>全部</td></tr><tr><td>33</td><td>ARA3011</td><td>27-32-11</td><td>P1495</td><td>7</td><td>全部</td></tr><tr><td>34</td><td>UNUSED</td><td></td><td></td><td></td><td>全部</td></tr><tr><td>35</td><td>ARA3010</td><td>27-32-11</td><td>P1495</td><td>6</td><td>全部</td></tr><tr><td>36</td><td>ARA3009</td><td>27-32-11</td><td>P1495</td><td>5</td><td>全部</td></tr><tr><td>37</td><td>ARA3008</td><td>27-32-11</td><td>P1495</td><td>4</td><td>全部</td></tr><tr><td>38</td><td>UNUSED</td><td></td><td></td><td></td><td>全部</td></tr><tr><td>39</td><td>ARA3014</td><td>27-32-11</td><td>P1495</td><td>10</td><td>013-999</td></tr><tr><td>40</td><td>ARA3015</td><td>27-32-11</td><td>P1495</td><td>2</td><td>全部</td></tr><tr><td>41</td><td>ARA3017</td><td>备用</td><td>空端</td><td></td><td>001-003</td></tr><tr><td>42</td><td>UNUSED</td><td></td><td></td><td></td><td>全部</td></tr><tr><td>43</td><td>UNUSED</td><td></td><td></td><td></td><td>全部</td></tr><tr><td>44</td><td>UNUSED</td><td></td><td></td><td></td><td>全部</td></tr><tr><td>45</td><td>UNUSED</td><td></td><td></td><td></td><td>全部</td></tr><tr><td colspan="7">制造商 ×××布线手册 连接图表 章节 P0100 出版日期 1973.04.25 91-21-01 页3</td></tr></table>

图5-3-1.3 样例一导线清单

<table><tr><td>导线</td><td>标识符</td><td>线规</td><td>类型</td><td>种类</td><td>长度</td><td>图表</td><td>设备</td><td>插针</td><td>设备</td><td>插针</td><td>有效性</td></tr><tr><td>ARA3001</td><td>R</td><td>24</td><td>VC</td><td>AA</td><td>8</td><td>27-32-11</td><td>P122</td><td>16</td><td>P1480</td><td>4</td><td>全部</td></tr><tr><td>ARA3002</td><td>B</td><td>24</td><td>VC</td><td>AA</td><td></td><td>27-32-11</td><td>P122</td><td>17</td><td>P1480</td><td>5</td><td>全部</td></tr><tr><td>ARA3003</td><td>Y</td><td>24</td><td>VC</td><td>AA</td><td></td><td>27-32-11</td><td>P122</td><td>18</td><td>P1480</td><td>6</td><td>全部</td></tr><tr><td>ARA3004</td><td>R</td><td>24</td><td>VC</td><td>AB</td><td>8</td><td>27-32-11</td><td>P122</td><td>12</td><td>P1480</td><td>7</td><td>全部</td></tr><tr><td>ARA3005</td><td>B</td><td>24</td><td>VC</td><td>AB</td><td></td><td>27-32-11</td><td>P122</td><td>13</td><td>P1480</td><td>8</td><td>全部</td></tr><tr><td>ARA3006</td><td>Y</td><td>24</td><td>VC</td><td>AB</td><td></td><td>27-32-11</td><td>P122</td><td>14</td><td>P1480</td><td>9</td><td>全部</td></tr><tr><td>ARA3007</td><td></td><td>22</td><td>UF</td><td></td><td>8</td><td>27-32-11</td><td>P122</td><td>15</td><td>P1480</td><td>10</td><td>全部</td></tr><tr><td>ARA3008</td><td>R</td><td>24</td><td>VC</td><td>AC</td><td>8</td><td>27-32-11</td><td>P122</td><td>37</td><td>P1495</td><td>4</td><td>全部</td></tr><tr><td>ARA3009</td><td>B</td><td>24</td><td>VC</td><td>AC</td><td></td><td>27-32-11</td><td>P122</td><td>36</td><td>P1495</td><td>5</td><td>全部</td></tr><tr><td>ARA3010</td><td>Y</td><td>24</td><td>VC</td><td>AC</td><td></td><td>27-32-11</td><td>P122</td><td>35</td><td>P1495</td><td>6</td><td>全部</td></tr><tr><td>ARA3011</td><td>R</td><td>24</td><td>VC</td><td>AD</td><td>8</td><td>27-32-11</td><td>P122</td><td>33</td><td>P1495</td><td>7</td><td>全部</td></tr><tr><td>ARA3012</td><td>B</td><td>24</td><td>VC</td><td>AD</td><td></td><td>27-32-11</td><td>P122</td><td>32</td><td>P1495</td><td>8</td><td>全部</td></tr><tr><td>ARA3013</td><td>Y</td><td>24</td><td>VC</td><td>AD</td><td></td><td>27-32-11</td><td>P122</td><td>31</td><td>P1495</td><td>9</td><td>全部</td></tr><tr><td>ARA3014</td><td></td><td>22</td><td>UF</td><td></td><td>8</td><td>27-32-11</td><td>P122</td><td>39</td><td>P1495</td><td>10</td><td>013-999</td></tr><tr><td>ARA3015</td><td></td><td>22</td><td>UF</td><td></td><td>8</td><td>27-32-11</td><td>P122</td><td>40</td><td>P1495</td><td>2</td><td>全部</td></tr><tr><td>ARA3017</td><td></td><td>22</td><td>UF</td><td></td><td>8</td><td>备用</td><td>P122</td><td>41</td><td>空端</td><td></td><td>001-003</td></tr><tr><td>ARA3018</td><td></td><td>22</td><td>UF</td><td></td><td>8</td><td>27-32-11</td><td>P122</td><td>21</td><td>P1483</td><td>2</td><td>全部</td></tr><tr><td>ARA3019</td><td></td><td>22</td><td>UF</td><td></td><td>8</td><td>27-32-11</td><td>P122</td><td>22</td><td>P1483</td><td>5</td><td>全部</td></tr><tr><td>ARA3020</td><td></td><td>22</td><td>UF</td><td></td><td>8</td><td>27-32-11</td><td>P122</td><td>4</td><td>TB257</td><td>H15</td><td>全部</td></tr><tr><td>ARA3021</td><td></td><td>22</td><td>UF</td><td></td><td>8</td><td>27-32-11</td><td>P122</td><td>7</td><td>TB220</td><td>H11</td><td>全部</td></tr><tr><td>ARA3022</td><td></td><td>22</td><td>UF</td><td></td><td>5</td><td>27-32-11</td><td>TB220</td><td>H11</td><td>P1507</td><td>13</td><td>全部</td></tr><tr><td>ARA3023</td><td></td><td>22</td><td>UF</td><td></td><td>8</td><td>27-32-11</td><td>P122</td><td>9</td><td>P1525</td><td>6</td><td>全部</td></tr><tr><td>ARA3024</td><td></td><td>22</td><td>UF</td><td></td><td>8</td><td>27-32-11</td><td>P122</td><td>10</td><td>P1525</td><td>1</td><td>全部</td></tr><tr><td>ARA3025</td><td></td><td>22</td><td>UF</td><td></td><td>8</td><td>27-32-11</td><td>P122</td><td>11</td><td>P1525</td><td>2</td><td>全部</td></tr><tr><td>ARA3026</td><td></td><td>22</td><td>UF</td><td></td><td>8</td><td>备用</td><td>P122</td><td>25</td><td>P1480</td><td>12</td><td>001-003</td></tr><tr><td>ARA3031</td><td></td><td>16</td><td>UA</td><td></td><td>7</td><td>27-32-11</td><td>P1563</td><td>10</td><td>TB257</td><td>H15</td><td>全部</td></tr><tr><td rowspan="9" colspan="12">制造商 ×××布线手册 出版日期 04.25/73 导线目录 章节</td></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr></table>

有效页目录(LEP)应规定为横向栏格式。(关于纸张输出的示图参见[图5-3-1.4])。

图5-3-1.4 样例一维修手册一系统说明部分的有效页目录

<table><tr><td colspan="8">有效页目录</td></tr><tr><td>章-节-题目</td><td>配置</td><td>页</td><td>日期</td><td>章-节-题目</td><td>配置</td><td>页</td><td>日期</td></tr><tr><td>27-00-00</td><td></td><td>1</td><td>1991.01.15</td><td>27-10-00</td><td></td><td>18</td><td>1991.01.15</td></tr><tr><td>27-00-00</td><td></td><td>2</td><td>1991.01.15</td><td>27-10-00</td><td></td><td>19</td><td>1991.01.15</td></tr><tr><td>27-00-00</td><td></td><td>3</td><td>1991.01.15</td><td>27-10-00</td><td></td><td>20</td><td>1991.01.15</td></tr><tr><td>27-00-00</td><td></td><td>4</td><td>1991.01.15</td><td>27-10-00</td><td></td><td>21</td><td>1991.01.15</td></tr><tr><td>27-00-00</td><td></td><td>5</td><td>1991.01.15</td><td>27-10-00</td><td></td><td>22</td><td>1991.01.15</td></tr><tr><td>27-00-00</td><td></td><td>6</td><td>1991.01.15</td><td>27-10-00</td><td></td><td>23</td><td>1991.01.15</td></tr><tr><td>27-00-00</td><td></td><td>7</td><td>1991.01.15</td><td>27-10-00</td><td></td><td>24</td><td>1991.01.15</td></tr><tr><td>27-00-00</td><td></td><td>8</td><td>1991.01.15</td><td>27-10-00</td><td></td><td>25</td><td>1991.01.15</td></tr><tr><td>27-00-00</td><td></td><td>9</td><td>1991.01.15</td><td>27-10-00</td><td></td><td>26</td><td>1991.01.15</td></tr><tr><td>27-00-00</td><td></td><td>10</td><td>1991.01.15</td><td>27-10-00</td><td></td><td>27</td><td>1991.01.15</td></tr><tr><td>27-00-00</td><td></td><td>11</td><td>1991.01.15</td><td>27-10-00</td><td></td><td>28</td><td>1991.01.15</td></tr><tr><td>27-00-00</td><td></td><td>12</td><td>1991.01.15</td><td>27-10-00</td><td></td><td>29</td><td>1991.01.15</td></tr><tr><td>27-00-00</td><td></td><td>13</td><td>空白</td><td>27-10-00</td><td></td><td>30</td><td>1991.01.15</td></tr><tr><td>27-10-00</td><td></td><td>1</td><td>1991.01.15</td><td>27-10-00</td><td></td><td>31</td><td>1991.01.15</td></tr><tr><td>27-10-00</td><td></td><td>2</td><td>1991.01.15</td><td>27-10-00</td><td></td><td>32</td><td>1991.01.15</td></tr><tr><td>27-10-00</td><td></td><td>3</td><td>1991.01.15</td><td>27-10-00</td><td></td><td>33</td><td>1991.01.15</td></tr><tr><td>27-10-00</td><td></td><td>4</td><td>1991.01.15</td><td>27-10-00</td><td></td><td>34</td><td>1991.01.15</td></tr><tr><td>27-10-00</td><td></td><td>5</td><td>1991.01.15</td><td>27-10-00</td><td>1</td><td>35</td><td>1991.01.15</td></tr><tr><td>27-10-00</td><td></td><td>6</td><td>1991.01.15</td><td>27-10-00</td><td>2</td><td>35</td><td>1991.01.15</td></tr><tr><td>27-10-00</td><td></td><td>7</td><td>1991.01.15</td><td>27-10-00</td><td></td><td>36</td><td>1991.01.15</td></tr><tr><td>27-10-00</td><td></td><td>8</td><td>1991.01.15</td><td>27-10-00</td><td></td><td>37</td><td>1991.01.15</td></tr><tr><td>27-10-00</td><td></td><td>9</td><td>1991.01.15</td><td>27-10-00</td><td></td><td>38</td><td>1991.01.15</td></tr><tr><td>27-10-00</td><td></td><td>10</td><td>1991.01.15</td><td>27-10-00</td><td></td><td>39</td><td>1991.01.15</td></tr><tr><td>27-10-00</td><td></td><td>11</td><td>1991.01.15</td><td>27-10-00</td><td></td><td>40</td><td>1991.07.15</td></tr><tr><td>27-10-00</td><td></td><td>12</td><td>1991.01.15</td><td>27-10-00</td><td></td><td>41</td><td>1991.07.15</td></tr><tr><td>27-10-00</td><td></td><td>13</td><td>1991.01.15</td><td>27-10-00</td><td></td><td>42</td><td>1991.07.15</td></tr><tr><td>27-10-00</td><td></td><td>14</td><td>1991.01.15</td><td>27-10-00</td><td></td><td>43</td><td>1991.07.15</td></tr><tr><td>27-10-00</td><td></td><td>15</td><td>1991.01.15</td><td>27-10-00</td><td></td><td>44</td><td>1991.07.15</td></tr><tr><td>27-10-00</td><td></td><td>16</td><td>1991.01.15</td><td>27-10-00</td><td></td><td>45</td><td>1991.07.15</td></tr><tr><td>27-10-00</td><td></td><td>17</td><td>1991.01.15</td><td>27-10-00</td><td></td><td>46</td><td>1991.07.15</td></tr></table>

目录页应采用双栏格式。（关于纸张输出的示图参见[图5-3-1.5]）。

![](images/5719b32571c1791bb52fcf0a163eae3de879d364ac7a75e75fcc8b1355bdaf65.jpg)  
图5-3-1.5 样例一SDS的目录

# 1.1.2.1 复制标准

所有文本应在单个栏内进行处理，不要求对齐页面右边界。除布线图页、折页和用于缩微胶卷的页外，所有的页均应为双面打印。当示图被水平地复制在页面上时，示图的顶部应始终朝向图页的左边（参见[图5-3-1.6])。所有包含文本或示图的页面上应包含制造商的名称和出版物标题。

![](images/f09679899dfc020b73f786ce1d5d473123c0cad98c9980cb731c4485e0baf3ee.jpg)  
图5-3-1.6 样例一质量控制目标

重量与平衡手册的“飞行报告”章中的页面不必双面打印。

# 1.1.2.2. 页边距限制

装订边界为1.12英寸，外边界为0.62英寸，上边界为1.00英寸，下边界为1.00英寸。

注：除1.12"装订边界外，任何一种边界限制都可以进行调整。

注：所有页面都有一个0.625英寸的上边界。该位置的下部0.5英寸处应包括制造商标识、飞机型别和手册标题(故障报告手册)。与装订边界相对的位置应有0.25英寸的页边空白。

注：除装订边界应为1.12英寸外，边界限制应不适用。

在页面左上角应留出一个2.00英寸  $\times 0.75$  英寸的空白区域，以允许个别操作者用来标记页码。该空白区域可以是顶部空白的一部分。

应在标题的顶部与页面的上边界之间的左边留出一个0.38英寸的空白区域，以允许打印机夹紧纸张。

进行页面边距设置时可将下边界缩减为1.00英寸。

![](images/1ef185ee54c24916007a20c542d97f900b8397ee60cdb44bc79107f226f7f7dd.jpg)  
图5-3-1.7 样例一《服务通报》页面，纵向布局

![](images/0d07791847c13e19452a17512d3313174583d811f16852c174e431ff4e0ca588.jpg)  
图5-3-1.8 样例一临时更改单页面一纵向布局

![](images/e13d7f46aa97258938caca45e1c755350dba193b09792d4d4422035c45084c2d.jpg)  
图5-3-1.9 样例一临时更改单页面一横向布局

![](images/533cd803e26aa9e65b3b4ba726043f5361b390414a9f3c603d8e56f1f8eb2ca2.jpg)  
图5-3-1.10 样例一故障报告手册(FRM)布局

![](images/73ecfebc777806257010770bae8ed91baa2cc6782a3a8c3d42b065dd88a56c82.jpg)  
图5-3-1.11 样例一手册页面，纵向布局[m101101]

![](images/873fdfa7b0f19624d670b8a1225fbdc93db58fd0731d6c17afc41a9570c307db.jpg)  
图5-3-1.12 样例一手册页面，横向布局[m101102]

# 1.1.2.3 页的编号方式和日期

所有出版物的首页应是一个右手页，并且页码应位于页脚中且右对齐。

每一页在页面的右下角必须具有章/节/题目、页码和日期，且不应占据边界空白的位置。（对于右手页），章/节/题目号应放置在页码和日期的左侧，它们之间的间距不超过五个字符间距。（参见[图5-3-1.11]和[图5-3-1.12])。

政府的规章要求制造商的页码标记应打印在页面装订线以内。

所有前置材料应由它们的名称、页码和日期来标识。每一个标题应从右手页开始。

当使用页号组时，页的编号应从右手页开始。页号组中包含的标准空白页的页码应标识在前一页，在两个页码之间画一条斜线。

- 每一页应带有服务通报编号。页码应直接放置在服务通报编号的下面(参见下列典型实例)。每个服务通报页应从第1页开始编号。在所有要求页码编排的部分，页码应连续。另外，服务通报的标题页应说明整个服务通报所包含的总页数。

表5-3-1.1 服务通报页码编号方式  

<table><tr><td>例子</td><td>例子</td></tr><tr><td>RTA41-23-1 共 4 页, 第 1 页</td><td>747-21-1 共 6 页, 第 1 页</td></tr><tr><td>RTA41-23-2 共 5 页, 第 1 页</td><td>747-21-2 共 7 页, 第 1 页</td></tr></table>

发动机改装服务通报的每个主要部分都应具有单独的页页组并编号(例如计划信息、实施指令和材料信息)。其中, 附加页号组可用于在章/节级别或其它的数据逻辑划分点, 以便有效地隔离信息。

除标题页外的所有前置材料应由 ATA 编号的 3 要素、分节 (参见[3-1-3.1])、页码和出版日期(参

见[图3-1-5.2])来标识。每一分节应从右手页开始。

如果前一个图的最后一个文本页是一个右手页，则新增示图(图形)可以放置在该右手页的背面。如果前一个图的最后一个文本页是一个左手页，则新增示图(图形)可以放置在一个空白右手页的背面。

如果分系统或分分系统级别必需一幅示图(图形)，在这种极端情况下，该示图可以放在该节标题页的背面。

下列实例图示了一个典型手册页面。请注意，章/节/题目和页进行了标识(参见[图5-3-1.13])：

# 制造商名称

# 手册的名称

# 增压叶片作动筒——维护实施

# 1. 增压叶片作动筒的拆卸/安装

![](images/40cf0f5f7f095007d2830b3b1c1afac05961326288c89527ffd7cbae51688da1.jpg)  
图5-3-1.13 页面编号实例[m101301a]

A. 增压叶片作动筒的拆卸。

(1) 拆掉2个维护口盖的增压导管。  
(2）分解作动筒和位置指示器的电插头。

注意：为便于以后安装，观察并记住衬套和垫圈的装配顺序。

(3）拆卸稳定器拉杆与摇臂插销螺栓的连接螺栓。  
(4）拆卸作动筒与摇臂连接的插销螺栓。

B. 安装的准备。

![](images/3140caa9b3238fd0a6aba8dad76a7dd31e89df2327502e42fa2edb18a2aa76c5.jpg)

注意：作动筒的行程已在工厂调整好。不允许调整中间的轴或限动开关。搬运作动筒时应小心以免转动作动筒的头部和改变工厂已调好的位置。

(1) 从旧的叶片作动筒上拆卸增压叶片传感器和支架组件。并在大致相同的位置安装替换的传感器和支架组件。

注：作动筒分左右件，左右件的件号不同。

(2) 按下述步骤调定叶片位置传感器：

警告：设备通电工作时要格外小心。

(a) 连接作动筒电插头，并将作动筒与机翼结构紧挨着接地。将驾驶舱中的增压叶片控制开关扳到“拖曳”位置。检查作动筒是否收回到后极限位置。

注：除冰加温开关，必须接通或者辅助加热控制开关必须在“准备”位置。

(b) 连接位置传感器电插头。变流机电源接通并且作动筒接地后，移动位置传感器杆在作动筒中间轴上的夹子，以使驾驶舱中的位置指针指向拖曳固定传感器组件。  
(3) 检查作动筒极限开关的罩子上钻有合适的排放孔并且位置合适。

有效性：全部

78-11-02

201页

1980.06.27

注：修理编号/构型等应直接显示在章/节/题目下面。

在要求折叠的页上进行折叠时，应使页码可见(参见[图3-1-12.17])。页号组中的标准空白页的页码应在前一页进行标识(例如折叠页的背面)。

# 1.1.2.3.1 简明机载设备维修手册(ACMM)

在简明机载设备维修手册(ACMM)中，页码应从第1页开始显示，并应显示总页数；例如，共8页，第1页。

更改日期应在所有页中出现。

允许将资料的若干个小标题组合在一个页上。

# 5-3-2 缩微胶卷形式

# 1 表达方式一胶卷

# 1.1 胶卷的设计

当进行24:1(连环画面模式)拍摄时，图像的放置应使11英寸页边垂直于胶片的长边。当使用36:1缩影时，这些页的11英寸页边应平行于胶片的长边（电影模式）， $8.5^{\prime \prime} \times 11^{\prime \prime}$  的页应成对并排拍摄（参见[图5-3-2.1])。

![](images/f6f40770924846b49326d3ccd224ca4813e8c0ad44eef0554e6cb5213df03940.jpg)

![](images/36f5e0722536991c8d1dee7946f958220b459fb42ee6990bc64f8297a457cf08.jpg)  
→

![](images/82c41fb5c0abb92f68ed7dc054d1d48f56c65a11721c34e464672967af08b544.jpg)  
25

![](images/e3e1b503fb36ee4a5ff8084f0fb87a7ba159730108a325bc634b1d5a167601a0.jpg)

![](images/6949ee666ab6629a08c9a1b44364af811334924472e9665ff36db885536cec86.jpg)  
25

![](images/2df60cff9a21f24e22de58ecb0df9ae09a938bd5038ebc396372f99f96a15f3e.jpg)

![](images/38b8c804d8b8d072b54cb50c31807d38f91b6567e52b0969401574d52c5ac92e.jpg)

![](images/6c163d2306471321b70971984b7bf08dc67269022fe637f76c5d821ffd8ad338.jpg)

![](images/ec47ed483f4b6a927d133769b2911455e5d2fd1fc77cb76dd148954e6e3608ec.jpg)

![](images/0ca3aca1f252cf223a70b17523d6f0e5eeed426e24525d38286074947ee5cca4.jpg)  
图5-3-2.1 样例一胶卷的页面设计

24:1 缩影拍摄（连环画面模式），显示章号前导段、章标题和章号，以及  $8_{2}^{1}\times 11$  和“ $11\times 16$ ”页面布局。

![](images/a905abd63014e60f23397f13a7baeedae34fcb2f864c98d2dbc5e32c229131e4.jpg)

![](images/5f2b96d51e54ad639cb57dedafed97ed7fae4f6dfcce1edcbaa72305f110bb9b.jpg)

![](images/141766ab2381520a823769abf8953be44f65cf0ac0470ea2e14b05be1185aace.jpg)

![](images/e88872d0f06126e6d0eb56ee821d4cb44342ddaa75205def26a095db7eb7753f.jpg)

![](images/3d5c49b0a286a486a127f3320c8db889bd9d2e0c17a588550acf4420767e3c98.jpg)

![](images/ef1ee2d1182bc97cf40ed3070f6985755e060f7f84e78c1cf0bd3b0be902c0d4.jpg)

![](images/e08e96211a012dd49e99ebacaa4ba24901ccb259a0e8bb794eee78718fbf57b0.jpg)

![](images/e234bf16fb5073ad1bb498a0759d263a9c29f39d059d515f017e88ded784463d.jpg)

36:1 缩影拍摄（电影模式），显示章号前导段、章标号和章号，以及  $8_{2}^{1}\times 11$  和“  $11\times 16$  ”页面布局。

除非操作员有其它规定，否则胶片上的曝光图像应位于  $16\mathrm{mm}$  宽度胶片的中心  $\pm 0.76\mathrm{mm}$  处。胶片上图像之间的间距不应超过  $3\mathrm{mm}(0.125^{\prime \prime})$  。

页面应按正确的顺序被拍摄。对于36:1成对缩影拍摄的页面，应始终按照右手页跟随左手页的顺序编排。

每卷胶卷的第一幅图像应是手册的标题页，包括设备类型标识、标题内容、编码和分发日期，并用尽可能大的字符。

每卷胶卷的第二幅图像应是一个质量控制目标页。缩微复制分辨率测试图表[NIST SRM 1010a]或可选[ISO 3334]2号测试图表应以  $20 - 1\mathrm{b}$  磅大小放置于图像中心。以白色为底色，垂直线平行于帧的边线。在页面的每一个角上都应有一个测试图表的副本，其垂直线与帧边线成45度角。反射系数为  $6\%$  的2英寸纯黑正方形应放置在测试图表的一侧，黑色外框的2英寸白色正方形应放置在测试图表的另一侧。（参见[图5-3-1.6])

每卷胶卷的最后一幅图像应与如上所述的第二幅图像相同。

对于24:1缩影，每章开始的前10幅图像应由章号引导，后跟该章标题和章号的一幅图像组成。对于36:1缩影，前10对图像应由章号引导，后跟该章标题和章号的一对图像组成。（参见[图5-3-2.1]和[图5-3-2.2])。

![](images/f7cfe8c159306c2d5e24590d8db8e47fd3b0ecfdaf4458cb9cc0ffd38c91f5ee.jpg)  
图5-3-2.2 样例一字体大小和样式

除非一章的内容超出了一卷胶卷的容量，否则应一次完成拍摄，不将一章内容分开到两卷胶片中。

在每卷胶卷上，所拍摄的第一幅图像之前和最后一幅图像之后应有3英尺的空白胶片。除非操作员规定，否则不要求为检索目的而对胶卷进行索引。

如果要拍摄临时更改单，则临时更改单在拍摄前应放置在出版物中受影响的那一页之后。

受临时更改影响的正常页面在拍摄前应用一个指向邻近临时更改单的大箭头来标记，以引起读者对所存在的临时更改的注意。

# 1.2 缩微比率

操作员规定的缩微比率应为24:1或36:1。

# 1.3 密度和分辨率

在每一幅质量控制目标图像(参见[图5-3-1.6])上的白色正方形的背景密度通常应在视觉扩散传播密度1.0和1.2之间，相同目标图像上的黑色正方形的密度不应超过0.1。如果缩微过程中黑色正方形的视觉扩散传播密度不超过0.1，那么白色正方形的视觉扩散传播密度最大到1.5是可接受的，这可作为一种备选方式，视觉扩散传播密度应满足[ISO6200](2和3组)(缩微照相术一银的密度一明胶片)的要求。这些图形仅适用于第一次和第二次生成的用于为分发而制作复制件的镀银负片。如果第二次生成的镀银负片具有阳性，则操作员应规定它的密度要求。为了使后续生产胶片(的)衰减最小，分辨率不应低于下面列出的数值。

表 5-3-2.1 原版底片分辨率表  

<table><tr><td></td><td>负片</td><td colspan="3">复制的胶片</td></tr><tr><td></td><td>第一次生产</td><td colspan="3">第二次生产</td></tr><tr><td>缩微比率</td><td>最小值</td><td>分辨率线/mm</td><td>最小值</td><td>分辨率线/mm</td></tr><tr><td>24X</td><td>5.0</td><td>120</td><td>4.5</td><td>108</td></tr><tr><td>36X</td><td>4.0</td><td>144</td><td>3.6</td><td>130</td></tr></table>

注：胶片类型、基材、厚度、以及阴性或阳性应由操作员规定。如果操作员规定第二次生产的复制底片为阳性，他也应规定其分辨率的要求。

# 1.4 拼接

在复制用原版胶卷中应不允许拼接。原版镀银负片中允许拼接。采用热熔拼接技术，每个拼接处与相邻拍摄图像隔开的最小宽度为  $2\mathrm{mm}$  。其它拼接形式仅允许用于章之间，这样的拼接处与相邻拍摄图像隔开的最小宽度为  $2.5\mathrm{mm}$  。

# 1.5 胶卷的复制件

注：包装(胶卷筒、胶卷盒、标签等)类型应由操作员规定。

分辨率应不低于下表中列出的各项数值：

表 5-3-3.2 分发的复制件分辨率  

<table><tr><td>缩微比率</td><td>最小值</td><td>分辨率线/mm</td></tr><tr><td>24X</td><td>4.0</td><td>98</td></tr><tr><td>36X</td><td>3.2</td><td>115</td></tr></table>

注：胶卷的类型、基材、厚度、颜色以及阴性或阳性应按照操作员的规定。

除了首尾外，不允许拼接其它部位。

应将章的完整内容按照可行的方式尽可能紧密地填充到胶卷盘、胶卷筒、胶卷盒等中，尽量不要对章进行分割。

# 2 表达方式一缩微胶片

用于生产原版缩微胶片的原始文件的质量应符合可复制性和清晰性的相关要求。

应根据操作者的要求提供原版和/或中间版的缩微胶片，以允许复制分发用的缩微胶片。它们应能生产符合质量标准规定的分发用的缩微胶片。标题背景应不适用本规定。

# 2.1 缩微胶片的设计

仅提供24X的有效缩影的缩微胶片格式类型1(14列  $\times 7$  行  $= 98$  帧)（参见[图5-3-2.3])。

缩微胶片应按照操作者的要求以负片或阳片的形式提供。

对于信息区域不能包含在单帧或双帧中的一个文件，既不应分段，也不应以低于标准的缩减分辨率进行拍摄。必须以正确的尺寸制作原版。

标题应出现在指定的保留区域(参见[图5-3-2.3])。

标题内容不应使用附加行。

除非操作员规定其它颜色作为背景色或无背景色，否则标题背景应为白色。标题应如下方式排列，从左手边开始，在图示(参见[图5-3-2.4])的位置使用空格定位。

1. 制造商徽标。(参见下面的注)  
2. 手册或目录标题。  
3. 个别缩微胶片的内容包括章/节/题目（对于零件目录也包含图形编号）、章标题以及特殊缩微胶片的简要内容。  
4. 缩微胶片的文件编号由章号后跟一个文件顺序号组成，每章的序号从“1”开始。例如，27-1、27-2、28-1、28-2等。  
5. 缩微胶片的修改日期应显示在标题区域的右下部。

图5-3-2.3 样例一缩微胶片、布局和尺寸  
![](images/ce9a52bedd942e970cfce4bba3ba62ceab4f9f8581877357d59c1ff633d5e232.jpg)  
注：如果出版物是用户定制的，那么航空公司徽标也必须位于该区域内。

![](images/618aff76cc6e426af2faf5beb3d9d74c8e3fbeb82aeb5fa80c71ce7bd7e2ae63.jpg)  
图5-3-2.4 标题样例一零件目录样例一缩微胶片、标题布局

缩微图像的定位采用字母数字坐标标识的方法。

根据[3-1-5.7]，每个缩微胶片的第一帧或其它各帧(A1、A2等)都应包含一个目录，并应只列出那些特殊缩微胶片的内容。应提供一个附加栏，以便在使用目录选择对应页时，可给出该页的缩微胶片X-Y坐标(参见[图5-3-2.5])。

图5-3-2.5 样例一缩微胶片、目录

<table><tr><td colspan="5">制造商的名称</td></tr><tr><td colspan="4">图解零件目录</td><td>胶片26-3</td></tr><tr><td>题目</td><td>章节题目</td><td>图</td><td>有效性</td><td>随机存取器</td></tr><tr><td>灭火</td><td>26-21-00</td><td></td><td></td><td></td></tr><tr><td>辅助动力装置(APU)的灭火系统</td><td></td><td></td><td></td><td></td></tr><tr><td>涡轮盘,热释放指示器——机身中段</td><td></td><td></td><td></td><td></td></tr><tr><td>站位870到904.50主起落架舱门到左机翼整流罩</td><td>26-21-01</td><td>1</td><td></td><td>A2</td></tr><tr><td>喷嘴的安装——机身中段,龙骨架区域</td><td>26-21-03</td><td>1</td><td></td><td>A5</td></tr><tr><td>喷嘴</td><td></td><td></td><td></td><td></td></tr><tr><td>螺母</td><td></td><td></td><td></td><td></td></tr><tr><td>管接头</td><td></td><td></td><td></td><td></td></tr><tr><td>面板的安装,地面控制——左机翼站位215</td><td>26-21-04</td><td>1</td><td>901913</td><td>A8</td></tr><tr><td>面板的安装,地面控制——左机翼站位215</td><td>26-21-04</td><td>1A</td><td>914999</td><td>B1</td></tr><tr><td>灭火瓶</td><td></td><td></td><td></td><td></td></tr><tr><td>支架组件——防火切断开关</td><td></td><td></td><td></td><td></td></tr><tr><td>弹簧——控制板</td><td></td><td></td><td></td><td></td></tr><tr><td>开关及作动机构——灭火瓶的喷散</td><td></td><td></td><td></td><td></td></tr><tr><td>开关组件——火警关断</td><td></td><td></td><td></td><td></td></tr><tr><td>管路的安装——左机身中段、机轮舱和机翼内段</td><td>26-21-02</td><td>1</td><td></td><td>A3</td></tr><tr><td>转接头</td><td></td><td></td><td></td><td></td></tr><tr><td>软管</td><td></td><td></td><td></td><td></td></tr><tr><td>密封件</td><td></td><td></td><td></td><td></td></tr><tr><td>导管</td><td></td><td></td><td></td><td></td></tr><tr><td>减压阀</td><td></td><td></td><td></td><td></td></tr><tr><td>发动机灭火系统</td><td></td><td></td><td></td><td></td></tr><tr><td>灭火瓶和阀的安装——机身尾段、站位1183</td><td>26-22-00</td><td>1</td><td></td><td>C1</td></tr><tr><td>角撑——支架</td><td></td><td></td><td></td><td></td></tr><tr><td>灭火瓶</td><td></td><td></td><td></td><td></td></tr><tr><td>指示器——喷散</td><td></td><td></td><td></td><td></td></tr><tr><td>指示器——热释放</td><td></td><td></td><td></td><td></td></tr><tr><td>导管</td><td></td><td></td><td></td><td></td></tr><tr><td>关断阀</td><td></td><td></td><td></td><td></td></tr><tr><td>手柄组件——火警关断(参见26-00-00遮光板的安装)</td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td>26-目录3页1968.05.06</td></tr></table>

根据[3-1-5.7]，对每个缩微胶片都应制作目录，并只列出那些特殊缩微胶片的内容。应提供一个附加栏，对于目录每项对应选择的页，显示缩微胶片的字母数字坐标(参见[图5-3-2.5])。

章目录应被拍摄在每章的第一个缩微胶片上。

手册或目录集中的第一个缩微胶片(INTRO-1)应包含缩微胶片的有效目录，便于航空公司操作员在任何时候确定手册是现行有效的。有效缩微胶片的目录应用数字列出缩微胶片，并显示每个缩微胶片的发行日期。有效缩微胶片的目录的更改应与每次修订保持一致(参见[图5-3-2.6])。

![](images/79fd005e5a5237ce4018681c9de14cc2a633ef81cb8c7971837ba4756751206c.jpg)  
图5-3-2.6 样例一有效缩微胶片的目录

对于缩微胶片式的手册或目录，应根据操作员的要求提供纸质打印的有效页目录。

每一个缩微胶片应具有一个有效日期；该日期可以是原始发布日期，如果有修订的，则是最新修订日期。

纸质发送函应涵盖缩微胶片出版物的每一处更改。另外，按[3-1-5.1]的要求，发送函应指明缩微胶片的删除和插入的情况，修订提要应按缩微胶片文件号的连续顺序进行分组排列。

修订号和修订日期应出现在出版物第一个缩微胶片(INTRO一1)的标题(区域)中。

# 2.2 缩微胶片的临时更改单

临时更改单应按如下方式提供：

1. 缩微胶片上的出版物的临时更改单应在拍摄前就放置在出版物中的正确位置。  
2. 受临时更改影响的正常页面在拍摄前应用一个指向邻近临时更改单的大箭头来标记，以引起读者对临时更改的注意。  
3. 发送函应随上述修订的缩微胶片一起发布。  
4. 对于缩微胶片上的任何出版物不应发布纸质临时更改单。

作为一种候选方式，临时更改单可以由操作者选择用临时更改缩微胶片发布(参见[图5-3-2.4])。

1. 如果临时更改缩微胶片的内容在下次的定期修订时仍然有效，则它应被作为一项正常修订合并进手册中，或按照上述步骤重新发布。  
2. 当发布临时更改缩微胶片时，同时也应修订和重新发布临时胶片的有效缩微胶片目录。

3. 发送函应随上述临时更改缩微胶片一起发布。  
4. 临时更改缩微胶片的标题应按照(参见[图5-3-2.4])中的样例来制作。  
5. 临时更改缩微胶片应给出与它修改的正常缩微胶片相同的章/顺序编号，后跟一个字母A作为后缀。例如：26-1A、31-7A等。临时缩微胶片在归档时应紧随在正常缩微胶片之后。  
6. 每个临时更改缩微胶片应包括有关的章/节，页和有效性引用，以允许读者能够容易地将胶片内容与被该临时更改缩微胶片所更改或补充的数据联系起来。并且，应专门提供一节说明更改原因，以帮助确定临时缩微胶片的适用性或有效性。（参见[图5-3-2.4])这些信息不用放大就应清晰易读。  
7. 临时修改的内容应直接从原因段下方的A-1行开始，并应按B、C、D行继续，然后根据需要再排后续行。

# 5-4 检索

# 5-4-1 检索实现方法简介

# 1 范围

航空公司及其产品支援制造商正在开发有关于技术手册的检索系统标准。本文件根据检索功能要求(参见[2-2-1])中规定的功能要求，阐述了检索系统的实现方法。

本文定义了检索系统的三个级别，并确定了每一级别适用的标准。检索系统的三个级别是：初级、中级和高级，定义如下：

初级检索系统是一个具有最低功能的基本级别系统，按照ATA2200规范，初级检索系统可以是基于页的。虽然某些内容要求没有按照系统要求来描述，但初级系统必须满足所有内容和格式的要求。初级检索系统设定为不能修改从制造商处接收的信息。这包括由航空公司发布的中间修订或由制造商发布的TR(临时更改单)。

中级检索系统是基于信息而不是基于页的。它详细说明了系统的一组最低的功能和信息要求。例如，中级通过文件定义了目录结构，定义了交叉引用要求、便于查询的逻辑划分。总的来说，当不需要特定的技术解决方案或终端用户实现的特定数据模型时，中级检索系统在初级检索系统的基础上增强了功能。这里要注意的是，初级检索系统的要求是面向页设计的，不能向上用于中级和高级。

高级检索系统也是基于信息的，但它包括纲要模型和易于共享与重用的数据的访问标准。高级检索系统对于一个具有多系统互联和信息共享功能的企业级信息系统而言是必需的。例如，维修信息数据库能作为任务卡、工程指令、相应的管理活动信息等的直接数据源，并支持诸如维修计划和安排、库存控制，任务完成情况和记录保存等的企业级信息系统接口。

符合某个级别的要求是逐级增加的。除非本标准另外规定，否则中级检索系统隐含地要求应符合初级检索系统的所有部分，而高级检索系统隐含地要求应符合中级检索系统的所有部分。这里要注意的是，系统可能符合某一级别，但也可包括下一级别的特性并满足下一级别的需要。

除非另外规定，中级是检索系统默认的交付级别。

本文件的标题级别确定了与该节相关的相应级别，下表列出了这些级别的一个摘要：

1.1 各级别摘要  

<table><tr><td>节</td><td>级别</td></tr><tr><td>2.1 客户服务器模型</td><td>高级</td></tr><tr><td>2.2 数据模型</td><td>高级</td></tr><tr><td>2.3 数据格式</td><td></td></tr><tr><td>2.3.1 从服务器返回的数据(schemas)</td><td>高级</td></tr><tr><td>2.3.2 数据导出</td><td>中级</td></tr><tr><td>2.3.3 TR 交换格式</td><td>高级</td></tr><tr><td>2.4 硬件平台</td><td>初级</td></tr><tr><td>2.5 打印介质标签</td><td>初级</td></tr></table>

# 2 适用标准

以下标准来自 iSpec 2200，通过在本文正文中的引用，构成了本标准的条款：

# 2.1 适用标准和系统级别

<table><tr><td>光栅和图形格式</td><td>INT</td><td>[5-2-4] 图形交换
[5-2-5] 智能图形交换</td></tr><tr><td>客户/服务器通信接口: 开放式数据库连接([ODBC])</td><td>ADV</td><td>[5-4-2]客户机服务器通信协议</td></tr><tr><td>检索功能要求</td><td>ENTR</td><td>[2-2-1]检索功能要求</td></tr><tr><td>文件纲要模型 (iSpec2200 中所有已认证的)</td><td>ADV</td><td>[4-3] 文件纲要模型</td></tr><tr><td>结构化全文本查询语言</td><td>ADV</td><td>[5-4-3] SFQL3:结构化查询语言</td></tr><tr><td>适用的文件类型定义</td><td>ADV</td><td>[题目 Section 4-2] Document DTDs
[4-2] 文件 DTD</td></tr><tr><td>文件类型定义的功能要求</td><td>ADV</td><td>[4-2-1] DTD 要求 (GENREQ)</td></tr><tr><td>文件类型定义的要求文件</td><td>ADV</td><td>[4-2-2] DTD 功能要求指南 (FUNCREQ)</td></tr><tr><td>文件类型定义的技术要求文件</td><td>ADV</td><td>[4-2-3] DTD 技术要求 (TECHREQ)</td></tr><tr><td>ATA 通用支持数据词典</td><td>ENTR</td><td>[ATA CSDD]</td></tr></table>

# 3 应用程序简介

下文中描述了符合检索系统的标准的实现要求。

# 3.1 客户端/服务器模型[高级]

系统必须按照客户端/服务器模型划分。

# 3.1.1 客户端/服务器语言

查询请求和在客户端/服务器间返回的数据必须遵循[5-4-3]规定的结构化全文本查询语言。

# 3.1.2 客户端/服务器协议

需要一个终端对终端的客户端/服务器协议。该协议是依赖于操作系统的，应满足 Microsoft Windows™ 环境。

# 3.1.3. 客户端软件

客户端软件至少必须提供ATA RETRIEVAL.FUNCREQ(ATA检索.功能要求)中详细规定的最低功能。根据SFQL和以下标准，客户端必须能显示从服务器返回的数据。

- 图形交换[5-2-4]  
- 适用文件类型定义[4-2]  
- 功能要求(FUNCREQ)[4-2-2]  
一般要求(GENREQ)[4-2-1]  
技术要求(TECHREQ)[4-2-3]  
- 纲要模型[4-3]

# 3.1.4 服务器软件

服务器软件必须对客户端提供必要的数据访问能力，以提供ATA RETRIEVAL.FUNCREQ(ATA检索.功能要求)中详细规定的最低功能。

另外，一个服务器必须包括以下特性：

S1. 它必须能动态地从一个可配置的本地“更新”目录将临时更改单整合到数据库，其中临时更改单应符合 ATA 格式 (SGML DTD 实例)。  
S2. 它必须按照本地(LTRC)和在同一目录里提供的制造商临时修改(MTRC)控制清单来控制整合

临时更改单。

S3. 当数据库更新完成，应在本地打印机上或以一个 ASCII 码文件形式生成一个报告，以确认指定的更新项目，并记录处理过程中出现的任何问题或误差。日志中的项目应是更新集的一个可跟踪标志符（参见[5-4-1.3.1.5]）。  
S4. 更新过的数据库应给出一个原始数据和 TR 数据的综合视图。这个综合视图以基本数据和 TR 数据的 ATA 纲要模型和 ATA DTD 为依据。

# 3.1.5 数据库更新软件

制造商或航空公司，采用ATA SGML TR机制，将临时更改单输入到系统。如图1所示，基于SGML的TR被SFQL服务器设备供应商所提供的一个可用的专门的数据库更新(DB-Update)程序(它也可能作为服务器包的一部分来分发)所处理。这样，就产生一个能用于原始数据库(CD-ROM)的DB-Diff升级包，或一个更新了的数据库(当前的更新版次+原始数据库)。一旦安装了更新软件包，信息被显而易见地集成进数据库中。然而，更改信息仍然使用现有的ATA纲要模型信息及同这些更改数据一起返回SGML标记信息来标识。

![](images/178c8c2957775747b1257f3ae5da1ce4cec9407001df12737897da6758231e38.jpg)  
图5-4-1.1 原始数据、更新数据和检索过程

# 3.1.5.1 操作

书馆DB一Updat模型是一个单一目的的数据库更新系统，它是用于建立光盘上的原始数据库的索引引擎的一个子集。该系统的细节可以是专用的，只是它必须满足下列规范：

R1. 在输入时，DB—Update 软件必须以符合 ATA 的 SGML 和 ATA 图形格式获取临时修改(TR)数据。DB—Update 软件必须用一个给定的原始(或原始+更新)数据库来处理它，该数据库已经包括与位置标识类型(例如章)和 TR 更新数据的指定文件实例相匹配的组装表。  
R2.DB-Update软件应使用简单的“邮箱”机制来生成数据库的更新资料。一个用户可配置的“收件箱”目录将控制所有添加进数据库的文件。也就是说，标准ATA交换格式的TR被“投进”收件箱，自动地添加到活动数据库中(能通过服务器集成或通过用户提示来决定)。假如需要索引，DB-Update软件可以显示一个“选项”对话框或启动其它用户交互程序。  
R3. 在一个可配置的“发件箱”目录中，DB-Update 软件应生成所有必须传输到终端用户工作站的用于更新的文件。这个文件集反映了一个对目标数据库“不同的”更新，因而被称作 DB-Diff 升级包。除了必须包括可用控制文件、MTRC 和 LTRC 以外，DB-Diff 文件包实际上可以是专用的。  
R4. 所有在终端用户的工作站上需要安装的更新内容是由“发件箱”目录的销售商指定内容以一个可配置“更新”目录的形式传输到终端用户工作站。当更新内容添加到检索系统的终端用户硬盘的指定区域时，服务器应当(在下次调用时)向其任何客户端自动提供更新数据库视图检查。  
R5. DB一Diff 升级包必须携带能被记录在检索系统工作站日志里的一个唯一标识符，以便在 DB一Update 日志文件中跟踪所增 DB一Diff。

# 3.1.5.2 索引要求

R1. DB—Update 软件必须能有效地将一个新行添加到一个基于数据库的 ATA 纲要模型的现有表中，并能完成基于更新信息的 ATA DTD 错级别的逻辑数据库模型的任何级联的更改。一个允许的例外情况是，当一个表涉及到将全新文件添加到数据库时，软件可以禁止在该表中添加一行数据（例如到一个 ATA 文件表）。  
R2.DB-Update软件必须能有效地从一个基于数据库的ATA纲要模型的现有表中删除一行，并能完成基于更新信息的ATA DTD锚级别的逻辑数据库模型的任何级联的更改。  
R3. DB-Update 软件必须能有效地替换一个基于数据库的 ATA 纲要模型的现有表中的一行，并能完成基于更新信息的 ATA DTD 锚级别的逻辑数据库模型的任何级联的更改。  
R4. DB-Update 软件必须保存所有关于数据库更改的一个日志（必须包括 TR 顺序号、日期和时间，以及表明谁被授权将 TR 增加进 DB-DIFF 文件的一个条目）。  
R5. 对应于数据库的更改，DB—Update 软件必须更新 ATA 参考和 ATA 引用表中的超连接信息。  
R6. DB—Update 软件必须用源自 ATA DTD 关于更新的信息建立 TRINFO 表。  
R7. 当数据库更新完成时，将在“发件箱”中以 ASCII 文件形式生成一个报告，以确认指定的更新项目，并记录处理过程中出现的任何问题或误差。

# 3.2 数据模型[高级]

数据方案必须符合所有已批准的 iSpec 2200 方案(参见[4-3])

# 3.3 数据格式

# 3.3.1 从服务器返回的数据[高级]

必须按照 iSpec 2200 方案中所规定的格式将数据从服务器返回到客户端应用程序。

# 3.3.2 数据导出[中级]

如果系统以SGML格式导出数据，那么，所导出的数据必须符合所有适用于ATA SGML文件的要求，以及关于该文件类型的任何ATA DTD的要求，如果系统导出图形数据，它必须符合相应的iSpec 2200图形类标准。

# 3.3.3 TR交换格式[高级]

按照 ATA 文本和图形标准，TR(临时更改单)必须以 SGML 格式交付。

另外，每一组源自制造商或航空公司的TR(临时更改单)将同一个控制清单一起发布。针对于制造商或航空公司的控制清单是由服务器使用的独立的ASCII文件，用以将TR(临时更改单)合成到当前数据库中。只有合成标志为“Y”值的那些TR(临时更改单)被合并。

表 5-4-1.1 TR 控制清单(制造商)  

<table><tr><td>字段</td><td>解释</td><td>是否必需?</td><td>栏中起始位</td><td>栏中终止位</td><td>类型</td></tr><tr><td>合成标志</td><td>该标志表明服务器是否应将该TR 合成进数据库。</td><td>是</td><td>1</td><td>1</td><td>Y, N</td></tr><tr><td>TR 日期</td><td>数据的原始提供者发布 TR 的日期,格式为“yyy-mm-dd”(不带引号)</td><td>是</td><td>3</td><td>12</td><td>(日期型)</td></tr><tr><td>TR</td><td>根据 ATA2200 的一个唯一标识的编号</td><td>是</td><td>14</td><td>41</td><td>(字符型)</td></tr></table>

航空公司的TR控制清单可以具有“替换”制造商清单中那些内容的条目，也就是说，航空公司可以包括源自制造商清单的一个条目，但要将其合成标志设置为“N”。这就避免了将该TR增加进数据库中。

表 5-4-1.2 TR 控制清单 (航空公司)  

<table><tr><td>字段</td><td>解释</td><td>是否必需?</td><td>栏中起始位</td><td>栏中终止位</td><td>类型</td></tr><tr><td>合成标志</td><td>该标志表明服务器是否应将该TR合成进数据库。</td><td>是</td><td>1</td><td>1</td><td>Y，N</td></tr><tr><td>TR日期</td><td>数据的原始提供者发布TR的日期，格式为“yyyy-mm-dd”（不带引号）</td><td>是</td><td>3</td><td>12</td><td>(日期型)</td></tr><tr><td>TR</td><td>根据ATA2200的一个唯一标识的编号</td><td>是</td><td>14</td><td>41</td><td>(字符型)</td></tr><tr><td>TR发布日期</td><td>航空公司发布制造商的TR或供他们自己使用的TR的日期</td><td>否</td><td>43</td><td>51</td><td>(日期型)</td></tr><tr><td>航空公司参考</td><td>授权编写的一个唯一ID</td><td>否</td><td>53</td><td>68</td><td>(字符型)</td></tr><tr><td>航空公司授权编写ID</td><td>授权编写的一个唯一ID</td><td>否</td><td>70</td><td>80</td><td>(字符型)</td></tr></table>

# 3.4 硬件平台

新型的终端用户的分布式软件必须支持[表5-4-1.3]中所示的最低硬件和操作系统配置。名称为推荐的最低配置一栏中的信息定义了符合ATA检索系统的最低配置。所有声称具有兼容性的产品必须满足本平台基础上的功能要求。该配置是评定与标准兼容性的一个最低配置——这并不排除为了快速解压或打印等而使用平台的一个更快速版本、更多内存、网卡、特定加速卡的配置。当然任何更高级的产品对应用软件的作用是不言而喻的。附加软件要求可能需要一个比最低平台配置更高级的配置。

表 5-4-1.3 推荐的基本兼容性 PC 最低配置  

<table><tr><td>设备</td><td>推荐最低(配置)</td></tr><tr><td>计算机</td><td>兼容 IBM PC</td></tr><tr><td></td><td>Pentium - 166</td></tr><tr><td>内存</td><td>32MB</td></tr><tr><td>可用硬盘空间</td><td>100 MB 空间</td></tr><tr><td>软驱</td><td>3.5&quot; 1.44 MB (HD)</td></tr><tr><td>环境</td><td>Windows NT 4/SP-3 或 Windows 95</td></tr><tr><td>输入设备</td><td>任何 MS-Windows 兼容的设备</td></tr><tr><td>监视器/显示适配器</td><td>任何 MS-Windows 兼容的色彩或 256 色灰度</td></tr><tr><td>尺寸</td><td>17&quot;</td></tr><tr><td>分辨率</td><td>1024 x 768</td></tr><tr><td>打印机/打印接口</td><td>任何 MS-Windows 兼容的 300 dpi 页面打印机</td></tr><tr><td>纸</td><td>标准略大的 A/B 尺寸</td></tr><tr><td>CD-ROM 驱动程序</td><td>ISO 9660 兼容的、MS-Windows 兼容的驱动程序</td></tr><tr><td>速度</td><td>8 速</td></tr><tr><td>通信</td><td>参见[5-4-4]</td></tr><tr><td>解压</td><td>软件3(版本)</td></tr></table>

# 5-4-2 客户端/服务器通信接口

# 1 前言

在 ATA 检索标准中，软件的独立性是通过将检索软件分成两层来提供的：一层是针对索引详细内容中专用知识的搜索引擎，另一层是应用(表达)软件，该软件负责检索系统的用户浏览(用户界面)操作。

该标准是一个客户端/服务器体系结构。应用程序是客户端。当用户运行应用程序时，应用程序连接到一个能对磁盘上数据进行索引访问的服务器(在需要时必须启动)上。但是，SFQL 标准只规定了在客户端和服务器之间执行查询和请求的基于 SQL 的语法。因此在客户端和服务器之间必须有一个管理通讯的标准接口。

# 2 范围

本简介按照[5-4-1]CDPROFILE的规定，说明了Microsoft [ODBC]应用编程接口(API)在一个ATA标准检索系统中的应用。

在[5-4-1]中详细说明操作环境和硬件配置。

# 3 适用文件

Microsoft [ODBC]。Microsoft 开放式数据库连接([ODBC])协议。Microsoft Visual C++ 帮助文档，Microsoft、Redmond、WA。

# 4 传输文件

所有磁盘在其根目录下应包含一个名为CONTENTS.TXT的传输文件。

文件应被格式化为若干区段。每个区段应从一个附带方括号的区段名开始。跟在区段名后的行应按如下形式：

<variable_name>='<value>该区段名为[SFQLSERVER ODBC]，为强制性区段，它包括可用于各种操作系统的[ODBC]信息(例如Windows、Mac和Unix)。在本区段中有三个必须的<variable_name>，如下：

<table><tr><td>DATASOURCNAME
标识数据库(数据源名称或“DSN”)的字符串,可用于一个[ODBC]连接调用:</td></tr><tr><td>ODBCDRIVERNAME
这个字符串表示在[ODBC]管理程序中显示的驱动程序名,标识服务器的:</td></tr><tr><td>SERVERDATE
表述该服务器的发布日期,是由连字符分隔的整型数,例如: yyyy-mm-dd。另外,如下变量必须至少定义一个,这取决于支持的操作系统环境:</td></tr><tr><td>SETUPWIN32
Windows 32位[ODBC]驱动程序的安装程序的名称、路径和扩展名。</td></tr><tr><td>SETUPWIN16
Windows 16位[ODBC]驱动程序的安装程序的名称、路径和扩展名。</td></tr><tr><td>SETUPMAC
对于Macintosh的[ODBC]驱动程序的安装程序的名称、路径和扩展名</td></tr><tr><td>SETUPxxx
“xxx”环境的[ODBC]驱动程序的安装程序的名称、路径和扩展名。其中XXX是针对一个操作系统可执行环境,如Solaris_86、Linux、Ultrix等的一个唯一标识符。如果对文件进行分发,则发送文件应有另一个标题为[DOCS]的区段。[DOCS]区段必须包含以下的变量定义:</td></tr><tr><td>DOC_SET
对用户的文件集进行标识的名称。</td></tr><tr><td>BUILDNBR
表示正在传输的文件数据库创建版本的一个编号。当比较两个创建版本号时,较大的编号一般表示一个较新创建的版本。</td></tr><tr><td>COUNT
本次发布所包括的文件数量。</td></tr><tr><td>另外,[DOCS]区段应有N个编号的附加变量集合,其中N是上述的COUNT变量值。编号的集合由以下变量名和集合编号组成,下面的后缀字符“X”可用集合编号的数字替换。</td></tr><tr><td>MODEL_x
文件适用的模型
DOCTYPE_x
文件类型名(如AIPC、EIPC)</td></tr><tr><td>DESCRIP_x
对用户的文件进行标识最多使用70个字符的描述性文本。</td></tr><tr><td>SELECT_x
一个SFQL SELECT语句(省略关键字SELECT),用以返回包含文件的全部文本的一个单独行。该变量允许不依赖于方案进行浏览和数据导出。</td></tr><tr><td>SCHEMADATE_x
控制该文件的标准方案的发布日期,如果适用,用被连字符分隔的整数来表示,如yyyy-mm-dd。文件可包含其它区段和注释。注释行的第一个字符是一个分号(“;”)。注释不能与区段名或一个标准传输文件的示例:
一个标准传输文件的示例:
;这个磁盘是可交换磁盘的一个示范;依据ATA/AIA标准
[SFQLSERVER ODBC]</td></tr></table>

```txt
DATASOURCNAME  $\equiv$  ATA Maintenance Catalog   
ODBCDRIVERNAME  $\equiv$  ATA SFQL3 Server   
SETUPWIN32  $\equiv$  odbc\setup32.exe   
SETUPWIN16  $\equiv$  odbc\setup16.exe   
SETUPMAC  $\equiv$  odbc\setupmac.exe   
[DOCS]   
DOC_SET  $\equiv$  Maintenance and Troubleshooting   
BUILDNBR  $= 12$    
COUNT  $= 2$    
MODEL_1=A320   
DOCTYPE_1  $\equiv$  AMM   
DESCRIP_1=Aircraft Maintenance Manual for A320, Version 29   
SELECT_1  $\equiv$  document_text FROM ATA_DOCWHERE ATA_DOC_ID  $= 123456$  . SCHEMADATE_1  $= 1992 - 12 - 01$    
MODEL_2  $\equiv$  A320   
DESCRIP_2  $\equiv$  Illustrated Parts Catalog for A320, Version 27.   
DOCTYPE_2  $\equiv$  AIPC   
SELECT_2  $\equiv$  document_text FROM ATA_DOC WHERE ATA_DOC_ID  $= 123459$  . SCHEMADATE_2  $= 1992 - 12 - 01$    
[ANY OTHER SECTION NAME]   
MYVARIABLE  $= 3$
```

# 5 安装

分发介质应包含一个[ODBC]安装程序，用来安装销售商的[ODBC]驱动程序和SFQL服务端程序，如果两者相分离的话。

# 6 通信接口

本应用程序简述文件的目的是尽可能最小化地或不扩展地使用标准[ODBC]。但是，为了利用全文本索引数据，SFQL扩展性必须映射进[ODBC]的兼容级别。

# 6.1 ODBC实现工具

服务器(检索引擎)和客户端(用户界面)之间的接口应遵循标准[ODBC]版本3的规则。通过利用在客户端对[ODBC]驱动程序的[ODBC]函数调用，来建立客户端和服务器之间的通信过程。

# 6.2 ODBC扩展性

一个 ATA 数据源可只使用标准[ODBC]，或它可以包含依据 SFQL 的附加全文本数据库特性。这些增强的特性只适用于 ATA 定义的数据类型“TEXT_INDEXED”。为了表示支持 SFQL 扩展性的一个栏，驱动程序应：

- 对于栏属性 SQL_DESC_TYPE_NAME 返回“TEXT_INDEXED”。使用 [ODBC] 函数 SQLColAttribute，并将参数 fFieldIdentifier 设置为 SQL_DESC_TYPE_NAME，可以检索该属性。

# 7 兼容性

有两类兼容性软件：驱动程序和客户端(程序)

按照下列通用要求，一个符合ATA要求的驱动程序应遵循Microsoft [ODBC]版本3的以下通用要求。一个ATA兼容的驱动程序：

1. 执行完整的核心[ODBC]语法。但是，对于只读数据源，某些数据操纵语言(DML)语句和数据定义语句(DDL)并不适用，按照[ODBC]的定义，将返回错误。  
2. 应至少符合1级[ODBC]API。  
3. 另外，对于[ODBC]SQL语法，驱动程序(和在两级或三级系统情况下的底层数据服务程序)必须

支持在ATA.RETRIEVAL.SFQL版本3(或更新的)中规定的SFQL(参见[5-4-3])。

4. 按照[ODBC]互操作的指导方法，可允许从不同的制造商处连接客户端并使用数据。

一个符合ATA要求的客户端(应用程序)必须：

1. 测试和处理返回码，以便由于驱动程序和数据源(如只读)的差异而出现的错误可圆满地恢复。  
2. 按照[ODBC]互操作的指导方法，允许最佳的互操作性体现在程序运行时间而不是在程序编制时间。  
3. 只能通过[ODBC]接口才能与数据源对话

# 5-4-3 SFQL3：结构化全文本查询语言

# 1 概念介绍

# 1.1 目的

本规范是由航空运输协会(ATA)/航天工业协会(AIA)高级检索技术工作组联合编制的检索标准的组成部分。iSpec 2200 检索标准讲述了对包含文字、图像和字段数据(全文本数据库)的数据库的不依赖于销售商的标准化访问(内容)。

为了实现全文本数据库访问的标准化，ATA iSpec 2200 检索标准针对网络系统和单机系统，都沿用了一种客户端/服务器的方式。在这种方式中，检索引擎(对索引进行查询)和终端用户应用软件(管理用户的请求并显示数据)是分离的，它们之间的界面是标准化的(参见[图 5-4-3.1])，只要两层之间的通信是标准化的，就能从任何终端用户的检索系统交互地访问具有明显差异数据/索引层(如来自不同的承包商)的数据库。

数据库的交互性有许多显而易见的优点

- 单个用户界面可用于访问一致性的数据库(如来不同承包商的);  
- 可开发专用的、以任务为中心的界面，以共享一个公共信息源；  
- 信息提供者可获得任何服务供应商创建的磁盘，不会影响终端用户的界面；  
- 信息提供者能选择终端用户软件，不强迫他们选择数据编制服务程序。

为了实现客户端/服务器层的标准化，必须规定客户端界面的各个不同级别：

1）客户端和服务器交换请求和数据的机制；  
2）客户端/服务器请求机制的语法和语义：  
3）交换的数据类型和数据格式

现行标准规定了客户端/服务器请求机制的语法和语义。但客户端/服务器实现工具是应用传统使用的SQL去解决字段式数据库问题，而SQL目前并不支持全文本数据和操作。

因此，本文件详细说明了结构化全文本查询语言(SFQL)：它是对ISO和ANSI标准的结构化查询语言(SQL)的扩展，以增加对全文本索引信息和数据的访问能力。

本规范遵循三个基本原则：

- 规定 SFQL 是对 SQL 语法  ${}^{2}$  的一个扩展 “插件”。  
- 本规范中的所有新结构由 SQL 语法样式组成；并且  
新结构不应与任何已知的 SQL 结构发生冲突

![](images/f7707a817e94b08eacac69cb7ab0dae9279fd15d9817160035b99b04f145e842.jpg)  
图5-4-3.1 软件实现方法

# 1.3 数据库模型

SFQL 中的数据库模型是以传统的关系模型为基础，然后又对其进行了充分的扩展。SFQL 方案将文件和其子组件（如一个 DTD 定义的）映射为以表的形式组织的几组全文本文件，其中，一个表表示了一组逻辑文件实体（如“章”、“节”或“标题”），或一组更加传统的 SQL 实体，如“零件”或“工具”。对于一个给定表来说，表中各栏表述了该逻辑实体的不同属性，包括用于链接其它逻辑实体的信息。

SFQL 数据库中的扩展是特定 indexed text(索引文本)栏(数据类型 TEXT_INDEXED)的附加部分。虽然特定的映射关系取决于方案，但一个索引文本栏除了基本 SQL 模块匹配能力之外，还包含了可应用全文本查询技术(如短语和模糊查询)进行查询的信息。

通过将文本映射到表这种精密的方式，取决于数据库编写者的数据模型设计(纲要模型)。一组由“编写者”、“标题”和非结构化文本组成的“非结构化”的文件，可存入一个具有“编写者”、“标题”和“document_text(文件一文本)”栏的 SFQL 表中，其中，编写者和标题栏保存这些特定数据项，而 document_text 栏包含完整的文件文本。

更复杂的文件结构(如层次结构)也可采用以多重表来体现层次结构的不同视图的方式来表述(参见

[4-3])。(参见[图5-4-3.1])显示了用于构建文件中一个“章一节一题目”层次结构的表集合的一个例子。

![](images/26ef0941fa89d0efcebceba28d7d6841bcd0b875c752d91296e09b6a7af86a2c.jpg)  
图5-4-3.2 一个分层文件到一个纲要模型的映射示例

重要的是，要注意(参见[图5-4-3.2])表模型只是一个概念模型，而底层的物理模型才是与数据库相关的。当考虑引入数据冗余的如上所述的方案时，如上述方案时，这一点尤其重要。SFQL系统预期设计成为可对方案有效的处理，其中方案的索引文本字段可以表述来自重叠的、引入数据冗余的原始文件的信息。例如，一个数据库系统可以在内部简单地使用对于索引文本栏的一个通用数据结构的指针，而不是将数据分割成与信息的逻辑视图相关的数据结构。

# 1.4 元信息方案

类似SQL，每个SFQL执地程序为每一个目录(一组方案)提供了一个信息方案，它包含了关于数据方案的信息，例如表和栏的名称。SFQL支持SQL的Information_Schema(信息方案)，并以一个称为SFQL_Info_Schema(参见[5-4-3.6])的单独方案的形式提供给该方案的数据。

# 2 SFQL 的详细说明

SFQL 全文本管理扩展定义为一组对 SQL2 语法的扩展。SFQL 中推荐的在标准 SQL 语法中增加的内容应是最少的，以允许其在许多现行平台上执行。实际上，除了一个新定义的文本数据类型 (TEXT_INDEXED) 之外，扩展性能被设计为任何数据类型都是完全清晰的。换句话说，对于除了 TEXT_INDEXED 之外的所有数据类型，符合 SQL2 初级标准的实现工具都应遵循本标准。

扩展分为以下方面：

SQL数据类型扩展[5-4-3.2.1]

- SQL 语法扩展[5-4-3.2.2]  
- 环境扩展[5-4-3.2.3]

# 2.1 SQL数据类型扩展

为了将 SFQL 功能加入到 SQL 语法中，并不与 SQL 语义发生冲突，扩展的 SFQL 语句只能应用于一个 SFQL 特定的数据类型 TEXT_INDEXED。

# 2.1.1 索引文本

TEXT_INDEXED 是 SQL 字符串VARCHAR 数据类型的超类，它由一个字符序列组成，并用一个执行程序定义其长度。TEXT_INDEXED 数据类型的栏可以是 SFQL 指定的 CONTAINS 谓词的目标，并充当 HITS 函数的参数。一个 TEXT_INDEXED 栏总是具有字查询和短语查询的能力，这和用通用 SQL 谓词对 CHAR 栏操作相同。如果在 FT_PROX_xxx 栏中指出的话，TEXT_INDEXED 栏还允许进行模糊查询，其中 xxx 可以是 CHARACTERS（字符）、WORDS（词）、SENTENCES（句子）或 PARAGRAPHS（段落）。

一个查询的  $<$  search_condition  $>$  （<查询条件  $\succ$  ）中至少有一个 TEXT_INDEXED 栏，可使用<select_list>(<选择列表  $\succ$  )中的RELEVANCE函数。

# 2.2 SQL语法扩展

语法扩展的目的是，对 TEXT_INDEXED 数据类型求值的附加谓词进行详细说明，并依据 SQL2 的谓词逻辑返回 TRUE(真)、FALSE(假)或 UNKNOWN(未知)。

# 2.2.1 符号

以下语法扩展用巴科斯一诺尔范式(BNF)表达，其中：

关键字(语法的文字部分)用大写字母表示  
- 生成式符号(对于语法中出现的使用“=”号生成式规则的符号)用尖括号封闭。

在表达 SQL2 生成式符号时，其名称以 sql 作为前导字符；例如，当涉及到 SQL 的 <predicate > 生成式时，其 SFQL 生成式符号是 <sql predicate>

- 在本规范中不可打印的文字字符用带下划线的文本描述方式表示。

使用以下附加语法符号：

- 方括号([ ])用来表示可选择的元素。  
- 圆括号()表示可以重复一次或多次的元素。  
- 大括号  $\left\{\left\{\right\}\right)$  表示元素组。

# 2.2.1.1 格式

通过SQL2生成式的以下变化，SFQL谓词扩展被链接到SQL2语法：

```txt
<predicate> # := <sq predicate>  
| <sq predicate>  
<sq predicate> ::= <contains predicate>  
<contains predicate> ::= <sq column specification>  
[NOT] CONTAINS { <contains condition>  
| <sq quantifier> <sq scalar subquery>}  
The <contains_prediction> evaluates to TRUE whenever the <contains_condition> evaluates to JE when applied to the <column>.
```

当 <contains_condition> 用于 <column> 时，只要 <contains_condition> 等于 TRUE，那么 <contains_prediction> 等于 TRUE。

```txt
<contains condition> ::= <contains term>
| <contains condition> <contains or operator> <contain term>
<contains or operator> ::= vertical bar character
<contains term> ::= <contains factor>
| <contains term> & <contains factor>
<contains factor> ::= [~] <contains primary>
<contains primary> ::= <sub>sub</sub> contains predicate>
| (<contains condition>)
```

```txt
|<string list>  
<proximate predicate> ::= <string list> WITHIN <distance> OF <string list>  
[IN_ORDER]
```

该谓词用于测试近似度。近似度基于多个<document unit>(<文件单元>)。只要<string list>中的一个字符串与第二个<string list>中的一个或多个字符串比较结果在规定的范围之内，则该条件的求值结果为TRUE。

IN_ORDER修改了查询，以使匹配行按照<proximate predicate>规定的顺序显示。

```txt
<string list> ::= <string list term> | <string list>, <string list term>
```

<string list>中的条件通过逻辑或(or)的关系构成一个<contains primary>，因此：

```javascript
'A', 'B' & 'C' is equivalent to: ('A'|'B') & 'C'
```

'A'，'B' & 'C' 等价于('A'|'B') & 'C'

```txt
stringlistterm> ：  $\equiv$  <sqlpattern>   
|<predicatefunction>   
|<sqcolumn specification>
```

<string list term>求值结果可以为当前数据库词分隔符定义的一个或多个词赋值。当求值结果为多个词时，那么隐含地表明服务器应按照谓词子句的方法来匹配短语。

基于CONTAINS谓词进行短语和混合词匹配的匹配方法是由系统决定的，这并不等价于针对数据的短语的模式匹配，因为特殊的词分隔符(空白)和其它特殊字符可以不必明确地表示在索引中。但是，在比较之前，SFQL查询解释程序应保证短语或混合词被等效地处理为栏中文本的索引，以便在基于栏的索引中，CONTAINS子句中的条件或短语中出现这样的字符而被排除在匹配之外。

从<contains predicate>的短语中去除分隔符(词、句子和短语)是全文本检索的一个固有特性，不必通知就能自动执行。索引和查询过程中使用的分隔符可从信息方案的SEPARATORS表中检索到。

注意，<like predicate>可用于查询包括结束符、分隔符和所有禁止符在内的词或字符的任意模式。

```txt
<distance> ::= <unsigned integer> <document unit>
```

根据所指定的<document unit>，Distance(距离)被定义为两个术语位置之间差距的绝对值。例如，在字符串“The cows came home. Wait until tomorrow.”中，词“Cows”的位置为2，“came”的位置为3等。因此，“Cows”与“came”词的距离为1(2减3的绝对值)，而“Home”与“Cows”词的距离为2(4减2的绝对值)。词“Cows”与“Home”句子的距离为0(句子位置1减句子位置1的绝对值)，而与“Tomorrow”句子的距离为1(句子位置1减句子位置2的绝对值)。

```txt
<document unit> ::=CHARACTERS  
| WORDS  
| SENTENCES  
| PARAGRAPHS
```

<document unit>规定了<proximate predicate>的距离单位。为了确定在一个给定栏支持哪种文件单位，必须参考INFO_SCHEMA栏的表。一个方案可能不支持任何<document units>，因此也不支持模糊查询。这使得客户端程序的开发变得复杂化，因此建议对于TEXT类型的所有栏(支持CONTAINS谓词部分)，必须支持<document unit>为WORDS(的情况)。

# 2.2.1.2 语法规则

与 SQL [ISO/IEC 9075:1992] 中定义规则相同，对于应用 <sqpl predicate> 的每一行，求值结果为 TRUE、FALSE或 UNKNOWN。

# 2.2.1.3 函数定义

有两类函数：

常用函数用于对<where_clause>或<select_list>中的<value_expression>信息进行转换或限定

- 谓词函数用于修改谓词中的条件

# 2.2.1.3.1 常用函数

# 2.2.1.3.1.1 函数

<general_function>可用于可使用的<value_expression>的任何地方。参见[5-4-3.4]可获知关于函数的详细描述。

# 2.2.1.3.1.2 格式

```cpp
<general function># ::= <hits>
| <relevance>
<hits> # ::= HITS (<column specification>, <term option>, <scope|)
<term option> # ::= TERMS_QUERY
| TERMS_HIGHLIGHT
| TERMS_HIT
<scope> # ::= SCOPE_ROW
| SCOPE_TOTAL
<relevance> # ::= RELEVANCE ([<string literal>])
```

当当前行的查询条件与导出表的其它行进行比较时，<relevance>函数返回与当前行关联的等级。每个服务程序可以有它自己的判定关联性的方法。关联性可选参数是由服务程序决定的。

# 2.2.1.3.1.3 语法规则

<general>函数中使用的<column specification>必须是TEXT_INDEXED类型。

# 2.2.1.3.2 文本谓词函数

# 2.2.1.3.2.1 函数

<text predicate function><文本谓词函数  $\succ$  ）只能用在<search condition>(<查询条件  $\succ$  )的<predicate>(<谓词  $\succ$  )子句中。

# 2.2.1.3.2.2 格式

```cpp
<text predicate function> ::= <thesaurus>
<thesaurus> ::= THESAURUS ( <string literal>, <word operator>) <word operator> ::= WORD_SYNONYM
| WORD_BROADEN
| WORD_NARROW
```

# 2.2.1.3.2.3 语法规则

谓词函数只可在用于 TEXT_INDEXED 栏的 SFQL 扩展的<contains predicate>内部使用。

# 2.3 环境扩展

# 2.3.1 错误处理

在SQLSTATE(SQL状态)下，一个基于SFQL的服务程序可以返回标准错误号和消息的基本集合，这与SQL相同。对此不进行扩展。

# 2.3.2 服务器兼容模式

# 2.3.2.1 检测服务器和方案信息

SFQL 提供了方案信息表，以确定一个特定服务器的性能和方案。这些表用于提供由服务器管理的有关方案的特定信息。它们可从使用标准 SFQL 查询语义的应用程序中检索到。（SFQL 信息方案为这些表提供了详细的方案[5-4-3.6]。）

# 2.3.2.2 功能级别

SFQL支持三个功能级别，对应于SQL2中的三个级别(参见[5-4-3.5]——与SFQL一致)。

# 3 SFQL指定保留字

# 3.1 SFQL-增加到SQL语法的保留字

SFQL 保留字列表包括了[ISO/IEC 9075:1992]关键字中增加的附加关键字。

表 5-4-3.1 SFQL 保留字  

<table><tr><td>Reserved Words 保留字</td></tr><tr><td>CHARACTERS</td></tr><tr><td>CONTAINS</td></tr><tr><td>IN_ORDER</td></tr><tr><td>PARAGRAPHS</td></tr><tr><td>RELEVANCE</td></tr><tr><td>SENTENCES</td></tr><tr><td>SFQL</td></tr><tr><td>TEXT_INDEXED</td></tr><tr><td>THESAURUS</td></tr><tr><td>WITHIN</td></tr><tr><td>WORDS</td></tr><tr><td>WORD_SYNONYM</td></tr><tr><td>WORD_BROADEN</td></tr><tr><td>WORD_NARROW</td></tr></table>

# 4 SFQL 函数目录

# 4.1 常用函数

常用函数说明了在一个查找中的数据使用前，或数据返回前的服务器执行的处理过程。<general_function>可以构成<select_list>或<where_clause>中的<value_expression>。列在这里的常用函数只适用于TEXT_INDEXED类型的栏。这些函数还是SQL标准函数。

# 4.1.1 采样

格式。HITS(COLUMN_SPECIFICATION，TERM_OPTION，SCOPE)

描述。HITS函数返回与当前行给定的<column_specification>中匹配的查询数目。

TERM_OPTION 指定了服务器使用的对采样进行计数的评判准则。有效值列在下表中：

表 5-4-3.2 Term option(条件选项值)  

<table><tr><td>TERMS_HIGHLIGHT</td><td>由匹配代码标记的指定&lt;column&gt;定义的文本中的位置数目。它始终等于匹配 代码对的数目。</td></tr><tr><td>TERMS_HIT</td><td>由服务器采样确定的文本中的位置数目。采样标准对于每个服务器可以不同, 这可以取决于允许的专门特性,如,MATCH FUZZY。因为它可以将若干匹 配代码对放置到突出显示的不相交的采样位置,因此该数目可以少于匹配代 码对总数。</td></tr><tr><td>TERMS_QUERY</td><td>在文本中与原始查询条件匹配的位置数目,不考虑像 MATCH FUZZY 这样的选项设置。</td></tr></table>

SCOPE 指定函数的目标。当<identifier>SCOPE_TOTAL 指定了导出表的行时，<identifier><标识符  $>$  =SCOPE_ROW 将 SCOPE 设置为当前行。

返回格式。整型。

返回值。采样数。

# 4.1.2 关联性

格式。RELEVANCE()

描述。RELEVANCE函数返回由服务器定义的对于当前行的关联等级。SERVER_INFO表中的标准服务属性SFQL_RELEVANCE_METHOD返回的较高级别是指显示较多关联行还是较少关联行。

返回格式。整型

返回值。该值指由服务程序生成的关联等级。如果服务器不支持关联级别，则对所有行返回相同值。

# 4.2 谓词函数

谓词函数只能用于<query_specification>（<查询说明>)的WHERE_clause>(WHERE子句>)的boolean term>(<布尔条件>)中。

# 4.2.1 词库

格式。THESAURUS(WORD, OPERATOR)

描述。THESAURUS函数标识由服务器判定的等于特定词WORD的条件。服务程序扩展了查询条件，用以包括处理查询之前的等效条件。返回的数据等于原始查询中的<where_clause>明确引用了<string_list>中的所有等效条件时的返回值。

OPERATOR规定了由服务程序用以确定等效性的判定准则。下表中列出了有效值。

THESAURUS函数使用指定的操作符(见下表)对被认为等效于WORD的一个条件列表进行了扩展。

表5-4-3.3 操作符的值  

<table><tr><td>WORD_BROADEN</td><td>将WORD扩展为一个条件列表，以规定一种更通用的形式。例如，“蔬菜”是比“马铃薯”更通用的形式。</td></tr><tr><td>WORD_NARROW</td><td>将WORD扩展为是特定实例的一个条件列表。例如，“黛西”（名）是“弗劳尔”（姓氏）的一个实例。</td></tr><tr><td>WORD_SYNONYM</td><td>将WORD扩充为一个具有近似含义的条件列表。例如，“沙发”可以被认为是“躺椅”的同义词。</td></tr></table>

返回格式。不返回数据（不用于<select_list>）

返回值。无

谓词动作。将谓词应用于一个条件列表被认为等效于WORD。

# 5 SFQL一致性真值表

表 5-4-3.4 一致性真值表  

<table><tr><td>种类</td><td>功能性</td><td>初级SFQL</td><td>中级SFQL</td><td>完全SFQL</td><td>注 释</td></tr><tr><td colspan="6">数据类型</td></tr><tr><td></td><td>字符串类型</td><td>是</td><td>是</td><td>是</td><td></td></tr><tr><td></td><td>国标字符</td><td>否</td><td>否</td><td>是</td><td></td></tr><tr><td></td><td>精确数字类型</td><td>是</td><td>是</td><td>是</td><td></td></tr><tr><td></td><td>近似数字类型</td><td>否</td><td>否</td><td>是</td><td></td></tr><tr><td></td><td>日期时间</td><td>是</td><td>是</td><td>是</td><td></td></tr><tr><td></td><td>间隔时间</td><td>否</td><td>否</td><td>是</td><td></td></tr><tr><td></td><td>位串类型</td><td>否</td><td>是</td><td>是</td><td></td></tr><tr><td></td><td>TEXT_INDEXED</td><td>是</td><td>是</td><td>是</td><td>如果限定的方案不需要该类型,则可以将一个服务器“捆绑”到一个数据库。如果该类型被省略,则SFQL还原为SQL</td></tr><tr><td colspan="6">特性</td></tr><tr><td></td><td>SQL2“初级 SQL”</td><td>是</td><td>是</td><td>是</td><td>依据SQL2 [ISO9075]</td></tr><tr><td></td><td>SQL2 “中级”</td><td>否</td><td>是</td><td>是</td><td>依据 SQL2 [ISO9075]</td></tr><tr><td></td><td>SQL2 “高级”</td><td>否</td><td>否</td><td>是</td><td>依据 SQL2 [ISO9075]</td></tr><tr><td></td><td>SQL2 信息方案</td><td>否</td><td>是</td><td>是</td><td>依据 SFQL 级别要求。这里作为一个独立的特性被包括,只是为了强调初级 SQL2 不支持信息方案。</td></tr><tr><td colspan="6">Text_Info_Schema</td></tr><tr><td></td><td>SERVER_INFO</td><td>是</td><td>是</td><td>是</td><td></td></tr><tr><td></td><td>SERVER_settings</td><td>是</td><td>是</td><td>是</td><td></td></tr><tr><td></td><td>SCHEMATA</td><td>是</td><td>是</td><td>是</td><td></td></tr><tr><td></td><td>TABLES</td><td>是</td><td>是</td><td>是</td><td></td></tr><tr><td></td><td>COLUMNS</td><td>是</td><td>是</td><td>是</td><td></td></tr><tr><td></td><td>STOPWORDS</td><td>是</td><td>是</td><td>是</td><td></td></tr><tr><td></td><td>WORD_INDEX</td><td>是</td><td>是</td><td>是</td><td></td></tr><tr><td></td><td>SEPARATORS</td><td>是</td><td>是</td><td>是</td><td></td></tr><tr><td></td><td>SUPRESSED chai</td><td>是</td><td>是</td><td>是</td><td></td></tr><tr><td></td><td>THESAURUS</td><td>是</td><td>是</td><td>是</td><td></td></tr></table>

# 6 信息方案

在 SQL2 中，一个被称为 Information_Schema(信息方案) 的方案包含了 SQL 标准表(视图)，这些表(视图)含有由服务器管理的关于数据库的特定信息。使用标准 SQL 可对这些视图中的信息进行检索。信息方案本身被当作一组视图，其中底层表是实现工具(软件)定义的。

SFQL 系统支持标准的 SQL 信息方案（根据一致性级别的需要），此外还支持一个被称为 SFQL Info_Schema 的 SFQL 特定信息方案。该方案包含了有助于用 SFQL 扩展对数据库进行管理的附加信息。为了避免改变包括映射到一致性级别的 SQL 执行语义（Information_Schema 对于初级 SQL 不是必需的），该方案与 Information_Schema 一起以在逻辑上相互独立的形式同时被包括。

为了确保 SFQL 系统在任何级别都有完整的方案信息, 对于 Information_Schema(方案、表和分栏表) 通用的 SFQL_Info_Schema 中的表包括了来自两个方案的栏。

表5-4-3.5 Sfql_info_schema视图  

<table><tr><td>SERVER_INFO</td><td>关于服务器和其限制的信息</td></tr><tr><td>SERVER_settings</td><td>当前选项设置。(通过&lt;set_environment_statement&gt;改变)</td></tr><tr><td>SCHEMATA</td><td>通过服务器可访问的方案集合</td></tr><tr><td>TABLES</td><td>通过服务器可访问的表</td></tr><tr><td>ColumNS</td><td>每个表中可访问的栏</td></tr><tr><td>STOPWORDS</td><td>不包括在WORD_INDEX中的词</td></tr><tr><td>WORD_INDEX</td><td>词索引</td></tr><tr><td>SEPARATORS</td><td>用作全文本索引的分隔符的字符或字符序列。</td></tr><tr><td>SUPRESSED_CHARS</td><td>为了全文本索引的目的而从词中省略的字符或字符序列</td></tr><tr><td>THESAURUS</td><td>词库操作的词列表(同义词、广义词、狭义词)</td></tr></table>

# 6.1 SERVER_INFO视图

该视图包含关于服务器及其限制的信息。

表 5-4-3.6 Server_info 视图  

<table><tr><td>栏</td><td>类型</td><td>描述</td></tr><tr><td>SERVER_ATTRIBUTE*</td><td>CHAR</td><td>用行描述的服务器属性名称。[表5-4-3.7]中给出了标准服务器属性设置。</td></tr><tr><td>SERVER_VALUE</td><td>CHAR</td><td>SERVER_ATTRIBUTE 的值。注意值的字符表示法可以被转换成[表5-4-3.7]中给出的本地类型。</td></tr></table>

表 5-4-3.7 标准服务器属性  

<table><tr><td>SERVER_ATTRIBUTE</td><td>描述</td></tr><tr><td>SFQL_MANUFACTURERMARK</td><td>制造商的版权/商标通告</td></tr><tr><td>SFQL_MANUFACTURERNAME</td><td>制造商名称</td></tr><tr><td>SFQL_MATCH_CODE_END</td><td>匹配文本后的字符</td></tr><tr><td>SFQL_MATCH_CODE_START</td><td>匹配文本前的字符</td></tr><tr><td>SFQL_OPTIMUM_ANYCASE</td><td>不区分大小写匹配的服务器优化法的数字级别,与其它方法相关。</td></tr><tr><td>SFQL_OPTIMUM_EXACTCASE</td><td>精确大小写匹配的服务器优化法的数字级别,与其它方法相关。</td></tr><tr><td>SFQL_OPTIMUM FUZZY</td><td>模糊匹配的服务器优化法的数字级别,与其它方法相关。</td></tr><tr><td>SFQL_RELEVANCE_MAX</td><td>数字关联范围的上端数值</td></tr><tr><td>SFQL_RELEVANCE_METHOD</td><td>由服务器使用的对于关联级别的技术描述</td></tr><tr><td>SFQL_RELEVANCE_MIN</td><td>数字关联范围的下端数值</td></tr><tr><td>SFQL_RELEVANCE_ORDER</td><td>“HIGH”表示较高级的关联级别,表明一个文件可以更好地匹配用户的请求;“LOW”表示较低级的关联级别可以更好地匹配。</td></tr><tr><td>SFQL_RELEVANCESupported</td><td>如果服务器支持 RELEVANCE 函数,则结果为 “TRUE”,否则为 “FALSE”。</td></tr><tr><td>SFQL_VERSION_LEVEL</td><td>SFQL 级别。“1”=初级,“2”=中级 SFQL,“3”=高级 SFQL。参见[5-4-3.5]关于一致性级别的定义。</td></tr><tr><td>SFQL_VERSIONMajor</td><td>SFQL 主版本号,如,“3”表示 SFQL 3.x.</td></tr><tr><td>SFQL_VERSIONMinor</td><td>SFQL 次版本号 例如,“0”表示 SFQL 3.0.</td></tr><tr><td>SFQL_UPDATE_SUPPORTED</td><td>如果服务器支持 SHOW_UPDATES 的服务器设置,则结果为 “TRUE”,否则为 “FALSE”。如果为 “FALSE”,则检查窗口和数据库更新视图始终相同。</td></tr></table>

# 6.2 服务器设置视图

该可更新视图用于设置或检索服务器上的当前选项设置。

表 5-4-3.8 Server_settings 视图  

<table><tr><td>栏</td><td>类型</td><td>描述</td></tr><tr><td>SERVER_OPTION*</td><td>CHAR</td><td>用行描述的服务器选项名。[表5-4-3.9]中给出了标准的服务器选项设置</td></tr><tr><td>SERVER_VALUE</td><td>CHAR</td><td>SERVER_OPTION的值。注意值的字符可以被转换成[表5-4-3.7]中给出的本地类型。</td></tr></table>

表5-4-3.9 Server_settings属性  

<table><tr><td>SETTING_ATTRIBUTE</td><td>描述</td></tr><tr><td>SFQL_CURRENT_CATALOG</td><td>当前默认的CATALOG(目录)名,可通过&lt;set_environment_statement&gt;改变</td></tr><tr><td>SFQL_CURRENT_SCHEMA</td><td>当前默认的 SCHEMA(方案)名,可通过&lt;set_environment_statement&gt;改变</td></tr><tr><td>SFQL_MATCH_METHOD</td><td>该属性用于设置或返回查询过程中匹配类型,在查询中该匹配类型可有效。</td></tr><tr><td></td><td>SERVER_VALUE 栏可以被设置,或返回下列值之一:</td></tr><tr><td>SFQL_SHOW_MATCHES</td><td>如果设置为 “TRUE”,则匹配代码被设置为在文本中返回;如果设置为 “FALSE”,则不返回匹配代码。</td></tr><tr><td>SFQL-show Updates</td><td>如果 SFQLSHOWUpdates 设置为 “TRUE”,则服务器被设置为返回在查询响应时数据的最新当前视图。如果为 “FALSE”,则服务器被设置为,显示自最后的检查窗口起返回的数据,该检查窗口由应用软件定义。缺省为 “TRUE”,即使服务器不支持更新(这种情况下,检查窗口和更新视图相同)。</td></tr></table>

# 6.3 SCHEMATA视图

该视图包含了服务器可访问的方案的信息。对于视图中的每个唯一的目录名，都有一个INFO_SCHEMA作为目录中所有其它方案的补充。该视图必须包括以下<column>:

表5-4-3.10 方案视图  

<table><tr><td>栏</td><td>类型</td><td>描述</td></tr><tr><td>...依据 SQL2 的栏...</td><td></td><td>依据[ISO/IEC 9075:1992]规范的所有标准栏</td></tr><tr><td>DESCRIVATIVE_NAME</td><td>CHAR</td><td>适于终端用户表示的方案名称</td></tr><tr><td>DESCRIPTION</td><td>CHAR</td><td>适于终端用户表示的方案的文本描述。</td></tr></table>

# 6.4 TABLES 视图

该视图包含了服务器可访问的表信息。每行表示一个由服务器管理的不同表。<column>描述了对于特定表有效的选项。INFO_SCHEMA 表也在该表中描述。该视图必须包含以下<column>:

表5-4-3.11 表视图  

<table><tr><td>栏</td><td>类型</td><td>描述</td></tr><tr><td>...依据 SQL2 的栏...</td><td></td><td>依据[ISO/IEC 9075:1992]规范的所有标准栏</td></tr><tr><td>DESCRIVATIVE_NAME</td><td>CHAR</td><td>适于终端用户表示的表名称</td></tr><tr><td>DESCRIPTION</td><td>CHAR</td><td>适于终端用户表示的表的文本描述。</td></tr></table>

# 6.5 COLUMNS视图

在每个SFQL服务器可访问的表中，ColumNS视图包含一个<column>描述。该视图必须包含以下<column>:

表5-4-3.12 栏视图  

<table><tr><td>栏</td><td>类型</td><td>描述</td></tr><tr><td>...依据 SQL2 的栏...</td><td></td><td>依据[ISO/IEC 9075:1992]规范的所有标准栏</td></tr><tr><td>COLUMN DESCRIPTION</td><td>CHAR</td><td>&lt;column&gt;的文本描述</td></tr><tr><td>FT_WILDCARD</td><td>CHAR</td><td>三位字符映射表指通配符的可能位置。字符映射表中的字符可以是:N——Neither,该位置不支持通配符B——Both,该位置支持所有通配符%——该位置只支持‘%’通配符——该位置只支持‘_’通配符字符映射表的三个位置,表示操作是否支持PREFIX(前缀)、EMBEDDED(内含词)或SUFFIX(后缀)的用法。</td></tr><tr><td>FULL_TEXT_INDEXED</td><td>CHAR</td><td>如果全文本操作适用于该栏,则结果为“TRUE”(如,CONTAINS子句可以用于查找栏中数据)。如果为“FALSE”,则前缀为“FT_”的ColumNS视图的栏不适用于该行表述的栏。</td></tr><tr><td>FT_STOP_WORD_LIST</td><td>CHAR</td><td>表的结束符清单的名称。STOPWORDS表的值和STOP_WORD_LIST栏中的该值由适用于该表的结束符清单组成。几个表可以使用相同的结束符清单。如果一个结束符清单不适用,则该字段将包含一个空字符串。</td></tr><tr><td>FT_DEPLURALIZATION</td><td>CHAR</td><td>如果词的形式仅在有(字母)数目不同时是匹配的,那么结果为“TRUE”,否则为“FALSE”。例如,支持混合复数形式词的栏可以将查询条件“his”与表中的词“him”进行匹配。如果希望支持,可通过将MATCH_METHOD设置为MATCH_FUZZY。</td></tr><tr><td>FT_POSSESSIVE_FLX</td><td>CHAR</td><td>如果词的形式仅在所有格形式不同时是匹配的,则结果为“TRUE”,否则为“FALSE”。例如,支持所有格灵活性的一栏可以将查询条件“his”与栏中的词“him”进行匹配。如果希望支持,可通过将MATCH_METHOD设置为MATCH_FUZZY。</td></tr><tr><td>FT_PUNCTUATION_FLX</td><td>CHAR</td><td>如果词的形式仅在有标点符号不同时是匹配的,则结果为“TRUE”,否则为“FALSE”。例如,支持标点符号灵活性的一栏可以将以将查询术语“house”与栏中的词“house?”进行匹配。如果希望支持,可通过将MATCH_METHOD设置为MATCH_FUZZY。</td></tr><tr><td>FT_SYNONYM</td><td>CHAR</td><td>如果 THESAURUS WORD_SYNONYM可用,则结果为“TRUE”,否则为“FALSE”。例如,支持WORD-SYNONYM(同义词)的一栏可以将查询条件“house”(家庭)与栏中的词“home”(家)进行匹配。</td></tr><tr><td>FT_BROADEN</td><td>CHAR</td><td>如果 THESAURUS_WORD_BROADEN 可用,则结果为“TRUE”,否则为“FALSE”。例如,支持WORD-BROADEN(广义词)的一栏可以将查询条件“猫”与栏中的词“动物”进行匹配。</td></tr><tr><td>FT_NARROW</td><td>CHAR</td><td>如果 THESAURUS_WORD_NARROW 可用,则结果为“TRUE”,否则为“FALSE”。例如,支持WORD-NARROW(狭义词)的一栏可以将以将查询条件“气体”与栏中的词“氧气”进行匹配。</td></tr><tr><td>FT_TRANSP_OR_SEPAR</td><td>CHAR</td><td>如果短语中词的位置进行了调换或分隔而仍然是匹配的,则结果为“TRUE”,否则为“FALSE”。例如,支持调换或分隔的一栏可以将查询条件“except for club members(除了俱乐部会员以外)”与栏中的短语“club members excepted(俱乐部全员除外)”进行匹配。如果希望支持,可通过将MATCH_METHOD设置为MATCH FUZZY。</td></tr><tr><td>FT_VERB_STEMMING</td><td>CHAR</td><td>如果动词形式共享一个通用的词干时是匹配的,则结果为“TRUE”,否则为“FALSE”。例如,支持动词词干的一栏可以将查询术语“is”与栏中的词“were”进行匹配。如果希望支持,可通过将MATCH_METHOD设置为MATCH FUZZY。</td></tr><tr><td>FT_PROX_CHARACTERS</td><td>CHAR</td><td>如果近似度可以用字符数目表达,则结果为“TRUE”,否则为“FALSE”。</td></tr><tr><td>FT_PROXWORDS</td><td>CHAR</td><td>如果近似度可以用词数目表达,则结果为“TRUE”,否则为“FALSE”。</td></tr><tr><td>FT_PROXSENTENCES</td><td>CHAR</td><td>如果近似度可以用句子数目表达,则结果为“TRUE”,否则为“FALSE”。</td></tr><tr><td>FT_PROX_PARAGRAPHS</td><td>CHAR</td><td>如果近似度可以用段落数目表达,则结果为“TRUE”,否则为“FALSE”。</td></tr><tr><td>FTSEPWORDS</td><td>CHAR</td><td>栏的SEPARATORS视图中的词分隔符列表名称。行的SEPARATOR栏的值集合和一个匹配的SEPARATOR_LIST栏由分隔符列表和索引词序列组成。一个或多个栏可以使用同一分隔符列表。如果一个词分隔符列表不可用,则该字段应包含一个空字符串。</td></tr><tr><td>FTSEPSENTENCES</td><td>CHAR</td><td>栏的SEPARATORS视图中的句子分隔符列表名称。行的SEPARATOR栏中的值集合和一个匹配的SEPARATOR_LIST栏由分隔符列表和索引句子序列组成。一个或多个栏可以使用同一分隔符列表。如果一个句子分隔符列表不可用,则该字段应包含一个空字符串。</td></tr><tr><td>FTSEP_PARAGRAPHS</td><td>CHAR</td><td>栏的SEPARATORS视图中的段落分隔符列表名称。行的SEPARATOR栏中的值集合和一个匹配的SEPARATOR_LIST栏由分隔符列表和索引段落序列组成。一个或多个栏可以使用同一分隔符列表。如果一个段落分隔符列表不可用,则该字段应包含一个空字符串。</td></tr><tr><td>FT_SUP_CHARACTERS</td><td>CHAR</td><td>栏的禁止符列表名称。在 SUPPRESSED_CHARS 视图中的 SUPRESSED栏中的值集合和 SUPRESSED_LIST栏中的该值由禁止符列表和按 WORDS 索引的全文本字符序列组成。一个或多个栏可以使用同一 SUPPRESSED_CHARS 列表。如果一个禁止符列表不可用，则该字段应包含一个空字符串。</td></tr></table>

# 6.6 结束符视图

STOPWORDS视图包含了在WORD_INDEX中不包括的词集合(参见[5-4-3.6.7])。该视图必须包括以下<column>:

表5-4-3.13 Stop_words视图  

<table><tr><td>栏</td><td>类型</td><td>描述</td></tr><tr><td>STOP_WORD_LIST*</td><td>CHAR</td><td>结束符列表的名称。使用该结束符列表的栏应参考该名称。</td></tr><tr><td>STOP_WORD*</td><td>CHAR</td><td>未被索引的词。</td></tr></table>

# 6.7 #WORD_INDEX 视图

该视图包含全文本索引栏中的一个索引词。

表5-4-3.14 Word_index View  

<table><tr><td>栏</td><td>类型</td><td>描述</td></tr><tr><td>TABLE_CATALOG*</td><td>CHAR</td><td>包含方案的目录名。引用 SCHEMA 视图中CATALOG_NAME 的一个次关键字的组成部分。</td></tr><tr><td>SCHEMA_NAME*</td><td>CHAR</td><td>定义包含栏的表的方案名。引用 SCHEMA 视图中CATALOG_NAME 的一个次关键字。</td></tr><tr><td>TABLE_NAME*</td><td>CHAR</td><td>包含栏的表名，适用于一个 SFQL &lt;from_clause&gt;。引用 TABLES 视图的一个次关键字。</td></tr><tr><td>COLUMN_NAME*</td><td>CHAR</td><td>&lt;column&gt;(栏)名。引用 COLUMNIS 视图的一个次关键字。</td></tr><tr><td>TERM*</td><td>CHAR</td><td>索引术语。</td></tr><tr><td>ROWS</td><td>INTEGER</td><td>在表中，包含所引用栏中术语的行数。</td></tr><tr><td>OCCURRENCES</td><td>INTEGER</td><td>引用栏中 TERM(术语)的出现次数。</td></tr></table>

# 6.8 SEPARATORS视图

该视图包含在全文本索引步骤中用作分隔符(词、句子或字符)的字符集合。该视图必须包括以下<column>:

表5-4-3.15 分隔符视图  

<table><tr><td>栏</td><td>类型</td><td>描述</td></tr><tr><td>SEPARATOR_LIST*</td><td>CHAR</td><td>分隔符列表名，使用该分隔符列表的栏应引用 COLUMNS 视图的一个或多个下列栏中的这个名称 (FT_SEPWORDS、FT_SEPSENTENCES、FT_SEP_PARAGRPHS)。</td></tr><tr><td>SEPARATOR*</td><td>CHAR</td><td>分隔符，或字符序列，在全文本索引步骤执行期间使用。</td></tr></table>

# 6.9 SUPPRESSED_CHARS视图

该视图包含在全文本索引步骤执行期间从词中省略的特殊字符集合。这些字符和字符序列不从数据中删除，但它们在全文本查询的谓词(<contains_prediction>)中被忽略，以便能将它们与索引进行比较（在索引建立期间它们是禁止的）。该视图必须包括以下<column>:

表 5-4-3.16 #Suppressed-chars 视图  

<table><tr><td>栏</td><td>类型</td><td>描述</td></tr><tr><td>SUPRESSED_LIST*</td><td>CHAR</td><td>禁止字符列表名。使用该分隔符列表的栏应引用 COLUMNS视图的FT_SUPER_CHARACTERS栏中的列表名。</td></tr><tr><td>SUPRESSED*</td><td>CHAR</td><td>分隔符，或字符序列，除了构成结束符的序列外，在全文本索引步骤执行期间被忽略。</td></tr></table>

# 6.10 THESAURUS视图

该视图包含对于目录的词库条目集合。该视图必须包括以下<column>:

表 5-4-3.17 词库视图  

<table><tr><td>栏</td><td>类型</td><td>描述</td></tr><tr><td>TABLE_CATALOG*</td><td>CHAR</td><td>包含方案的目录名。引用 SCHEMA 视图中CATALOG_NAME 的一个次关键字的组成部分。</td></tr><tr><td>SCHEMA_NAME*</td><td>CHAR</td><td>方案名,该方案定义包含该栏的表。引用 SCHEMA视图中CATALOG_NAME 的一个次关键字。</td></tr><tr><td>TABLE_NAME*</td><td>CHAR</td><td>包含该栏的表名,适用于一个 SFQL &lt;from_clause&gt;中。引用 TABLES 视图的一个次关键字。</td></tr><tr><td>COLUMN_NAME*</td><td>CHAR</td><td>&lt;column&gt;(栏)名。引用 COLUMS 视图的一个次关键字。</td></tr><tr><td>TERM*</td><td>CHAR</td><td>扩充的词库术语</td></tr><tr><td>FUNCTION_CODE*</td><td>CHAR</td><td>表示词库功能的代码:</td></tr><tr><td></td><td></td><td>B = Broaden 广义词</td></tr><tr><td></td><td></td><td>S = Synonym 同义词</td></tr><tr><td></td><td></td><td>N = Narrow 狭义词</td></tr><tr><td>ALTERNATE_TERM*</td><td>CHAR</td><td>The alternate thesaurus term候选词库术语</td></tr></table>

# 7 错误代码目录

# 7.1 错误代码

SFQL中的错误代码应遵循SQL的SQLSTATE编码。

# 8 术语表

目录 方案的分组。每个方案目录都有它自己的信息方案(SFQL中的Text_Info_Schema)。

客户端(SFQL) 输入用户请求，并格式化和显示从SFQL“服务器”所接收数据的用户接口软件。

栏 在SFQL和SQL中，表的每一行由许多栏组成。栏包含对这个表有意义的数据。

单复数形式 能够接受以单数或复数形式以及与这两种形式均匹配的形式的查询条件。

<table><tr><td>导出表</td><td>类似于表,是由查询结果生成的一个行集合。客户端可以通过使用基于游标的 FETCH 命令从该集合中检索行。</td></tr><tr><td>匹配代码</td><td>插入到由服务器返回的文本中的字符串,以指示查找到的采样位置。客户端可以使用该信息,以执行用户接口函数,如用不同字体突出显示采样。</td></tr><tr><td>多重集</td><td>一个无序的对象集合,它不必独立。集合可以为空。</td></tr><tr><td>行</td><td>包含表中一个数据实例(如“Chapter(章)”表中的一个章)和其它任何属性的一个行,类似于一个 SQL 行</td></tr><tr><td>方案</td><td>通常,方案是数据的一种逻辑表示法,是面向一个特定数据库管理系统的方法,如对于一个 SQL 或 SFQL 数据库的一个数据模型。在 SQL 或 SFQL 中,一个方案是包含相关数据模型的表的一个集合。</td></tr><tr><td>服务程序(SFQL)</td><td>数据库引擎软件,用于查找并提供客户端请求的信息。</td></tr><tr><td>集合</td><td>独立对象的一个无序集合。集合可以为空。</td></tr><tr><td>SFQL 会话</td><td>在执行 SQL DISCONNECT 语句之前,通过 SQL CONNECT 语句在客户端和服务器之间建立的逻辑连接。</td></tr><tr><td>SFQL</td><td>结构化全文本查询语言。是 SQL 的扩展集,以允许访问全文本数据库。</td></tr><tr><td>词干</td><td>服务器能够匹配共享一个公用词干的动词形式的能力。</td></tr><tr><td>SQL</td><td>结构化查询语言。在关系型模式的基础上处理数据的一种代数学。由 IBM 发明,现在是一个 ANSI 和 ISO 标准。</td></tr><tr><td>表</td><td>类似于 SQL 表,数据库中始终具有一组行。</td></tr><tr><td>标记</td><td>文本中的一个标签,用于标识一个逻辑区域的开始和结束,或用于表示文本中的格式编排。SFQL 不关心文本中采用了什么标记方案,甚至 SFQL 不关心文本中是否有标记方案。标准通用置标语言 (SGML) 是与 SFQL 兼容的标记方法的一个范例。</td></tr><tr><td>视图</td><td>视图是由&lt;view_definition&gt;定义的已命名的导出表。它与术语 “视图表” 同义。</td></tr></table>

# 5-4-4 直接访问一在线访问

# 1 应用软件

直接在线访问规范定义了一个World Wide Web (WWW)标准的子集，以允许在行业内部协同工作。以下在线数据访问的简介已经被采用并可支持我们的共同需求。

TCP/IP网络协议  
- 通用 WWW 标准和公共 WEB 数据格式  
ZIP压缩支持  
文件传输协议 FTP)  
- 如果实施加密、数字签名和/或附加安全，那么应用软件应符合直接访问安全规范的要求[2-2-3]。  
- 任何一种 WEB 浏览器应至少支持下述内容:  
加密套接字协议层 (SSL) 安全  
- HTML和相关规范  
XML和相关规范  
- 脚本语言  
- 应能通过插件直接或用外部应用程序间接支持任何一种图形和多媒体格式，例如：  
GIF  
JPEG

CCITT Group IV TIFF  
- ATA CGM  
MPEG  
- QuickTime  
VMRL  
PNG  
- Portable Document Format(便携文档格式)([PDF])