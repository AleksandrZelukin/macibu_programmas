�
�d�\c           @   s�   d  GHd �  Z  d �  Z e d � Z e d k r� e d � Z e d k rV e d � Z n6 e d k rq e d � Z n e d k r� e d � Z n  e  �  n e d	 k r� d
 GHn  d S(   s   Поиграем в очкоc          C   s�  t  d k r d d g }  n? t  d k r9 d d d g }  n! t  d k rZ d d d d g }  n  d d d d d	 d
 g d } d d  l } | j | � t d � } x� | t  k  rXd | GHx� t rJt d � } | d k r*| j �  } d | GH|  | c | 7<|  | d k rd |  | GHPqGd |  | GHq� | d k r� d |  | GHPq� q� W| d 7} q� Wt d � } t d � } d } xM | t  k  r�| |  | k  r�|  | d k  r�|  | } | } n  | d 7} qzWd | GHt �  d  S(   Ni   i    i   i   i   i   i   i	   i
   i   i����t   0s   Игрок номер %ds   Берете карту? y/n
t   ys0   У вас карта достоинством %di   s1   У вас %d очков 
 Вы проигралиs   У вас %d очковt   ni   s(   Игрок номер %d Победил!(   t   it   randomt   shufflet   intt   Truet   inputt   popt   game(   t   countt   kolodaR   R   t   choicet   currentt   rest   chemp(    (    si   /Users/zelukin/Documents/OneDrive - Rīgas domes izglītības iestādes/PYTHON/Programmas/очко.pyt   start   sH    			 
		c          C   s:   t  d � }  |  d k r" t �  n |  d k r6 d GHn  d  S(   Ns!   Играем поновой? y/n
R   R   s2   Игра закончена,До свидания!(   R   R   (   R   (    (    si   /Users/zelukin/Documents/OneDrive - Rīgas domes izglītības iestādes/PYTHON/Programmas/очко.pyR
   *   s
    
s   Играем? y/n
R   s%   Сколько игроков? 2,3,4
t   2t   3t   4R   s   Удачи!N(   R   R
   R   R   R   R   (    (    (    si   /Users/zelukin/Documents/OneDrive - Rīgas domes izglītības iestādes/PYTHON/Programmas/очко.pyt   <module>   s   	(	
