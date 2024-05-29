-- MySQL dump 10.13  Distrib 8.0.36, for Linux (x86_64)
--
-- Host: localhost    Database: CVBuilder
-- ------------------------------------------------------
-- Server version	8.0.36-0ubuntu0.20.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `AwesomeResume`
--

DROP TABLE IF EXISTS `AwesomeResume`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `AwesomeResume` (
  `BaseTex` text,
  `Header` text,
  `School` text,
  `Experience` text,
  `Projects` text,
  `Skills` varchar(45) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `AwesomeResume`
--

LOCK TABLES `AwesomeResume` WRITE;
/*!40000 ALTER TABLE `AwesomeResume` DISABLE KEYS */;
/*!40000 ALTER TABLE `AwesomeResume` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `JakesTable`
--

DROP TABLE IF EXISTS `JakesTable`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `JakesTable` (
  `Header` text,
  `School` text,
  `Experience` text,
  `Projects` text,
  `Skills` text,
  `BaseTex` text,
  `keyid` varchar(45) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `JakesTable`
--

LOCK TABLES `JakesTable` WRITE;
/*!40000 ALTER TABLE `JakesTable` DISABLE KEYS */;
INSERT INTO `JakesTable` VALUES ('\n%----------HEADING----------\n% \\begin{tabular*}{\\textwidth}{l@{\\extracolsep{\\fill}}r}\n%   \\textbf{\\href{http://sourabhbajaj.com/}{\\Large Sourabh Bajaj}} & Email : \\href{mailto:sourabh@sourabhbajaj.com}{sourabh@sourabhbajaj.com}\\\\\n%   \\href{http://sourabhbajaj.com/}{http://www.sourabhbajaj.com} & Mobile : +1-123-456-7890 \\\\\n% \\end{tabular*}\n\n\\begin{center}\n    \\textbf{\\Huge \\scshape NAME} \\\\ \\vspace{1pt}\n    \\small PHONE $|$ \\href{mailto:x@x.com}{\\underline{EMAIL}} $|$ \n    \\href{https://linkedin.com/in/...}{\\underline{linkedin.com/in/LINKEDIN}} $|$\n    \\href{https://github.com/...}{\\underline{github.com/GITHUB}} 0\n\\end{center}','\n    \\resumeSubheading\n      {SCHOOL1}{SCHOOLLOCATION1, SCHOOLSTATE1}\n      {DEGREE1}{DEGREESTART1 -- DEGREEEND1}\n','\n    \\resumeSubheading\n      {TITLE1}{STARTDATE1 -- ENDDATE1}\n      {COMPANY1}{LOCATION1, STATE1}\n      \\resumeItemListStart\n        \\resumeItem{EXPERIENCE1BULLET1}\n		\\resumeItem{EXPERIENCE1BULLET2}\n		\\resumeItem{EXPERIENCE1BULLET3}\n        \\resumeItem{EXPERIENCE1BULLET4}\n      \\resumeItemListEnd\n','\n      \\resumeProjectHeading\n          {\\textbf{PROJECTTITLE1} $|$ \\emph{TECHLIST1}}{}\n          \\resumeItemListStart\n            \\resumeItem{PROJECT1BULLET1}\n            \\resumeItem{PROJECT1BULLET2}\n            \\resumeItem{PROJECT1BULLET3}\n            \\resumeItem{PROJECT1BULLET4}\n          \\resumeItemListEnd\n','\n    \\small{\\item{\n     \\textbf{SKILLSTITLE1}{: SKILLS1} \n\n    }}\n','\n%-------------------------\n% Resume in Latex\n% Author : Jake Gutierrez\n% Based off of: https://github.com/sb2nov/resume\n% License : MIT\n%------------------------\n\n\\documentclass[letterpaper,11pt]{article}\n\n\\usepackage{latexsym}\n\\usepackage[empty]{fullpage}\n\\usepackage{titlesec}\n\\usepackage{marvosym}\n\\usepackage[usenames,dvipsnames]{color}\n\\usepackage{verbatim}\n\\usepackage{enumitem}\n\\usepackage[hidelinks]{hyperref}\n\\usepackage{fancyhdr}\n\\usepackage[english]{babel}\n\\usepackage{tabularx}\n\\input{glyphtounicode}\n\n\n%----------FONT OPTIONS----------\n% sans-serif\n% \\usepackage[sfdefault]{FiraSans}\n% \\usepackage[sfdefault]{roboto}\n% \\usepackage[sfdefault]{noto-sans}\n% \\usepackage[default]{sourcesanspro}\n\n% serif\n% \\usepackage{CormorantGaramond}\n% \\usepackage{charter}\n\n\n\\pagestyle{fancy}\n\\fancyhf{} % clear all header and footer fields\n\\fancyfoot{}\n\\renewcommand{\\headrulewidth}{0pt}\n\\renewcommand{\\footrulewidth}{0pt}\n\n% Adjust margins\n\\addtolength{\\oddsidemargin}{-0.5in}\n\\addtolength{\\evensidemargin}{-0.5in}\n\\addtolength{\\textwidth}{1in}\n\\addtolength{\\topmargin}{-.5in}\n\\addtolength{\\textheight}{1.0in}\n\n\\urlstyle{same}\n\n\\raggedbottom\n\\raggedright\n\\setlength{\\tabcolsep}{0in}\n\n% Sections formatting\n\\titleformat{\\section}{\n  \\vspace{-4pt}\\scshape\\raggedright\\large\n}{}{0em}{}[\\color{black}\\titlerule \\vspace{-5pt}]\n\n% Ensure that generate pdf is machine readable/ATS parsable\n\\pdfgentounicode=1\n\n%-------------------------\n% Custom commands\n\\newcommand{\\resumeItem}[1]{\n  \\item\\small{\n    {#1 \\vspace{-2pt}}\n  }\n}\n\n\\newcommand{\\resumeSubheading}[4]{\n  \\vspace{-2pt}\\item\n    \\begin{tabular*}{0.97\\textwidth}[t]{l@{\\extracolsep{\\fill}}r}\n      \\textbf{#1} & #2 \\\\\n      \\textit{\\small#3} & \\textit{\\small #4} \\\\\n    \\end{tabular*}\\vspace{-7pt}\n}\n\n\\newcommand{\\resumeSubSubheading}[2]{\n    \\item\n    \\begin{tabular*}{0.97\\textwidth}{l@{\\extracolsep{\\fill}}r}\n      \\textit{\\small#1} & \\textit{\\small #2} \\\\\n    \\end{tabular*}\\vspace{-7pt}\n}\n\n\\newcommand{\\resumeProjectHeading}[2]{\n    \\item\n    \\begin{tabular*}{0.97\\textwidth}{l@{\\extracolsep{\\fill}}r}\n      \\small#1 & #2 \\\\\n    \\end{tabular*}\\vspace{-7pt}\n}\n\n\\newcommand{\\resumeSubItem}[1]{\\resumeItem{#1}\\vspace{-4pt}}\n\n\\renewcommand\\labelitemii{$\\vcenter{\\hbox{\\tiny$\\bullet$}}$}\n\n\\newcommand{\\resumeSubHeadingListStart}{\\begin{itemize}[leftmargin=0.15in, label={}]}\n\\newcommand{\\resumeSubHeadingListEnd}{\\end{itemize}}\n\\newcommand{\\resumeItemListStart}{\\begin{itemize}}\n\\newcommand{\\resumeItemListEnd}{\\end{itemize}\\vspace{-5pt}}\n\n%-------------------------------------------\n%%%%%%  RESUME STARTS HERE  %%%%%%%%%%%%%%%%%%%%%%%%%%%%\n\n\n\\begin{document}\n\n\n%-------------------------------------------\n\\end{document}\n\n','jakes');
/*!40000 ALTER TABLE `JakesTable` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `StylishTable`
--

DROP TABLE IF EXISTS `StylishTable`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `StylishTable` (
  `Header` text,
  `School` text,
  `Experience` text,
  `Projects` text,
  `Skills` text,
  `BaseTex` text,
  `keyid` varchar(45) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `StylishTable`
--

LOCK TABLES `StylishTable` WRITE;
/*!40000 ALTER TABLE `StylishTable` DISABLE KEYS */;
INSERT INTO `StylishTable` VALUES ('\n\n%----------------------------------------------------------------------------------------\n% HEADER SECTION\n%----------------------------------------------------------------------------------------\n\n{\\fontsize{24}{24}\\selectfont\\scshape\\textls[200]{NAME}} % Your name at the top\n\n\\vspace{0.5cm} % Extra whitespace after the large name at the top\n\n\\fontsize{10}{14}\\selectfont % Reduce font size\n{\\Large\\Letter} \\textls[150]{EMAIL\\ {\\Large\\Telefon} PHONE} % Your email address and phone number\n\n','\n\\gray Period & \\textbf{DEGREESTART1 --- DEGREEEND1}\\\\\n\\gray Degree & \\textbf{DEGREE1}\\\\\n\\gray University & \\textbf{SCHOOL1} \\hfill SCHOOLLOCATION1, SCHOOLSTATE1\\\\\n','\n\\gray Period & \\textbf{STARTDATE1 --- ENDDATE1}\\\\\n\\gray Employer & \\textbf{COMPANY1} \\hfill LOCATION1, STATE1\\\\\n\\gray Job Title & \\textbf{TITLE1}\\\\\n    & EXPERIENCE1BULLET1. \\\\\n    & EXPERIENCE1BULLET2. \\\\\n    & EXPERIENCE1BULLET3. \\\\\n    & EXPERIENCE1BULLET4. \\\\\n','\n\n\\gray Period & \\textbf{PSTARTDATE1 --- PENDDATE1}\\\\\n\\gray Title & \\textbf{TITLE1} \\\\\n\\gray Technologies & \\textbf{TECHLIST1}\\\\\n    & PROJECT1BULLET1. \\\\\n    & PROJECT1BULLET2. \\\\\n    & PROJECT1BULLET3. \\\\\n    & PROJECT1BULLET4. \\\\\n\n','\n\nSKILLSTITLE1 \\& SKILLS1 \\\\\n\n','\n%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%\n% Stylish Curriculum Vitae\n% LaTeX Template\n% Version 1.1 (September 10, 2021)\n%\n% This template originates from:\n% https://www.LaTeXTemplates.com\n%\n% Authors:\n% Stefano (https://www.kindoblue.nl)\n% Vel (vel@LaTeXTemplates.com)\n%\n% License:\n% CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)\n%\n%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%\n\n\\documentclass[a4paper, oneside, final]{scrartcl} % Paper options using the scrartcl class\n\n\\usepackage{scrlayer-scrpage} % Provides headers and footers configuration\n\\usepackage{titlesec} % Allows creating custom \\sections\n\\usepackage{marvosym} % Allows the use of symbols\n\\usepackage{tabularx,colortbl} % Advanced table configurations\n\\usepackage{ebgaramond} % Use the EB Garamond font\n\\usepackage{microtype} % To enable letterspacing\n\\usepackage{geometry} % To reduce margins\n\n% Reduce margins\n\\geometry{\n    top=0.5cm,\n    bottom=1cm,\n    left=1.5cm,\n    right=1.5cm,\n    headsep=5pt,\n    footskip=10pt\n}\n\n% Section formatting\n\\titleformat{\\section}{\\large\\scshape\\raggedright}{}{0em}{}[\\titlerule]\n\n% Custom highlighting for sections\n\\newcommand{\\gray}{\\rowcolor[gray]{.90}}\n\n% Font settings for footer\n\\renewcommand{\\headfont}{\\normalfont\\rmfamily\\scshape}\n\n\\begin{document}\n\n\\begin{center} % Center everything in the document\n\n\n\\end{center}\n\n\\end{document}\n\n','stylish');
/*!40000 ALTER TABLE `StylishTable` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `TemplateTable`
--

DROP TABLE IF EXISTS `TemplateTable`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `TemplateTable` (
  `keyid` varchar(10) DEFAULT NULL COMMENT 'sa',
  `Templates` text
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `TemplateTable`
--

LOCK TABLES `TemplateTable` WRITE;
/*!40000 ALTER TABLE `TemplateTable` DISABLE KEYS */;
INSERT INTO `TemplateTable` VALUES ('jakes','\n%-------------------------\n% Resume in Latex\n% Author : Jake Gutierrez\n% Based off of: https://github.com/sb2nov/resume\n% License : MIT\n%------------------------\n\n\\documentclass[letterpaper,11pt]{article}\n\n\\usepackage{latexsym}\n\\usepackage[empty]{fullpage}\n\\usepackage{titlesec}\n\\usepackage{marvosym}\n\\usepackage[usenames,dvipsnames]{color}\n\\usepackage{verbatim}\n\\usepackage{enumitem}\n\\usepackage[hidelinks]{hyperref}\n\\usepackage{fancyhdr}\n\\usepackage[english]{babel}\n\\usepackage{tabularx}\n\\input{glyphtounicode}\n\n\n%----------FONT OPTIONS----------\n% sans-serif\n% \\usepackage[sfdefault]{FiraSans}\n% \\usepackage[sfdefault]{roboto}\n% \\usepackage[sfdefault]{noto-sans}\n% \\usepackage[default]{sourcesanspro}\n\n% serif\n% \\usepackage{CormorantGaramond}\n% \\usepackage{charter}\n\n\n\\pagestyle{fancy}\n\\fancyhf{} % clear all header and footer fields\n\\fancyfoot{}\n\\renewcommand{\\headrulewidth}{0pt}\n\\renewcommand{\\footrulewidth}{0pt}\n\n% Adjust margins\n\\addtolength{\\oddsidemargin}{-0.5in}\n\\addtolength{\\evensidemargin}{-0.5in}\n\\addtolength{\\textwidth}{1in}\n\\addtolength{\\topmargin}{-.5in}\n\\addtolength{\\textheight}{1.0in}\n\n\\urlstyle{same}\n\n\\raggedbottom\n\\raggedright\n\\setlength{\\tabcolsep}{0in}\n\n% Sections formatting\n\\titleformat{\\section}{\n  \\vspace{-4pt}\\scshape\\raggedright\\large\n}{}{0em}{}[\\color{black}\\titlerule \\vspace{-5pt}]\n\n% Ensure that generate pdf is machine readable/ATS parsable\n\\pdfgentounicode=1\n\n%-------------------------\n% Custom commands\n\\newcommand{\\resumeItem}[1]{\n  \\item\\small{\n    {#1 \\vspace{-2pt}}\n  }\n}\n\n\\newcommand{\\resumeSubheading}[4]{\n  \\vspace{-2pt}\\item\n    \\begin{tabular*}{0.97\\textwidth}[t]{l@{\\extracolsep{\\fill}}r}\n      \\textbf{#1} & #2 \\\\\n      \\textit{\\small#3} & \\textit{\\small #4} \\\\\n    \\end{tabular*}\\vspace{-7pt}\n}\n\n\\newcommand{\\resumeSubSubheading}[2]{\n    \\item\n    \\begin{tabular*}{0.97\\textwidth}{l@{\\extracolsep{\\fill}}r}\n      \\textit{\\small#1} & \\textit{\\small #2} \\\\\n    \\end{tabular*}\\vspace{-7pt}\n}\n\n\\newcommand{\\resumeProjectHeading}[2]{\n    \\item\n    \\begin{tabular*}{0.97\\textwidth}{l@{\\extracolsep{\\fill}}r}\n      \\small#1 & #2 \\\\\n    \\end{tabular*}\\vspace{-7pt}\n}\n\n\\newcommand{\\resumeSubItem}[1]{\\resumeItem{#1}\\vspace{-4pt}}\n\n\\renewcommand\\labelitemii{$\\vcenter{\\hbox{\\tiny$\\bullet$}}$}\n\n\\newcommand{\\resumeSubHeadingListStart}{\\begin{itemize}[leftmargin=0.15in, label={}]}\n\\newcommand{\\resumeSubHeadingListEnd}{\\end{itemize}}\n\\newcommand{\\resumeItemListStart}{\\begin{itemize}}\n\\newcommand{\\resumeItemListEnd}{\\end{itemize}\\vspace{-5pt}}\n\n%-------------------------------------------\n%%%%%%  RESUME STARTS HERE  %%%%%%%%%%%%%%%%%%%%%%%%%%%%\n\n\n\\begin{document}\n\n%----------HEADING----------\n% \\begin{tabular*}{\\textwidth}{l@{\\extracolsep{\\fill}}r}\n%   \\textbf{\\href{http://sourabhbajaj.com/}{\\Large Sourabh Bajaj}} & Email : \\href{mailto:sourabh@sourabhbajaj.com}{sourabh@sourabhbajaj.com}\\\\\n%   \\href{http://sourabhbajaj.com/}{http://www.sourabhbajaj.com} & Mobile : +1-123-456-7890 \\\\\n% \\end{tabular*}\n\n\\begin{center}\n    \\textbf{\\Huge \\scshape NAME} \\\\ \\vspace{1pt}\n    \\small PHONE $|$ \\href{mailto:x@x.com}{\\underline{EMAIL}} $|$ \n    \\href{https://linkedin.com/in/...}{\\underline{linkedin.com/in/LINKEDIN}} $|$\n    \\href{https://github.com/...}{\\underline{github.com/GITHUB}}\n\\end{center}\n\n\n%-----------EDUCATION-----------\n\\section{Education}\n  \\resumeSubHeadingListStart\n    \\resumeSubheading\n      {SCHOOL1}{SCHOOLLOCATION1, SCHOOLSTATE1}\n      {DEGREE1}{DEGREESTART1 -- DEGREEEND1}\n    \\resumeSubheading\n      {SCHOOL2}{SCHOOLLOCATION2, SCHOOLSTATE2}\n      {DEGREE2}{DEGREESTART2 -- DEGREEEND2}\n  \\resumeSubHeadingListEnd\n\n\n%-----------EXPERIENCE-----------\n\\section{Experience}\n  \\resumeSubHeadingListStart\n\n    \\resumeSubheading\n      {EXPERIENCE1}{STARTDATE1 -- ENDDATE1}\n      {COMPANY1}{LOCATION1, STATE1}\n      \\resumeItemListStart\n        \\resumeItem{EXPERIENCE1BULLET1}\n        \\resumeItem{EXPERIENCE1BULLET2}\n        \\resumeItem{EXPERIENCE1BULLET3}\n      \\resumeItemListEnd\n      \n% -----------Multiple Positions Heading-----------\n%    \\resumeSubSubheading\n%     {Software Engineer I}{Oct 2014 - Sep 2016}\n%     \\resumeItemListStart\n%        \\resumeItem{Apache Beam}\n%          {Apache Beam is a unified model for defining both batch and streaming data-parallel processing pipelines}\n%     \\resumeItemListEnd\n%    \\resumeSubHeadingListEnd\n%-------------------------------------------\n\n    \\resumeSubheading\n      {EXPERIENCE2}{STARTDATE2 -- ENDDATE2}\n      {COMPANY2}{LOCATION2, STATE2}\n      \\resumeItemListStart\n        \\resumeItem{EXPERIENCE2BULLET1}\n        \\resumeItem{EXPERIENCE2BULLET2}\n        \\resumeItem{EXPERIENCE2BULLET3}\n      \\resumeItemListEnd\n\n    \\resumeSubheading\n      {EXPERIENCE3}{STARTDATE3 -- ENDDATE3}\n      {COMPANY3}{LOCATION3, STATE3}\n      \\resumeItemListStart\n        \\resumeItem{EXPERIENCE3BULLET1}\n        \\resumeItem{EXPERIENCE3BULLET2}\n        \\resumeItem{EXPERIENCE3BULLET3}\n      \\resumeItemListEnd\n\n  \\resumeSubHeadingListEnd\n\n\n%-----------PROJECTS-----------\n\\section{Projects}\n    \\resumeSubHeadingListStart\n      \\resumeProjectHeading\n          {\\textbf{PROJECTTITLE1} $|$ \\emph{TECHLIST1}}{PSTARTDATE1 -- PSTENDDATE1}\n          \\resumeItemListStart\n            \\resumeItem{PROJECT1BULLET1}\n            \\resumeItem{PROJECT1BULLET2}\n            \\resumeItem{PROJECT1BULLET3}\n            \\resumeItem{PROJECT1BULLET4}\n          \\resumeItemListEnd\n      \\resumeProjectHeading\n          {\\textbf{PROJECTTITLE2} $|$ \\emph{TECHLIST2}}{PSTARTDATE2 -- PSTENDDATE2}\n          \\resumeItemListStart\n            \\resumeItem{PROJECT2BULLET1}\n            \\resumeItem{PROJECT2BULLET2}\n            \\resumeItem{PROJECT2BULLET3}\n            \\resumeItem{PROJECT2BULLET4}\n          \\resumeItemListEnd\n    \\resumeSubHeadingListEnd\n\n\n\n%\n%-----------PROGRAMMING SKILLS-----------\n\\section{Technical Skills}\n \\begin{itemize}[leftmargin=0.15in, label={}]\n    \\small{\\item{\n     \\textbf{SKILLSTITLE1}{: SKILLS1} \\\\\n     \\textbf{SKILLSTITLE2}{: SKILLS2} \\\\\n     \\textbf{SKILLSTITLE3}{: SKILLS3} \\\\\n     \\textbf{SKILLSTITLE4}{: SKILLS4}\n    }}\n \\end{itemize}\n\n\n%-------------------------------------------\n\\end{document}\n\n'),('stylish','\n%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%\n% Stylish Curriculum Vitae\n% LaTeX Template\n% Version 1.1 (September 10, 2021)\n%\n% This template originates from:\n% https://www.LaTeXTemplates.com\n%\n% Authors:\n% Stefano (https://www.kindoblue.nl)\n% Vel (vel@LaTeXTemplates.com)\n%\n% License:\n% CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)\n%\n%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%\n\n\\documentclass[a4paper, oneside, final]{scrartcl} % Paper options using the scrartcl class\n\n\\usepackage{scrlayer-scrpage} % Provides headers and footers configuration\n\\usepackage{titlesec} % Allows creating custom \\sections\n\\usepackage{marvosym} % Allows the use of symbols\n\\usepackage{tabularx,colortbl} % Advanced table configurations\n\\usepackage{ebgaramond} % Use the EB Garamond font\n\\usepackage{microtype} % To enable letterspacing\n\\usepackage{geometry} % To reduce margins\n\n% Reduce margins\n\\geometry{\n    top=0.5cm,\n    bottom=1cm,\n    left=1.5cm,\n    right=1.5cm,\n    headsep=5pt,\n    footskip=10pt\n}\n\n% Section formatting\n\\titleformat{\\section}{\\large\\scshape\\raggedright}{}{0em}{}[\\titlerule]\n\n% Custom highlighting for sections\n\\newcommand{\\gray}{\\rowcolor[gray]{.90}}\n\n% Font settings for footer\n\\renewcommand{\\headfont}{\\normalfont\\rmfamily\\scshape}\n\n\\begin{document}\n\n\\begin{center} % Center everything in the document\n\n%----------------------------------------------------------------------------------------\n% HEADER SECTION\n%----------------------------------------------------------------------------------------\n\n{\\fontsize{24}{24}\\selectfont\\scshape\\textls[200]{NAME}} % Your name at the top\n\n\\vspace{0.5cm} % Extra whitespace after the large name at the top\n\n\\fontsize{10}{14}\\selectfont % Reduce font size\n{\\Large\\Letter} \\textls[150]{EMAIL\\ {\\Large\\Telefon} PHONE} % Your email address and phone number\n\n%----------------------------------------------------------------------------------------\n% WORK EXPERIENCE SECTION\n%----------------------------------------------------------------------------------------\n\n\\section{Experience}\n\n\\begin{tabularx}{0.97\\linewidth}{>{\\raggedleft\\scshape}p{2cm}X}\n\\gray Period & \\textbf{STARTDATE1 --- ENDDATE1}\\\\\n\\gray Employer & \\textbf{COMPANY1} \\hfill LOCATION1, STATE1\\\\\n\\gray Job Title & \\textbf{TITLE1}\\\\\n    & EXPERIENCE1BULLET1. \\\\\n    & EXPERIENCE1BULLET2. \\\\\n    & EXPERIENCE1BULLET3. \\\\\n    & EXPERIENCE1BULLET4. \\\\\n\\end{tabularx}\n\n%----------------------------------------------------------------------------------------\n% PROJECTS SECTION\n%----------------------------------------------------------------------------------------\n\n\\section{Projects}\n\n\\begin{tabularx}{0.97\\linewidth}{>{\\raggedleft\\scshape}p{2cm}X}\n\\gray Period & \\textbf{PSTARTDATE1 --- PENDDATE1}\\\\\n\\gray Title & \\textbf{TITLE1} \\\\\n\\gray Technologies & \\textbf{TECHLIST1}\\\\\n    & PROJECT1BULLET1. \\\\\n    & PROJECT1BULLET2. \\\\\n    & PROJECT1BULLET3. \\\\\n    & PROJECT1BULLET4. \\\\\n\\end{tabularx}\n\n%----------------------------------------------------------------------------------------\n% EDUCATION SECTION\n%----------------------------------------------------------------------------------------\n\n\\section{Education}\n\n\\begin{tabularx}{0.97\\linewidth}{>{\\raggedleft\\scshape}p{2cm}X}\n\\gray Period & \\textbf{DEGREESTART1 --- DEGREEEND1}\\\\\n\\gray Degree & \\textbf{DEGREE1}\\\\\n\\gray University & \\textbf{SCHOOL1} \\hfill SCHOOLLOCATION1, SCHOOLSTATE1\\\\\n\\end{tabularx}\n\n\\vspace{10pt}\n\n%----------------------------------------------------------------------------------------\n% SKILLS SECTION\n%----------------------------------------------------------------------------------------\n\n\\section{Skills}\n\n\\begin{tabular}{ @{} >{\\bfseries}l @{\\hspace{6ex}} l }\nSKILLSTITLE1 \\& SKILLS1 \\\\\n\\end{tabular}\n\n%----------------------------------------------------------------------------------------\n\n\\end{center}\n\n\\end{document}\n\n');
/*!40000 ALTER TABLE `TemplateTable` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;