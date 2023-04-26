##
## EPITECH PROJECT, 2023
## B-MAT-500-MPL-5-1-309pollution-etienne.licheron
## File description:
## Makefile
##

PRJ	=	309pollution

all	:
		cp $(PRJ).py $(PRJ)
		chmod +x $(PRJ)

clean	:
		rm -f $(PRJ)

fclean	:	clean

re	:	fclean all