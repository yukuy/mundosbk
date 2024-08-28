-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 28-08-2024 a las 17:59:07
-- Versión del servidor: 10.4.32-MariaDB
-- Versión de PHP: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `mundosbk`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `comentarios`
--

CREATE TABLE `comentarios` (
  `id` int(11) NOT NULL,
  `idUsuarios` int(11) NOT NULL,
  `idMotos` int(11) NOT NULL,
  `comentario` varchar(1000) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

--
-- Volcado de datos para la tabla `comentarios`
--

INSERT INTO `comentarios` (`id`, `idUsuarios`, `idMotos`, `comentario`) VALUES
(4, 1, 8, 'muy buena moto \r\n');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `marca`
--

CREATE TABLE `marca` (
  `id` int(11) NOT NULL,
  `nombre` varchar(45) DEFAULT NULL,
  `modelo` varchar(45) DEFAULT NULL,
  `serie` varchar(45) DEFAULT NULL,
  `logo` varchar(200) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

--
-- Volcado de datos para la tabla `marca`
--

INSERT INTO `marca` (`id`, `nombre`, `modelo`, `serie`, `logo`) VALUES
(1, 'YAMAHA', '2015-2024', 'yzf-r', NULL),
(2, 'HONDA', '2015-2024', 'cbr', NULL),
(3, 'SUSUKY', '2015-2020', 'gsxr', NULL),
(4, 'KAWASAKY', '2015-2024', 'ZX-RR', NULL),
(5, 'BMW', '2015-2024', 'S-RR', NULL),
(6, 'DUCATI', '2015-2024', 'panigale', NULL);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `motos`
--

CREATE TABLE `motos` (
  `id` int(11) NOT NULL,
  `nombre` varchar(45) DEFAULT NULL,
  `cantidad` int(11) DEFAULT NULL,
  `precio` int(11) DEFAULT NULL,
  `foto` varchar(200) DEFAULT NULL,
  `descripcion` text DEFAULT NULL,
  `marca_id` int(11) NOT NULL,
  `usuarios_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

--
-- Volcado de datos para la tabla `motos`
--

INSERT INTO `motos` (`id`, `nombre`, `cantidad`, `precio`, `foto`, `descripcion`, `marca_id`, `usuarios_id`) VALUES
(8, 'GSX-S 750', 30, 55000000, 'xayA7v8C.jpg', 'La Suzuki GSX-S750 es una motocicleta naked deportiva que combina un diseño agresivo con un rendimiento excepcional. Equipada con un motor de 749 cc, ofrece una potencia suave y controlable, ideal tanto para el uso en ciudad como para rutas más largas. Su chasis compacto y ágil proporciona una experiencia de conducción dinámica, mientras que su estética moderna y elegante capta la atención al instante.', 3, 1),
(9, 'M 1000R', 17, 200000000, 'gsouYktl.jpg', 'La BMW M 1000 R es una motocicleta naked de alto rendimiento que lleva la emoción de la pista a las calles. Con un motor de 999 cc derivado de la superbike M 1000 RR, ofrece una potencia impresionante y una aceleración explosiva. Su chasis y suspensión ajustados para la máxima precisión aseguran un manejo ágil y preciso. Además, cuenta con tecnología avanzada y un diseño aerodinámico que refuerza su carácter deportivo y agresivo, haciendo de la M 1000 R una máquina diseñada para los entusiastas más exigentes.', 5, 1),
(11, 'ZX10RR', 30, 120000000, 'F0lMKR4K.jpg', 'La Kawasaki ZX-10RR es una versión de alto rendimiento de la ZX-10R, diseñada específicamente para la competición. Equipada con un motor de 998 cc, entrega una potencia impresionante con una configuración optimizada para la pista. Destaca por su chasis ágil, suspensión avanzada y frenos de alta precisión, todo orientado a ofrecer la máxima velocidad y control en circuitos. Su diseño aerodinámico y acabados exclusivos la convierten en una de las motos más deseadas para los entusiastas de la velocidad y la competición.', 4, 4);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `usuarios`
--

CREATE TABLE `usuarios` (
  `id` int(11) NOT NULL,
  `nombre` varchar(45) DEFAULT NULL,
  `correo` varchar(200) DEFAULT NULL,
  `clave` varchar(200) DEFAULT NULL,
  `telefono` bigint(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

--
-- Volcado de datos para la tabla `usuarios`
--

INSERT INTO `usuarios` (`id`, `nombre`, `correo`, `clave`, `telefono`) VALUES
(1, 'yuky', 'yuky@com.co', 'scrypt:32768:8:1$Z5ycmpwL268WTfOw$5ab56b102b14eb4a90cc1ad6477f6b846e57ea3e71c3dc6ff84ad0d7acff94bed0159f16a0c9062034ac1243006db3e0ad227c2b3d28a7a4a48fbd4977f2b32f', 3213345445),
(2, 'scar', 'scar@con', 'scrypt:32768:8:1$VlvzeCxxNdwSFeBg$c50a2ac275cfba26e99cdff0337c1fdb8077cb49d40581b2f8c5936cdd311eea05d7d12df2f3ad1e9dc443f84d742a5deb25234da8c0bbfc87a9368dd6e2d9ef', 3213345445),
(3, 'juan', 'juan@com.co', 'scrypt:32768:8:1$AUyyRWVfr8CpkRJh$986f50a71a77a2e1ca59193abdff05a36d2e9459a3188638f9f63d0065f3afde9f24902828c8f4d49667356ca5d23d046076df1d57c7e5f44f5e3102580186e0', 3213386883),
(4, 'jhonny', 'jhonny@com.co', 'scrypt:32768:8:1$DAbFA1qTT9D5VN7N$8c67435aa3aae2eb4928b153a4ab4bceb6e0c7d8757123484f6f5afdf387d8c08a34f3b0b9900971f0b4fc51cabc7a937231837df49a7325e7d7f409ca3bd8a9', 3213345445);

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `comentarios`
--
ALTER TABLE `comentarios`
  ADD PRIMARY KEY (`id`,`idUsuarios`,`idMotos`),
  ADD KEY `fk_usuarios_has_motos_motos1_idx` (`idMotos`),
  ADD KEY `fk_usuarios_has_motos_usuarios1_idx` (`idUsuarios`);

--
-- Indices de la tabla `marca`
--
ALTER TABLE `marca`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `motos`
--
ALTER TABLE `motos`
  ADD PRIMARY KEY (`id`,`marca_id`,`usuarios_id`),
  ADD KEY `fk_repuestos_marca1_idx` (`marca_id`),
  ADD KEY `fk_motos_usuarios1_idx` (`usuarios_id`);

--
-- Indices de la tabla `usuarios`
--
ALTER TABLE `usuarios`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `comentarios`
--
ALTER TABLE `comentarios`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT de la tabla `marca`
--
ALTER TABLE `marca`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT de la tabla `motos`
--
ALTER TABLE `motos`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;

--
-- AUTO_INCREMENT de la tabla `usuarios`
--
ALTER TABLE `usuarios`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `comentarios`
--
ALTER TABLE `comentarios`
  ADD CONSTRAINT `fk_usuarios_has_motos_motos1` FOREIGN KEY (`idMotos`) REFERENCES `motos` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  ADD CONSTRAINT `fk_usuarios_has_motos_usuarios1` FOREIGN KEY (`idUsuarios`) REFERENCES `usuarios` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION;

--
-- Filtros para la tabla `motos`
--
ALTER TABLE `motos`
  ADD CONSTRAINT `fk_motos_usuarios1` FOREIGN KEY (`usuarios_id`) REFERENCES `usuarios` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  ADD CONSTRAINT `fk_repuestos_marca1` FOREIGN KEY (`marca_id`) REFERENCES `marca` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
