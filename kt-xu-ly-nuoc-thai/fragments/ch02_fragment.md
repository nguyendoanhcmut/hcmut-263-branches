## Chương 02: Bể Điều hòa (Equalization Tank)

### 1. Tổng quan và Cơ chế Điều hòa Dòng chảy & Tải lượng (Overview and Equalization Principles)
#### 1.1. Dao động lưu lượng và nồng độ chất ô nhiễm trong nước thải (Diurnal Variations in Wastewater)
##### 1.1.1. Bản chất dao động lưu lượng theo chu kỳ ngày đêm (Diurnal Flowrate Fluctuations)
###### 1.1.1.1. Đặc trưng hệ số không điều hòa theo thời gian ($K_{max}$, $K_{min}$)
- Hệ số không điều hòa theo giờ lớn nhất ($K_{h,max} = Q_{max} / Q_{avg}$) phản ánh biên độ đỉnh xung thủy lực, dao động phổ biến từ $1.5$ đến $2.5$ đối với đô thị lớn và có thể vượt $3.0 - 4.5$ đối với các trạm quy mô nhỏ ($Q < 5,000 \text{ m}^3/\text{ngày}$).
- Hệ số không điều hòa giờ nhỏ nhất ($K_{h,min} = Q_{min} / Q_{avg}$) ghi nhận vào rạng sáng (02:00 - 05:00) thường giảm sâu xuống $0.2 - 0.4$, tạo nên khoảng chênh lệch lưu lượng cực hạn lớn gây bất lợi nghiêm trọng cho chế độ thủy lực.
- Đường cong biến thiên lưu lượng 24 giờ (Diurnal Hydrograph Curve) thể hiện hai đỉnh nhọn đặc trưng: đỉnh buổi sáng (07:00 - 10:00) do hoạt động vệ sinh, sinh hoạt cá nhân bắt đầu ngày mới; đỉnh buổi tối (18:00 - 21:00) do nấu nướng và sinh hoạt gia đình.
###### 1.1.1.2. Nguồn gốc phát sinh và tác động của sinh hoạt đô thị và ca sản xuất công nghiệp
- Nước thải sinh hoạt đô thị phản ánh chặt chẽ nhịp sinh học của cư dân: lưu lượng giảm mạnh về đêm khi hoạt động dùng nước ngừng trệ, tăng vọt vào giờ cao điểm sáng và chiều tối.
- Nước thải công nghiệp phát sinh dao động gián đoạn phụ thuộc vào ca sản xuất, chu kỳ xả thải theo mẻ (Batch Discharges) từ các công đoạn súc rửa thiết bị (CIP - Clean In Place), xả đáy nồi hơi, tháo bể ngâm kiềm/axit, tạo ra các xung dòng chảy tức thời cực lớn.
- Dòng nước ngầm thẩm thấu (Infiltration) qua mạng lưới cống rò rỉ và nước mưa chảy tràn (Inflow) xâm nhập qua hố ga vào mùa mưa làm thay đổi đột ngột biên độ dòng chảy đầu vào trạm xử lý.
##### 1.1.2. Biến thiên nồng độ chất ô nhiễm và tải lượng hữu cơ (Constituent Load & Concentration Variations)
###### 1.1.2.1. Quy luật biến thiên đồng thời giữa nồng độ $BOD_5$, COD, TSS và lưu lượng $Q$
- Nồng độ các chất ô nhiễm hữu cơ ($BOD_5$, COD) và chất rắn lơ lửng (TSS) không giữ nguyên mà dao động đồng pha với lưu lượng nước thải.
- Vào các khung giờ lưu lượng đỉnh ($Q_{max}$), nồng độ chất ô nhiễm cũng đạt cực đại do các hoạt động xả thải đậm đặc diễn ra cùng lúc (ví dụ $BOD_5$ thô tăng từ mức nền ban đêm $45 - 60 \text{ mg/L}$ lên đến đỉnh $280 - 305 \text{ mg/L}$).
- Tải lượng ô nhiễm tức thời ($M(t) = Q(t) \cdot C(t)$) có biên độ dao động gấp nhiều lần biên độ lưu lượng đơn thuần, với tỷ số đỉnh trên đáy ($M_{max} / M_{min}$) có thể lên tới $10:1$ đến $25:1$.
###### 1.1.2.2. Hiện tượng sốc tải hữu cơ (Organic Shock Loading) đối với công trình xử lý
- Hiện tượng tăng vọt tải lượng chất nền (Substrate Spike) diễn ra đột ngột khiến tỷ số $F/M$ (Food to Microorganism) trong bể sinh học tăng cao đột biến, vượt ngưỡng chịu đựng sinh lý của bùn hoạt tính.
- Quá tải hữu cơ gây suy giảm oxy hòa tan trầm trọng ($DO \to 0 \text{ mg/L}$), cản trở quá trình nitrat hóa, kích thích vi khuẩn dạng sợi (Filamentous Bacteria) phát triển quá mức dẫn đến phồng bùn (Sludge Bulking).
- Ngược lại, vào ban đêm khi tải lượng giảm sâu, vi sinh vật thiếu cơ chất dinh dưỡng rơi vào pha hô hấp nội bào (Endogenous Respiration), gây hiện tượng tự tiêu sinh khối và làm tan rã bông bùn hữu hiệu.
#### 1.2. Mục đích và chức năng cốt lõi của bể điều hòa (Core Purpose and Functions)
##### 1.2.1. San phẳng xung thủy lực và ổn định lưu lượng (Hydraulic Shock Equalization)
- Lưu trữ lượng nước thải dư thừa trong các khung giờ cao điểm có lưu lượng $Q_{in} > Q_{avg}$ và bổ sung xả bù vào các khung giờ thấp điểm khi $Q_{in} < Q_{avg}$.
- Chuyển đổi dòng vào có lưu lượng biến thiên hỗn loạn $Q_{in}(t)$ thành dòng ra có lưu lượng không đổi hoặc biến thiên trơn tru theo lưu lượng trung bình thiết kế $Q_{out} \approx Q_{avg}$.
- Ngăn ngừa hiện tượng tràn bờ, ngập lụt cục bộ hoặc quá tải vận tốc dòng chảy qua các công trình lắng, lọc hạ nguồn.
##### 1.2.2. Làm đều nồng độ chất ô nhiễm và tải lượng khối lượng (Constituent Mass Load Dampening)
- Khuấy trộn liên tục khối nước thải lưu trữ với các mẻ nước thải mới tiếp nhận nhằm triệt tiêu các đỉnh nồng độ cao (Spikes) và hòa loãng các thung lũng nồng độ thấp (Troughs).
- Cung cấp dòng thải có nồng độ chất ô nhiễm $C_{out}(t)$ ổn định quanh giá trị trung bình gia quyền lưu lượng ($C_{avg}$), triệt tiêu hoàn toàn hiện tượng sốc tải hữu cơ cho các bể sinh học.
- Đảm bảo thời gian lưu bùn (SRT), thời gian lưu nước (HRT) và tải trọng thể tích ($L_V$) của các bể vi sinh phía sau luôn duy trì ở điểm làm việc tối ưu.
##### 1.2.3. Trung hòa sơ bộ pH và pha loãng các dòng thải độc hại (pH Neutralization & Toxic Dilution)
- Tận dụng phản ứng tự trung hòa giữa các dòng thải có tính axit xả ra vào các thời điểm khác nhau với dòng thải có tính kiềm xả ra trong chu kỳ ngày.
- Giảm thiểu nhu cầu châm hóa chất axit hoặc xút ngoại lai tại cụm trung hòa hóa lý, tiết kiệm đáng kể chi phí vận hành.
- Hòa loãng nhanh chóng các xung chất ức chế độc hại đối với vi sinh vật (như kim loại nặng, chất hoạt động bề mặt, clo dư, formaldehyde hoặc hóa chất tẩy rửa công nghiệp) xuống dưới ngưỡng nồng độ giới hạn gây độc.
#### 1.3. Lợi ích kỹ thuật và kinh tế của bể điều hòa (Engineering & Economic Benefits)
##### 1.3.1. Cải thiện hiệu suất và độ ổn định của các công trình sinh học hạ nguồn (Biological Process Protection)
###### 1.3.1.1. Giữ ổn định tỷ số thức ăn trên vi sinh vật ($F/M$) và nồng độ bùn hoạt tính ($MLSS$)
- Tỷ số $F/M$ duy trì trong dải kiểm soát tối ưu (ví dụ $0.2 - 0.4 \text{ kg } BOD_5 / (\text{kg } MLVSS \cdot \text{ngày})$ đối với bùn hoạt tính truyền thống), ngăn ngừa hiện tượng quá tải tải trọng hữu cơ hoặc thiếu đói cơ chất.
- Tốc độ sinh trưởng vi sinh vật ổn định giúp bùn hoạt tính tạo bông tốt, giảm hàm lượng sinh khối trôi ra theo nước sau lắng.
###### 1.3.1.2. Ổn định nhu cầu cung cấp oxy hòa tan ($DO$) và ngăn ngừa hiện tượng bùn nổi/phồng (Sludge Bulking)
- Đường cong tiêu thụ oxy ($OUR$ - Oxygen Uptake Rate) được san phẳng, loại bỏ nhu cầu quạt gió phải đáp ứng các đỉnh tiêu thụ oxy đột biến vượt quá công suất thiết kế.
- Kiểm soát ổn định nồng độ $DO$ bể hiếu khí trong dải $2.0 - 2.5 \text{ mg/L}$, ngăn chặn sự sinh sôi của vi khuẩn dạng sợi (như *Sphaerotilus natans*, *Type 021N*) vốn thường bùng phát khi $DO$ giảm thấp do sốc tải hữu cơ.
- Ổn định chỉ số thể tích bùn ($SVI \le 100 - 120 \text{ mL/g}$), đảm bảo bùn lắng nhanh và kết khối chặt chẽ trong bể lắng đợt 2.
##### 1.3.2. Nâng cao hiệu quả quá trình hóa lý và kiểm soát châm hóa chất (Chemical Treatment & Coagulation Control)
###### 1.3.2.1. Giảm thiểu dao động pH và tiết kiệm hóa chất điều chỉnh ($H_2SO_4$, $NaOH$, vôi)
- Biên độ dao động pH nước cấp đầu vào qua bể điều hòa giảm từ dải rộng ($5.0 - 9.5$) về dải hẹp ($6.8 - 7.5$), giúp hệ thống tự động hóa điều khiển pH bằng bộ điều khiển PID hoạt động ổn định, loại trừ hiện tượng trễ dao động quá mức (Overshooting/Hunting).
- Giảm thiểu lượng hóa chất tiêu tốn lên đến $30 - 50\%$ so với châm trực tiếp trên dòng chảy biến thiên tức thời.
###### 1.3.2.2. Kiểm soát chính xác liều lượng chất keo tụ và trợ keo tụ
- Hệ thống bơm định lượng phèn nhôm, phèn sắt ($FeCl_3$, $PAC$) và polymer ($PAM$) vận hành theo tỷ lệ dòng chảy cố định hoặc tín hiệu đo nồng độ ổn định, đạt hiệu suất keo tụ - tạo bông cao nhất.
- Tránh hiện tượng châm thiếu hóa chất gây đục dòng ra lúc đỉnh tải hoặc châm thừa hóa chất gây lãng phí và cản trở lắng lúc đáy tải.
##### 1.3.3. Tối ưu hóa kích thước và chi phí đầu tư các công trình đơn vị tiếp theo (Downstream Footprint & Capex Reduction)
###### 1.3.3.1. Giảm diện tích mặt thoáng và đường kính bể lắng đợt 1, đợt 2 (Clarifier Area Sizing)
- Bể lắng đợt 1 và đợt 2 chỉ cần định kích thước theo lưu lượng trung bình ổn định $Q_{avg}$ thay vì phải thiết kế theo lưu lượng đỉnh tức thời $Q_{max} = K_{max} \cdot Q_{avg}$.
- Tải trọng bề mặt (Surface Overflow Rate - $SOR$) và tải trọng chất rắn (Solids Loading Rate - $SLR$) không bị vượt ngưỡng cho phép, cho phép giảm diện tích xây dựng bể lắng từ $25 - 40\%$.
###### 1.3.3.2. Tối ưu hóa diện tích bề mặt bể lọc và chu kỳ rửa lọc (Filtration Sizing & Backwash Frequency)
- Giảm số lượng ngăn bể lọc cát nhanh hoặc mô-đun lọc đĩa/màng do tốc độ lọc thiết kế ($v_{filter}$) duy trì hằng định.
- Tốc độ tích tụ cặn đồng đều kéo dài chu kỳ lọc giữa hai lần rửa lọc, giảm tỷ lệ nước dùng cho rửa ngược tự thân của trạm xử lý.
#### 1.4. Nhược điểm và thách thức vận hành (Drawbacks and Operational Challenges)
##### 1.4.1. Yêu cầu diện tích mặt bằng xây dựng lớn (Land Footprint Requirement)
- Bể điều hòa đòi hỏi thể tích lưu trữ tương đương $15 - 30\%$ tổng lưu lượng ngày của trạm, chiếm tỷ trọng lớn trong tổng diện tích chiếm đất của toàn bộ nhà máy xử lý nước thải.
- Khó khăn trong việc bố trí tại các khu vực đô thị chật hẹp hoặc các nhà máy công nghiệp có quỹ đất hạn chế.
##### 1.4.2. Gia tăng chi phí đầu tư thiết bị cơ điện và năng lượng tiêu thụ (Capex & Energy Demand)
- Đòi hỏi vốn đầu tư ban đầu bổ sung đáng kể cho kết cấu bê tông/hồ lót màng HDPE, hệ thống máy khuấy chìm, máy thổi khí chuyên dụng, dàn ống đĩa phân phối khí, trạm bơm nước thải và thiết bị đo mức liên tục.
- Tiêu hao điện năng thường xuyên 24/24 giờ để vận hành động cơ máy khuấy chìm và máy thổi khí nhằm duy trì cặn lơ lửng và chống bốc mùi.
##### 1.4.3. Nguy cơ phân hủy yếm khí gây mùi hôi thối ($H_2S$, mercaptans) khi thiếu sục khí
- Nước thải sinh hoạt và công nghiệp hữu cơ lưu lại trong bể trong điều kiện tĩnh hoặc thiếu hụt oxy sẽ nhanh chóng chuyển sang pha yếm khí (Septic Conditions).
- Vi khuẩn khử sunfat phân hủy các hợp chất chứa lưu huỳnh tạo thành khí hydro sunfua ($H_2S$), mercaptans và axit hữu cơ bay hơi có mùi trứng thối nồng nặc, gây ô nhiễm môi trường không khí xung quanh và ăn mòn công trình bê tông cốt thép.
##### 1.4.4. Hiện tượng lắng cặn đáy bể khi khuấy trộn không đạt vận tốc tới hạn
- Nếu công suất khuấy cơ học hoặc cường độ sục khí không đạt giá trị thiết kế ($< 0.004 \text{ kW/m}^3$), cặn lơ lửng, cát mịn và bùn hữu cơ sẽ lắng đọng tạo thành lớp bùn đáy dày đặc tại các góc chết.
- Cặn tích tụ lâu ngày làm giảm dần thể tích hữu ích của bể, gây tắc nghẽn cửa hút bơm nước thải và phát sinh mùi hôi cục bộ khi bùn đáy phân hủy kỵ khí.

