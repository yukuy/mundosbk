-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 12-09-2024 a las 22:41:11
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
(4, 1, 8, 'muy buena moto \r\n'),
(7, 4, 8, 'es muy bersatil'),
(8, 1, 8, 'es la mejor');

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
  `video_url` varchar(200) NOT NULL,
  `descripcion` text DEFAULT NULL,
  `marca_id` int(11) NOT NULL,
  `usuarios_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

--
-- Volcado de datos para la tabla `motos`
--

INSERT INTO `motos` (`id`, `nombre`, `cantidad`, `precio`, `foto`, `video_url`, `descripcion`, `marca_id`, `usuarios_id`) VALUES
(8, 'GSX-S 750', 8, 65000000, 'xayA7v8C.jpg', 'https://www.youtube.com/watch?v=A1FiIP45vGw', 'La Suzuki GSX-S750 es una motocicleta naked deportiva que combina un diseño agresivo con un rendimiento excepcional. Equipada con un motor de 749 cc, ofrece una potencia suave y controlable, ideal tanto para el uso en ciudad como para rutas más largas. Su chasis compacto y ágil proporciona una experiencia de conducción dinámica, mientras que su estética moderna y elegante capta la atención al instante.', 3, 1),
(9, 'M 1000R', 17, 200000000, 'gsouYktl.jpg', 'https://www.youtube.com/watch?v=7FExLWI7fmQ', 'La BMW M 1000 R es una motocicleta naked de alto rendimiento que lleva la emoción de la pista a las calles. Con un motor de 999 cc derivado de la superbike M 1000 RR, ofrece una potencia impresionante y una aceleración explosiva. Su chasis y suspensión ajustados para la máxima precisión aseguran un manejo ágil y preciso. Además, cuenta con tecnología avanzada y un diseño aerodinámico que refuerza su carácter deportivo y agresivo, haciendo de la M 1000 R una máquina diseñada para los entusiastas más exigentes.', 5, 1),
(11, 'ZX10RR', 30, 120000000, 'F0lMKR4K.jpg', 'https://www.youtube.com/watch?v=TrD8qIW2fGM', 'La Kawasaki ZX-10RR es una versión de alto rendimiento de la ZX-10R, diseñada específicamente para la competición. Equipada con un motor de 998 cc, entrega una potencia impresionante con una configuración optimizada para la pista. Destaca por su chasis ágil, suspensión avanzada y frenos de alta precisión, todo orientado a ofrecer la máxima velocidad y control en circuitos. Su diseño aerodinámico y acabados exclusivos la convierten en una de las motos más deseadas para los entusiastas de la velocidad y la competición.', 4, 4),
(12, 'GSX-R 600', 65, 90000000, 'Gsxr600 Suzuki.jpg', 'https://www.youtube.com/watch?v=vw_OuH7phTg', 'La Suzuki GSX-R600 es una deportiva con motor de 599 cc de funcionamiento emocionante y muy fiable. Dispone de un propulsor de cuatro cilindros y 125 hp de potencia, dos modos de conducción y embrague antirrebote para conseguir un control total en cualquier situación.', 3, 5),
(13, 'MT 09', 1, 65000000, 'mt 09.jpg', '', 'La MT-09 SP es famosa por su agilidad y estabilidad, que se ven reforzadas por una ergonomía sofisticada que permite al usuario sentirse más conectado a la máquina al ofrecerle una libertad de movimiento mayor con diferentes estilos de conducción.', 1, 6),
(14, 'BMW S1000 RR', 1, 180000000, 'BWM S1000rr.jpg', 'https://www.youtube.com/watch?v=v6edU1hil88', 'Con la motocicleta S 1000 RR 2021 no tendrás límite, te impulsará a 152 kW (207 CV) invitándote a buscar la trazada ideal, sintiendo la libertad y seguridad que te da este modelo, el que empuja hacia adelante con un par máximo de 113 Nm a 11.000 rpm, y una curva de par de al menos 100 Nm en rangos de velocidades de 5.500 a 14.500 [rpm]. A diez años desde la primera generación de la RR, avanzado a un nuevo nivel de rendimiento, reelaborando los componentes de la RR desde la parte delantera de la moto, hasta la trasera, logrando con ello menor peso y un rendimiento altamente potente. Prepárate para la pole position y la victoria, la S 1000 RR 2021, te espera.', 5, 5);

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
(4, 'jhonny', 'jhonny@com.co', 'scrypt:32768:8:1$DAbFA1qTT9D5VN7N$8c67435aa3aae2eb4928b153a4ab4bceb6e0c7d8757123484f6f5afdf387d8c08a34f3b0b9900971f0b4fc51cabc7a937231837df49a7325e7d7f409ca3bd8a9', 3213345445),
(5, 'andrey', 'andrey@com.co', 'scrypt:32768:8:1$sK93XXEq70HNIspW$debecd24e7a4213ee7bc00b55a496b88295e15f1298b6aed39f6aa89a15d4bc4b8b19f4749e41f797b3193bd445ba61916b02b522735d90469e576c29cfccac5', 3213386883),
(6, 'yu', 'yu@com.co', 'scrypt:32768:8:1$lNylL2CAuKTeSnkB$f2d23a926b3369b2c0ec734b86bf97c5a33776055db93795e69fcdcbe94ac7580bc1a0100f704f1de87118f620ca1cfde30143c166204f5e8493916692c73cef', 3115986078);

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
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;

--
-- AUTO_INCREMENT de la tabla `marca`
--
ALTER TABLE `marca`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT de la tabla `motos`
--
ALTER TABLE `motos`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=15;

--
-- AUTO_INCREMENT de la tabla `usuarios`
--
ALTER TABLE `usuarios`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

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
