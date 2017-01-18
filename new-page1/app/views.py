#encoding:utf-8

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

from flask import render_template
from forms import SubmitForm
from app import app
from forms import User
from flask import request,flash,redirect


@app.route('/')
@app.route('/indexapp')
def indexapp():
	pageData = {'agentLeve':'S3',  #经纪人等级
				  'position':'347,388,332',  #客户持仓
				  'winterGift':[{'img':'../static/images/agent-img1.jpg',   #图片地址
								 'leve':'S2',                 #领取等级
								 'giftDC':"leme蓝牙耳机水滴版",     #礼品描述
								 'abled':0}],            #是否可以领取
				'birthdayGift':[{'img':'../static/images/agent-img2.jpg',
								 'leve':'S2',
								 'giftDC':'罗技(Logitech)K810无线蓝牙炫光键盘',
								 'abled':1},
								{'img':'../static/images/agent-img3.jpg',
								 'leve':'S2',
								 'giftDC':'小米无人机,探索触手可及的新视角',
								 'abled':2}]}

	return render_template("indexapp.html",pageData = pageData)

@app.route('/indexdet')
def indexdet():
	return render_template("indexdet.html")
@app.route('/S2ward',methods=['GET','POST'])
def S2ward():

	form = SubmitForm()

	if form.is_submitted():
		user = User()
		user.info['name'] = request.form.get('name',type=str,default=None)
		user.info['tel'] = request.form.get('tel',type=str,default=None)
		user.info['oidname'] = request.form.get('oidname',type=str,default=None)
		user.info['add'] = request.form.get('add',type=str,default=None)
		print user.info
		return render_template('/result.html')
	#user = User()
	#user.info['name'] = request.form.get('name',type=str,default=None)
	#user.info['tel'] = request.form.get('tel',type=str,default=None)
	#user.oidname = form.oidname.date
	#user.add = form.add.date
	flash('thaks')
	return render_template('S2ward.html',form=form)
@app.route('/result')
def result():
	return render_template("result.html")
	
@app.errorhandler(404)
def page_not_found(error):
	return render_template('404.html'), 404

