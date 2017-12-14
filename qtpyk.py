# -*- coding: utf-8 -*-
 
 
 
#!/usr/bin/python
 
import sys
import random
from PyQt4 import QtGui, QtCore,Qt
 
class report_painter:
    '''����������'''
    def __init__(self,parent):
         
        #��ʼ��
        self.parent = parent
        self.paint = QtGui.QPainter()
        self.paint.begin(self.parent)
 
        #���ÿ����
        #self.paint.setRenderHint(QtGui.QPainter.Antialiasing)
        #�����߶���
        self.metrics = self.paint.fontMetrics()
         
        #���������
        self.fonts = dict()
        self.fonts['default'] = QtGui.QFont('Serif', 9, QtGui.QFont.Light)
        self.fonts['yahei_14_bold']= QtGui.QFont('Serif',12,QtGui.QFont.Bold)
        self.fonts['yahei_14']= QtGui.QFont('Serif',12,QtGui.QFont.Light)
        self.setFont('default')
 
        #���ñ�ˢ��ʽ��
        self.pens = dict()
         
        #��ɫ 1px��  1px�� 2px�� ����
        self.pens['red_1px_dashline'] =  QtGui.QPen( QtCore.Qt.red, 1, QtCore.Qt.DashLine) 
        self.pens['red_1px_dashline'].setDashPattern([1,2])
 
        #��ɫ 1px�� ʵ����
        self.pens['red'] = QtGui.QPen( QtCore.Qt.red, 1, QtCore.Qt.SolidLine)
        #��ɫ 3px�� ʵ����
        self.pens['red_2px'] = QtGui.QPen( QtCore.Qt.red, 2, QtCore.Qt.SolidLine)
        #��ɫ 2px�� ʵ����
        self.pens['red_3px'] = QtGui.QPen( QtCore.Qt.red, 3, QtCore.Qt.SolidLine)
        #��ɫ 1px�� ʵ����
        self.pens['yellow'] = QtGui.QPen( QtCore.Qt.yellow, 1, QtCore.Qt.SolidLine)
        #��ɫ 1px�� ʵ����
        self.pens['white']  = QtGui.QPen( QtCore.Qt.white , 1, QtCore.Qt.SolidLine)
        #��ɫ 1px�� ʵ����
        self.pens['gray']   = QtGui.QPen( QtCore.Qt.gray, 1, QtCore.Qt.SolidLine)
        #��ɫ 1px�� ʵ����
        self.pens['green']   = QtGui.QPen( QtCore.Qt.green, 1, QtCore.Qt.SolidLine)
        #��ɫ 3px�� ʵ����
        self.pens['green_2px']   = QtGui.QPen( QtCore.Qt.green, 2, QtCore.Qt.SolidLine)
        #���� 1px��  1px�� 2px�� ����
        self.pens['cyan_1px_dashline'] =  QtGui.QPen( QtCore.Qt.cyan, 1, QtCore.Qt.DashLine) 
        self.pens['cyan_1px_dashline'].setDashPattern([3,2])
        #��ô��ڵĳ��Ϳ�
        size      = self.parent.size()
        self.w    = size.width()
        self.h    = size.height()
 
        #����grid���������Ҳ����߾�
        self.grid_padding_left   = 45  #��ಹ���߾�
        self.grid_padding_right  = 245 #�Ҳಹ���߾�
        self.grid_padding_top    = 25  #���������߾�
        self.grid_padding_bottom = 17  #�ײ������߾�
             
        #��ʼ����
        self.start_paint()
 
 
        self.paint.end()   #����
    '''�������̲���'''
    def start_paint(self):
        self.PriceGridPaint()
        self.rightGridPaint()
        self.timelinePaint()
        self.topInfoPaint()
        self.rulerPaint()
        self.VolumeGridPaint()
        self.volumePaint()
        self.pricePaint()
        self.xyPaint()
    '''����ʹ�õ�����'''
    def setFont(self,code='default'):
        self.paint.setFont(self.fonts[code])
         
    '''����ʹ�õı�ˢ'''
    def setPen(self,code='default'):
        self.paint.setPen(self.pens[code])
         
    '''���ƹɼ����Ʊ��'''
    def PriceGridPaint(self):
        self.setPen('red')
        self.paint.setBrush(QtCore.Qt.NoBrush)
         
        sum_width  = self.grid_padding_left+self.grid_padding_right
        sum_height = self.grid_padding_top+self.grid_padding_bottom
 
        grid_height = self.h-sum_height
 
        #���߿�
        self.paint.drawRect(self.grid_padding_left,self.grid_padding_top,
                            self.w-sum_width,self.h-sum_height)
        #�ɽ��������Ƶķֽ���
        self.paint.drawLine(self.grid_padding_left,grid_height*0.7+self.grid_padding_top,
                            self.w-self.grid_padding_right,grid_height*0.7+self.grid_padding_top)
 
        #��Ʊ�����м���
        self.paint.drawLine(self.grid_padding_left+1,
                            grid_height*0.35+self.grid_padding_top,
                            self.w-self.grid_padding_right
                            ,grid_height*0.35+self.grid_padding_top)
 
        #��������
        self.paint.drawLine(0,self.h-self.grid_padding_bottom,self.w-self.grid_padding_right+44,self.h-self.grid_padding_bottom)
        self.paint.drawLine(0,self.h-self.grid_padding_bottom+16,self.w,self.h-self.grid_padding_bottom+16)
 
        self.paint.drawLine(self.w-self.grid_padding_right,0,
                            self.w-self.grid_padding_right,self.h-self.grid_padding_bottom+16)
        self.paint.drawLine(self.w-self.grid_padding_right+44,0,
                            self.w-self.grid_padding_right+44,self.h-self.grid_padding_bottom+16)
        self.setPen('yellow')
        self.paint.drawText(self.w-self.grid_padding_right+5,self.h-self.grid_padding_bottom-4,QtCore.QString('�ɽ���'))
        self.setPen('white')
        #���½�����
        self.paint.drawText(self.w-self.grid_padding_right+12,self.h-self.grid_padding_bottom+12,QtCore.QString('ʵʱ'))
    '''���Ƴɽ������Ʊ��'''
    def VolumeGridPaint(self):
        sum_width  = self.grid_padding_left + self.grid_padding_right
        sum_height = self.grid_padding_top  + self.grid_padding_bottom
         
        grid_height = self.h-sum_height
        max_volume = self.parent.stk_data['max_vol']
         
        px_h_radio = max_volume/(grid_height*0.3)
         
        self.setPen('red_1px_dashline')
         
         
        grid_num = 6
        x = grid_num
        cnt = grid_height*0.3/grid_num
        for i in range(0,grid_num):
            self.setPen('red_1px_dashline')
            #��������
            y1 = self.grid_padding_top+(grid_height*0.7)+i*cnt
            x1 = self.grid_padding_left
            x2 = self.grid_padding_left+self.w-sum_width
             
            self.paint.drawLine(x1,y1,x2,y1) #����λ����
             
            vol_int = int(cnt*x*px_h_radio)
            vol_str = str(vol_int)
            fw = self.metrics.width(vol_str) #������ֿ��
            fh = self.metrics.height()/2   #������ָ߶�
            self.setPen('yellow')
            self.paint.drawText(x2+40-fw,y1+fh,vol_str) #д������
            self.setPen('white')
            self.paint.drawText(x1-2-self.metrics.width(str(x)),y1+fh,str(x))    #д������
            x-=1
             
         
    '''���������Ϣ�����̿ڵ�����'''
    def rightGridPaint(self):
        self.setPen('red')
        #������Ϣ����֮��ķָ���
        _h = 0
        _x = self.w-self.grid_padding_right+44
        self.paint.drawLine(self.w-1,0,self.w-1,self.h-self.grid_padding_bottom+16)
        self.paint.drawLine(0,0,0,self.h-self.grid_padding_bottom+16)
        self.paint.drawLine(0,_h,self.w,_h)
        _h+=23
        self.paint.drawLine(_x,_h,self.w,_h)
        _h+=24
        self.paint.drawLine(_x,_h,self.w,_h)
 
        _h+=93
        self.paint.drawLine(_x,_h,self.w,_h)
        _h+=20
        self.paint.drawLine(_x,_h,self.w,_h)
        _h+=93
        self.paint.drawLine(_x,_h,self.w,_h)
        _h+=123
        self.paint.drawLine(_x,_h,self.w,_h)
        _h+=23
        self.paint.drawLine(_x,_h,self.w,_h)
        #��Ʊ���ƺʹ���
        self.setFont('yahei_14_bold')
        self.setPen('yellow')
        name_str = QtCore.QString('%s %s'%(self.parent.stk_info['code'],self.parent.stk_info['name']))
        self.paint.drawText(_x+35,18,name_str)
        #ί�Ⱥ�ί��
        self.setFont('yahei_14')
        zx_str = QtCore.QString('����')
        self.paint.drawText(_x+3  ,156,zx_str)
        self.setPen('gray')
        wb_str = QtCore.QString('ί��')
        wc_str = QtCore.QString('ί��')
        xs_str = QtCore.QString('����')
        self.paint.drawText(_x+3  ,39,wb_str)
        self.paint.drawText(_x+100,39,wc_str)
        self.paint.drawText(_x+100,156,xs_str)
        fh = self.metrics.height()
         
        left_field_list = ['�ǵ�','�Ƿ�','���','����','�ܶ�','����','�ֱ�']
        i = 1
        for field in left_field_list:
            field_str = QtCore.QString(field)
            self.paint.drawText(_x+3,253+(i*17),field_str)
            i+=1
 
        right_field_list = ['����','ǰ��','��','���','���','����','����']
         
        i = 1
        for field in right_field_list:
            field_str = QtCore.QString(field)
            self.paint.drawText(_x+100,253+(i*17),field_str)
            i+=1
 
        wp_str = QtCore.QString('����')
        np_str = QtCore.QString('����')
        self.paint.drawText(_x+3,395,wp_str)
        self.paint.drawText(_x+100,395,np_str)
        #���٢ڢۢܢ�
         
        i = 0
        sell_queue = ['����','����','����','����','����']
        for sell in sell_queue:
            sell_str = QtCore.QString(sell)
            self.paint.drawText(_x+3,62+(i*18),sell_str)
            i+=1
        #��٢ڢۢܢ�
        buy_queue = ['���','���','���','���','���']
        for buy in buy_queue:
            buy_str = QtCore.QString(buy)
            self.paint.drawText(_x+3,87+(i*18),buy_str)
            i+=1
 
        self.setPen('red_2px')
        self.paint.drawLine(_x+1,377,_x+99,377)
        self.paint.drawLine(_x+1,46,_x+65,46)
        self.setPen('green_2px')
        self.paint.drawLine(_x+102,377,_x+199,377)
        self.paint.drawLine(_x+67,46,_x+199,46)
        self.setFont('default')
         
    '''�������Ҳ�ļ۸�̶�'''
    def rulerPaint(self):
         
        sum_width  = self.grid_padding_left+self.grid_padding_right
        sum_height = self.grid_padding_top+self.grid_padding_bottom
 
        grid_height = self.h-sum_height
         
        high = self.parent.stk_data['high']
        low  = self.parent.stk_data['low']
        lastclose = self.parent.stk_data['lastclose']
 
        top = high-lastclose
        bottom = lastclose-low
        if top>bottom:
            padding = top
        else:
            padding = bottom
             
        limit_top = lastclose+padding
        limit_low = lastclose-padding
 
 
        px_h_radio = (grid_height*0.7)/((limit_top-limit_low)*100)
 
         
        self.setPen('red_1px_dashline')
 
        grid_num = 16
        cnt = grid_height*0.7/grid_num
         
        for i in range(0,grid_num):
            self.setPen('red_1px_dashline')
            #��������
            y1 = self.grid_padding_top+i*cnt
            x1 = self.grid_padding_left
            x2 = self.grid_padding_left+self.w-sum_width
             
            self.paint.drawLine(x1,y1,x2,y1) #����λ����
             
            price_float = (limit_top - ((i*cnt)/px_h_radio/100)) #����۸�
            price = '%4.2f'%(price_float) #��ʽ���۸��str
             
            fw = self.metrics.width(price) #������ֿ��
            fh = self.metrics.height()/2   #������ָ߶�
 
            radio_float = (price_float/lastclose-1)*100 #���㲨���ٷֱ�
            radio_str   = "%2.2f%%"%(radio_float)      #��ʽ���ٷֱȳ�str
 
            r_fw = self.metrics.width(radio_str)
            r_fh = self.metrics.height()/2
            #�ж�����ʹ�õ���ɫ
            if price_float == lastclose:
                self.setPen('white')
            if price_float < lastclose:
                self.setPen('green')
                 
            self.paint.drawText(x1-fw-2,y1+fh,price) #д������
            self.paint.drawText(x2+40-r_fw,y1+r_fh,radio_str) #д������
    '''����x,y׼��'''
    def xyPaint(self):
        if self.parent.m_x >= self.grid_padding_left and self.parent.m_x<=self.w-self.grid_padding_right and self.parent.m_y>=self.grid_padding_top and self.parent.m_y<=self.h-self.grid_padding_bottom:
            self.setPen('gray')
            x1 = self.grid_padding_left
            x2 = self.w-self.grid_padding_right
            y1 = self.grid_padding_top
            y2 = self.h-self.grid_padding_bottom
            self.paint.drawLine(x1+1,self.parent.m_y,x2-1,self.parent.m_y)
            self.paint.drawLine(self.parent.m_x,y1+1,self.parent.m_x,y2-1)
             
             
     
    '''����ʱ����̶�'''
    def timelinePaint(self):
         
        fw = self.metrics.width('00:00') #�������ֵĿ��
         
        sum_width  = self.grid_padding_left+self.grid_padding_right
        sum_height = self.grid_padding_top+self.grid_padding_bottom
         
        grid_width = self.w-sum_width-2
         
         
        y1 = self.grid_padding_top
        y2 = y1+(self.h-sum_height)
 
        #ʱ��������
        self.setPen('red')
        x_pos = grid_width/2+self.grid_padding_left
         
        self.paint.drawLine(x_pos,y1,x_pos,y2)
        self.paint.drawText(x_pos-fw/2,y2+12,QtCore.QString('13:00'))
         
        #ʱ����09��30��
        x_pos = self.grid_padding_left
        self.paint.drawText(x_pos,y2+12,QtCore.QString('09:30'))
         
        #ʱ����10��30��
        x_pos = grid_width*0.25+self.grid_padding_left
        self.paint.drawLine(x_pos,y1,x_pos,y2)
        self.paint.drawText(x_pos-fw/2,y2+12,QtCore.QString('10:30'))
 
        #ʱ����14��00��
        x_pos = grid_width*0.75+self.grid_padding_left
        self.paint.drawLine(x_pos,y1,x_pos,y2)
        self.paint.drawText(x_pos-fw/2,y2+12,QtCore.QString('14:00'))
 
        #ʱ����15��00��
        x_pos = grid_width+self.grid_padding_left
        self.paint.drawText(x_pos-fw,y2+12,QtCore.QString('15:00'))
 
        #ʱ������ by 30min
        self.setPen('red_1px_dashline')
        x_pos_array = [0.125,0.375,0.625,0.875]
        for i in x_pos_array:
            x_pos = grid_width*i+self.grid_padding_left
            self.paint.drawLine(x_pos,y1,x_pos,y2)
 
         
    '''���Ʊ���Ϸ��Ĺ�Ʊ��Ϣ'''
    def topInfoPaint(self):
        self.setPen('yellow')
        self.paint.drawText(4+self.grid_padding_left,self.grid_padding_top-4
                            ,QtCore.QString(self.parent.stk_info['name'])) #��Ʊ����
        self.paint.drawText(4+self.grid_padding_left+120,self.grid_padding_top-4
                            ,QtCore.QString('�����ߣ�')) #������
        lastclose = self.parent.stk_data['lastclose']
        close     = self.parent.stk_data['close']
        mma       = self.parent.stk_data['list']['mma'][-1]
         
        if lastclose>close:
            self.setPen('green')
            str_1 = '%.2f -%.2f'%(close,lastclose-close)
        if lastclose==close:
            self.setPen('white')
            str_1 = '%.2f +%.2f'%(close,0.00)
        if lastclose<close:
            self.setPen('red')
            str_1 = '%.2f +%.2f'%(close,close-lastclose)
         
        if mma>close:
            self.setPen('green')
        if mma==close:
            self.setPen('white')
        if mma<close:
            self.setPen('red')
         
        self.paint.drawText(4+self.grid_padding_left+55,self.grid_padding_top-4,QtCore.QString(str_1))
        self.paint.drawText(4+self.grid_padding_left+165,self.grid_padding_top-4,QtCore.QString('%.2f'%mma)) #����
         
        #��ͣ��
        self.setPen('red')
        self.paint.drawText(4+self.grid_padding_left+200,self.grid_padding_top-4,QtCore.QString('��ͣ��:%.2f'%(lastclose*1.1))) #����
        #��ͣ��
        self.setPen('green')
        self.paint.drawText(4+self.grid_padding_left+280,self.grid_padding_top-4,QtCore.QString('��ͣ��:%.2f'%(lastclose*0.9))) #����
    '''���ƹɼ�����'''
    def pricePaint(self):
        sum_width  = self.grid_padding_left+self.grid_padding_right
        sum_height = self.grid_padding_top+self.grid_padding_bottom
 
        grid_height = self.h-sum_height-2
         
        high = self.parent.stk_data['high']
        low  = self.parent.stk_data['low']
        lastclose = self.parent.stk_data['lastclose']
 
        top = high-lastclose
        bottom = lastclose-low
        if top>bottom:
            padding = top
        else:
            padding = bottom
             
        limit_top = lastclose+padding
        limit_low = lastclose-padding
         
        h_radio = (grid_height*0.7)/((limit_top-limit_low)*100)
 
        w_radio = (self.w-sum_width-2)/240.00
        w = self.grid_padding_left
         
        self.setPen('white')
        path = QtGui.QPainterPath()
        path.moveTo(w,(limit_top-self.parent.stk_data['open'])*100*h_radio+self.grid_padding_top)
        i  = 1
        for price in self.parent.stk_data['list']['close']:
            w = i*w_radio+self.grid_padding_left
            y = (limit_top-price)*100*h_radio+self.grid_padding_top
            path.lineTo(w,y)
            i+=1
        self.paint.drawPath(path)
        self.setPen('cyan_1px_dashline')
        self.paint.drawLine(self.grid_padding_left+1,y,w-1,y)
        self.setPen('yellow')
        path = QtGui.QPainterPath()
        w = self.grid_padding_left
        path.moveTo(w,(limit_top-self.parent.stk_data['open'])*100*h_radio+self.grid_padding_top)
        i  = 1
        for price in self.parent.stk_data['list']['mma']:
            w = i*w_radio+self.grid_padding_left
            y = (limit_top-price)*100*h_radio+self.grid_padding_top
            path.lineTo(w,y)
            i+=1
        self.paint.drawPath(path)
         
         
    '''���Ƴɽ���'''
    def volumePaint(self):
        sum_width  = self.grid_padding_left + self.grid_padding_right
        sum_height = self.grid_padding_top  + self.grid_padding_bottom
 
        max_volume = self.parent.stk_data['max_vol'] #�����ӳɽ���
         
        w_radio = (self.w-sum_width-2)/240.00
        h_radio = ((self.h-sum_height-2)*0.3)/max_volume
 
        y = (self.h-sum_height)+self.grid_padding_top
         
        self.setPen('yellow')
 
 
             
        for i in range(1,len(self.parent.stk_data['list']['vol'])+1):
            x = i*w_radio+self.grid_padding_left
            y2 = h_radio*self.parent.stk_data['list']['vol'][i-1]
            self.paint.drawLine(x,y-1,x,y-y2)
 
