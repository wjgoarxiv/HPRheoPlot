# **HPRheoPlot**
::Automatic Graph Plotter for TA Instruments Rheometer Users::

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

## **Usage**
After installing the program, you can run the program by typing the following command in the terminal:
```
hprheoplot
```
When you firstly run the program, you don't have the `settings.txt` file. The program will create the `settings.txt` file and ask you to input several options. 
```
ERROR There is no `settings.txt` file in the current directory. I will make a new `settings.txt` file for you.
INFO The `settings.txt` file has been created. Please edit the file and run the program again.
```
The `settings.txt` looks like below:
```
###################################
############ SETTINGS.TXT #############
###################################

# This file is for the settings of the HPRheoPlot program. 
# NOTE: This file should be named as `settings.txt`. If isn't, the program cannot load the settings. 

###########################################################
# DW-directory: The directory location where the csv files from DWStemp program are located. 
DW-directory = ./DW/ 

# TRIOS-directory: The directory location where the csv files from TRIOS program are located. 
TRIOS-directory = ./TRIOS/ 

# graph-type: The type of graph that you want to plot (options: eta-t, eta-gamma, eta-delp, gamma-sigma) 
graph-type = eta-gamma

# graph-style: The style of graph that you want to plot (options: line, scatter) 
graph-style = scatter 

# line-width: The line width of the graph (example: 0.5, 1, 2.3, etc.) - this works when graph-style is line. 
line-width = 2 

# graph-decorate: Whether you want to decorate the graph (options: y, n) 
graph-decorate = y 

# curve-fit-equation: The equation that you want to use for the curve fit (options: Powerlaw, Cross, Sisko) 
curve-fit-equation = Sisko 
```
Note that program requires the directory locations where the raw data files are located. Make sure you have DWStemp raw files (CSV format) and TRIOS raw files (XLS format) in the directory locations that you input in the `settings.txt` file. Depending on the `graph-type` you selected, the program will export different types of graphs. 
### **CASE I: Viscosity-time plot (`eta-t`)**
If you want to draw the viscosity-time plot, you need to provide both the pressure info from the DW raw file (CSV format) and the viscosity info from the TRIOS raw file (XLS format). You can select the desired raw files via executing the program. 
```
INFO These are the DWStemp raw files that are in the folder. Please type the file number that you want to use:
```
Type the file number of the DWStemp raw file that you want to use. 
```
INFO These are the TRIOS raw excel files that are in the folder. Please type the file number that you want to use:
```
Type the file number of the TRIOS raw file that you want to use. You must choose the same file which was recorded at the same time as the DWStemp raw file. 
```
INFO The eta-t graph is saved as 'eta-t.png'.
```
The program will draw the viscosity-time plot and save it as `eta-t.png` in the current directory.

### **CASE II: Viscosity-shear rate plot (`eta-gamma`)**
If you want to draw the viscosity-shear rate plot, you only need to bring your TRIOS raw file (XLS format). You can select the desired raw file via executing the program. 
```
INFO These are the TRIOS raw excel files that are in the folder. Please type the file number that you want to use:
```
Type the file number of the TRIOS raw file that you want to use. The program will ask you to input the desired minimum shear rate value and the maximum shear rate value when you fit the data.
```
INFO Enter the desired minimum shear rate value [unit: s^-1] (e.g. 10):
```
```
INFO Enter the desired maximum shear rate value [unit: s^-1] (e.g. 500):
```
The program will export the curve fitting information based on your selected equation.
```
INFO The Cross model is selected.
INFO The Cross model fitting results are as follows.
```
```
INFO Flow sweep 3: K = ... , n = ... , eta0 = ... , eta_infty = ..., R^2 = ...
INFO Flow sweep 4: K = ... , n = ... , eta0 = ... , eta_infty = ..., R^2 = ...
```
Also, the program will draw the viscosity-shear rate plot and save it as `eta-gamma.png` in the current directory.
```
INFO The eta-gamma graph is saved as 'eta-gamma.png'.
```
### **CASE III: Viscosity-pressure plot (`eta-delp`)**
If you want to draw the viscosity-pressure plot, you need to prepare both the pressure info from the DW raw file (CSV format) and the viscosity info from the TRIOS raw file (XLS format). You can select the desired raw files via executing the program. 
```
INFO These are the DWStemp raw files that are in the folder. Please type the file number that you want to use:
```
```
INFO These are the TRIOS raw excel files that are in the folder. Please type the file number that you want to use:
```
If you successfully select the raw files, the program will draw the viscosity-pressure plot and save it as `eta-delp.png` in the current directory.
```
INFO The eta-delp graph is saved as 'eta-delp.png'.
```
### **CASE IV: Shear stress-shear rate plot (`gamma-sigma`)**
If you want to draw the shear stress-shear rate plot, you only need to bring your TRIOS raw file (XLS format). You can select the desired raw file via executing the program. 
```
INFO These are the TRIOS raw excel files that are in the folder. Please type the file number that you want to use:
```
Select the desired raw file number. The program will draw the shear stress-shear rate plot and save it as `gamma-sigma.png` in the current directory.
```
INFO The gamma-sigma graph is saved as 'gamma-sigma.png'.
```

### **EXTRA: Raw file format**
HPRheoPlot designed to treat the below raw files. If you have different raw files, you can modify the program to treat your raw files, or you can modify your format to the below format. 
#### **(1) DWStemp raw file (CSV format)**
```
RecNo.,Time,Pressure1,Pressure2,Temp.1,Temp.2,Temp. 3,Temp. 4
No.   ,sec,kgf/§²,kgf/§²,¡É,¡É,¡É,¡É
         1,        60,     36.93,      0.00,      0.00,      0.00,      0.00,      0.00
         2,       120,     36.83,      0.00,      0.00,      0.00,      0.00,      0.00
         3,       180,     36.69,      0.00,      0.00,      0.00,      0.00,      0.00
         4,       240,     36.54,      0.00,      0.00,      0.00,      0.00,      0.00
         5,       300,     36.36,      0.00,      0.00,      0.00,      0.00,      0.00
...
```
#### **(2) TRIOS raw file (XLS format)**
```
Flow ramp - 6					
Stress	Shear rate	Viscosity	Step time	Temperature	Normal stress
Pa	1/s	Pa.s	s	°C	Pa
30.1505	0.00356128	8466.19	6.03004	1	-0.132814
90.7678	0.00349795	25948.9	18.1535	1	-0.13352
150.733	0.00362841	41542.5	30.1466	1.01	-0.133736
...
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
  > <img src="https://github.com/wjgoarxiv/HPRheoPlot/blob/9c3bc4d16157a246181e3d36ed3f318c798a1517/(1)%20Opens%20files.png" style="width:70%;height:70%"/> <br>
  > (2) Right click that file and select `Export` - `To Excel`. <br>
  > <img src="https://github.com/wjgoarxiv/HPRheoPlot/blob/9c3bc4d16157a246181e3d36ed3f318c798a1517/(2)%20Right%20click%20-%20Export%20-%20To%20Excel.png" style="width:65%;height:65%"/> <br>
  > (3) In the `Details` tab, you should choose `Headings only`. Never includes `Include parameters` or `Include hidden points in output`. Includes all steps in the `Steps` tab. <br>
  > <img src="https://github.com/wjgoarxiv/HPRheoPlot/blob/9c3bc4d16157a246181e3d36ed3f318c798a1517/(3)%20File%20export.png" style="width:60%;height:60%"/> <br>
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