---

### 2. Phân loại Cấu hình Bể Điều hòa (Configuration Modes: In-Line vs. Off-Line)
#### 2.1. Cấu hình nối tiếp (In-Line Equalization)
##### 2.1.1. Sơ đồ công nghệ và nguyên lý thủy lực (Process Flowsheet & Hydraulic Principle)
- Toàn bộ lưu lượng nước thải đầu vào trạm xử lý $Q_{in}(t)$ bắt buộc phải đi trực tiếp qua bể điều hòa trước khi chảy vào các công trình xử lý phía sau:
  $$\text{Dòng vào } Q_{in}(t) \longrightarrow \boxed{\text{Bể Điều hòa In-Line}} \overset{Q_{out} \approx Q_{avg}}{\xrightarrow{\hspace{1.5cm}}} \text{Các công trình đơn vị hạ nguồn}$$
- Mức nước trong bể điều hòa biến thiên liên tục từ mức thấp nhất ($H_{min}$) vào thời điểm tích lũy thiếu hụt cực đại đến mức cao nhất ($H_{max}$) vào thời điểm tích lũy dư thừa cực đại.
- Dòng ra được duy trì hằng định thông qua trạm bơm biến tần hoặc hệ thống van tiết lưu tự động kết hợp đập tràn điều chỉnh mức.
##### 2.1.2. Khả năng điều hòa đồng thời lưu lượng và nồng độ (Simultaneous Flow & Mass Dampening)
- Do toàn bộ thể tích nước thải đều lưu lại và được xáo trộn hoàn toàn trong một không gian bể, cấu hình In-Line đạt hiệu quả tối ưu trong việc làm phẳng đồng thời cả lưu lượng thủy lực lẫn nồng độ chất ô nhiễm ($BOD_5$, COD, TSS, $N$, $P$).
- Biên độ nồng độ chất ô nhiễm dòng ra giảm mạnh nhất, tạo dòng cơ chất ổn định lý tưởng cho vi sinh vật trong hệ thống xử lý sinh học.
##### 2.1.3. Đánh giá ưu điểm, nhược điểm và phạm vi áp dụng (Pros, Cons & Application Range)
- **Ưu điểm**: Hiệu quả đệm tải lượng và làm đều nồng độ toàn diện nhất; sơ đồ công nghệ rõ ràng, dễ vận hành điều khiển dòng ra; bảo vệ tuyệt đối các công trình hạ nguồn khỏi mọi xung tải đột ngột.
- **Nhược điểm**: Toàn bộ lưu lượng nước thải đều phải được bơm cưỡng bức từ bể điều hòa lên các công trình phía sau, đòi hỏi công suất trạm bơm lớn và tiêu hao điện năng bơm nâng cao; thể tích bể yêu cầu lớn nhất.
- **Phạm vi áp dụng**: Áp dụng bắt buộc cho các trạm xử lý nước thải sinh hoạt đô thị và công nghiệp có dao động nồng độ chất ô nhiễm lớn, yêu cầu bảo vệ nghiêm ngặt hệ thống xử lý sinh học hiếu khí/thiếu khí.
#### 2.2. Cấu hình song song / Rẽ nhánh (Off-Line / Side-Stream Equalization)
##### 2.2.1. Sơ đồ công nghệ và cơ chế tách dòng vượt đỉnh (Peak Shaving & Split Flow)
- Chỉ phần lưu lượng nước thải vượt quá lưu lượng trung bình ($Q_{in}(t) - Q_{avg} > 0$) mới được chuyển nhánh (bằng đập tràn bên hoặc bơm chuyển dòng) đưa vào bể điều hòa Off-Line để lưu trữ tạm thời:
  $$\text{Dòng vào } Q_{in}(t) \longrightarrow \begin{cases} Q_{direct} \le Q_{avg} \longrightarrow \text{Công trình hạ nguồn} \\ Q_{excess} = Q_{in}(t) - Q_{avg} \longrightarrow \boxed{\text{Bể Điều hòa Off-Line}} \xrightarrow{Q_{return}} \text{Nhập dòng trở lại khi } Q_{in} < Q_{avg} \end{cases}$$
- Khi lưu lượng đầu vào giảm xuống dưới mức trung bình ($Q_{in}(t) < Q_{avg}$), nước thải tích trữ trong bể Off-Line được bơm hoàn lưu ngược trở lại tuyến xử lý chính để bổ sung cho đủ công suất $Q_{avg}$.
##### 2.2.2. Đặc điểm điều hòa lưu lượng và hạn chế trong làm đều nồng độ (Flow Balancing vs. Load Fluctuations)
- Cấu hình Off-Line làm đều lưu lượng thủy lực rất hiệu quả (cắt gọt đỉnh xung thủy lực - Peak Shaving), đảm bảo lưu lượng vào công trình sau không vượt quá $Q_{avg}$.
- **Hạn chế lớn**: Hiệu quả làm đều nồng độ chất ô nhiễm kém hơn đáng kể so với In-Line, vì dòng nước thải chảy thẳng trong giờ thấp điểm (nồng độ loãng) không được hòa trộn với khối nước thải đậm đặc đã tích trữ từ giờ cao điểm. Các xung nồng độ chất ô nhiễm vẫn có thể truyền qua hệ thống xử lý chính.
##### 2.2.3. Giảm chi phí bơm và năng lượng khuấy trộn (Energy & Pumping Optimization)
- Chỉ phải bơm một phần lưu lượng nước thải (chỉ phần nước vượt đỉnh và xả bù, chiếm khoảng $20 - 40\%$ tổng lưu lượng ngày), trong khi phần lớn dòng chảy tự chảy thẳng vào các bể lắng/bể sinh học.
- Tiết kiệm đáng kể điện năng bơm vận hành hàng ngày và chi phí năng lượng khuấy trộn do thể tích bể làm việc thực tế nhỏ hơn.
#### 2.3. Bảng so sánh toàn diện giữa cấu hình In-Line và Off-Line (Comprehensive Comparative Analysis)

