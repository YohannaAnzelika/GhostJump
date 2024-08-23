from dasar import *

# melakukan perhitungan skor dan menampilkan skor pada saat game dimulai
class Skor:
    def __init__(self,skor):
        self.__current_skor = skor
        self.__score_surf = font.render(f"score: {self.__current_skor}", False, ("#e6e7e7"))
        self.__score_rect = self.__score_surf.get_rect(center = (500, 300))
    def display_score(self):
        screen.blit(self.__score_surf, self.__score_rect) 
        return self.__current_skor
    

    def update(self):
        self.display_score()