Yêu cầu bài làm cụ thể gồm các nội dung sau:

1.Phát biểu bài toán (đặt trên đầu của file notebook):
    Phân tích dữ liệu nhằm khảo sát tính khả thi cho việc xây dựng mô hình dự đoán biến mục tiêu (target variable) Y từ các biến/đặc trưng (predictors/features) Xi (i=1..N).

    Nếu biến Y xác định cụ thể -> việc mô hình hóa là 1 trong 2 bài toán: phân lớp (classification) nếu Y là biến danh mục, hoặc hồi quy (regression) nếu Y là biến số (thực).

    Nếu biến Y không xác định cụ thể -> việc mô hình hóa là bài toán phân cụm (clustering).
    Chú ý: Phần mô hình hóa dành cho Bài tập theo sau, KHÔNG phải là nội dung của bài thi GK.
2.Thu thập dữ liệu: 
    - TỰ thu thập dữ liệu (tự crawl)
    - Số lượng mẫu: >1000 mẫu, dẫn nguồn dữ liệu và mô tả cách thức thu thập. 
    - Số lượng biến (variable/feature): >= 5 (trừ một số ngoại lệ do nhà cung cấp nội dung cung cấp quá ít dữ liệu mô tả).
    - Xuất ra các thống kê mô tả trực quan về dữ liệu đơn biến đối với một vài biến quan trọng để minh hoạ. 
3.
    Làm sạch và chuẩn hóa dữ liệu (data cleaning): mô tả cách xử lý và trực quan hoá sự thay đổi của phân bố dữ liệu trước và sau xử lý.

    Mã hoá dữ liệu (data encoding) cho dữ liệu danh mục (category) hoặc vector hoá dữ liệu text dùng công cụ xử lý ngôn ngữ tự nhiên (vd: NLTK toolkit).
4.Xây dựng và lựa chọn đặc trưng (feature engineering) (tham khảo: https://phamdinhkhanh.github.io/2019/01/07/Ky_thuat_feature_engineering.html)

5.Trực quan hoá mối quan hệ đa biến (bằng scatter plot, correlation map, distribution plot, lmplot, clustermap,…) để trả lời xem có thể có mối quan hệ tiềm ẩn nào đó giữa các biến trong tập dữ liệu hay ko, hoặc trực quan hoá không gian dữ liệu nhiều chiều (bằng t-SNE,..) để trả lời xem liệu có quan sát được tính chất cụm của tập dữ liệu đầu vào hay ko (https://www.datacamp.com/tutorial/introduction-t-sne).

6.Kết luận (đặt ở cuối của file notebook)::
    Bài toán đặt ra có khả thi (về dữ liệu) hay không. Vì sao?
    Nếu khả thi thì tập các đặc trưng hữu ích có thể dùng để xây dựng mô hình là gì?

7.Tài liệu tham khảo:
    Liệt kê các nguồn tham khảo ý tưởng, mã nguồn,… tại đây