| Tiêu chí So sánh | Cấu hình Nối tiếp (In-Line) | Cấu hình Rẽ nhánh (Off-Line) |
|---|---|---|
| **Vị trí bố trí** | Nằm trực tiếp trên trục dòng chảy chính của trạm xử lý | Nằm độc lập trên nhánh rẽ song song với tuyến xử lý chính |
| **Dòng chảy qua bể** | $100\%$ tổng lưu lượng nước thải ngày ($V_{total}$) | Chỉ phần lưu lượng vượt đỉnh ($Q_{in} > Q_{avg}$) |
| **Khả năng làm phẳng lưu lượng** | Tuyệt vời (Duy trì dòng ra cố định $Q_{out} \approx Q_{avg}$) | Rất tốt (Cắt gọt đỉnh lũy kế $Q \le Q_{avg}$) |
| **Khả năng làm đều nồng độ ô nhiễm** | Tối đa (Khuấy trộn toàn bộ thể tích nước thải 24h) | Trung bình - Kém (Dòng nền không được xáo trộn với dòng đỉnh) |
| **Khả năng pha loãng chất độc hại** | Rất cao, triệt tiêu xung độc tức thời | Thấp đối với dòng chảy trực tiếp |
| **Năng lượng bơm nước thải** | Cao (Bắt buộc bơm toàn bộ $100\%$ lưu lượng lên bể sau) | Thấp (Chỉ bơm phần nước thải hồi lưu $20 - 40\%$ thể tích) |
| **Năng lượng khuấy trộn/sục khí** | Lớn (Do thể tích bể lớn và vận hành liên tục 24/24) | Nhỏ hơn (Có thể ngắt hoặc giảm khuấy khi bể cạn) |
| **Vận hành và điều khiển** | Đơn giản, tự động điều khiển theo mức nước | Phức tạp hơn (Cần kiểm soát van điều tiết dòng rẽ và bơm bù) |
| **Khuyến nghị áp dụng** | Xử lý nước thải sinh hoạt và công nghiệp có sốc tải lớn | Mạng lưới thoát nước chung, trạm xử lý quy mô cực lớn cần tiết kiệm điện bơm |

---

### 3. Phương pháp Xác định Dung tích Bể Điều hòa (Equalization Tank Sizing Methodology)
#### 3.1. Phương pháp biểu đồ tích lũy khối lượng Rippl (Rippl Mass Diagram Method)
##### 3.1.1. Cơ sở lý thuyết và phương trình cân bằng khối lượng liên tục (Mass Balance Formulation)
###### 3.1.1.1. Phương trình vi phân tích phân và cân bằng thể tích vi mô
- Xét phương trình bảo toàn khối lượng liên tục đối với thể tích chất lỏng trong bể điều hòa tại thời điểm $t$:
  $$\frac{dV(t)}{dt} = Q_{in}(t) - Q_{out}(t)$$
- Tích phân hai vế từ thời điểm ban đầu $t_0 = 0$ đến thời điểm $t$:
  $$V(t) - V(0) = \int_{0}^{t} Q_{in}(\tau) d\tau - \int_{0}^{t} Q_{out}(\tau) d\tau$$
- Để lưu lượng xả ra sau điều hòa là hằng số không đổi triệt để trong chu kỳ 24 giờ ($T = 24 \text{ h}$), lưu lượng xả ra thiết kế bắt buộc phải bằng lưu lượng trung bình ngày:
  $$Q_{out}(t) = Q_{avg} = \frac{1}{T} \int_{0}^{T} Q_{in}(\tau) d\tau = \frac{V_{total}}{T}$$
###### 3.1.1.2. Phương trình dạng rời rạc theo chuỗi thời gian 24 giờ (`eq_ch02_01`)
- Trong thực tế tính toán kỹ thuật môi trường, chuỗi số liệu đo đạc lưu lượng được ghi nhận theo từng khoảng thời gian rời rạc $\Delta t = 1 \text{ giờ}$ ($i = 1, 2, \dots, 24$).
- Tổng thể tích nước thải ngày $V_{total}$ ($\text{m}^3/\text{ngày}$) và lưu lượng trung bình giờ $Q_{avg}$ ($\text{m}^3/\text{h}$):
  $$V_{total} = \sum_{i=1}^{24} Q_{in,i} \cdot \Delta t$$
  $$Q_{avg} = \frac{V_{total}}{24} = \frac{\sum_{i=1}^{24} Q_{in,i} \cdot \Delta t}{24}$$
- Độ chênh lệch thể tích tích lũy tại giờ thứ $t$ ($\Delta V(t)$, tính bằng $\text{m}^3$):
  $$\Delta V(t) = \sum_{i=1}^{t} (Q_{in,i} - Q_{avg}) \cdot \Delta t = \sum_{i=1}^{t} Q_{in,i} \cdot \Delta t - Q_{avg} \cdot t$$
- Dung tích hữu ích lý thuyết yêu cầu của bể điều hòa ($V_{theoretical}$, tính bằng $\text{m}^3$):
  $$V_{theoretical} = \max_{1 \le t \le 24}(\Delta V(t)) - \min_{1 \le t \le 24}(\Delta V(t))$$
##### 3.1.2. Quy trình lập biểu đồ đường tích lũy lưu lượng vào và ra (Cumulative Flow Curves)
###### 3.1.2.1. Đường cong tích lũy dòng vào $\sum V_{in}(t)$
- Trục hoành ($X$): Thời gian trong ngày từ 0 đến 24 giờ (bắt đầu từ 00:00).
- Trục tung ($Y$): Thể tích tích lũy ($\text{m}^3$).
- Đồ thị $\sum V_{in}(t) = \sum_{i=1}^t Q_{in,i} \cdot \Delta t$ là một đường cong bậc thang hoặc đường cong chữ S uốn lượn liên tục, có độ dốc thay đổi theo từng giờ: độ dốc thoải vào rạng sáng (lưu lượng nhỏ) và độ dốc dốc đứng vào các giờ cao điểm trưa và tối.
###### 3.1.2.2. Đường thẳng tích lũy dòng ra với lưu lượng trung bình cố định $\sum V_{out}(t) = Q_{avg} \cdot t$
- Biểu diễn tổng lượng nước thải tháo ra khỏi bể theo thời gian với giả định lưu lượng xả không đổi $Q_{out} = Q_{avg}$.
- Đồ thị là một đường thẳng tắp nối từ gốc tọa độ $(0, 0)$ đến điểm cuối ngày $(24, V_{total})$.
##### 3.1.3. Phương pháp tiếp tuyến song song đồ họa (Graphical Parallel Tangent Method)
###### 3.1.3.1. Điểm tiếp tuyến trên (Maximum Cumulative Surplus)
- Kẻ một đường thẳng song song với đường thẳng tích lũy dòng ra ($Q_{avg}$) và tiếp xúc với điểm uốn lượn nhô cao nhất phía trên của đường cong tích lũy dòng vào.
- Điểm tiếp xúc này tương ứng với thời điểm bể tích lũy lượng nước thặng dư cực đại ($\max \Delta V$).
###### 3.1.3.2. Điểm tiếp tuyến dưới (Maximum Cumulative Deficit)
- Kẻ đường thẳng thứ hai song song với đường $Q_{avg}$ và tiếp xúc với điểm uốn võng sâu nhất phía dưới của đường cong tích lũy dòng vào.
- Điểm tiếp xúc này phản ánh thời điểm bể cạn kiệt nhất, tức mức tích lũy thiếu hụt sâu nhất ($\min \Delta V$).
###### 3.1.3.3. Xác định dung tích hữu ích lý thuyết $V_{theoretical} = \max(\Delta V) - \min(\Delta V)$
- Khoảng cách thẳng đứng đo theo trục tung giữa hai đường tiếp tuyến song song chính là giá trị dung tích lưu trữ lý thuyết cần thiết $V_{theoretical}$.
- Đảm bảo bể không bao giờ bị tràn nước khi đầy nhất và không bị cạn đáy khi lưu lượng vào nhỏ nhất.
##### 3.1.4. Phương pháp bảng tính số học từng bước (Tabular Step-by-Step Calculation)
- Lập bảng tính 24 hàng đại diện cho 24 giờ trong ngày.
- Cột 1: Khoảng thời gian ($i$).
- Cột 2: Lưu lượng dòng vào từng giờ ($Q_{in,i}$, $\text{m}^3/\text{h}$).
- Cột 3: Thể tích dòng vào từng giờ ($V_{in,i} = Q_{in,i} \cdot 1\text{ h}$, $\text{m}^3$).
- Cột 4: Thể tích vào tích lũy ($\sum V_{in,i} = \sum_{k=1}^i V_{in,k}$, $\text{m}^3$).
- Cột 5: Thể tích ra tích lũy theo lưu lượng bình quân ($\sum V_{out,i} = Q_{avg} \cdot i$, $\text{m}^3$).
- Cột 6: Độ chênh lệch thể tích tích lũy ($\Delta V_i = \text{Cột 4} - \text{Cột 5}$, $\text{m}^3$).
- Tra bảng tìm giá trị lớn nhất ($\max \Delta V$) và giá trị nhỏ nhất ($\min \Delta V$).
- Hiệu số giữa hai giá trị cực trị chính là dung tích lý thuyết $V_{theoretical}$.
#### 3.2. Xác định dung tích thực tế và các hệ số an toàn (Practical Design Volume Considerations)
##### 3.2.1. Phương trình xác định dung tích thực tế (`eq_ch02_02`)
- Dung tích thực tế của bể điều hòa ($V_{practical}$, tính bằng $\text{m}^3$) được xác định bằng cách nhân dung tích lý thuyết với hệ số an toàn thực tế:
  $$V_{practical} = (1.1 \text{ đến } 1.2) \times V_{theoretical}$$
  $$V_{practical} = f_{safety} \cdot V_{theoretical} \quad \text{với } f_{safety} \in [1.10, 1.20]$$
##### 3.2.2. Hệ số an toàn thiết kế $f_{safety} = 1.1 - 1.2$ và các nguyên nhân kỹ thuật
###### 3.2.2.1. Dung tích chiếm chỗ của thiết bị sục khí, máy khuấy chìm và hệ thống phân phối khí
- Hệ thống đường ống cấp khí nhánh, đĩa màng phân phối khí, thanh giá đỡ, bệ đỡ máy khuấy chìm và thân máy bơm ngập nước chiếm chỗ một phần thể tích hữu ích trong lòng bể.
- Cần bù trừ $2 - 3\%$ thể tích cho phần dung tích choán chỗ cơ học này.
###### 3.2.2.2. Dung tích dự phòng cho các dòng hồi lưu nội bộ (Sludge Dewatering Filtrate, Filter Backwash)
- Trong quá trình vận hành trạm xử lý, các dòng nước thải nội bộ định kỳ được bơm tuần hoàn ngược về bể điều hòa:
  - Nước sau tách bùn từ máy ép bùn ly tâm, máy ép bùn băng tải hoặc máy ép bùn trục vít (Centrate / Filtrate) có nồng độ chất ô nhiễm và lưu lượng xung rất cao.
  - Nước rửa ngược từ bể lọc cát nhanh hoặc các thiết bị lọc màng hạ nguồn.
  - Dòng xả đáy từ thiết bị rửa cát hoặc hố thu nước vệ sinh khuôn viên trạm.
