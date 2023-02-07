# **HPRheoPlot**
::Automatic Graph Plotter for Ta Instruments Rheometer Users::

## **Introduction**
**HPRheoPlot** is designed for users who use *TA instruments rheometer* and *TRIOS* software. This program provides a convenient way to plot various types of rheological graphs with the data from your experiments. Since the TRIOS software does not provide a way to plot the graphs, this program will help you to plot the graphs automatically. 

## **Installation**
HPRheoPlot is available on PyPI, so you can download and install it via pip or pip3 by using the following command:
```
pip install HPRheoPlot
```
or
```
pip3 install HPRheoPlot
```
## **Features**
HPRheoPlot can draw 4 types of graphs. In the `settings.txt` file (HPRheometer initially creates this file if you don't have it), you can type the desired plot type that you want (`graph-type` option). The program will draw the graph that you want. The available graph types are:

- **Viscosity-Time Plot (`eta-t`).** To draw this plot, you need to provide the pressure info from the DW raw file (CSV format) and the viscosity info from the TRIOS raw file (XLS format). You can select the desired raw files via executing the program. 
- **Viscosity-Shear Rate Plot (`eta-gamma`).**: The program will search for the raw TRIOS file (XLS format) and allow you to select the curve fit models among Powerlaw, Cross, and Sisko model. You can also enter the desired shear rate range when the curve fit is in progress. The program will ask you to input the shear rate range. Each curve fit models are followed by the below equations: <br>
  > (Powerlaw model) $\eta = k \dot\gamma^{n}$ <br>
  > (Cross model) $\eta = \frac{\eta_0 - \eta_{\infty}}{1 + (K\dot\gamma)^{m}} + \eta_{\infty}$ <br>
  > (Sisko model) $\eta = \eta_{\infty} + k \dot\gamma^{n-1}$ <br>

  > Where $\eta$ is the apparent viscosity, $\dot\gamma$ is the shear rate, $K$ is the Cross constant, $k$ is the consistency index which is numerically equal to the viscosity at 1 $s^{-1}$. Also, $n$ is the power law index, $m$ is the shear-thinning index, which ranges from 0 (Newtonian) to 1 (infinitely shear-thinning) $\eta_0$ is the initial viscosity, and $\eta_{\infty}$ is the infinite viscosity. For detailed information, refer to the [reference pdf](https://cdn.technologynetworks.com/TN/Resources/PDF/WP160620BasicIntroRheology.pdf) file. <br>
- **Viscosity-Delta Pressure Plot (`eta-delp`).** The program will ask you to input a DW file (CSV format) and a raw TRIOS file (XLS format). Then, the program will match the dimensions of each raw file and plot the $\eta - \Delta{P}$ graph for you.
- **Shear Rate-Stress Plot (`gamma-sigma`).** The program will treat the stress data and shear rate data to plot this plot. If the yield stress measurement is included in the raw TRIOS file (XLS), the program will take the data and plot the shear rate-stress curve and mark and write the text in the output plot where the yield stress exists.

## **Disclaimer**
* I'm a gas hydrate researcher; therefore, HPRheoPlot is mainly designed for gas hydrate research. However, it can be used for other research fields as well if you modify the code depending on your needs.
* This program is NOT affiliated with TA instruments.
* You SHOULD export raw data from TRIOS software with following methods to successfully run HPRheoPlot.
  > (1) If you have finished projects in the TRIOS software, open files from the `file manager` tab. <br>
  > (2) Right click that file and select `Export` - `To Excel`. <br>
  > (3) In the `Details` tab, you should choose `Headings only`. Never includes `Include parameters` or `Include hidden points in output`. Includes all steps in the `Steps` tab. <br>
  > (4) If you used different steps of sequences, you should modify the original source code. HPRheoPlot only works for my custom sequence. It is same as below: <br>
  >> (a) Temperature ramp - 1 (down to the target temperature) <br>
  >> (b) Peak hold - 2 (hold the target temperature) <br>
  >> (c) Flow sweep - 3 (sweep the shear rate I) <br>
  >> (d) Flow sweep - 4 (sweee the shear rate II) <br>
  >> (e) Time sweep - 5 (sweep the time) <br>
  >> (f) Flow ramp - 6 (measuring the yield stress) <br>

  > **How to modify the source code?** 
  >> In the terminal, type 
  >> ```
  >> git clone https://github.com/wjgoarxiv/HPRheoPlot.git
  >> ```
  >> and hit enter. Then, type 
  >> ```
  >> cd HPRheoPlot 
  >> ```
  >> and hit enter. After that, type 
  >> ```
  >> nano HPRheoPlot.py
  >> ``` 
  >> and hit enter. You will see the source code. You can modify the source code by using the `nano` editor. <br>
  >> Search for the `def trioscsvtreat()` function. You will see the following code: <br>
  >> ```
  >> # Read the xls file
  >> xls = pd.ExcelFile(trios_file_list[trios_file_number])
  >>
  >> # Read the first sheet
  >> global df_peakhold2
  >> df_peakhold2 = pd.read_excel(xls, 'Peak hold - 2', skiprows=3)
  >>
  >> # Second page
  >> global df_flowsweep3
  >> try: 
  >>    df_flowsweep3 = pd.read_excel(xls, 'Flow sweep - 3', skiprows=3)
  >> except:
  >>    pass
  >> 
  >> # Third page
  >> global df_flowsweep4
  >> try:
  >>   df_flowsweep4 = pd.read_excel(xls, 'Flow sweep - 4', skiprows=3)
  >> except:
  >>   pass
  >> 
  >> # Fourth page
  >> global df_timesweep5
  >> try:
  >>  df_timesweep5 = pd.read_excel(xls, 'Time sweep - 5', skiprows=3)
  >> except:
  >>   pass
  >> 
  >> # Last page
  >> global df_flowramp6
  >> try:
  >>   df_flowramp6 = pd.read_excel(xls, 'Flow ramp - 6', skiprows=3)
  >> except:
  >>   pass
  >> ```
  >> These are the lines that read the data pages from the XLS file. You can modify the page names to match your sequence. For example, if you have a sequence like below: <br>
  >> (a) Temperature ramp - 1 (down to the target temperature) <br>
  >> (b) Peak hold - 2 (hold the target temperature) <br>
  >> (c) Flow ramp - 3 (measuring the yield stress) <br>
  >> The code should be modified as below: <br>
  >> ```
  >> # Read the xls file
  >> xls = pd.ExcelFile(trios_file_list[trios_file_number])
  >> 
  >> # Read the 1st sheet
  >> global df_temp_ramp1 = pd.read_excel(xls, 'Temperature ramp - 1', skiprows=3)
  >>
  >> # Read the 2nd sheet
  >> global df_peakhold2
  >> try:
  >>    df_peakhold2 = pd.read_excel(xls, 'Peak hold - 2', skiprows=3)
  >> except:
  >>    pass
  >>
  >> # Read the 3rd page
  >> global df_flowsweep3
  >> try:
  >>    df_flowsweep3 = pd.read_excel(xls, 'Flow ramp - 3', skiprows=3)
  >> except:
  >>    pass
  >> ```
  >> Save the modified source code by pressing `Ctrl + X` and hit `Y` to save the changes. <br>
  >> Then, execute your modifed script by typing 
  >> ```
  >> python3 HPRheoPlot.py
  >> ```
  >> in the terminal. The code will be normally executed.<br> 
  >> If you have any problem, leave *issues* in the github repository or contact me via [e-mail](woo_go@yahoo.com).

## **License**
This program is licensed under the MIT license.

## **Contact**
For any questions or feedback, please email me at woo_go@yahoo.com.

## **Contributing**
If you want to contribute to this project, please fork the repository and make changes as you'd like. Pull requests are welcome. 
