import sys
try:  
    import pygtk  
    pygtk.require("2.0")  
except:  
    pass  
try:  
    import gtk  
    import gtk.glade  
except:  
    print("GTK Not Availible")
    sys.exit(1)
#такой импорт делать обязательно
import math       
        
class silver():
    wTree = None
    b = None
    def __init__(self):
        self.wTree = gtk.glade.XML( "m.glade" )
        
        dic = { 
            "exit" : self.quit,
            "add_in_hide(1)" : self.add1,
            "add_in_hide(2)" : self.add2,
            "add_in_hide(3)" : self.add3,
            "add_in_hide(4)" : self.add4,
            "add_in_hide(5)" : self.add5,
            "add_in_hide(6)" : self.add6,
            "add_in_hide(7)" : self.add7,
            "add_in_hide(8)" : self.add8,
            "add_in_hide(9)" : self.add9,
            "add_in_hide(0)" : self.add0,
            "add_in_hide(+)" : self.add_pl,
            "add_in_hide(-)" : self.add_min,
            "add_in_hide(*)" : self.add_um,
            "add_in_hide(/)" : self.add_de,
            "add_in_hide(()" : self.add_s1,
            "add_in_hide())" : self.add_s2,
            "result" : self.result,
            "clear" : self.clear,
            "m_sim" : self.m_sim,
            "sqrt" : self.sqrt,
            "x^y" : self.pow,
            ",":self.z,
            "t":self.t,
            "sin":self.sin,
            "cos":self.cos,
            "pow_v" : self.pow_v,
            "otm_d1" : self.otm_d1,
            "sq" : self.sq,
            "otm_d2" : self.otm_d2,
            "sin_v" : self.sin_v,
            "otm_d3": self.otm_d3,
            "cos_v":self.cos_v,
            "otm_d4":self.otm_d4,
            "root":self.root,
            "root_v":self.root_v,
            "otm_d5":self.otm_d5,            
            #"destroy" : self.quit,
        }
        self.wTree.signal_autoconnect( dic )                
        gtk.main()
        self.all= self.wTree.get_widget("entry3").get_text()
    
    all= '' 
    def root(self,widget):
        #root = a**(1/n)
        self.wTree.get_widget("dialog5").show()        
        
    def root_v(self, widget):
        self.all= self.wTree.get_widget("entry3").get_text()
        p1 = self.wTree.get_widget("entry7").get_text()    
        p2 = self.wTree.get_widget("entry8").get_text()    
        p3 = 1/float(p2)
        self.all = str(self.all) + 'math.pow('+p1+','+str(p3)+')'
        self.wTree.get_widget("entry3").set_text(self.all)
        self.all=b = self.wTree.get_widget("entry3").get_text()    
    
    def sin(self,widget):
        self.wTree.get_widget("dialog3").show()
        
    def sin_v(self, widget):
        self.wTree.get_widget("entry3").set_text(self.all)
        p1 = self.wTree.get_widget("entry5").get_text()        
        p1 = str(p1)
        if p1 == '':
            p1 == '0'
        
        self.all = str(self.all) + 'math.sin('+p1+')'
        self.wTree.get_widget("entry3").set_text(self.all)
        self.wTree.get_widget("entry5").set_text('')
        self.wTree.get_widget("dialog3").hide()    
        
        
    def cos(self,widget):
        self.wTree.get_widget("dialog4").show()
        
        
    def cos_v(self, widget):
        self.wTree.get_widget("entry3").set_text(self.all)
        p1 = self.wTree.get_widget("entry6").get_text()        
        p1 = str(p1)
        if p1 == '':
            p1 == '0'
        
        self.all = str(self.all) + 'math.cos('+p1+')'
        self.wTree.get_widget("entry3").set_text(self.all)
        self.wTree.get_widget("entry6").set_text('')
        self.wTree.get_widget("dialog3").hide()    
    
    def t(self,widget):
        self.all= self.wTree.get_widget("entry3").get_text()
        self.all = str(self.all) + ','
        self.wTree.get_widget("entry3").set_text(self.all)
        self.all=b = self.wTree.get_widget("entry3").get_text()
        
    
    def z(self,widget):
        self.all= self.wTree.get_widget("entry3").get_text()
        self.all = str(self.all) + '.'
        self.wTree.get_widget("entry3").set_text(self.all)
        self.all=b = self.wTree.get_widget("entry3").get_text()
        
    
    def pow(self,widget):
        #$#####
        self.wTree.get_widget("dialog1").show()
        
        #$#####
        
    def pow_v(self, widget):
        self.wTree.get_widget("entry3").set_text(self.all)
        p1 = self.wTree.get_widget("entry1").get_text()        
        p2 = self.wTree.get_widget("entry2").get_text()
        p1 = str(p1)
        if p1 == '':
            p1 == '0'
        if p2 == '':
            p2 =='0'
                
        self.all = str(self.all) + 'math.pow('+p1+','+p2+')'
        self.wTree.get_widget("entry3").set_text(self.all)
        self.wTree.get_widget("entry1").set_text('')
        self.wTree.get_widget("entry2").set_text('')
        self.wTree.get_widget("dialog1").hide()    
        
    
    def otm_d1(self, widget):
        self.wTree.get_widget("dialog1").hide()
        
    def otm_d2(self , widget):
        self.wTree.get_widget("dialog2").hide()
        
    def otm_d3(self , widget):
        self.wTree.get_widget("dialog3").hide()
        
    def otm_d4(self , widget):
        self.wTree.get_widget("dialog4").hide()
        
    def otm_d5(self , widget):
        self.wTree.get_widget("dialog5").hide()
    
    def sqrt(self,widget):
        self.wTree.get_widget("dialog2").show()        
     
    
    def add1(self, widget):
        self.all= self.wTree.get_widget("entry3").get_text()
        self.all= self.wTree.get_widget("entry3").get_text()
        self.all = str(self.all) + '1'
        self.wTree.get_widget("entry3").set_text(self.all)
        
        
    def add2(self, widget):
        self.all= self.wTree.get_widget("entry3").get_text()
        self.all = str(self.all) + '2'
        self.wTree.get_widget("entry3").set_text(self.all)
        self.all=b = self.wTree.get_widget("entry3").get_text()
        
    def sq(self,widget):
            self.wTree.get_widget("entry3").set_text(self.all)
            p3 = self.wTree.get_widget("entry4").get_text()        
            p3 = str(p3)
            if p3 == '':
                p3 == '0'
                            
            self.all = str(self.all) + 'math.sqrt('+p3+')'
            self.wTree.get_widget("entry3").set_text(self.all)
            self.wTree.get_widget("entry4").set_text('')
            self.wTree.get_widget("dialog2").hide()    
    
    def add3(self, widget):
        self.all= self.wTree.get_widget("entry3").get_text()
        self.all = str(self.all) + '3'
        self.wTree.get_widget("entry3").set_text(self.all)
        self.all=b = self.wTree.get_widget("entry3").get_text()
        
        
    def add4(self, widget):
        self.all= self.wTree.get_widget("entry3").get_text()
        self.all = str(self.all) + '4'
        self.wTree.get_widget("entry3").set_text(self.all)
        self.all=b = self.wTree.get_widget("entry3").get_text()
        
        
    def add5(self, widget):
        self.all= self.wTree.get_widget("entry3").get_text()
        self.all = str(self.all) + '5'
        self.wTree.get_widget("entry3").set_text(self.all)
        self.all=b = self.wTree.get_widget("entry3").get_text()
        
        
    def add6(self, widget):
        self.all= self.wTree.get_widget("entry3").get_text()
        self.all = str(self.all) + '6'
        self.wTree.get_widget("entry3").set_text(self.all)
        self.all=b = self.wTree.get_widget("entry3").get_text()
        
        
    def add7(self, widget):
        self.all= self.wTree.get_widget("entry3").get_text()
        self.all = str(self.all) + '7'
        self.wTree.get_widget("entry3").set_text(self.all)
        self.all=b = self.wTree.get_widget("entry3").get_text()
        
        
    def add8(self, widget):
        self.all= self.wTree.get_widget("entry3").get_text()
        self.all = str(self.all) + '8'
        self.wTree.get_widget("entry3").set_text(self.all)
        self.all=b = self.wTree.get_widget("entry3").get_text()
        
        
    def add9(self, widget):
        self.all= self.wTree.get_widget("entry3").get_text()
        self.all = str(self.all) + '9'
        self.wTree.get_widget("entry3").set_text(self.all)
        self.all=b = self.wTree.get_widget("entry3").get_text()
        
        
    def add0(self, widget):
        self.all= self.wTree.get_widget("entry3").get_text()
        self.all = str(self.all) + '0'
        self.wTree.get_widget("entry3").set_text(self.all)
        self.all=b = self.wTree.get_widget("entry3").get_text()
        
        
    def add_pl(self, widget):
        self.all= self.wTree.get_widget("entry3").get_text()
        self.all = str(self.all) + '+'
        self.wTree.get_widget("entry3").set_text(self.all)
        self.all=b = self.wTree.get_widget("entry3").get_text()
        
        
    def add_min(self, widget):
        self.all= self.wTree.get_widget("entry3").get_text()
        self.all = str(self.all) + '-'
        self.wTree.get_widget("entry3").set_text(self.all)
        self.all=b = self.wTree.get_widget("entry3").get_text()
        
        
    def add_um(self, widget):
        self.all = str(self.all) + '*'
        self.wTree.get_widget("entry3").set_text(self.all)
        self.all=b = self.wTree.get_widget("entry3").get_text()
        
        
    def add_de(self, widget):
        self.all= self.wTree.get_widget("entry3").get_text()        
        self.all = str(self.all) + '/'
        self.wTree.get_widget("entry3").set_text(self.all)
        self.all=b = self.wTree.get_widget("entry3").get_text()
        
        
    def m_sim(self, widget):
        self.all= self.wTree.get_widget("entry3").get_text()
        self.all = str(self.all)[:-1]
        self.wTree.get_widget("entry3").set_text(self.all)
        self.all=b = self.wTree.get_widget("entry3").get_text()
        
            
        
    def clear(self, widget):
        self.all = ''
        self.wTree.get_widget("entry3").set_text(self.all)
        self.all=b = self.wTree.get_widget("entry3").get_text()
        
         
    def add_s1(self, widget):
        self.all= self.wTree.get_widget("entry3").get_text()
        self.all = str(self.all) + '('
        self.wTree.get_widget("entry3").set_text(self.all)
        self.all=b = self.wTree.get_widget("entry3").get_text()
        
         
        
    def add_s2(self, widget):
        self.all= self.wTree.get_widget("entry3").get_text()
        self.all = str(self.all) + ')'
        self.wTree.get_widget("entry3").set_text(self.all)
        self.all=b = self.wTree.get_widget("entry3").get_text()
        
         
    def result(self, widget):
        try:
            #self.all=str(self.all)
            self.all=b = self.wTree.get_widget("entry3").get_text()
            
            self.all=eval(self.all)
            self.wTree.get_widget("entry3").set_text(str(self.all))
        except:
            self.wTree.get_widget("hbox1").show()
            self.wTree.get_widget("entry3").set_text("ERROR")
    
    
    def quit(self, widget):
        sys.exit(0)

letsdothis=silver()