- Dự phòng lưu trữ cho các dòng hồi lưu này đòi hỏi hệ số an toàn bổ sung từ $5 - 10\%$.
###### 3.2.2.3. Dự phòng cho hiện tượng thấm, bốc hơi và đột biến lưu lượng mưa bất ngờ
- Tránh hiện tượng tràn bể khi xuất hiện các trận mưa bão cục bộ làm lưu lượng vượt quá số liệu khảo sát trung bình mùa khô ($3 - 5\%$).
##### 3.2.3. Dung tích chết và mức nước vận hành tối thiểu ($H_{min} \ge 1.5\text{ m}$)
###### 3.2.3.1. Độ ngập tối thiểu của đĩa phân phối khí để duy trì hiệu suất truyền oxy (OTE)
- Chiều sâu mức nước tối thiểu trong bể điều hòa không được phép hạ thấp dưới $1.5 \text{ m}$ ($H_{min} \ge 1.5 \text{ m}$):
  - Khi cột nước nông ($< 1.5 \text{ m}$), thời gian bọt khí tiếp xúc với nước quá ngắn, làm hiệu suất chuyển hóa oxy hòa tan ($OTE$ - Oxygen Transfer Efficiency) suy giảm nghiêm trọng.
  - Áp suất ngược của cột nước lên đĩa phân phối khí thay đổi thất thường gây rung giật màng đĩa khí.
###### 3.2.3.2. Độ ngập tối thiểu của cánh khuấy chìm chống tạo phễu xoáy (Vortexing) và xâm thực (Cavitation)
- Để máy khuấy chìm hoạt động ổn định, đỉnh cánh khuấy phải ngập sâu dưới mặt nước tự do ít nhất $0.8 - 1.0 \text{ m}$.
- Nếu mực nước tụt xuống sát cánh khuấy, dòng xoáy bề mặt sẽ cuốn không khí vào cánh khuấy tạo phễu xoáy (Vortex), gây ra hiện tượng xâm thực cơ học, rung lắc dữ dội và cháy động cơ chìm.
- Thể tích nước ứng với chiều sâu từ đáy bể đến mức nước tối thiểu $H_{min}$ chính là thể tích đệm tĩnh (Dead Volume / Minimum Liquid Heel):
  $$V_{dead} = A_{tank} \cdot H_{min}$$
##### 3.2.4. Chiều cao bảo vệ mặt thoáng (Freeboard) và dung tích đỉnh tràn khẩn cấp
- Chiều cao an toàn mặt thoáng ($H_{freeboard}$) quy định từ $0.5$ đến $0.8 \text{ m}$ tính từ mức nước dâng cao nhất ($H_{max}$) đến đỉnh thành tường bể bê tông.
- Chiều cao này ngăn chặn hiện tượng bọt khí và sóng nước bắn tóe ra ngoài khi dàn sục khí hoạt động mạnh, đồng thời dự phòng một khoảng dung tích an toàn chống tràn trước khi nước dâng chạm ngưỡng đập tràn khẩn cấp (Emergency Overflow Weir).

---

### 4. Thiết kế Hệ thống Khuấy trộn và Sục khí (Mixing and Aeration System Design)
#### 4.1. Hệ thống khuấy trộn cơ học chìm (Submersible Mechanical Mixing)
##### 4.1.1. Mục đích: Duy trì trạng thái lơ lửng của cặn rắn ($SS \approx 200\text{ mg/L}$)
- Giữ cho toàn bộ hàm lượng cặn lơ lửng trong nước thải đầu vào ($SS \approx 200 \text{ mg/L}$) luôn ở trạng thái lơ lửng thủy động học đồng nhất, ngăn chặn tuyệt đối sự sa lắng hình thành bùn đáy.
- Tạo vận tốc dòng chảy tuần hoàn trong bể đạt vận tốc tới hạn chống lắng ($v \ge 0.15 - 0.30 \text{ m/s}$) tại mọi vị trí trên sàn đáy bể.
##### 4.1.2. Phương trình công suất khuấy cơ học (`eq_ch02_05`)
###### 4.1.2.1. Chỉ tiêu suất công suất khuấy: $p_{unit} = 0.004 - 0.008\text{ kW/m}^3$ ($4 - 8\text{ W/m}^3$)
- Đối với nước thải sinh hoạt thông thường có hàm lượng $SS \approx 200 \text{ mg/L}$, định mức công suất khuấy trộn cơ học đơn vị tiêu chuẩn theo giáo trình và TCVN 7957:2008 là:
  $$p_{unit} = 0.004 \text{ đến } 0.008 \text{ kW/m}^3 \quad (4 \text{ đến } 8 \text{ W/m}^3 \text{ thể tích bể})$$
- Trường hợp nước thải công nghiệp có nồng độ chất rắn lơ lửng cao ($SS > 500 - 1,000 \text{ mg/L}$) hoặc chứa sợi dệt nhuộm, bột giấy, suất công suất khuấy cần nâng lên $0.010 - 0.015 \text{ kW/m}^3$ ($10 - 15 \text{ W/m}^3$).
###### 4.1.2.2. Tính toán tổng công suất lắp đặt $P_{mix} = p_{unit} \cdot V_{tank}$
- Tổng công suất cơ học yêu cầu ($P_{mix}$, tính bằng $\text{kW}$):
  $$P_{mix} = p_{unit} \times V_{tank}$$
- Với:
  - $p_{unit}$: Suất tiêu hao công suất khuấy trên một đơn vị thể tích ($0.004 - 0.008 \text{ kW/m}^3$).
  - $V_{tank}$: Tổng dung tích hình học làm việc của bể điều hòa ($\text{m}^3$).
  - Tổng công suất động cơ điện thực tế lắp đặt cần tính thêm hệ số dự phòng quá tải động cơ ($f_m = 1.15 - 1.25$) và hiệu suất truyền động.
##### 4.1.3. Đặc tính thủy lực và bố trí cánh khuấy chìm (Hydraulic Pattern & Mixer Placement)
###### 4.1.3.1. Cấu tạo máy khuấy chìm: cánh khuấy 2 lá hoặc 3 lá biên dạng thủy lực, động cơ kín nước IP68
- Cánh khuấy đúc bằng thép không gỉ SUS304/SUS316 hoặc vật liệu composite cốt sợi thủy tinh siêu bền, biên dạng thủy lực tự làm sạch (Self-cleaning Profile) chống rác sợi quấn kẹt.
- Động cơ chìm cách điện cấp H, cấp bảo vệ chống nước IP68, tích hợp cảm biến nhiệt bảo vệ cuộn dây và cảm biến rò rỉ độ ẩm buồng dầu.
###### 4.1.3.2. Hệ thống thanh trượt dẫn hướng (Guide Rail/Mast) và cần cẩu xoay (Davit Crane)
- Máy khuấy được lắp đặt trên hệ cột dẫn hướng thẳng đứng bằng thép không gỉ SUS304 (tiết diện hộp vuông hoặc ống tròn).
- Cơ cấu gá trượt (Sliding Shoe) cho phép hạ máy khuấy xuống vị trí làm việc sát đáy hoặc kéo nâng lên mặt sàn bể bằng tời cáp cơ khí/cần cẩu Davit xoay mà không cần phải xả cạn nước bể khi bảo trì bảo dưỡng.
###### 4.1.3.3. Định vị góc quay và hướng dòng chảy chống vùng chết ở các góc bể
- Máy khuấy được đặt ở độ cao cách đáy bể từ $0.5$ đến $0.8 \text{ m}$ và xoay lệch một góc nghiêng $\alpha = 15^\circ - 45^\circ$ so với thành tường dọc.
- Bố trí góc nghiêng tạo ra dòng đối lưu xoáy cuộn tuần hoàn dọc theo chu vi bể, quét sạch cặn lắng tại các góc chết và hướng dòng nước tuần hoàn liên tục về phía hố thu bơm.
#### 4.2. Hệ thống sục khí phân phối bọt khí (Diffused Air Aeration System)
##### 4.2.1. Cơ chế ngăn ngừa hiện tượng phân hủy yếm khí và khử mùi ($H_2S$)
- Cung cấp oxy hòa tan liên tục vào khối chất lỏng nhằm duy trì thế oxy hóa khử dương ($ORP > +50 \text{ mV}$), ức chế hoàn toàn hoạt động của vi khuẩn khử sunfat kỵ khí bắt buộc (*Desulfovibrio*).
- Ngăn chặn phản ứng sinh khí $H_2S$ theo cơ chế:
  $$\text{Chất hữu cơ} + SO_4^{2-} \xrightarrow{\text{Vi khuẩn kỵ khí}} S^{2-} + CO_2 + H_2O \xrightarrow{H^+} H_2S \uparrow \quad (\text{Bị triệt tiêu khi có } DO)$$
- Duy trì nồng độ oxy hòa tan dư tối thiểu $DO \ge 0.5 - 1.0 \text{ mg/L}$ trong suốt quá trình lưu giữ nước thải.
##### 4.2.2. Cường độ cấp khí duy trì điều kiện hiếu khí (Aerobic Condition Requirement)
###### 4.2.2.1. Suất cấp khí theo thể tích: $q_{unit,min} = 0.01 - 0.015\text{ m}^3\text{ khí}/(\text{m}^3\text{ bể}\cdot\text{phút})$
- Để kiểm soát mùi và duy trì điều kiện hiếu khí cơ bản, suất cấp khí tối thiểu đơn vị tính theo phút là:
  $$q_{unit,min} = 0.01 \text{ đến } 0.015 \text{ m}^3 \text{ khí} / (\text{m}^3 \text{ bể} \cdot \text{phút})$$
###### 4.2.2.2. Quy đổi sang lưu lượng theo giờ: $q_{unit,hr} = 0.6 - 0.9\text{ m}^3\text{ khí}/(\text{m}^3\text{ bể}\cdot\text{giờ})$
- Chuyển đổi sang đơn vị giờ:
  $$q_{unit,hr} = q_{unit,min} \times 60 = 0.01 \times 60 \text{ đến } 0.015 \times 60 = 0.60 \text{ đến } 0.90 \text{ m}^3 \text{ khí} / (\text{m}^3 \text{ bể} \cdot \text{giờ})$$
- Lưu lượng quạt gió yêu cầu cho chế độ sục khí hiếu khí chống mùi ($Q_{air,aerobic}$, tính bằng $\text{m}^3/\text{h}$):
  $$Q_{air,aerobic} = q_{unit,min} \times V_{tank} \times 60 = (0.60 \text{ đến } 0.90) \times V_{tank}$$
