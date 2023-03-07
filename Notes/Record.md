# BuildSiteInaMonth Record

一月建站，必学会



今天也就是刚刚开了个头，配置pycharm可以和github 推送就废了我小一会功夫
最终是通过gpg密钥配置了一下，不过今天还是不熬夜了，早点睡。

## Html入门

浏览器可以识别出各式标签，html语言 + css
flask框架支持将字符串写入文件。

一开始templates文件夹写错了

![image-20230302225134819](C:\Users\Admin\PycharmProjects\0301BuildSite\Notes\Record.assets\image-20230302225134819.png)



### 浏览器常用标签

#### 1 编码

```html

<meta charset="UTF-8">
```

#### 2 标签 title

```html
<title>FirstIndex</title>
```

#### 3 标题

```html
<h1>h1</h1>
```

#### 4 div 和 span

```html

<div>内容</div>
<span>asdfg</span>
```

- div 一个人占一整行，块级标签 类似`<h1>`这些都是div
- span 自己多大占多少，行内标签、内联标签

这两个标签很素，但未来通过css可以让它变得美观



#### 5 超链接

跳转到自己网站其他的地址

```html
<a href="http://127.0.0.1:5000/get/news">新闻</a>
<a href="/get/news">新闻</a>
```

跳转到别人的网站需要写上完整路径名

```html
<a href="https://www.baidu.com">百度</a>
```

#### 6 图片

自闭合标签

```html
直接显示别人的图片地址
<<img src="图片地址" alt="">
<img src="https://pica.zhimg.com/80/v2-e110c4ec6cbc6b51f1bac346d4d85ab1_1440w.webp"/>
```
显示自己的图片
- 自己项目中创建static目录，并将照片放上去
- 在页面引入图片 
```html
<<img src="/static/images/Manim.png" alt="">
```
可以通过一些设置设定图片高度和宽度
```html
<img style = "height:600px;width:300px" src="/static/images/Manim.png" alt="">
<img style = "width:40%" src="/static/images/Manim.png" alt="">
```
img标签也是一个行内标签，不设定的话，不会一次占一行。
> HTML 中的 <img> 标签可以设定宽度的百分比，但不能直接设定高度的百分比的原因是因为图片的高度是依赖于其宽度的。当你设定一个图片的宽度时，浏览器会自动根据图片的比例来计算其高度，以保持图片的比例不变。
> 如果你尝试设定图片的高度百分比，浏览器会无法确定图片的宽度，因为它无法确定图片的原始比例。这意味着图片可能会拉伸或扭曲，从而导致不良的视觉效果。
> 要解决这个问题，你可以使用 CSS 的 height 属性和 object-fit 属性来控制图片的高度和宽度。例如，你可以设置 height: 100% 和 object-fit: contain，这将使图片在保持其原始比例的同时适应其包含元素的高度。 


#### 目前学习标签小结
- 学习的标签
```html
<h1></h1>
<div></div>
<span></span>
<a></a>
<<img src="" alt="">
```
- 划分
```html
块级标签
    <h1></h1>
    <div></div>
行内标签
    <span></span>
    <a></a> 
    <img src="" alt="">
```

- 标签支持嵌套 
  可以实现图片超链接

```html
    <a href="https://kox.moe/c/18993.htm" target="_blank">
	<img style="150px"
	     src="/static/images/comic/03.png">
</a>
```



#### 7 列表

`ul` ` ol` 一个占一行，也是块级标签

```html
<ul>
    <li> 中国漫画 </li>
    <li> 日本漫画 </li>
    <li> 欧美漫画 </li>
</ul>

<ol>
    <li> 中国漫画 </li>
    <li> 日本漫画 </li>
    <li> 欧美漫画 </li>
</ol>
```

#### 8 表格

```html
<table border="1">
	<thead>
	<tr>
		<th>ID</th>
		<th>作品名</th>
		<th>作者</th>
	</tr>
	</thead>
	<tbody>
	<tr>
		<td>01</td>
		<td>狂赌之渊</td>
		<td>尚村透</td>
	</tr>
	<tr>
		<td>02</td>
		<td>新世纪福音战士</td>
		<td>貞本義行</td>
	</tr>
	<tr>
		<td>03</td>
		<td>一人之下</td>
		<td>米二</td>
	</tr>
	</tbody>
</table>
```

#### 9 input系列 7个

默认是行内标签

```html
<input type = "text ">输入文本
<input type="password">输入密码
<input type="file"> 选择文件
性别:
男<input type="radio" name="n1">单选框
女<input type="radio" name="n1">
	
爱好:
足球<input type="checkbox">
象棋<input type="checkbox">
篮球<input type="checkbox">
看书<input type="checkbox">

按钮
	<input type="button" value="提交"> //普通按钮
	<input type="submit" value="提交"> //提交表单
```

#### 10 下拉框

```html
<select>
    城市：
    <option>北京</option>
    <option>上海</option>
    <option>南京</option>
    <option>深圳</option>
</select>
```

多选下拉框

```html
<select multiple>
    城市：
    <option>北京</option>
    <option>上海</option>
    <option>南京</option>
    <option>深圳</option>
</select>
```

#### 11 多行文本

```html
<textarea></textarea>
```

#### 