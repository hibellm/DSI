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
-- Table structure for table `gmail`
--

DROP TABLE IF EXISTS `gmail`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `gmail` (
  `idgmail` int(11) NOT NULL,
  `gmSender` varchar(100) NOT NULL,
  `gmSubject` varchar(100) DEFAULT NULL,
  `gmType` varchar(45) DEFAULT NULL,
  `gmSentDate` datetime NOT NULL,
  PRIMARY KEY (`idgmail`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='List of gmail mails';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `gmail`
--

LOCK TABLES `gmail` WRITE;
/*!40000 ALTER TABLE `gmail` DISABLE KEYS */;
INSERT INTO `gmail` VALUES (1,'cdsr.bot@cdsr.com','Data Request from CDSR (Cellcept)','Data Request','2018-10-04 23:21:34'),(2,'cdsr.bot@cdsr.com','Inofrmation Request REF: xyz987','Information Request','2018-10-01 23:21:34'),(3,'Peter.parker@spiderman.dc','Internal sharing request REF:Harbor Use-case 22','Internal Data Request','2018-08-04 08:31:34'),(4,'cdsr.bot@cdsr.com','Data Request ABC-123','Data Request','2018-09-14 12:21:34');
/*!40000 ALTER TABLE `gmail` ENABLE KEYS */;
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