##### 4.2.3. Cường độ cấp khí kết hợp hiếu khí và khuấy trộn hoàn toàn (Aerobic + Complete Mixing Requirement)
###### 4.2.3.1. Suất cấp khí hỗn hợp: $q_{unit,hr} = 1.8 - 2.9\text{ m}^3\text{ khí}/(\text{m}^3\text{ bể}\cdot\text{giờ})$ (`eq_ch02_06`)
- Khi sử dụng hệ thống phân phối khí làm phương tiện duy nhất đảm nhiệm cả hai chức năng: vừa cung cấp oxy hòa tan chống phân hủy yếm khí, vừa tạo động lực xáo trộn hoàn toàn chống sa lắng cặn mà không dùng máy khuấy chìm, suất cấp khí bắt buộc phải tăng cao:
  $$q_{unit,hr} = 1.8 \text{ đến } 2.9 \text{ m}^3 \text{ khí} / (\text{m}^3 \text{ bể} \cdot \text{giờ})$$
  $$\left( \text{tương đương } 0.030 \text{ đến } 0.0483 \text{ m}^3 \text{ khí} / (\text{m}^3 \text{ bể} \cdot \text{phút}) \right)$$
- Phương trình tính toán tổng lưu lượng khí cấp của máy thổi khí (`eq_ch02_06`):
  $$Q_{air,mix} = q_{unit,hr} \times V_{tank} = (1.8 \text{ đến } 2.9) \times V_{tank} \quad (\text{m}^3/\text{h})$$
###### 4.2.3.2. Suất cấp khí trên đơn vị diện tích mặt nước: $q_{area} = 0.15 - 0.30\text{ m}^3\text{ khí}/(\text{m}^2\cdot\text{phút})$
- Để tạo trường vận tốc xáo trộn nâng cặn cuộn từ đáy lên bề mặt, cường độ thổi khí trên một đơn vị diện tích bề mặt đáy bể phải đạt:
  $$q_{area} = 0.15 \text{ đến } 0.30 \text{ m}^3 \text{ khí} / (\text{m}^2 \text{ mặt thoáng} \cdot \text{phút}) \quad (9.0 \text{ đến } 18.0 \text{ m}^3/(\text{m}^2 \cdot \text{h}))$$
- Đảm bảo mật độ bọt khí phân bố đồng đều trên toàn bộ mặt cắt ngang của bể.
##### 4.2.4. Hiệu quả phân hủy sinh học sơ bộ BOD nhờ sục khí (`eq_ch02_04`)
###### 4.2.4.1. Mức độ oxy hóa sinh học ngẫu nhiên: giảm xấp xỉ 10% $BOD_5$ thô ($\eta_{aeration} = 0.10$)
- Do nước thải được cấp khí oxy liên tục và tiếp xúc với vi sinh vật có sẵn trong nước thải ở điều kiện xáo trộn hoàn toàn, một quá trình oxy hóa sinh học hiếu khí sơ bộ diễn ra tự nhiên trong bể điều hòa.
- Hiệu suất loại bỏ $BOD_5$ ngẫu nhiên đạt khoảng $10\%$ ($\eta_{aeration} = 0.10$ hay $10\%$).
- Nồng độ $BOD_5$ thực tế của dòng nước thải chảy ra khỏi bể điều hòa vào các công trình sinh học hạ nguồn được tính theo công thức (`eq_ch02_04`):
  $$BOD_{eff} = BOD_{avg} \times (1 - \eta_{aeration}) = BOD_{avg} \times (1 - 0.10) = 0.90 \times BOD_{avg}$$
- Trong đó:
  - $BOD_{eff}$: Nồng độ $BOD_5$ sau điều hòa dẫn sang công trình tiếp theo ($\text{mg/L}$).
  - $BOD_{avg}$: Nồng độ $BOD_5$ trung bình gia quyền lưu lượng sau khi hòa trộn hoàn toàn ($\text{mg/L}$).
###### 4.2.4.2. Tác động của quá trình sục khí lên cấu trúc cặn và khả năng phân hủy tiếp theo
- Quá trình sục khí bẻ gãy các phân tử hữu cơ mạch dài, tạo điều kiện thủy phân sơ bộ một phần chất hữu cơ không tan thành chất hữu cơ hòa tan dễ phân hủy sinh học ($RBCOD$ - Readily Biodegradable COD).
- Hỗ trợ làm tăng hoạt tính sinh học và giảm tải lượng cho bể Aerotank phía sau.
##### 4.2.5. Lựa chọn thiết bị thổi khí và mạng lưới phân phối (Blowers & Diffuser Grid)
###### 4.2.5.1. Máy thổi khí kiểu thể tích dạng thùy quay (Roots Rotary Lobe Blowers)
- Lựa chọn máy thổi khí kiểu Roots 3 thùy (Tri-lobe Roots Blower) có biến tần điều khiển áp suất và lưu lượng.
- Trang bị van một chiều, khớp nối mềm cao su chống rung, van an toàn bảo vệ quá áp (Pressure Relief Valve), đồng hồ đo áp lực màng và vỏ cách âm giảm ồn ($< 75 - 80 \text{ dBA}$).
###### 4.2.5.2. Màng đĩa thổi khí tinh/thô (Fine Bubble vs. Coarse Bubble Membrane Diffusers)
- **Đĩa phân phối bọt khí tinh (Fine Bubble, $\phi 1 - 3 \text{ mm}$)**: Màng EPDM/PTFE có hiệu suất truyền oxy cao ($OTE = 4.0 - 6.5\%/\text{m}$ độ sâu ngập nước), giúp tiết kiệm điện năng của máy thổi khí. Tuy nhiên, dễ bị nghẹt lỗ màng nếu cặn bùn lắng đọng khi ngừng cấp khí.
- **Đầu phân phối bọt khí thô (Coarse Bubble, $\phi \ge 5 \text{ mm}$)**: Chế tạo bằng inox hoặc nhựa UPVC, không lo tắc nghẽn, tạo động lực cuộn xoáy cơ học cực mạnh rất phù hợp cho mục đích khuấy trộn chống sa lắng cặn trong bể điều hòa.
###### 4.2.5.3. Yêu cầu cô lập hệ thống cấp khí bể điều hòa khỏi mạng cấp khí bể sinh học hiếu khí
- **Quy tắc kỹ thuật bắt buộc**: Tuyệt đối không dùng chung một tuyến ống cấp khí chính từ một cụm máy thổi khí chung cho cả bể điều hòa và bể vi sinh hiếu khí (Aerotank).
- **Lý do kỹ thuật**: Mực nước trong bể điều hòa thay đổi liên tục ($H_{min} \leftrightarrow H_{max}$), dẫn đến áp suất thủy tĩnh đối áp (Backpressure) tại các đĩa khí biến thiên liên tục. Nếu đấu chung với bể Aerotank (vốn có mực nước cố định), khí nén sẽ bị dồn lệch sang nơi có trở lực thấp hơn, gây mất kiểm soát lưu lượng khí và có nguy cơ làm cháy động cơ máy thổi khí. Hệ thống cấp khí bể điều hòa phải có máy thổi khí và tuyến ống độc lập hoàn toàn.

---

