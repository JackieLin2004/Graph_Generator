# Graph_Generator

## Python语言设计与实践 第一次项目

[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)

### 需求

- 一键生成一个图，并把相应的连接矩阵构建出来，并把连接矩阵存进Excel表中


- 解决最短路算法问题，解决 `PageRank` 算法问题，并做出相应的排序

### 分析

- 我们组本项目采用了无向图和有向图两种方式供用户选择，用 `networkx` 和 `matplotlib` 两个库来创建图，同时采用 `xlsxwriter` 
  将连接矩阵导出为Excel


- 同时采用目前最新 `PySide6` 库来创建UI界面，并使用 `qt_material` 中的配置文件来美化界面，使用 `scipy` 库来做改进所支持的结点数


- 在解决第二次需求的过程中，处理最短路算法和 `PageRank` 算法，用到 `plotly.graph_objects` 和 `plotly_express` 来分别绘制柱状图和散点图。由于
  这两个库生成的图片会自动生成 `html`文件用以展示图片，所以在 `Frame` 的最后调用析构函数来删除冗余的 `html` 文件

### 环境

`python` 版本:3.11

### 项目框架的说明

- `images` 文件夹中存放生成的图片，以有向图和无向图进行分类存放


- `Kernel` 文件夹中为核心功能的 `Python` 文件


- `xlsx` 文件夹中存放生成的Excel文件，同样是以有向图和无向图进行分类存放


- `config.txt` 中为本项目需要的所有配置，配置环境时可采用以下命令行安装库

```
pip install networkx
pip install matplotlib
pip install xlsxwriter
pip install PySide6
pip install qt_material
pip install scipy
pip install plotly
pip install plotly_express
```

- `Frame.py` 为本项目的整体架构文件


- `generator_ui.py` 为 `generator_ui.ui` 转成的 `Python` 文件，里面是UI界面的代码，通过以下命令转换：

```
pyside6-uic generator_ui.ui -o generator_ui.py
```


- `main.py` 文件运行 `Frame.py` 中的 `run` 函数，以此执行项目


- `temp` 文件夹保存生成的 `html` 文件，等待后续的删除；同时利用 `dat.dat` 文件来占位


- `version` 文件夹保存的是上一版本的相关代码


- 由于参考代码中生成的图片会覆盖原先生成的图片，所以本项目对这部分进行优化，引入时间 `time` 
模块，用时间戳命名图片和Excel文件，这样可以保证名字永远唯一而不被覆盖

### 改进

- 由于一开始原本的库只能支持最多200多个结点，临时改进，下载一个 `scipy` 库，就可以支持到1000个结点


- 下来查阅资料发现是 `networkx` 底层处理大数据的时候会用到 `scipy` 库，所以加上这个库才可以处理更大的数据


- 同时这次版本的UI界面相对于上一版本也有一定的改进和升级

### 关于算法的一些说明

本项目主要包括两个算法，分别是 `最短路算法` 和 `PageRank` 算法

- 对于最短路算法，整体包含两种，分别是 **单源最短路** 和 **多源最短路** ，多源最短路的典型代表是 `Floyd` ，而单源最短路
的典型代表是 `Dijkstra` 而由于 `Dijkstra` 不能处理负权的情况，所以这里采用了能处理负权的 `Bellman-Ford` 和 `SPFA` 
算法，其中后者是前者加了队列优化


- 然后对于 `Floyd` ，我们不仅调用了相关库函数，也自己实现了这个算法，并且给出相应运行效率的对比图；而对于单源最短路算法，
我们也自己实现了 `SPFA` 算法并与库函数的 `Bellman-Ford` 作比较


- 最后对于 `PageRank` 算法，我们也同样给出了自己模拟的过程，并与库函数的原生方法做对比

### 小组成员

Lin Xiaoyi, Tang Jiajun, Wang Zhen, Chen Guanrui, Wang Jing

### 此项目仅供学习交流使用，转载请注明出处！
