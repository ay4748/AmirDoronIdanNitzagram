import pygame

from constants import *
from helpers import screen


class Post:
    """
    A class used to represent post on Nitzagram
    """

    def init(self,username, location, description):
        self.username = username
        self.location = location
        self.description = description
        self.likes_counter = 0
        self.comments = []

    def display(self):
        """
        Display the Post image/Text, description, location, likes and comments
        on screen

        :return: None
        """


        font = pygame.font.SysFont("chalkduster.ttf", UI_FONT_SIZE)

        user_name = font.render(self.username, True, BLACK)
        screen.blit(user_name, (USER_NAME_X_POS, USER_NAME_Y_POS))  #display the user name

        location = font.render(self.location, True, BLACK)
        screen.blit(location, (LOCATION_TEXT_X_POS, LOCATION_TEXT_Y_POS)) #display the location

        like_counter = font.render(str(self.like_counter), True, BLACK)
        screen.blit(like_counter, (LIKE_TEXT_X_POS, LIKE_TEXT_Y_POS)) #display the likes number

        description = font.render(self.description, True, LIGHT_GRAY)
        screen.blit(description, (DESCRIPTION_TEXT_X_POS, DESCRIPTION_TEXT_Y_POS)) #display the descripotion

        self.display_comments()


    def display_comments(self):
        """
        Display comments on post. In case there are more than 4
        comments, show only 4 comments chosen by reset_comments_display_index

        :return: None
        """
        position_index = self.comments_display_index
        # If there are more than 4 comments, print "view more comments"
        if len(self.comments) > NUM_OF_COMMENTS_TO_DISPLAY:
            comment_font = pygame.font.SysFont('chalkduster.ttf',
                                               COMMENT_TEXT_SIZE)
            view_more_comments_button = comment_font.render("view more comments",
                                                            True, LIGHT_GRAY)
            screen.blit(view_more_comments_button, (VIEW_MORE_COMMENTS_X_POS,
                                                    VIEW_MORE_COMMENTS_Y_POS))

        # Display 4 comments starting from comments_display_index
        for i in range(0, len(self.comments)):
            if position_index >= len(self.comments):
                position_index = 0
            self.comments[position_index].display(i)
            position_index += 1
            if i >= NUM_OF_COMMENTS_TO_DISPLAY - 1:
                break

    def add_like(self):
        self.like_counter += 1

    def add_comment(self, text):
        com = Comment(text)
        self.comments.append(com)