### 5. Thiết kế Hình học, Xây dựng Công trình và Thiết bị Phụ trợ (Tank Geometry, Civil Construction & Auxiliary Systems)
#### 5.1. Hình học bể và ngăn ngừa hiện tượng ngắn mạch (Tank Geometry & Hydraulic Short-Circuiting)
##### 5.1.1. Tỷ lệ hình học tối ưu giữa chiều dài, chiều rộng và chiều sâu (L:W:H Aspect Ratios)
###### 5.1.1.1. Hạn chế thiết kế dạng mương dài hẹp (Long Narrow Rectangular Channels)
- Tránh tuyệt đối thiết kế bể điều hòa có dạng hình chữ nhật quá hẹp và kéo dài (tỷ lệ $L/W > 4:1$ đến $5:1$) vì hình học này tạo ra mô hình dòng chảy nút (Plug Flow Reactor - PFR), triệt tiêu hoàn toàn khả năng xáo trộn giữa các mảng nước vào ở các thời điểm khác nhau.
- Hình học tối ưu cho xáo trộn hoàn toàn (Completely Stirred Tank Reactor - CSTR) là hình vuông ($L/W \approx 1:1$) hoặc hình chữ nhật ngắn ($L/W \approx 1.5:1$ đến $2:1$), hoặc hình tròn có đường kính tương đương.
###### 5.1.1.2. Bố trí vách ngăn hướng dòng (Baffle Walls) để triệt tiêu dòng chảy tắt
- Trường hợp diện tích mặt bằng bắt buộc phải xây dựng bể dài, cần bố trí các vách ngăn lượn sóng hoặc tường hướng dòng có lỗ thông đáy/tràn mặt để kéo dài đường đi của dòng chảy, đồng thời triệt tiêu hiện tượng đoản mạch thủy lực (Short-Circuiting) - nơi dòng nước mới vào đi thẳng ra cửa hút bơm mà chưa kịp hòa trộn với khối nước cũ.
##### 5.1.2. Thiết kế công trình thu nước vào và phân phối dòng chảy (Inlet Structures)
- Cửa tiếp nhận nước thải vào bể điều hòa phải đặt ở vị trí cách xa cửa tháo nước ra tối đa có thể (bố trí ở hai đầu đối diện theo đường chéo của bể).
- Trang bị máng phân phối răng cưa hoặc đường ống phân phối đục lỗ ngập nước nhằm tiêu năng dòng chảy và dàn đều nước thải trên toàn bộ bề rộng của bể.
##### 5.1.3. Thiết kế hố thu bơm và công trình tháo nước ra (Outlet Structures & Pump Sumps)
- Hố thu bơm chìm (Pump Sump Pit) được thiết kế hạ thấp sâu hơn sàn đáy bể từ $0.5$ đến $0.8 \text{ m}$ với độ dốc vát đáy $i \ge 10 - 15\%$ hướng tâm về phía bơm.
- Thiết kế này tạo điều kiện cho bơm chìm có thể hút kiệt nước khi cần thau rửa bảo trì, đồng thời tập trung cặn nặng về phễu thu để bơm hút xả ra ngoài.
#### 5.2. Giải pháp xây dựng và kết cấu công trình (Civil Structural Configurations)
##### 5.2.1. Bể bê tông cốt thép toàn khối (Reinforced Concrete Tanks)
###### 5.2.1.1. Ưu điểm: Độ bền cao, tiết kiệm diện tích mặt bằng, thích hợp trạm công suất lớn hoặc đô thị
- Kết cấu thành tường đứng bằng bê tông cốt thép mác cao (M300 / B22.5 trở lên), cốt thép chịu lực hai lớp chống nứt và chịu áp lực đất/nước lớn.
- Khai thác tối đa chiều sâu xây dựng hữu ích ($H = 4.0 - 6.0 \text{ m}$), giúp tiết kiệm diện tích mặt đất tối đa, phù hợp cho các khu công nghiệp tập trung và các đô thị lớn.
###### 5.2.1.2. Yêu cầu chống thấm, chống ăn mòn axít béo và khí sinh học
- Phải sử dụng phụ gia chống thấm tinh thể thẩm thấu trong bê tông, bố trí băng cản nước (Waterstop PVC/Hydrophilic Swellable Strip) tại tất cả các mạch ngừng thi công.
- Bề mặt tường trong vùng biến thiên mực nước tiếp xúc với khí $H_2S$ phải được sơn phủ lớp màng epoxy hoặc sơn polyurea kháng hóa chất chống hiện tượng ăn mòn biogenic sulfuric acid.
##### 5.2.2. Hồ đất lót màng chống thấm địa kỹ thuật (Geomembrane-Lined Earthen Basins)
###### 5.2.2.1. Ưu điểm chi phí đầu tư thấp nhất đối với diện tích đất mở rộng
- Là giải pháp xây dựng có chi phí đầu tư xây dựng cơ bản (Capex) thấp nhất, giảm từ $50 - 70\%$ so với bể bê tông cốt thép tương đương thể tích.
- Đặc biệt phù hợp cho các nhà máy chế biến nông thủy sản, nhà máy đường, tinh bột sắn ở vùng nông thôn có sẵn diện tích đất rộng lớn.
###### 5.2.2.2. Tiêu chuẩn màng HDPE (chiều dày 1.5 - 2.0 mm), mái dốc bờ kè (1:2 đến 1:3), mương neo màng (Anchor Trench)
- Bờ đê đất đắp được đầm nén đạt độ chặt $K \ge 0.95$, mái taluy nghiêng với hệ số dốc từ $1:2$ đến $1:3$ để chống trượt lở đất.
- Lót màng chống thấm địa kỹ thuật bằng bạt HDPE (High-Density Polyethylene) nguyên sinh chiều dày tối thiểu $\ge 1.5 \text{ mm}$ (khuyến nghị $2.0 \text{ mm}$).
- Đỉnh màng trên bờ đê phải được cố định chắc chắn trong rãnh neo (Anchor Trench) kích thước chuẩn sâu $0.5 \text{ m} \times$ rộng $0.5 \text{ m}$ và chèn lấp bằng đất sỏi đầm chặt hoặc đổ bê tông khóa chốt.
###### 5.2.2.3. Biện pháp bảo vệ màng chống rách khi lắp đặt máy khuấy và lưới phân phối khí
- Tại các vị trí đặt bệ đỡ đĩa thổi khí, chân đế giá đỡ ống và khu vực phía dưới cánh khuấy chìm, phải hàn gia cường thêm một lớp màng HDPE đệm (Sacrificial Wear Sheet) hoặc đổ các tấm đan bê tông bảo vệ để chống rách màng do cọ xát hoặc tia nước áp lực cao.
#### 5.3. Hệ thống bơm nước thải và kiểm soát mức nước tự động (Pumping & Automated Level Instrumentation)
##### 5.3.1. Trạm bơm nước thải điều hòa sử dụng biến tần (VFD Pumps)
###### 5.3.1.1. Điều chỉnh lưu lượng bơm cấp liên tục, ổn định vào các công trình hạ nguồn
- Trang bị tối thiểu 2 máy bơm chìm nước thải (1 chạy, 1 dự phòng luân phiên $100\%$ công suất) kết hợp biến tần điều khiển tốc độ quay (VFD - Variable Frequency Drive).
- Biến tần điều chỉnh tần số động cơ ($30 - 50 \text{ Hz}$) để giữ lưu lượng dòng nước cấp vào các bể sinh học phía sau luôn bám sát lưu lượng trung bình thiết kế $Q_{avg}$, loại trừ xung sốc cơ học cho đường ống dẫn.
###### 5.3.1.2. Chế độ vận hành luân phiên (Duty/Standby) và giảm dòng khởi động
- PLC tự động đổi ca máy bơm sau mỗi chu kỳ chạy (ví dụ 8 - 12 giờ) để mài mòn cơ học đồng đều giữa các tổ bơm.
- Biến tần thực hiện khởi động mềm (Soft Start) và dừng mềm (Soft Stop), triệt tiêu hoàn toàn dòng điện khởi động đỉnh và hiện tượng búa nước (Water Hammer) trên đường ống áp lực.
##### 5.3.2. Cảm biến đo mức nước liên tục (Continuous Level Transmitters)
###### 5.3.2.1. Cảm biến siêu âm (Ultrasonic Level Sensor) hoặc Radar không tiếp xúc
- Lắp đặt thiết bị đo mức liên tục công nghệ sóng siêu âm hoặc sóng vi ba Radar không tiếp xúc phía trên nắp bể, truyền tín hiệu tương tự $4 - 20 \text{ mA}$ hoặc Modbus RTU về bộ điều khiển lập trình PLC.
- Thiết bị đo mức đo đạc chính xác chiều cao cột nước hữu ích trong bể theo thời gian thực ($H(t)$) với độ sai số $< 0.2\%$.
###### 5.3.2.2. Lập trình PLC điều khiển phân cấp mức (Stop low, Start 1 pump, Start 2 pumps, High alarm)
- **Mức rất thấp (Low-Low Level $\le 1.5\text{ m}$)**: Kích hoạt khóa liên động ngắt khẩn cấp toàn bộ máy bơm và máy thổi khí để chống cháy động cơ.
- **Mức thấp (Low Level = $1.8\text{ m}$)**: Bơm vận hành ở tần số tối thiểu ($30 \text{ Hz}$) hoặc dừng bơm chính.
- **Mức bình thường (Normal Operating Level = $2.5 - 3.8\text{ m}$)**: Bơm 1 vận hành ở tần số điều tiết ổn định, lưu lượng đạt chuẩn $Q_{avg}$.
- **Mức cao (High Level = $4.2\text{ m}$)**: Bơm 1 tăng tốc lên tần số tối đa ($50 \text{ Hz}$), cảnh báo mức cao trên màn hình HMI/SCADA.
- **Mức rất cao (High-High Level = $4.5\text{ m}$)**: Tự động khởi động đồng thời cả 2 bơm chạy hết công suất để chống tràn bể, kích hoạt còi báo động khẩn cấp.
##### 5.3.3. Khóa liên động an toàn và thiết bị dự phòng sự cố (Safety Interlocks & Redundancy)
###### 5.3.3.1. Phao báo mức cao độc lập (Backup High-Level Float Switch) kích hoạt còi/đèn và bơm khẩn cấp
- Cảm biến siêu âm có thể bị sai lệch tín hiệu do bọt khí xốp phủ bề mặt, sương mù ngưng tụ hoặc hơi ẩm đóng bám trên đầu dò.
- Do đó, bắt buộc phải lắp đặt một phao cơ báo mức dạng quả cầu nghiêng (Suspended Float Switch) độc lập hoàn toàn, đấu dây cứng trực tiếp vào mạch điều khiển rơ-le của tủ điện mà không phụ thuộc vào phần mềm PLC.
- Khi phao mức cao nổi nghiêng, công tắc lập tức đóng mạch kích hoạt còi hú, đèn chớp báo động và cưỡng bức khởi động bơm xả tràn khẩn cấp.
###### 5.3.3.2. Khóa ngắt mức thấp cho máy bơm và máy khuấy để chống chạy khô
- Phao ngắt mức cạn độc lập (Low-Level Float) ngắt nguồn động lực máy bơm khi mực nước tụt xuống dưới bầu hút bơm, chống hiện tượng xâm thực phá hủy phốt cơ khí và cháy cuộn dây stato.
###### 5.3.3.3. Khóa ngắt mức thấp cho máy thổi khí khi mức nước hạ dưới $1.5\text{ m}$
- Tích hợp khóa liên động trên tủ điều khiển máy thổi khí: Khi mức nước trong bể giảm xuống dưới ngưỡng tối thiểu $1.5 \text{ m}$, mạch điều khiển tự động ngắt máy thổi khí nhằm ngăn ngừa rung giật đĩa khí và bảo vệ động cơ quạt gió.
#### 5.4. Tiết kiệm năng lượng và tối ưu hóa chi phí vận hành (Energy Efficiency & Optimization)
##### 5.4.1. Nghiên cứu tình huống cải tạo hệ thống sục khí tiết kiệm năng lượng (Case Study: 135 HP Energy Savings)
- Bài học thực tế từ công trình nâng cấp cải tạo hệ thống sục khí bể điều hòa (Slide Frame 25 / Hình 25):
  - Thay thế hệ thống phân phối khí bọt thô hiệu suất thấp và quạt gió ly tâm điều khiển van tiết lưu cơ học bằng hệ thống máy thổi khí biến tần kết hợp đĩa màng bọt tinh hiệu suất cao ($OTE$ tăng từ $1.5\%/\text{m}$ lên $5.5\%/\text{m}$).
  - Tối ưu hóa thuật toán điều khiển cấp khí theo tín hiệu nồng độ $DO$ và mức nước thực tế.
  - Kết quả dự án mang lại mức tiết kiệm điện năng khổng lồ lên tới **$135 \text{ HP}$** (tương đương xấp xỉ $100.7 \text{ kW}$ công suất tiêu thụ liên tục), giảm hàng tỷ đồng tiền điện vận hành mỗi năm và thu hồi vốn đầu tư chỉ sau chưa đầy 2 năm vận hành.
##### 5.4.2. Tận dụng biểu giá điện theo giờ (Peak/Off-Peak Power Tariff Scheduling)
- Bể điều hòa cho phép người vận hành chủ động điều tiết dung lượng tích trữ:
  - Tích trữ tối đa lượng nước thải trong các khung giờ cao điểm giá điện (09:30 - 11:30 và 17:00 - 20:00) bằng cách giảm nhẹ lưu lượng bơm xả.
  - Tăng công suất bơm xả sạch lượng nước tồn trữ vào các khung giờ thấp điểm ban đêm (22:00 - 04:00 sáng hôm sau) khi giá điện sản xuất giảm sâu tới $60\%$.
  - Tiết kiệm đáng kể chi phí tiền điện năng lượng cho toàn trạm mà vẫn đảm bảo an toàn quá trình xử lý.

---

### 6. Bài toán Tính toán Thực hành và Ví dụ Điển hình (Design Practice & Worked Numerical Problems)
#### 6.1. Bài tập EX-CH02-01: Tính toán Dung tích Bể Điều hòa theo Phương pháp Biểu đồ Tích lũy Khối lượng Rippl
##### 6.1.1. Đề bài và bộ số liệu chuỗi thời gian lưu lượng 24 giờ (`tbl_ch02_01`)
- **Nguồn bài tập**: HCMUT-263, Slide 9 (Slide Frame 17).
- **Yêu cầu kỹ thuật**: Xác định dung tích yêu cầu của bể điều hòa (dung tích lý thuyết $V_{theoretical}$ và dung tích thực tế $V_{practical}$) dựa trên chuỗi số liệu đo đạc lưu lượng thực tế theo từng giờ trong ngày được cho trong bảng dưới đây.
##### 6.1.2. Bảng tính toán chi tiết 24 giờ: Lưu lượng vào, Thể tích vào, Tích lũy vào, Tích lũy ra, Độ chênh tích lũy $\Delta V(t)$

