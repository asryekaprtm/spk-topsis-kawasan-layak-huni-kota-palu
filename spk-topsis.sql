-- phpMyAdmin SQL Dump
-- version 5.0.3
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Waktu pembuatan: 01 Jul 2024 pada 17.05
-- Versi server: 10.4.14-MariaDB
-- Versi PHP: 7.4.11

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `spk-topsis`
--

-- --------------------------------------------------------

--
-- Struktur dari tabel `alternative`
--

CREATE TABLE `alternative` (
  `id` int(1) NOT NULL,
  `merek` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data untuk tabel `alternative`
--

INSERT INTO `alternative` (`id`, `merek`) VALUES
(1, 'Lenovo'),
(2, 'MSI'),
(3, 'Asus'),
(4, 'Toshiba'),
(6, 'HP'),
(7, 'dell');

-- --------------------------------------------------------

--
-- Struktur dari tabel `kriteria`
--

CREATE TABLE `kriteria` (
  `id` int(11) NOT NULL,
  `ram` varchar(100) NOT NULL,
  `ssd` varchar(100) NOT NULL,
  `processor` varchar(100) NOT NULL,
  `ukuran_layar` varchar(100) NOT NULL,
  `harga` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data untuk tabel `kriteria`
--

INSERT INTO `kriteria` (`id`, `ram`, `ssd`, `processor`, `ukuran_layar`, `harga`) VALUES
(1, '0.2', '0.15', '0.4', '0.15', '0.1');

-- --------------------------------------------------------

--
-- Struktur dari tabel `matriks_terbobot`
--

CREATE TABLE `matriks_terbobot` (
  `id` int(11) NOT NULL,
  `merek` varchar(100) NOT NULL,
  `c1` varchar(100) NOT NULL,
  `c2` varchar(100) NOT NULL,
  `c3` varchar(100) NOT NULL,
  `c4` varchar(100) NOT NULL,
  `c5` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data untuk tabel `matriks_terbobot`
--

INSERT INTO `matriks_terbobot` (`id`, `merek`, `c1`, `c2`, `c3`, `c4`, `c5`) VALUES
(1, 'Lenovo', '0.093', '0.061', '0.142', '0.07', '0.035'),
(2, 'MSI', '0.093', '0.076', '0.236', '0.056', '0.071'),
(3, 'Toshiba', '0.074', '0.076', '0.236', '0.07', '0.035'),
(4, 'HP', '0.093', '0.061', '0.142', '0.07', '0.035'),
(5, 'Dala', '0.093', '0.061', '0.094', '0.07', '0.035');

-- --------------------------------------------------------

--
-- Struktur dari tabel `penilaian`
--

CREATE TABLE `penilaian` (
  `id` int(11) NOT NULL,
  `merek` varchar(100) NOT NULL,
  `ram` varchar(100) NOT NULL,
  `ssd` varchar(100) NOT NULL,
  `processor` varchar(100) NOT NULL,
  `ukuran_layar` varchar(100) NOT NULL,
  `harga` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data untuk tabel `penilaian`
--

INSERT INTO `penilaian` (`id`, `merek`, `ram`, `ssd`, `processor`, `ukuran_layar`, `harga`) VALUES
(1, 'Lenovo', '5', '4', '3', '5', '1'),
(2, 'MSI', '5', '5', '5', '4', '2'),
(4, 'Toshiba', '4', '5', '5', '5', '1'),
(6, 'HP', '5', '4', '3', '5', '1'),
(8, 'Dala', '5', '4', '2', '5', '1');

-- --------------------------------------------------------

--
-- Struktur dari tabel `preferensi`
--

CREATE TABLE `preferensi` (
  `id` int(11) NOT NULL,
  `merek` varchar(100) NOT NULL,
  `nilai_preferensi` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Indexes for dumped tables
--

--
-- Indeks untuk tabel `alternative`
--
ALTER TABLE `alternative`
  ADD PRIMARY KEY (`id`);

--
-- Indeks untuk tabel `kriteria`
--
ALTER TABLE `kriteria`
  ADD PRIMARY KEY (`id`);

--
-- Indeks untuk tabel `matriks_terbobot`
--
ALTER TABLE `matriks_terbobot`
  ADD PRIMARY KEY (`id`);

--
-- Indeks untuk tabel `penilaian`
--
ALTER TABLE `penilaian`
  ADD PRIMARY KEY (`id`);

--
-- Indeks untuk tabel `preferensi`
--
ALTER TABLE `preferensi`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT untuk tabel yang dibuang
--

--
-- AUTO_INCREMENT untuk tabel `alternative`
--
ALTER TABLE `alternative`
  MODIFY `id` int(1) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT untuk tabel `kriteria`
--
ALTER TABLE `kriteria`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT untuk tabel `matriks_terbobot`
--
ALTER TABLE `matriks_terbobot`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT untuk tabel `penilaian`
--
ALTER TABLE `penilaian`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT untuk tabel `preferensi`
--
ALTER TABLE `preferensi`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
