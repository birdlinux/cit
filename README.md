<center> <h1 align="center" >CIT</h1> </center>

<center>
  <p align="center">
    Enhancing Productivity and Streamlining Project Management with a User-Friendly Git Wrapper
  </p>
</center>
  
<p align="center">
  <img src="https://github.com/birdlinux/cit/assets/123122904/e326769b-dbe1-4d3d-b35a-6e332f63f62d" width="1620" height="auto"/>
</p>

<div align="center">
  | Name  |  Type   | Creation Date  |
  | :---: | :-----: | :------------: |
  |  CIT  | Wrapper | 13th June 2023 |

  [Description](#Description) - [Philosophy](#Philosophy) - [Installation](#Installation)
</div>
  
<center> <h1 align="center" id="Description">Description</h1> </center>
<center> 
  <p align="center" >
    CIT is a powerful Git wrapper designed to boost productivity and simplify project management. With its intuitive interface and robust feature set, CIT empowers developers to effortlessly navigate the complexities of version control, resulting in efficient and clean code commits.
      
    <br/>
    Built with ease of use in mind, CIT offers a user-friendly interface that simplifies Git operations. Whether you're a seasoned professional or new to version control, CIT ensures a seamless experience throughout your software development journey.
  </p>
</center>
<br / >

<center> <h1 align="center" id="Philosophy">Philosophy</h1> </center
  <center>
    <p align="center">
      At the core of CIT's philosophy is a commitment to simplicity. The tool boasts an intuitive command-line interface that enables developers, regardless of their experience level, to swiftly grasp its functionalities. Whether you are a seasoned professional or a newcomer to version control, CIT's ease of use ensures a smooth and seamless experience throughout your software development journey.
    </p>
  </center>
<br / >

<center> <h1 align="center" id="Installation">Installation</h1> </center
<div align="left">

1. Cloning the Repository
  

```
  git clone https://github.com/birdlinux/cit/
  cd cit
  ```

  
2. Installing Modules
  

```
  python3 -m pip install -r requirements.txt
  ```

3. Moving it to `.scripts`
  

```
  mkdir ~/.scripts/
  cp cit.py ~/.scripts/
  ```

4. Adding an alias (Edit your Bash, ZSH, Fish... RC file) [Add this at the end of the file]
  

```
  alias cit="python3 ~/.scripts/cit.py"
  ```

5. Open a new terminal and run the wrapper
  

```
  $ cit
  ```
</div>  
