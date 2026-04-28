# 🛡️ Sentinel Metrics: Customer Retention & Churn Analytics

**Sentinel Metrics** es una plataforma integral de análisis de datos diseñada para ayudar a las empresas a identificar y retener clientes en riesgo. El sistema combina el procesamiento de grandes volúmenes de datos con una interfaz visual intuitiva, permitiendo una toma de decisiones proactiva basada en el comportamiento real del usuario.

---

## 🚀 Características Principales

* **Detección Automática de Churn:** Algoritmo basado en SQL que clasifica a los usuarios en niveles de riesgo (**Bajo, Medio, Alto**) según su actividad reciente.
* **Simulación de Big Data:** Generador de datos integrado capaz de poblar la base de datos con miles de registros de actividad realistas para pruebas de estrés.
* **Dashboard Interactivo:** Visualización en tiempo real de métricas clave, distribución de riesgos y tablas de vigilancia de usuarios.
* **Infraestructura Automatizada:** Configuración del entorno mediante **Ansible** para garantizar despliegues consistentes y rápidos.

---

## 🛠️ Stack Tecnológico

| Componente | Tecnología |
| :--- | :--- |
| **Lenguaje** | Python 3.14 |
| **Base de Datos** | MySQL (Vistas optimizadas) |
| **Visualización** | Streamlit |
| **DevOps** | Ansible |
| **Librerías** | Pandas, SQLAlchemy, Faker, Matplotlib |

---

## 📂 Estructura del Proyecto

* `setup_env.yml`: Playbook de Ansible para configurar dependencias y servicios.
* `seed_data.py`: Script para la generación y carga masiva de datos de prueba.
* `dashboard.py`: Aplicación web interactiva para la visualización de métricas de retención.
* `requirements.txt`: Lista de dependencias del proyecto.

---

## ⚙️ Instalación y Uso

1. **Preparar el entorno:**
   ```bash
   ansible-playbook setup_env.yml
