-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3306
-- Generation Time: Jun 22, 2024 at 06:25 AM
-- Server version: 8.0.30
-- PHP Version: 8.1.10

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `userdata`
--

-- --------------------------------------------------------

--
-- Table structure for table `hospital`
--

CREATE TABLE `hospital` (
  `Nameoftablets` varchar(100) DEFAULT NULL,
  `ref` varchar(100) NOT NULL,
  `Dose` varchar(100) DEFAULT NULL,
  `NumberofTablets` varchar(100) DEFAULT NULL,
  `Lot` varchar(100) DEFAULT NULL,
  `Issuedate` varchar(100) DEFAULT NULL,
  `ExpDate` varchar(100) DEFAULT NULL,
  `DailyDose` varchar(100) DEFAULT NULL,
  `StorageAdvice` varchar(100) DEFAULT NULL,
  `nhsNumber` varchar(100) DEFAULT NULL,
  `PatientName` varchar(100) DEFAULT NULL,
  `DateOfBirth` varchar(100) DEFAULT NULL,
  `PatientAddress` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `hospital`
--

INSERT INTO `hospital` (`Nameoftablets`, `ref`, `Dose`, `NumberofTablets`, `Lot`, `Issuedate`, `ExpDate`, `DailyDose`, `StorageAdvice`, `nhsNumber`, `PatientName`, `DateOfBirth`, `PatientAddress`) VALUES
('Adderall', '331', '20 mg', '212', '55', '212', '34', '12', 'l', '321', 'daslkd', '34', 'Sqw');

-- --------------------------------------------------------

--
-- Table structure for table `register`
--

CREATE TABLE `register` (
  `fname` varchar(45) NOT NULL,
  `contact` varchar(45) NOT NULL,
  `email` varchar(45) NOT NULL,
  `securityQ` varchar(45) NOT NULL,
  `securityA` varchar(45) NOT NULL,
  `password` varchar(45) NOT NULL,
  `lname` varchar(45) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `register`
--

INSERT INTO `register` (`fname`, `contact`, `email`, `securityQ`, `securityA`, `password`, `lname`) VALUES
('lutfi', '03193017', '2222@m.com', 'Your Bestfriend', 'guling', '123', 'alfaridzi'),
('andes', '23103018081', 'asloak@m.com', 'Your Birth Place', 'medan', '123', 'sitepu'),
('iqbal', '0812192913', 'iqball@gmail.com', 'Your School Name', 'sma7', '123', 'himni'),
('rio', '23982093810', 'wjeijo@jwoa.com', 'Your Birth Place', 'lampung', '456', 'a');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `hospital`
--
ALTER TABLE `hospital`
  ADD PRIMARY KEY (`ref`);

--
-- Indexes for table `register`
--
ALTER TABLE `register`
  ADD PRIMARY KEY (`email`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
