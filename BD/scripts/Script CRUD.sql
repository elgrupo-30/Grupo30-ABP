USE sistema_usuarios;

-- 1. Crear usuario
DELIMITER //
CREATE PROCEDURE crear_usuario(
    IN p_nombre VARCHAR(100),
    IN p_email VARCHAR(100),
    IN p_contraseña_hash VARCHAR(255),
    IN p_rol_nombre VARCHAR(50)
)
BEGIN
    DECLARE v_rol_id INT;
    
    -- Obtener ID del rol
    SELECT id INTO v_rol_id FROM roles WHERE nombre = p_rol_nombre;
    
    -- Insertar nuevo usuario
    INSERT INTO usuarios (nombre, email, contraseña_hash, rol_id)
    VALUES (p_nombre, p_email, p_contraseña_hash, v_rol_id);
    
    SELECT CONCAT('Usuario ', p_nombre, ' creado exitosamente') AS resultado;
END //
DELIMITER ;

-- 2. Leer usuarios
DELIMITER //
CREATE PROCEDURE leer_usuarios(
    IN p_filtrar_rol VARCHAR(50)
BEGIN
    IF p_filtrar_rol IS NULL THEN
        SELECT u.id, u.nombre, u.email, r.nombre AS rol, u.fecha_registro
        FROM usuarios u JOIN roles r ON u.rol_id = r.id;
    ELSE
        SELECT u.id, u.nombre, u.email, r.nombre AS rol, u.fecha_registro
        FROM usuarios u JOIN roles r ON u.rol_id = r.id
        WHERE r.nombre = p_filtrar_rol;
    END IF;
END //
DELIMITER ;

-- 3. Actualizar usuario
DELIMITER //
CREATE PROCEDURE actualizar_usuario(
    IN p_id INT,
    IN p_nombre VARCHAR(100),
    IN p_email VARCHAR(100),
    IN p_contraseña_hash VARCHAR(255),
    IN p_rol_nombre VARCHAR(50)
)
BEGIN
    DECLARE v_rol_id INT;
    
    -- Validar email único si se cambia
    IF p_email IS NOT NULL THEN
        IF EXISTS (SELECT 1 FROM usuarios WHERE email = p_email AND id != p_id) THEN
            SELECT 'Error: El email ya está en uso' AS resultado;
            LEAVE proc_label;
        END IF;
    END IF;
    
    -- Obtener ID del rol si se especifica
    IF p_rol_nombre IS NOT NULL THEN
        SELECT id INTO v_rol_id FROM roles WHERE nombre = p_rol_nombre;
    END IF;
    
    -- Actualizar campos
    UPDATE usuarios SET
        nombre = IFNULL(p_nombre, nombre),
        email = IFNULL(p_email, email),
        contraseña_hash = IFNULL(p_contraseña_hash, contraseña_hash),
        rol_id = IFNULL(v_rol_id, rol_id)
    WHERE id = p_id;
    
    SELECT CONCAT('Usuario ID ', p_id, ' actualizado') AS resultado;
END //
DELIMITER ;

-- 4. Eliminar usuario
DELIMITER //
CREATE PROCEDURE eliminar_usuario(
    IN p_id INT
)
BEGIN
    DECLARE v_es_admin BOOLEAN;
    DECLARE v_total_admins INT;
    
    -- Verificar si es admin
    SELECT COUNT(*) INTO v_es_admin
    FROM usuarios u JOIN roles r ON u.rol_id = r.id
    WHERE u.id = p_id AND r.nombre = 'admin';
    
    -- Contar admins totales
    SELECT COUNT(*) INTO v_total_admins
    FROM usuarios u JOIN roles r ON u.rol_id = r.id
    WHERE r.nombre = 'admin';
    
    -- Validar no eliminar último admin
    IF v_es_admin AND v_total_admins <= 1 THEN
        SELECT 'Error: No se puede eliminar el último administrador' AS resultado;
    ELSE
        DELETE FROM usuarios WHERE id = p_id;
        SELECT CONCAT('Usuario ID ', p_id, ' eliminado') AS resultado;
    END IF;
END //
DELIMITER ;

-- Ejemplos de uso:
-- CALL crear_usuario('Ana López', 'ana@example.com', 'hash_contraseña', 'usuario');
-- CALL leer_usuarios(NULL);
-- CALL actualizar_usuario(2, 'Juan Pérez Actualizado', NULL, NULL, NULL);
-- CALL eliminar_usuario(3);