class Test(QtGui.QWidget):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.setMinimumSize(640, 430) #���ô�����С�ߴ�
        self.setGeometry(300, 300, 960, 650)
        self.setWindowTitle(QtCore.QString('�����ѻ���[�ڲ��������԰�]-����ʵʱ����'))
        self.setStyleSheet("QWidget { background-color: black }")
        self.setWindowIcon(QtGui.QIcon('ruby.png'))
        self.setMouseTracking(True)
        self.m_x = 0 #���x��λ��
        self.m_y = 0 #���y��λ��
         
        self.stk_info = {}
         
        self.stk_info['name'] = '�㽭����'
        self.stk_info['code'] = '600120'
        self.stk_info['market'] = 'SH'
         
        self.stk_data = {}
        self.stk_data['list'] = {} #�ɼ�����
        self.stk_data['list']['time']  = [] #ʱ��
        self.stk_data['list']['open']  = [] #���̼�
        self.stk_data['list']['high']  = [] #��߼�
        self.stk_data['list']['low']   = [] #��ͼ�
        self.stk_data['list']['close'] = [] #���̼�
        self.stk_data['list']['vol']   = [] #�ɽ���
        self.stk_data['list']['amount']= [] #�ɽ���
        self.stk_data['list']['mma']= []   #��ʱ����
         
        self.stk_data['list']['buy_port'] = [(0.00,0),(0.00,0),(0.00,0),(0.00,0),(0.00,0)]  #����ǰ��
        self.stk_data['list']['sell_port'] = [(0.00,0),(0.00,0),(0.00,0),(0.00,0),(0.00,0)] #����ǰ��
         
        #��ȡ����
        f = open('SH600120.txt','r')
        data = f.readlines()
        f.close()
         
        for row in data:
            vars = row.split(' ')
            self.stk_data['list']['time'].append(vars[1])
            self.stk_data['list']['open'].append(float(vars[2]))
            self.stk_data['list']['high'].append(float(vars[3]))
            self.stk_data['list']['low'].append(float(vars[4]))
            self.stk_data['list']['close'].append(float(vars[5]))
            self.stk_data['list']['vol'].append(int(float(vars[6])))
            self.stk_data['list']['amount'].append(int(float(vars[7])))
             
            sum_vol = sum(self.stk_data['list']['vol'])
            sum_amt = sum(self.stk_data['list']['amount'])
 
            self.stk_data['list']['mma'].append(float(sum_amt)/(sum_vol*100.00))
             
        self.stk_data['lastclose'] = 10.12 #��һ�����������̼�
        self.stk_data['open'] = self.stk_data['list']['open'][0]       #���̼�
        self.stk_data['high'] = max(self.stk_data['list']['high'])     #��߼�
        self.stk_data['low']  = min(self.stk_data['list']['low'])      #��ͼ�
        self.stk_data['close']= self.stk_data['list']['close'][-1]     #���̼�
        self.stk_data['max_vol']  = max(self.stk_data['list']['vol'])  #������߳ɽ���
         
             
    def mouseMoveEvent(self, event):
        self.m_x =  int(event.x())
        self.m_y =  int(event.y())
        self.repaint()
    def paintEvent(self, event):
        report_painter(self)
 
app = QtGui.QApplication(sys.argv)
dt = Test()
dt.show()
app.exec_()