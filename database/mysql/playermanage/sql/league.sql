-- phpMyAdmin SQL Dump
-- version 4.5.2
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: 07-Out-2016 às 16:32
-- Versão do servidor: 10.1.13-MariaDB
-- PHP Version: 5.6.23

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `league`
--

DELIMITER $$
--
-- Procedures
--
CREATE DEFINER=`root`@`localhost` PROCEDURE `addAbate` (IN `id` INT(11))  NO SQL
UPDATE time SET time.abates = time.abates+1 WHERE time.time_id = id$$

DELIMITER ;

-- --------------------------------------------------------

--
-- Estrutura da tabela `jogador`
--

CREATE TABLE `jogador` (
  `jogador_id` int(11) NOT NULL,
  `time_id` int(11) DEFAULT NULL,
  `nome` varchar(45) DEFAULT NULL,
  `abates_totais` int(11) DEFAULT NULL,
  `mortes_totais` int(11) DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

--
-- Extraindo dados da tabela `jogador`
--

INSERT INTO `jogador` (`jogador_id`, `time_id`, `nome`, `abates_totais`, `mortes_totais`) VALUES
(1, 1, 'Italus', 5, 2),
(2, 1, 'Thiago', 10, 7),
(3, 1, 'Gabriela', 1, 3),
(4, 1, 'Macabeus', 0, 3),
(5, 1, 'Trabson', 14, 0),
(6, 2, 'Douglas', 8, 8),
(7, 2, 'Estela', 2, 2),
(8, 2, 'Elias', 25, 15),
(9, 2, 'Designer', 3, 1),
(10, 2, 'Pistela', 2, 9),
(12, 3, 'Moskito', 3, 5),
(13, 3, 'Kira', 1, 9),
(16, 3, 'Alsaher', 7, 1),
(17, 3, 'Rodrix', 2, 20),
(18, 3, 'Lalitax', 7, 5);

--
-- Acionadores `jogador`
--
DELIMITER $$
CREATE TRIGGER `addTabate` AFTER UPDATE ON `jogador` FOR EACH ROW CALL addAbate(NEW.`time_id`)
$$
DELIMITER ;

-- --------------------------------------------------------

--
-- Estrutura da tabela `partida`
--

CREATE TABLE `partida` (
  `partida_id` int(11) NOT NULL,
  `timeA_id` int(11) DEFAULT NULL,
  `timeB_id` int(11) DEFAULT NULL,
  `abates_timeA` int(11) DEFAULT NULL,
  `abates_timeB` int(11) DEFAULT NULL,
  `vencedor_id` int(11) DEFAULT NULL,
  `torneio_id` varchar(45) DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

--
-- Extraindo dados da tabela `partida`
--

INSERT INTO `partida` (`partida_id`, `timeA_id`, `timeB_id`, `abates_timeA`, `abates_timeB`, `vencedor_id`, `torneio_id`) VALUES
(1, 1, 2, 20, 10, 1, '1'),
(2, 2, 3, 30, 15, 2, '1'),
(3, 1, 3, 10, 5, 1, '1');

-- --------------------------------------------------------

--
-- Estrutura da tabela `personagem`
--

CREATE TABLE `personagem` (
  `personagem_id` int(11) NOT NULL,
  `personagem_nome` varchar(45) DEFAULT NULL,
  `personagem_preco` int(11) DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

--
-- Extraindo dados da tabela `personagem`
--

INSERT INTO `personagem` (`personagem_id`, `personagem_nome`, `personagem_preco`) VALUES
(1, 'Ashe', 1200),
(2, 'Vayne', 2000),
(3, 'Tryndamere', 1200),
(4, 'Blitzcrank', 2000),
(5, 'Amumu', 2000),
(6, 'Fiora', 4500),
(7, 'Sona', 6300),
(10, 'Alistar', 900),
(8, 'Morgana', 6300),
(9, 'Kayle', 4500);

-- --------------------------------------------------------

--
-- Estrutura da tabela `personagem_comprado`
--

CREATE TABLE `personagem_comprado` (
  `personagem_id` int(11) NOT NULL,
  `jogador_id` int(11) DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

--
-- Extraindo dados da tabela `personagem_comprado`
--

INSERT INTO `personagem_comprado` (`personagem_id`, `jogador_id`) VALUES
(1, 1),
(2, 1),
(3, 1),
(4, 1),
(5, 1),
(1, 2),
(2, 2),
(1, 3),
(4, 3);

-- --------------------------------------------------------

--
-- Estrutura da tabela `time`
--

CREATE TABLE `time` (
  `time_id` int(11) NOT NULL,
  `nome_time` varchar(45) DEFAULT NULL,
  `abates` int(11) DEFAULT NULL,
  `mortes` int(11) DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

--
-- Extraindo dados da tabela `time`
--

INSERT INTO `time` (`time_id`, `nome_time`, `abates`, `mortes`) VALUES
(1, 'BepidPower', 30, 15),
(2, 'AlbusNox', 40, 35),
(3, 'Invocados', 20, 40);

-- --------------------------------------------------------

--
-- Estrutura da tabela `torneio`
--

CREATE TABLE `torneio` (
  `torneio_id` int(11) NOT NULL,
  `regiao_torneio` varchar(45) DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

--
-- Extraindo dados da tabela `torneio`
--

INSERT INTO `torneio` (`torneio_id`, `regiao_torneio`) VALUES
(1, 'Brasil');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `jogador`
--
ALTER TABLE `jogador`
  ADD PRIMARY KEY (`jogador_id`);

--
-- Indexes for table `partida`
--
ALTER TABLE `partida`
  ADD PRIMARY KEY (`partida_id`);

--
-- Indexes for table `personagem`
--
ALTER TABLE `personagem`
  ADD PRIMARY KEY (`personagem_id`);

--
-- Indexes for table `personagem_comprado`
--
ALTER TABLE `personagem_comprado`
  ADD KEY `jogador_id` (`jogador_id`),
  ADD KEY `jogador_id_2` (`jogador_id`);

--
-- Indexes for table `time`
--
ALTER TABLE `time`
  ADD PRIMARY KEY (`time_id`);

--
-- Indexes for table `torneio`
--
ALTER TABLE `torneio`
  ADD PRIMARY KEY (`torneio_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `jogador`
--
ALTER TABLE `jogador`
  MODIFY `jogador_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=19;
--
-- AUTO_INCREMENT for table `partida`
--
ALTER TABLE `partida`
  MODIFY `partida_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;
--
-- AUTO_INCREMENT for table `personagem`
--
ALTER TABLE `personagem`
  MODIFY `personagem_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;
--
-- AUTO_INCREMENT for table `time`
--
ALTER TABLE `time`
  MODIFY `time_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
