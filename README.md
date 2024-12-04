# JetCAP-tool
JetCAP(Jet Engine Cycle Analysis and Performance) is an Jet engine cycle analysis tool for undergraduate aerospace engineering students. It can conduct PCA(Parametric Cycle analysis) and EPA(Engine Performance analysis) on Turbojet/Turbofan &amp; Ramjet engines. It can even be used for engine cycle optimization for different mission requirements.


## Code Structure

Jet CAP utilizes a modular object-oriented approach to represent various engine components and their interactions. Here's a breakdown of the key classes and their functionalities:

**Classes:**

* **Atmosphere:** Stores ambient temperature (T0) and pressure (P0).
* **Fuel:** Stores properties of the fuel used in the engine cycle.
* **Aircraft:** Combines `Atmosphere` and `Fuel` objects, representing the aircraft's operating environment and fuel type.
* **Nozzle:**
    - Stores the nozzle pressure ratio.
    - Provides the `output_Pt_Tt` function that calculates the outlet total pressure (Pt) and total temperature (Tt) based on the inlet values.
    - **Connection:** Used to initialize the diffuser and exit nozzle of the engine.
* **Fan:** Stores the fan pressure ratio.
* **Compressor:**
    - Stores the compressor pressure ratio.
    - Provides the `output_Pt_Tt` function to calculate the outlet Pt and Tt based on inlet values and total temperature ratio function.
    - **Connection:** Used to initialize the low-pressure (LP) and high-pressure (HP) compressors.
* **Combustor:**
    - Stores the combustor temperature ratio and fuel-air ratio.
    - Provides the `output_Pt_Tt` function to calculate the outlet Pt and Tt based on inlet values and total temperature ratio function.
* **Turbine:**
    - Stores the turbine pressure ratio.
    - Provides the `output_Pt_Tt` function to calculate the outlet Pt and Tt based on inlet values and total temperature ratio function.
    - **Connection:** Used to initialize the LP and HP turbines.

**Class Connections and Workflow:**

The `Aircraft` class provides the initial conditions for the engine cycle by specifying the ambient atmospheric conditions and fuel properties. The engine cycle analysis then proceeds as follows:

1. **Inlet:** The `Nozzle` class (used as the diffuser) calculates the initial total pressure and temperature at the engine inlet based on the ambient conditions.
2. **Fan and Compressor:** The inlet conditions are passed to the `Fan` and `Compressor` classes (LP and HP) to calculate the conditions after compression.
3. **Combustor:** The compressed air is mixed with fuel in the `Combustor` class, resulting in increased total temperature and pressure.
4. **Turbine:** The high-temperature and high-pressure gas from the combustor is expanded through the `Turbine` class (LP and HP) to generate power.
5. **Nozzle:** Finally, the expanded gas is accelerated through the `Nozzle` class (used as the exit nozzle) to generate thrust.

By creating separate classes for each component and defining clear connections between them, Jet CAP promotes code modularity, reusability, and maintainability. This structure also facilitates the analysis of different engine cycles and the optimization of performance parameters.


## For ME643 Aircraft and Rocket Propulsion Students
Future batches of the ME643 course taught by Prof. Dilip S. Sundaram can download the .exe file to get the software.
This OneDrive link has the JetCAP.exe 
**: https://onedrive.live.com/?id=AB594DA0FBDB58ED%21sa1e6f362b99e450481f64399ba2afaa2&cid=AB594DA0FBDB58ED** 
