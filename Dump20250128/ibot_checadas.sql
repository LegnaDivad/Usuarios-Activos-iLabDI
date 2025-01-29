-- MySQL dump 10.13  Distrib 8.0.40, for macos14 (arm64)
--
-- Host: localhost    Database: ibot
-- ------------------------------------------------------
-- Server version	9.1.0

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
-- Table structure for table `checadas`
--

DROP TABLE IF EXISTS `checadas`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `checadas` (
  `identificador` varchar(255) NOT NULL,
  `horaEntrada` time NOT NULL,
  `fechaEntrada` date NOT NULL,
  `horaSalida` time DEFAULT NULL,
  `fechaSalida` date DEFAULT NULL,
  `Horas` time DEFAULT NULL,
  `id` int NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`id`),
  KEY `fk_identificador_alumnos` (`identificador`),
  CONSTRAINT `fk_identificador_alumnos` FOREIGN KEY (`identificador`) REFERENCES `alumno` (`idChat`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `checadas`
--

LOCK TABLES `checadas` WRITE;
/*!40000 ALTER TABLE `checadas` DISABLE KEYS */;
INSERT INTO `checadas` VALUES ('1','08:00:00','2025-01-09','12:00:00','2025-01-09','04:00:00',6),('2','09:15:00','2025-01-09','13:15:00','2025-01-09','04:00:00',7),('3','10:30:00','2025-01-09','14:30:00','2025-01-09','04:00:00',8),('4','07:45:00','2025-01-09','11:45:00','2025-01-09','04:00:00',9),('5','08:30:00','2025-01-09','12:30:00','2025-01-09','04:00:00',10),('6','08:30:00','2025-01-09','12:30:00','2025-01-09','04:00:00',11),('6','08:30:00','2025-01-09','09:30:00','2025-01-09',NULL,12);
/*!40000 ALTER TABLE `checadas` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-01-28 22:54:11
