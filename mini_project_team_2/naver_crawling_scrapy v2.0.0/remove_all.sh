dir="naver_movie_reply"
if [ -d "$dir" ]
then
	rm -rf naver_movie_reply/ run_movie_reply.sh run_movie.sh
	echo "Prior Project removed"
	echo "Ready to create New Porject"
else
	echo "Ready to create New Porject"
fi


