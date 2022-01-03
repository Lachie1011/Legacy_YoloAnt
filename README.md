# YoloAnt <br/>
**A tool to assist in the training of custom YoloV5 models.** <br/> 
This tool has been designed to allow a user to annotate copious amounts of images to train a model based off a smaller model.<br/>

**Project vision:**<br/> 
This tool was originally designed to train a YoloV5 model for the QUT Motorsport Driverless team, however the aim with this project now is to generalise the class system so that it can be used with any YoloV5 custom training applications. <br/>

**Usage:**  <br/>
Commandline Arguments: <br/>
- To pass location of image folder: -i/--images <br/>

congif.yaml: <br/>
- Train/ Validation/ Test Ratios: must all equal up to 1 e.g 0.7, 0.2, 0.1 is fine. But 0.8, 0.4, 0.3 isnt. <br/>  
- Weights: path to the weights file: must be provided and must be in .pt format <br/>  
- Conf: confidence threshold for annotations <br/>  
- Classes: classes to be detected (still needs to be generalised) <br/>  

**Future goals:** <br/>
- Generalise class system. <br/>  
- Create manual annotation functionality embedded in yoloAnt to adjust unsatisfactory results.  <br/>  
- Functionality to jump to an image to annote/ being able to traverse through the system instead of just linearly. 
- General redundancy and error handling
<br/><br/>

**Application within the QUT motorsport team:**<br/> 
Utilising an unreliable model annotated manually with 460 images, we were able to annotate 6000 images, of those 4200 were accepted, within a similar timeframe to produce a model which is to be used in the perception node of the car. <br/>

460 image model : <br/>
![Alt Text](https://media.giphy.com/media/EmDeospWo0yu62B8UY/giphy.gif)

4200 image model : <br/>
![Alt Text](https://media.giphy.com/media/MjSE1cD01BMe0IlvRU/giphy.gif)

<br/> By Lachlan Masson and Brayth Tarlinton 