| Chu kỳ | Khung giờ | Lưu lượng $Q_{in}$ ($\text{m}^3/\text{h}$) | Thể tích vào $V_{in}$ ($\text{m}^3$) | Tích lũy vào $\sum V_{in}$ ($\text{m}^3$) | Tích lũy ra $\sum V_{out}$ ($\text{m}^3$) | Độ chênh lệch $\Delta V(t)$ ($\text{m}^3$) | Trạng thái tích lũy |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|
| **M-1** | 00:00 - 01:00 | 990 | 990 | 990 | 1,106.25 | -116.25 | Thiếu hụt |
| **1-2** | 01:00 - 02:00 | 792 | 792 | 1,782 | 2,212.50 | -430.50 | Thiếu hụt |
| **2-3** | 02:00 - 03:00 | 594 | 594 | 2,376 | 3,318.75 | -942.75 | Thiếu hụt |
| **3-4** | 03:00 - 04:00 | 468 | 468 | 2,844 | 4,425.00 | -1,581.00 | Thiếu hụt |
| **4-5** | 04:00 - 05:00 | 378 | 378 | 3,222 | 5,531.25 | -2,309.25 | Thiếu hụt |
| **5-6** | 05:00 - 06:00 | 360 | 360 | 3,582 | 6,637.50 | -3,055.50 | Thiếu hụt |
| **6-7** | 06:00 - 07:00 | 432 | 432 | 4,014 | 7,743.75 | -3,729.75 | Thiếu hụt |
| **7-8** | 07:00 - 08:00 | 738 | 738 | 4,752 | 8,850.00 | **-4,098.00** | **Thiếu hụt cực đại ($\min \Delta V$)** |
| **8-9** | 08:00 - 09:00 | 1,278 | 1,278 | 6,030 | 9,956.25 | -3,926.25 | Bắt đầu tích lũy lại |
| **9-10** | 09:00 - 10:00 | 1,476 | 1,476 | 7,506 | 11,062.50 | -3,556.50 | Bù thiếu hụt |
| **10-11** | 10:00 - 11:00 | 1,530 | 1,530 | 9,036 | 12,168.75 | -3,132.75 | Bù thiếu hụt |
| **11-N** | 11:00 - 12:00 | 1,548 | 1,548 | 10,584 | 13,275.00 | -2,691.00 | Bù thiếu hụt |
| **N-13** | 12:00 - 13:00 | 1,530 | 1,530 | 12,114 | 14,381.25 | -2,267.25 | Bù thiếu hụt |
| **13-14** | 13:00 - 14:00 | 1,458 | 1,458 | 13,572 | 15,487.50 | -1,915.50 | Bù thiếu hụt |
| **14-15** | 14:00 - 15:00 | 1,386 | 1,386 | 14,958 | 16,593.75 | -1,635.75 | Bù thiếu hụt |
| **15-16** | 15:00 - 16:00 | 1,260 | 1,260 | 16,218 | 17,700.00 | -1,482.00 | Bù thiếu hụt |
| **16-17** | 16:00 - 17:00 | 1,170 | 1,170 | 17,388 | 18,806.25 | -1,418.25 | Bù thiếu hụt |
| **17-18** | 17:00 - 18:00 | 1,170 | 1,170 | 18,558 | 19,912.50 | -1,354.50 | Bù thiếu hụt |
| **18-19** | 18:00 - 19:00 | 1,188 | 1,188 | 19,746 | 21,018.75 | -1,272.75 | Bù thiếu hụt |
| **19-20** | 19:00 - 20:00 | 1,314 | 1,314 | 21,060 | 22,125.00 | -1,065.00 | Bù thiếu hụt |
| **20-21** | 20:00 - 21:00 | 1,440 | 1,440 | 22,500 | 23,231.25 | -731.25 | Bù thiếu hụt |
| **21-22** | 21:00 - 22:00 | 1,440 | 1,440 | 23,940 | 24,337.50 | -397.50 | Bù thiếu hụt |
| **22-23** | 22:00 - 23:00 | 1,368 | 1,368 | 25,308 | 25,443.75 | -135.75 | Bù thiếu hụt |
| **23-M** | 23:00 - 24:00 | 1,242 | 1,242 | 26,550 | 26,550.00 | **0.00** | **Thặng dư cực đại ($\max \Delta V$)** |
| **Tổng** | **24 giờ** | - | **26,550** | - | **26,550** | - | **Cân bằng ngày hoàn hảo** |

##### 6.1.3. Xác định lưu lượng trung bình giờ $Q_{avg}$ và tổng thể tích ngày $V_{total}$
- **Bước 1: Tính tổng lượng nước thải ngày**:
  $$V_{total} = \sum_{i=1}^{24} Q_{in,i} \cdot \Delta t = 26,550.0 \text{ m}^3/\text{ngày}$$
- **Bước 2: Tính lưu lượng trung bình giờ (Lưu lượng xả ra cố định)**:
  $$Q_{avg} = \frac{V_{total}}{24} = \frac{26,550.0 \text{ m}^3}{24 \text{ h}} = 1,106.25 \text{ m}^3/\text{h}$$
- **Đặc trưng dòng vào**:
  - Lưu lượng đỉnh cực đại: $Q_{max} = 1,548.0 \text{ m}^3/\text{h}$ (xảy ra lúc 11:00 - 12:00).
  - Lưu lượng đáy cực tiểu: $Q_{min} = 360.0 \text{ m}^3/\text{h}$ (xảy ra lúc 05:00 - 06:00).
  - Hệ số không điều hòa giờ lớn nhất: $K_{h,max} = \frac{1,548.0}{1,106.25} \approx 1.40$.
  - Hệ số không điều hòa giờ nhỏ nhất: $K_{h,min} = \frac{360.0}{1,106.25} \approx 0.325$.
##### 6.1.4. Phân tích giá trị thặng dư cực đại $\max(\Delta V)$ và thiếu hụt cực đại $\min(\Delta V)$
- **Bước 3: Tra bảng xác định các giá trị cực trị của chuỗi $\Delta V(t)$**:
  - Giá trị thặng dư tích lũy cực đại: $\max(\Delta V(t)) = 0.00 \text{ m}^3$ (đạt được tại giờ thứ 24, tức lúc 24:00 đêm).
  - Giá trị thiếu hụt tích lũy cực đại: $\min(\Delta V(t)) = -4,098.00 \text{ m}^3$ (xuất hiện tại cuối giờ thứ 8, tức lúc 08:00 sáng).
##### 6.1.5. Tính toán dung tích lý thuyết $V_{theoretical}$ và dung tích thực tế $V_{practical}$ theo hệ số an toàn 1.1 - 1.2
- **Bước 4: Áp dụng phương trình cân bằng khối lượng Rippl (`eq_ch02_01`)**:
  $$V_{theoretical} = \max(\Delta V(t)) - \min(\Delta V(t)) = 0.00 - (-4,098.00) = 4,098.00 \text{ m}^3$$
  *(Dung tích lý thuyết bằng đúng $15.43\%$ tổng lưu lượng ngày của nhà máy).*
- **Bước 5: Áp dụng hệ số an toàn thực tế $f_{safety} = 1.1 - 1.2$ (`eq_ch02_02`)**:
  - Với cận dưới an toàn ($1.1 \times$):
    $$V_{practical,min} = 1.10 \times 4,098.00 \text{ m}^3 = 4,507.80 \text{ m}^3$$
  - Với cận trên an toàn ($1.2 \times$):
    $$V_{practical,max} = 1.20 \times 4,098.00 \text{ m}^3 = 4,917.60 \text{ m}^3$$
  - **Kết luận dung tích thiết kế**: Lựa chọn dung tích thực tế trong dải **$V_{practical} = 4,507.8 - 4,917.6 \text{ m}^3$** (chọn thiết kế điển hình $V = 4,700.0 \text{ m}^3$).
##### 6.1.6. Tính toán kích thước hình học bể (Chiều sâu, Diện tích mặt bằng, Kích thước dài x rộng)
- Giả sử chọn chiều sâu nước vận hành hữu ích biến thiên:
  - Chiều sâu mức nước tối thiểu: $H_{min} = 1.50 \text{ m}$ (đáp ứng điều kiện sục khí và ngập cánh khuấy).
  - Khoảng biến thiên mực nước làm việc: $\Delta H = 3.00 \text{ m}$.
  - Chiều sâu mức nước tối đa: $H_{max} = H_{min} + \Delta H = 1.50 + 3.00 = 4.50 \text{ m}$.
  - Chiều cao bảo vệ mặt thoáng: $H_{freeboard} = 0.50 \text{ m}$.
  - Tổng chiều sâu xây dựng thành bể: $H_{total} = 4.50 + 0.50 = 5.00 \text{ m}$.
- Diện tích mặt bằng yêu cầu:
  $$A_{tank} = \frac{V_{practical}}{\Delta H} = \frac{4,700.0 \text{ m}^3}{3.00 \text{ m}} \approx 1,566.7 \text{ m}^2$$
- Bố trí chia thành 2 đơn nguyên bể làm việc song song để linh hoạt vận hành và bảo trì:
  - Diện tích mỗi đơn nguyên: $A_1 = 1,566.7 / 2 \approx 783.3 \text{ m}^2$.
  - Chọn tỷ lệ chiều dài trên chiều rộng $L/W = 1.25 : 1$.
  - Chiều rộng mỗi đơn nguyên: $W = \sqrt{783.3 / 1.25} = 25.0 \text{ m}$.
  - Chiều dài mỗi đơn nguyên: $L = 1.25 \times 25.0 = 31.35 \text{ m}$ (chọn chẵn $L = 31.5 \text{ m}$).
  - Kích thước phủ bì mỗi đơn nguyên: $L \times W \times H = 31.5 \text{ m} \times 25.0 \text{ m} \times 5.0 \text{ m}$.

---

#### 6.2. Bài tập EX-CH02-02: Đánh giá Hiệu quả Điều hòa Nồng độ BOD và Tải lượng Khối lượng Ô nhiễm
##### 6.2.1. Đề bài và bộ số liệu chuỗi thời gian 24 giờ của Lưu lượng $Q_i$ và Nồng độ $BOD_5$ ($C_i$) (`tbl_ch02_02`)
- **Nguồn bài tập**: HCMUT-263, Slide 9 (Slide Frame 25).
- **Yêu cầu kỹ thuật**:
  1. Xác định tải lượng khối lượng $BOD_5$ theo từng giờ và tổng tải lượng ô nhiễm trong 24 giờ.
  2. Tính toán nồng độ $BOD_5$ trung bình sau điều hòa khi xáo trộn hoàn toàn ($C_{avg}$).
  3. Đánh giá nồng độ $BOD_5$ dòng ra khi xét đến hiệu ứng phân hủy hiếu khí sơ bộ $10\%$ do hệ thống sục khí cung cấp ($BOD_{eff}$).
  4. Đánh giá mức độ san phẳng sốc tải hữu cơ bảo vệ hệ thống sinh học.
