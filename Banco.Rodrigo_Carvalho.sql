-- phpMyAdmin SQL Dump
-- version 4.5.4.1
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: 19-Out-2023 às 22:59
-- Versão do servidor: 5.7.11
-- PHP Version: 5.6.18

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `bd_geren_tarefa`
--
CREATE DATABASE IF NOT EXISTS `bd_geren_tarefa` DEFAULT CHARACTER SET latin1 COLLATE latin1_swedish_ci;
USE `bd_geren_tarefa`;

-- --------------------------------------------------------

--
-- Estrutura da tabela `tb_controle`
--

CREATE TABLE `tb_controle` (
  `cod` int(11) NOT NULL,
  `descri` varchar(60) DEFAULT NULL,
  `dataI` date DEFAULT NULL,
  `dataT` date DEFAULT NULL,
  `respo` varchar(30) DEFAULT NULL,
  `tipo` varchar(10) DEFAULT NULL,
  `obs` varchar(150) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Extraindo dados da tabela `tb_controle`
--

INSERT INTO `tb_controle` (`cod`, `descri`, `dataI`, `dataT`, `respo`, `tipo`, `obs`) VALUES
(2, 'jskadhdlkjsahkdhsakjdhkjsa', '2001-01-01', '2002-01-01', 'dsakjdhaskjhdklas', 'Media', 'hsadjahskdjhaskjdhaksjdgkasjghdaskjghdakjsdghkjasdghjkhkjaghdkjasgdkjasg');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `tb_controle`
--
ALTER TABLE `tb_controle`
  ADD PRIMARY KEY (`cod`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `tb_controle`
--
ALTER TABLE `tb_controle`
  MODIFY `cod` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
