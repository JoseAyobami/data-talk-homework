def main():
    print("Hello from pipeline-2!")


if __name__ == "__main__":
    main()



# docker run -it \
#   -e PGADMIN_DEFAULT_EMAIL="pgadmin@pgadmin.com" \
#   -e PGADMIN_DEFAULT_PASSWORD="pgadmin" \
#   -v pgadmin_data:/var/lib/pgadmin \
#   -p 8080:80 \
#   dpage/pgadmin4