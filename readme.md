# ⚽ TeamBuilder

**Algoritmos y Estructuras de Datos I**  
Proyecto de aplicación para armar equipos equilibrados de fútbol amateur entre amigos.

## 👥 Integrantes

- Nicolás Diez - LU: 1157582
- Lucio Dillon - LU: 1156126  
- Neyen Ergas - LU: 1209504  
- Iván Rapisarda - LU: 1055142

---

## 📌 Descripción

TeamBuilder es una app de consola desarrollada en Python que permite:

- Gestionar una base de datos de jugadores.
- Armar equipos de manera automática y equilibrada.
- Registrar partidos con sus resultados y estadísticas individuales.
- Generar rankings y análisis de rendimiento.

El objetivo es brindar una herramienta práctica y entretenida para organizar partidos más justos, reduciendo la subjetividad a la hora de armar equipos.

---

## 🧠 ¿Cómo funciona?

- Se cargan los jugadores con sus estadísticas: goles, partidos jugados, calificaciones, rachas y rating general.
- Se seleccionan los jugadores para el próximo partido.
- El sistema arma dos equipos lo más parejos posible (según rating, promedio, racha, etc.).
- Se registra el resultado del partido (goles, calificaciones, goles individuales).
- Las estadísticas de los jugadores se actualizan automáticamente.
- Todo se guarda en archivos JSON.

---

## 🚀 Características

### ✅ Gestión de jugadores
- Alta, baja y edición de jugadores.
- Visualización completa con estadísticas actualizadas.

### 🤖 Armado automático de equipos
- Basado en estadísticas como rating, promedio de calificación, goles y racha.
- Algoritmo mejora con el tiempo a medida que se registran más partidos.

### 📊 Registro y análisis de partidos
- Registro de resultados, goles individuales y calificaciones.
- Actualización automática del rendimiento.
- Rankings, goleadores y rachas positivas/negativas.

### 💾 Persistencia
- Uso de archivos para mantener los datos entre ejecuciones.

### 🔍 Validaciones
- Control de entradas inválidas.
- Errores comunes manejados (jugador inexistente, formato incorrecto, número impar de jugadores, etc.).

### 🧪 Pruebas unitarias
- Verificación del cálculo de estadísticas, armado de equipos y actualización post-partido.

---

## 📅 Entregables

### 40% - Versión Inicial
- Gestión de jugadores.
- Selección de jugadores.
- Armado simple de equipos.
- Persistencia básica.
- Menú por consola.

### 80% - Versión Intermedia
- Registro de partidos.
- Calificaciones individuales.
- Actualización de estadísticas.
- Rankings y rachas.
- Validaciones mejoradas.

### 100% - Versión Final
- Historial completo y exportable.
- Sistema refinado de ranking.
- Aplicación de bonificaciones/penalizaciones por racha.
- Pruebas completas.
- Código modular y documentado.
- Preparación de demo.

