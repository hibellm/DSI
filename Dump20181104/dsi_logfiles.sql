CREATE DATABASE  IF NOT EXISTS `dsi` /*!40100 DEFAULT CHARACTER SET utf8 */;
USE `dsi`;
-- MySQL dump 10.13  Distrib 5.7.12, for Win64 (x86_64)
--
-- Host: localhost    Database: dsi
-- ------------------------------------------------------
-- Server version	5.7.17-log

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `logfiles`
--

DROP TABLE IF EXISTS `logfiles`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `logfiles` (
  `logfileid` int(11) NOT NULL AUTO_INCREMENT,
  `filename` varchar(45) NOT NULL,
  `filedescription` varchar(500) DEFAULT NULL,
  `pathtofile` varchar(100) DEFAULT NULL,
  `filehash` varchar(20) DEFAULT NULL,
  `filecreatedate` datetime DEFAULT NULL,
  `category` varchar(45) NOT NULL,
  `jirakey` varchar(8) DEFAULT NULL,
  `filecat` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`logfileid`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8 COMMENT='log information for a file';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `logfiles`
--

LOCK TABLES `logfiles` WRITE;
/*!40000 ALTER TABLE `logfiles` DISABLE KEYS */;
INSERT INTO `logfiles` VALUES (1,'text.txt','a description of the text file','c:/abc/xyz','a6ed0c785d4590bc95c2','2018-10-27 23:18:44','ABC','RCR-3','content'),(2,'data1.sas7bdat','The main SAS dataset from Study ABC','c:/abc/xyz','80c93ca4d04b5367abc9','2018-10-27 23:20:19','ABC','RCR-3','content'),(3,'data2.sas7bdat','The secondary SAS dataset from Study ABC','c:/abc/xyz','64dfa8100a6bb2c34373','2018-10-27 23:20:49','ABC','RCR-3','content'),(4,'doc.pdf','The Autogenerated documentation for Study ABC','c:/abc/xyz/documentation','24cc42a6ca852ccdfaae','2018-10-27 23:21:26','ABC','RCR-3','content'),(5,'abc.zip','The zipfile of deliverables for Study ABC','c:/abc/xyz/delivery','389cf23951b1af6b9f56','2018-10-27 23:22:09','ABC','RCR-3','zip'),(6,'mjh.csv','Document test','c:/xyz/__x/documentation','b4c5a82be9d228146cf3','2018-11-17 10:20:49','XYZ','RCR-2','content'),(7,'other.csv','Raw data file','c:/xyz/data','24cc42a6xxx52ccdfaae','2018-11-17 11:20:49','XYZ','RCR-2','content'),(8,'other.csv','Raw data file (copy for testing Jira key)','c:/xyz/data','24cc42a6xxx52ccdfaae','2018-07-27 11:20:49','XYZ','RCR-5','content');
/*!40000 ALTER TABLE `logfiles` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-11-04 21:03:28