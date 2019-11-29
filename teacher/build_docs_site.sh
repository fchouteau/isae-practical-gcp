rm -rf ../docs
cd docs && reveal-md . --css static/style.css --static=../../docs --static-dirs=static --absolute-url https://fchouteau.github.io/isae-practical-gcp
cp static/style.css ../../docs/css/style.css
cp 0_index.html ../../docs/index.html
sed -i 's|<link rel="stylesheet" href="/css/theme/black.css" id="theme" />|<link rel="stylesheet" href="/css/theme/white.css" />|g' ../../docs/index.html
sed -i 's|color: white;|color: black;|g' ../../docs/index.html
sed -i 's|<link rel="stylesheet" href="./_assets/static/style.css" />|<link rel="stylesheet" href="./css/style.css" />|g' ../../docs/index.html
sed -i 's|<link rel="stylesheet" href="./_assets/static/style.css" />|<link rel="stylesheet" href="./css/style.css" />|g' ../../docs/0_intro.html
sed -i 's|<link rel="stylesheet" href="./_assets/static/style.css" />|<link rel="stylesheet" href="./css/style.css" />|g' ../../docs/1_cloud.html
sed -i 's|<link rel="stylesheet" href="./_assets/static/style.css" />|<link rel="stylesheet" href="./css/style.css" />|g' ../../docs/2_docker.html
sed -i 's|<link rel="stylesheet" href="./_assets/static/style.css" />|<link rel="stylesheet" href="./css/style.css" />|g' ../../docs/3_gcp_4_data_science.html
sed -i 's|<link rel="stylesheet" href="./_assets/static/style.css" />|<link rel="stylesheet" href="./css/style.css" />|g' ../../docs/4_conclusion.html
cd ..