##### 6.2.2. Bảng tính toán chi tiết tải lượng khối lượng $BOD_5$ theo từng giờ ($M_i = Q_i \cdot C_i$)

| Chu kỳ | Khung giờ | Lưu lượng $Q_i$ ($\text{m}^3/\text{h}$) | Nồng độ $BOD_5$ ($C_i$, $\text{mg/L}$) | Tải lượng giờ ($M_i$, $\text{g/h}$) | Tải lượng giờ ($M_i$, $\text{kg/h}$) | Tỷ trọng tải lượng ($M_i / M_{total}$) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| **M-1** | 00:00 - 01:00 | 990 | 150 | 148,500 | 148.50 | $2.90\%$ |
| **1-2** | 01:00 - 02:00 | 792 | 115 | 91,080 | 91.08 | $1.78\%$ |
| **2-3** | 02:00 - 03:00 | 594 | 75 | 44,550 | 44.55 | $0.87\%$ |
| **3-4** | 03:00 - 04:00 | 468 | 50 | 23,400 | 23.40 | $0.46\%$ |
| **4-5** | 04:00 - 05:00 | 378 | **45 (min)** | 17,010 | **17.01 (min)** | **$0.33\%$** |
| **5-6** | 05:00 - 06:00 | 360 | 60 | 21,600 | 21.60 | $0.42\%$ |
| **6-7** | 06:00 - 07:00 | 432 | 90 | 38,880 | 38.88 | $0.76\%$ |
| **7-8** | 07:00 - 08:00 | 738 | 130 | 95,940 | 95.94 | $1.87\%$ |
| **8-9** | 08:00 - 09:00 | 1,278 | 175 | 223,650 | 223.65 | $4.37\%$ |
| **9-10** | 09:00 - 10:00 | 1,476 | 200 | 295,200 | 295.20 | $5.76\%$ |
| **10-11** | 10:00 - 11:00 | 1,530 | 215 | 328,950 | 328.95 | $6.42\%$ |
| **11-N** | 11:00 - 12:00 | 1,548 | 220 | 340,560 | 340.56 | $6.65\%$ |
| **N-13** | 12:00 - 13:00 | 1,530 | 220 | 336,600 | 336.60 | $6.57\%$ |
| **13-14** | 13:00 - 14:00 | 1,458 | 210 | 306,180 | 306.18 | $5.98\%$ |
| **14-15** | 14:00 - 15:00 | 1,386 | 200 | 277,200 | 277.20 | $5.41\%$ |
| **15-16** | 15:00 - 16:00 | 1,260 | 190 | 239,400 | 239.40 | $4.67\%$ |
| **16-17** | 16:00 - 17:00 | 1,170 | 180 | 210,600 | 210.60 | $4.11\%$ |
| **17-18** | 17:00 - 18:00 | 1,170 | 170 | 198,900 | 198.90 | $3.88\%$ |
| **18-19** | 18:00 - 19:00 | 1,188 | 175 | 207,900 | 207.90 | $4.06\%$ |
| **19-20** | 19:00 - 20:00 | 1,314 | 210 | 275,940 | 275.94 | $5.39\%$ |
| **20-21** | 20:00 - 21:00 | 1,440 | 280 | 403,200 | 403.20 | $7.87\%$ |
| **21-22** | 21:00 - 22:00 | 1,440 | **305 (max)** | 439,200 | **439.20 (max)** | **$8.57\%$** |
| **22-23** | 22:00 - 23:00 | 1,368 | 245 | 335,160 | 335.16 | $6.54\%$ |
| **23-M** | 23:00 - 24:00 | 1,242 | 180 | 223,560 | 223.56 | $4.36\%$ |
| **Tổng** | **24 giờ** | **26,550** | - | **5,123,160** | **5,123.16** | **100.0%** |

##### 6.2.3. Tính toán tổng tải lượng $BOD_5$ ngày ($M_{total}$) và nồng độ bình quân gia quyền lưu lượng ($C_{avg}$) (`eq_ch02_03`)
- **Bước 1: Tính tổng tải lượng khối lượng $BOD_5$ trong ngày**:
  $$M_{total} = \sum_{i=1}^{24} M_i = \sum_{i=1}^{24} (Q_i \cdot C_i \cdot 1\text{ h}) = 5,123,160 \text{ g/ngày} = 5,123.16 \text{ kg/ngày}$$
- **Bước 2: Tính nồng độ $BOD_5$ trung bình gia quyền lưu lượng theo phương trình cân bằng khối lượng (`eq_ch02_03`)**:
  $$C_{avg} = \frac{\sum_{i=1}^{24} Q_i \cdot C_i}{\sum_{i=1}^{24} Q_i} = \frac{M_{total}}{V_{total}}$$
  $$C_{avg} = \frac{5,123,160 \text{ g}}{26,550 \text{ m}^3} = 192.9627... \text{ g/m}^3 \approx 192.96 \text{ mg/L}$$
- **Đặc trưng dao động nồng độ dòng vào thô**:
  - Nồng độ $BOD_5$ thô nhỏ nhất: $C_{min} = 45.0 \text{ mg/L}$ (lúc 04:00 - 05:00 rạng sáng).
  - Nồng độ $BOD_5$ thô lớn nhất: $C_{max} = 305.0 \text{ mg/L}$ (lúc 21:00 - 22:00 đêm).
  - Tỷ số dao động nồng độ cực đại trên cực tiểu:
    $$\text{Tỷ số dao động} = \frac{C_{max}}{C_{min}} = \frac{305.0}{45.0} = 6.78 \text{ lần}$$
  - Tỷ số dao động tải lượng giờ cực đại trên cực tiểu:
    $$\frac{M_{max}}{M_{min}} = \frac{439.20 \text{ kg/h}}{17.01 \text{ kg/h}} = 25.82 \text{ lần}$$
##### 6.2.4. Tính toán nồng độ $BOD_5$ dòng ra khi xét đến hiệu quả phân hủy sinh học sơ bộ 10% do sục khí ($BOD_{eff}$) (`eq_ch02_04`)
- **Bước 3: Đánh giá hiệu quả oxy hóa hiếu khí sơ bộ nhờ hệ thống sục khí**:
  - Hệ thống sục khí trong bể điều hòa cung cấp oxy hòa tan liên tục, kích thích quá trình tự phân hủy sinh học hiếu khí với hiệu suất loại bỏ $BOD_5$ ngẫu nhiên là $\eta_{aeration} = 10\%$ ($0.10$).
  - Áp dụng phương trình xác định nồng độ sau sục khí (`eq_ch02_04`):
    $$BOD_{eff} = C_{avg} \times (1 - \eta_{aeration}) = 192.96 \text{ mg/L} \times (1 - 0.10)$$
    $$BOD_{eff} = 192.96 \times 0.90 = 173.664 \text{ mg/L} \approx 173.67 \text{ mg/L}$$
  - Lượng $BOD_5$ được phân hủy sơ bộ ngay trong bể điều hòa:
    $$\Delta M_{BOD} = M_{total} \times 0.10 = 5,123.16 \times 0.10 = 512.316 \text{ kg/ngày}$$
##### 6.2.5. Phân tích định lượng mức độ san phẳng nồng độ và loại bỏ hoàn toàn hiện tượng sốc tải hữu cơ
- **So sánh trước và sau điều hòa**:
  - **Trước điều hòa**: Dòng nước thải đi thẳng vào bể vi sinh với nồng độ biến thiên dữ dội từ $45 \text{ mg/L}$ đến $305 \text{ mg/L}$ (biên độ gấp $6.78$ lần); tải lượng dao động từ $17.01 \text{ kg/h}$ đến $439.20 \text{ kg/h}$ (biên độ gấp $25.82$ lần). Vi sinh vật trong bể Aerotank liên tục bị sốc tải nặng vào ban đêm và đói cơ chất vào rạng sáng, hệ thống quạt gió không thể điều chỉnh bám đuổi kịp thời.
  - **Sau điều hòa**: Toàn bộ dao động nồng độ được làm phẳng tuyệt đối về một giá trị duy nhất hằng định $192.96 \text{ mg/L}$ (nếu chỉ khuấy cơ học) hoặc $173.67 \text{ mg/L}$ (nếu kết hợp sục khí hiếu khí). Tải lượng $BOD_5$ đưa vào bể Aerotank ổn định tuyệt đối ở mức:
    $$M_{downstream} = Q_{avg} \times BOD_{eff} = 1,106.25 \text{ m}^3/\text{h} \times 0.17367 \text{ kg/m}^3 = 192.12 \text{ kg/h}$$
  - Loại bỏ $100\%$ xung sốc tải trọng hữu cơ, giảm $10\%$ tải trọng hữu cơ thiết kế cho bể sinh học, đảm bảo quá trình nitrat hóa và tạo bông lắng của bùn hoạt tính diễn ra hoàn hảo.

---

### 7. Quy chuẩn Kỹ thuật và Tiêu chuẩn Thiết kế Áp dụng (Regulatory Standards & Technical Compliance)
#### 7.1. Tiêu chuẩn quốc gia TCVN 7957:2008 về Thoát nước - Mạng lưới và Công trình bên ngoài
- **Điều khoản quy định về bể điều hòa**:
  - Hướng dẫn phương pháp xác định dung tích điều hòa lưu lượng dựa trên biểu đồ tích lũy dòng vào thực tế hoặc hệ số dao động giờ theo quy mô dân số trạm xử lý.
  - Quy định suất tiêu hao năng lượng khuấy trộn cơ học không được nhỏ hơn $0.004 \text{ kW/m}^3$ ($4 \text{ W/m}^3$) đối với nước thải sinh hoạt nhằm chống lắng cặn.
  - Quy định vận tốc dòng chảy tuần hoàn tối thiểu trong bể $\ge 0.15 \text{ m/s}$.
  - Quy định cường độ cấp khí tối thiểu để duy trì điều kiện hiếu khí và chống bốc mùi hôi thối.
#### 7.2. Quy chuẩn kỹ thuật quốc gia QCVN 14:2008/BTNMT về Nước thải Sinh hoạt
- **Mối liên hệ kỹ thuật công nghệ**:
  - Quy định giá trị nồng độ giới hạn cho phép ($C_{max}$) của các thông số ô nhiễm chính xả ra nguồn tiếp nhận: cột A và cột B đối với $BOD_5$, COD, TSS, $NH_4^+$, tổng $N$, tổng $P$.
  - Bể điều hòa đóng vai trò là "lá chắn bảo vệ" tiên quyết của toàn bộ quy trình công nghệ xử lý: nếu không có bể điều hòa làm đều lưu lượng và nồng độ, các đỉnh sốc tải sẽ xuyên qua các công trình lắng và sinh học, dẫn đến hiện tượng trôi bùn, suy giảm hiệu suất nitrat hóa và gây vi phạm tức thời quy chuẩn xả thải QCVN 14:2008/BTNMT.
