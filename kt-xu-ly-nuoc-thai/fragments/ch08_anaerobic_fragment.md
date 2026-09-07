## Chương 08: Xử lý Sinh học Kỵ khí (Biological Anaerobic Unit Processes)

### 8.1. Cơ sở Hóa sinh & Vi sinh của Quá trình Phân hủy Kỵ khí (Biochemistry & Microbiology of Anaerobic Digestion)

#### 8.1.1. Bốn Giai đoạn Chuyển hóa Kỵ khí Liên hoàn (Four Sequential Stages of Anaerobic Digestion)
Quá trình phân hủy kỵ khí là chuỗi phản ứng sinh hóa liên tục được thực hiện bởi mạng lưới consortia vi sinh vật kỵ khí dị dưỡng và cổ khuẩn kỵ khí nghiêm ngặt, chuyển đổi các hợp chất hữu cơ phức tạp thành khí sinh học (chủ yếu là $\text{CH}_4$ và $\text{CO}_2$).

##### 8.1.1.1. Giai đoạn 1: Thủy phân (Hydrolysis)
Quá trình chuyển hóa các đại phân tử hữu cơ dạng hạt hoặc keo không tan thành các phân tử monomer hòa tan đơn giản.

###### 8.1.1.1.1. Cơ chế Enzyme ngoại bào & Động học Thủy phân
- **Cơ chế tiết enzyme ngoại bào:** Vi khuẩn thủy phân (chủ yếu thuộc các chi *Clostridium*, *Bacteroides*, *Bacillus*) bám dính lên bề mặt cơ chất hạt và tiết ra các enzyme ngoại phân giải (extracellular hydrolytic enzymes) như cellulase, amylase, protease, lipase.
- **Phản ứng phân cắt sinh hóa:**
  - *Carbohydrate phức tạp (Polysaccharide):* Bị bẻ gãy liên kết glycosidic tạo thành đường đơn (monosaccharide: glucose, fructose, galactose, xylose).
  - *Protein & Polypeptide:* Bị phân cắt liên kết peptide bởi enzyme protease/peptidase tạo thành các chuỗi peptide ngắn và amino acid tự do.
  - *Lipid & Triacylglycerol:* Bị thủy phân bởi lipase tạo thành glycerol và các axit béo mạch dài (Long-Chain Fatty Acids - LCFA như palmitic, oleic, stearic).
- **Mô hình động học thủy phân:**
  - Động học bậc nhất đối với cơ chất phức tạp:
    $$\frac{dS_p}{dt} = -k_h \cdot S_p$$
    Trong đó:
    - $S_p$: Nồng độ cơ chất dạng hạt (g COD/m³ hoặc mg/L).
    - $k_h$: Hằng số tốc độ thủy phân ($d^{-1}$, điển hình $0.05 - 0.20\text{ d}^{-1}$ ở $35^\circ\text{C}$).
    - $t$: Thời gian phản ứng (d).
  - Đối với cơ chất có cấu trúc màng cellulose/lignin dày, mô hình Contois bề mặt hoặc mô hình Hill thường được sử dụng do tốc độ phụ thuộc vào diện tích bề mặt tiếp xúc của hạt rắn.

###### 8.1.1.1.2. Các yếu tố ảnh hưởng & Tác nhân giới hạn tốc độ (Rate-Limiting Step)
- **Bước giới hạn tốc độ xử lý:** Trong nước thải hoặc bùn thải có hàm lượng chất rắn lơ lửng cao (Particulate COD $> 30 - 40\%$, bùn hoạt tính dư WAS, rác thực phẩm), giai đoạn thủy phân là bước chậm nhất (rate-limiting step) quyết định toàn bộ thời gian lưu bùn (SRT) yêu cầu của hệ thống kỵ khí.
- **Ảnh hưởng của kích thước hạt:** Kích thước hạt rắn càng bé thì tỷ diện tích tiếp xúc ($S/V$) càng lớn, tạo điều kiện thuận lợi cho enzyme ngoại bào tấn công, làm tăng $k_h$.
- **Ảnh hưởng của tiền xử lý (Pretreatment):** Tiền xử lý nhiệt ($60 - 180^\circ\text{C}$), siêu âm (ultrasound disintegration), kiềm hóa ($\text{NaOH}$), hoặc nghiền cơ học giúp phá vỡ màng tế bào vi khuẩn và cấu trúc lignin, tăng tốc độ hòa tan cơ chất lên $200 - 500\%$.

##### 8.1.1.2. Giai đoạn 2: Lên men Axit sinh Axit béo bay hơi (Acidogenesis / Fermentation)
Quá trình chuyển hóa các monomer hòa tan sinh ra từ bước thủy phân thành các axit béo bay hơi mạch ngắn (VFAs), rượu, axit hữu cơ, khí $\text{CO}_2$ và $\text{H}_2$.

###### 8.1.1.2.1. Con đường chuyển hóa Carbon & Quần thể vi khuẩn lên men
- **Quần thể vi sinh vật Acidogenic:** Chủ yếu là các vi khuẩn kỵ khí bắt buộc và kỵ khí tùy tiện (facultative anaerobes) thuộc ngành *Firmicutes*, *Bacteroidetes* (ví dụ *Clostridium*, *Lactobacillus*, *Escherichia*, *Streptococcus*).
- **Tốc độ tăng trưởng cao:** Vi khuẩn lên men có tốc độ sinh trưởng cực nhanh ($\mu_{max} = 1.0 - 2.5\text{ d}^{-1}$) và hệ số sản lượng sinh khối cao ($Y_H = 0.15 - 0.25\text{ g VSS/g COD}$), nhanh hơn nhiều so với vi sinh vật methanogen.
- **Con đường đường phân (Glycolysis / Embden-Meyerhof-Parnas pathway):**
  - Chuyển hóa glucose thành pyruvate qua trung gian NADH:
    $$\text{C}_6\text{H}_{12}\text{O}_6 + 2\text{NAD}^+ \rightarrow 2\text{CH}_3\text{COCOO}^- + 2\text{NADH} + 2\text{H}^+$$
  - Tùy thuộc vào áp suất riêng phần của hydro ($p_{H_2}$) và pH mà pyruvate được chuyển hóa tiếp thành các sản phẩm lên men khác nhau.

###### 8.1.1.2.2. Các sản phẩm chuyển hóa chính (VFAs, Ethanol, Lactic acid, $H_2$, $CO_2$)
- **Phổ sản phẩm lên men:**
  - *Axit béo bay hơi (VFAs):* Acetic acid ($\text{CH}_3\text{COOH}$), Propionic acid ($\text{CH}_3\text{CH}_2\text{COOH}$), Butyric acid ($\text{CH}_3\text{CH}_2\text{CH}_2\text{COOH}$), Iso-butyric, Valeric, Iso-valeric acids.
  - *Rượu và axit trung gian:* Ethanol ($\text{C}_2\text{H}_5\text{OH}$), Lactic acid ($\text{CH}_3\text{CHOHCOOH}$).
  - *Khí hòa tan:* Khí hydro ($\text{H}_2$) và carbon dioxide ($\text{CO}_2$).
- **Phương trình lên men sinh butyrate và acetate:**
  $$\text{C}_6\text{H}_{12}\text{O}_6 + 2\text{H}_2\text{O} \rightarrow 2\text{CH}_3\text{COOH} + 2\text{CO}_2 + 4\text{H}_2 \quad (\Delta G^{\circ'} = -206.1\text{ kJ/rxn})$$
  $$\text{C}_6\text{H}_{12}\text{O}_6 \rightarrow \text{CH}_3\text{CH}_2\text{CH}_2\text{COOH} + 2\text{CO}_2 + 2\text{H}_2 \quad (\Delta G^{\circ'} = -254.8\text{ kJ/rxn})$$
- **Phương trình lên men sinh propionate:**
  $$\text{C}_6\text{H}_{12}\text{O}_6 + 2\text{H}_2 \rightarrow 2\text{CH}_3\text{CH}_2\text{COOH} + 2\text{H}_2\text{O} \quad (\Delta G^{\circ'} = -358.2\text{ kJ/rxn})$$
  *(Lưu ý: Sự hình thành propionate tiêu thụ $H_2$, thường xảy ra khi áp suất hydro nội bào tăng cao).*

##### 8.1.1.3. Giai đoạn 3: Sinh Axetat (Acetogenesis)
Quá trình oxy hóa các sản phẩm trung gian của giai đoạn acidogenesis (propionate, butyrate, ethanol, LCFA) thành acetate, $\text{H}_2$ và $\text{CO}_2$ bởi nhóm vi khuẩn đặc thù.

###### 8.1.1.3.1. Vi khuẩn sinh Axetat bắt buộc (Obligate Hydrogen-Producing Acetogens - OHPA)
- **Đặc điểm sinh lý vi khuẩn OHPA:** Thuộc các chi *Syntrophobacter* (chuyên phân giải propionate như *Syntrophobacter wolinii*), *Syntrophomonas* (chuyên phân giải butyrate và axit béo chuỗi dài như *Syntrophomonas wolfei*), *Pelotomaculum*.
- **Hệ số sinh trưởng thấp:** Vi khuẩn OHPA có tốc độ tăng trưởng rất thấp ($\mu_{max} \approx 0.1 - 0.2\text{ d}^{-1}$) và hệ số năng lượng tự do thấp, đòi hỏi thời gian lưu bùn dài và điều kiện môi trường ổn định.

###### 8.1.1.3.2. Chuyển hóa Axit béo chuỗi ngắn (Propionate, Butyrate) thành Acetate
- **Oxy hóa Propionate:**
  $$\text{CH}_3\text{CH}_2\text{COO}^- + 3\text{H}_2\text{O} \rightarrow \text{CH}_3\text{COO}^- + \text{HCO}_3^- + \text{H}^+ + 3\text{H}_2 \quad (\Delta G^{\circ'} = +76.1\text{ kJ/mol})$$
- **Oxy hóa Butyrate:**
  $$\text{CH}_3\text{CH}_2\text{CH}_2\text{COO}^- + 2\text{H}_2\text{O} \rightarrow 2\text{CH}_3\text{COO}^- + \text{H}^+ + 2\text{H}_2 \quad (\Delta G^{\circ'} = +48.3\text{ kJ/mol})$$
- **Oxy hóa Ethanol:**
  $$\text{CH}_3\text{CH}_2\text{OH} + \text{H}_2\text{O} \rightarrow \text{CH}_3\text{COO}^- + \text{H}^+ + 2\text{H}_2 \quad (\Delta G^{\circ'} = +9.6\text{ kJ/mol})$$
- **Ý nghĩa nhiệt động lực học:** Cả 3 phản ứng trên đều có $\Delta G^{\circ'} > 0$ ở điều kiện tiêu chuẩn, nghĩa là phản ứng **không thể tự xảy ra** trừ khi sản phẩm ($\text{H}_2$) được tiêu thụ liên tục để giữ nồng độ cực thấp trong dung dịch.

##### 8.1.1.4. Giai đoạn 4: Sinh Methane (Methanogenesis)
Giai đoạn cuối cùng trong chuỗi phân hủy kỵ khí, biến đổi acetate, hydro và carbon dioxide thành khí methane ($\text{CH}_4$). Thực hiện bởi Cổ khuẩn sinh methane (Methanogenic Archaea) kỵ khí tuyệt đối.

###### 8.1.1.4.1. Nhóm vi sinh vật Cổ khuẩn Metan hóa Phân giải Axetat (Acetoclastic Methanogens)
- **Đặc trưng:** Đóng góp khoảng $65 - 72\%$ tổng lượng methane sinh ra trong quá trình phân hủy kỵ khí nước thải đô thị và công nghiệp thông thường.
- **Phương trình chuyển hóa sinh hóa:**
  $$\text{CH}_3\text{COO}^- + \text{H}_2\text{O} \rightarrow \text{CH}_4 + \text{HCO}_3^- \quad (\Delta G^{\circ'} = -31.0\text{ kJ/mol})$$
- **Hai chi vi sinh vật chính:**
  - *Methanosaeta (trước đây là Methanothrix):*
    - Hình thái: Dạng sợi mảnh dài, tạo mạng lưới khung xương vững chắc cho hạt bùn UASB.
    - Ái lực cơ chất cực cao: $K_s$ rất thấp ($20 - 40\text{ mg COD/L}$ acetate), tăng trưởng ưu thế ở nồng độ acetate thấp ($< 100 - 150\text{ mg/L}$).
    - Tốc độ sinh trưởng chậm: $\mu_{max} \approx 0.10 - 0.12\text{ d}^{-1}$.
  - *Methanosarcina:*
    - Hình thái: Dạng cụm cầu khuẩn (coccoid packets / sarcina clumps), có lớp vỏ bọc dày chống chịu sốc môi trường.
    - Ái lực cơ chất thấp hơn: $K_s$ cao ($200 - 400\text{ mg COD/L}$ acetate), phát triển mạnh khi nồng độ acetate cao hoặc khi bể bị quá tải hữu cơ.
    - Tốc độ sinh trưởng nhanh hơn: $\mu_{max} \approx 0.30 - 0.40\text{ d}^{-1}$. Có khả năng linh hoạt sử dụng cả acetate lẫn $\text{H}_2/\text{CO}_2$ và methanol.

###### 8.1.1.4.2. Nhóm vi sinh vật Cổ khuẩn Metan hóa Khử Hydro (Hydrogenotrophic Methanogens)
- **Đặc trưng:** Đóng góp khoảng $28 - 35\%$ tổng lượng methane sinh ra; đóng vai trò then chốt "hút sạch" hydro để duy trì hoạt động của vi khuẩn acetogenic.
- **Phương trình chuyển hóa sinh hóa:**
  $$4\text{H}_2 + \text{HCO}_3^- + \text{H}^+ \rightarrow \text{CH}_4 + 3\text{H}_2\text{O} \quad (\Delta G^{\circ'} = -135.6\text{ kJ/mol})$$
- **Các chi vi sinh vật chính:** *Methanobacterium*, *Methanobrevibacter*, *Methanococcus*, *Methanospirillum*.
- **Tốc độ sinh trưởng:** Rất nhanh so với nhóm acetoclastic ($\mu_{max} = 0.4 - 1.2\text{ d}^{-1}$), thời gian thế hệ chỉ từ $6 - 12\text{ giờ}$ ở $35^\circ\text{C}$.

###### 8.1.1.4.3. Nhóm vi sinh vật Cổ khuẩn Metan hóa Methyltrophic (Methylotrophic Methanogens)
- **Chuyển hóa các hợp chất methyl:** Sử dụng methanol, methylamines, dimethyl sulfide làm cơ chất.
- **Phương trình chuyển hóa methanol điển hình:**
  $$4\text{CH}_3\text{OH} \rightarrow 3\text{CH}_4 + \text{CO}_2 + 2\text{H}_2\text{O} \quad (\Delta G^{\circ'} = -319.4\text{ kJ/rxn})$$
- **Chi đại diện:** *Methanolobus*, *Methanosarcina*. Thường đóng vai trò quan trọng trong nước thải công nghiệp hóa chất, bột giấy, tái chế giấy.

---

#### 8.1.2. Chuyển hóa Hydro Gian bào & Cân bằng Nhiệt động lực học (Interspecies Hydrogen Transfer & Thermodynamics)

##### 8.1.2.1. Nguyên lý Quan hệ Cộng sinh Dưỡng hỗ (Syntrophic Cooperation)

###### 8.1.2.1.1. Năng lượng tự do Gibbs ($\Delta G^{\circ'}$) và Áp suất riêng phần $H_2$
- **Mối liên hệ nhiệt động lực học thực tế:** Năng lượng tự do thực tế của phản ứng chuyển hóa propionate hoặc butyrate phụ thuộc trực tiếp vào nhiệt độ và áp suất riêng phần khí hydro tự do ($p_{H_2}$) theo định luật Nernst:
  $$\Delta G' = \Delta G^{\circ'} + R \cdot T \cdot \ln\left( \frac{[\text{Acetate}] \cdot [\text{HCO}_3^-] \cdot (p_{H_2})^3}{[\text{Propionate}]} \right)$$
  Trong đó:
  - $\Delta G^{\circ'} = +76.1\text{ kJ/mol}$ (ở $25^\circ\text{C}, 1\text{ atm}$, pH 7.0).
  - $R = 8.314\times 10^{-3}\text{ kJ/(mol}\cdot\text{K)}$.
  - $T$: Nhiệt độ tuyệt đối (K).

###### 8.1.2.1.2. Ngưỡng áp suất riêng phần Hydro giới hạn ($p_{H_2} < 10^{-4}\text{ atm}$)
- **Cửa sổ nhiệt động học (Thermodynamic Window):**
  - Để phản ứng oxy hóa propionate có $\Delta G' < 0$ (phản ứng tự phát), áp suất riêng phần $p_{H_2}$ bắt buộc phải duy trì ở mức **cực thấp**:
    $$p_{H_2} < 10^{-4}\text{ atm} \quad (10 - 100\text{ Pa}, \text{tương đương } [\text{H}_2]_{aq} < 10^{-6}\text{ mol/L})$$
  - Đồng thời, để phản ứng sinh methane từ hydro của Methanogen xảy ra thuận lợi ($\Delta G' < -15\text{ kJ/mol}$ để tổng hợp được 1 ATP), áp suất $p_{H_2}$ phải lớn hơn ngưỡng tối thiểu:
    $$p_{H_2} > 10^{-6}\text{ atm} \quad (0.1\text{ Pa})$$
  - Do đó, "cửa sổ nhiệt động học" cho sự cộng sinh syntrophic chỉ tồn tại trong dải hẹp:
    $$10^{-6}\text{ atm} \le p_{H_2} \le 10^{-4}\text{ atm}$$
- **Truyền dẫn Hydro gian bào (Interspecies Hydrogen Transfer - IHT):**
  - Vi khuẩn sinh axetat (OHPA) và cổ khuẩn methanogen khử hydro phải nằm ở khoảng cách vật lý cực gần ($< 1 - 2\ \mu\text{m}$) bên trong cấu trúc bông bùn hoặc hạt bùn kỵ khí.
  - Ngoài IHT qua khuếch tán phân tử, quá trình truyền electron trực tiếp gian bào (Direct Interspecies Electron Transfer - DIET) qua pili dẫn điện (nanowires) hoặc vật liệu carbon dẫn điện (biochar, than hoạt tính PAC) cũng đóng vai trò gia tốc phản ứng.

##### 8.1.2.2. Động lực Tích lũy Axit béo bay hơi (VFAs Dynamics & Inhibition)

###### 8.1.2.2.1. Đặc trưng các loại VFA: Acetic, Propionic, Butyric, Iso-butyric, Valeric
- **Acetic Acid ($\text{CH}_3\text{COOH}$):** Cơ chất trực tiếp của Methanosaeta và Methanosarcina; ít độc nhất, nồng độ an toàn trong bể ổn định $< 200 - 300\text{ mg/L}$.
- **Propionic Acid ($\text{CH}_3\text{CH}_2\text{COOH}$):** Axit khó chuyển hóa nhất vì rào cản năng lượng Gibbs dương cao; là tác nhân ức chế hàng đầu đối với methanogens.
- **Butyric & Iso-butyric Acid:** Dễ phân giải hơn propionic acid; nồng độ tăng cao phản ánh giai đoạn acidogenesis bị biến động tải.

###### 8.1.2.2.2. Chỉ số Độc hại của Axit Propionic và Tỷ lệ Propionate/Acetate
- **Ngưỡng ức chế:** Nồng độ Propionate vượt quá $1,000\text{ mg/L}$ bắt đầu ức chế rõ rệt hoạt tính methanogen; nồng độ $> 2,000 - 3,000\text{ mg/L}$ có thể gây tê liệt hoàn toàn quá trình tạo khí methane.
- **Tỷ lệ Propionate / Acetate:**
  - Vận hành ổn định: $[\text{Propionate}] / [\text{Acetate}] < 0.1 - 0.2$.
  - Dấu hiệu cảnh báo sớm: Khi tỷ lệ này tăng vượt $0.5 - 0.8$, hệ thống đang chịu quá tải hoặc mất cân bằng vi sinh kỵ khí nghiêm trọng.

##### 8.1.2.3. Cân bằng Đệm và Tỷ số VFA/Alkalinity (Buffering Capacity & Stability Indicator)

###### 8.1.2.3.1. Hệ đệm Bicarbonate ($CO_2 - HCO_3^-$) trong Môi trường Kỵ khí
- Khí quyển trong bể kỵ khí chứa $30 - 40\%\ \text{CO}_2$. Sự hòa tan của $\text{CO}_2$ thiết lập cân bằng đệm carbonic:
  $$\text{CO}_2\text{ (khí)} \rightleftharpoons \text{CO}_2\text{ (lỏng)} + \text{H}_2\text{O} \rightleftharpoons \text{H}_2\text{CO}_3^* \rightleftharpoons \text{H}^+ + \text{HCO}_3^-$$
- Độ kiềm Bicarbonate (Bicarbonate Alkalinity - BA) có nhiệm vụ trung hòa lập tức các proton $\text{H}^+$ giải phóng từ VFAs:
  $$\text{CH}_3\text{COOH} + \text{HCO}_3^- \rightarrow \text{CH}_3\text{COO}^- + \text{H}_2\text{O} + \text{CO}_2 \uparrow$$
- Để giữ pH bể kỵ khí không bị tụt dốc khi phát sinh axit, độ kiềm Bicarbonate cần duy trì ở mức tối thiểu:
  $$\text{Alkalinity} \ge 2,500 - 4,000\text{ mg CaCO}_3\text{/L}$$

###### 8.1.2.3.2. Chỉ số Tỷ số VFA/Alkalinity (Chỉ số Ripley / FOS/TAC) và Ngưỡng Kiểm soát An toàn
- **Định nghĩa:** Tỷ số giữa tổng nồng độ axit béo bay hơi (tính theo $\text{mg CH}_3\text{COOH/L}$) và tổng độ kiềm (tính theo $\text{mg CaCO}_3\text{/L}$):
  $$\text{Tỷ số Ripley} = \frac{\text{VFA (mg/L as CH}_3\text{COOH)}}{\text{Total Alkalinity (mg/L as CaCO}_3)}$$
- **Thang đánh giá trạng thái vận hành kỵ khí:**
  - **$\text{VFA/Alk} < 0.3 - 0.4$:** Hệ thống vận hành tối ưu, khả năng đệm dồi dào, sinh khí metan ổn định.
  - **$0.4 \le \text{VFA/Alk} \le 0.6$:** Trạng thái bất ổn định nhẹ (process instability), tích lũy axit nhẹ; cần giảm tải nạp hoặc theo dõi chặt chẽ.
  - **$0.6 < \text{VFA/Alk} \le 0.8$:** Hệ thống bị quá tải nghiêm trọng, nguy cơ chua hóa cao; phải lập tức giảm mạnh lưu lượng nước thải cấp vào và bổ sung kiềm.
  - **$\text{VFA/Alk} > 0.8$:** Bể kỵ khí đã bị "chua hóa hoàn toàn" (sour digester), hoạt tính methanogen bị ức chế nặng nề, pH tụt dốc, ngừng sinh khí metan.

---

### 8.2. Các Thông số Vận hành Cốt lõi & Kiểm soát Ức chế Độc tính (Operating Parameters & Inhibition Control)

#### 8.2.1. Vùng Nhiệt độ Hoạt động (Temperature Regimes)

##### 8.2.1.1. Chế độ Nhiệt độ Ưa ấm (Mesophilic Regime: $35 - 38^\circ\text{C}$)

###### 8.2.1.1.1. Đặc điểm động học sinh trưởng, độ ổn định và tiêu thụ năng lượng
- **Nhiệt độ tối ưu:** $35 - 37^\circ\text{C}$ (dải phổ biến nhất trong thực tế công nghiệp).
- **Hằng số động học đặc trưng tại $35^\circ\text{C}$:**
  - Tốc độ sinh trưởng cực đại: $\mu_m = 0.30 - 0.38\text{ d}^{-1}$ (điển hình $0.35\text{ d}^{-1}$).
  - Hệ số phân hủy nội bào: $b_H = 0.02 - 0.04\text{ d}^{-1}$ (điển hình $0.03\text{ d}^{-1}$).
  - Hệ số sản lượng: $Y_H = 0.05 - 0.10\text{ g VSS/g COD}$ (điển hình $0.08\text{ g VSS/g COD}$).
  - Hằng số nửa tốc độ: $K_s = 60 - 500\text{ mg COD/L}$ (điển hình $120\text{ mg/L}$).
- **Ưu điểm:** Khả năng duy trì cân bằng vi sinh cao, ít nhạy cảm với biến động tải, bùn lắng tốt, tiêu thụ nhiệt gia nhiệt ở mức vừa phải.

###### 8.2.1.1.2. Độ nhạy nhiệt độ ($\Delta T < \pm 1^\circ\text{C/d}$)
- Quần thể methanogen cực kỳ mẫn cảm với sự thay đổi nhiệt độ đột ngột.
- Biến thiên nhiệt độ trong ngày phải được khống chế nghiêm ngặt:
  $$\Delta T \le \pm 1.0 - 1.5^\circ\text{C/ngày}$$
- Biến thiên nhiệt độ $\Delta T > 2 - 3^\circ\text{C/ngày}$ có thể làm giảm $30 - 50\%$ hoạt tính sinh methane và dẫn đến tích lũy VFA tức thì.

##### 8.2.1.2. Chế độ Nhiệt độ Ưa nhiệt (Thermophilic Regime: $55 - 60^\circ\text{C}$)

###### 8.2.1.2.1. Tốc độ chuyển hóa cao, khử trùng mầm bệnh, rủi ro tích lũy VFA
- **Nhiệt độ tối ưu:** $55^\circ\text{C}$.
- **Tốc độ phản ứng sinh hóa cao:** Tốc độ phản ứng tăng gấp $2 - 3$ lần theo quy tắc Van 't Hoff / Arrhenius, cho phép áp dụng tải trọng hữu cơ thể tích (OLR) cao hơn $50 - 100\%$.
- **Khả năng tiêu diệt mầm bệnh:** Tiêu diệt hầu như hoàn toàn giun sán, trứng ký sinh trùng, vi khuẩn gây bệnh (*Salmonella*, *E. coli*), đáp ứng tiêu chuẩn loại A cho bùn sau xử lý.
- **Rủi ro vận hành:**
  - Độ nhạy cảm nhiệt độ cực cao ($\Delta T < \pm 0.5^\circ\text{C/ngày}$).
  - Nồng độ amonia tự do ($\text{NH}_3$) tăng cao do cân bằng hóa học dịch chuyển ở nhiệt độ cao, gây ức chế methanogen.
  - Bùn hạt khó hình thành hoặc cấu trúc hạt kém ổn định hơn so với mesophilic.

###### 8.2.1.2.2. So sánh hiệu quả giữa Mesophilic và Thermophilic
| Tiêu chí | Vùng Ưa ấm (Mesophilic $35 - 38^\circ\text{C}$) | Vùng Ưa nhiệt (Thermophilic $55 - 60^\circ\text{C}$) |
| :--- | :--- | :--- |
| **Thời gian lưu bùn yêu cầu ($\text{SRT}_{min}$)** | $15 - 25\text{ ngày}$ | $8 - 12\text{ ngày}$ |
| **Tải trọng OLR cho phép** | Trung bình - Cao ($5 - 15\text{ kg COD/m}^3\cdot\text{d}$) | Rất cao ($15 - 30\text{ kg COD/m}^3\cdot\text{d}$) |
| **Độ ổn định quá trình** | Rất cao, bùn đệm tốt | Nhạy cảm với sốc tải và sốc nhiệt |
| **Chất lượng nước đầu ra** | COD hòa tan thấp hơn, ổn định | Thường có VFA dư cao hơn ($100 - 300\text{ mg/L}$) |
| **Năng lượng gia nhiệt** | Thấp - Trung bình | Rất cao (yêu cầu nguồn nhiệt thải dồi dào) |

##### 8.2.1.3. Vận hành ở Nhiệt độ Thấp (Psychrophilic / Ambient: $< 25^\circ\text{C}$)
- Áp dụng trong xử lý nước thải sinh hoạt đô thị ở vùng nhiệt đới/cận nhiệt đới ($20 - 25^\circ\text{C}$) hoặc mùa đông ($15 - 20^\circ\text{C}$).
- **Quy tắc bù trừ SRT:** Tốc độ phản ứng giảm, đòi hỏi phải tăng mạnh thời gian lưu bùn (SRT) để ngăn ngừa rửa trôi vi sinh vật methanogen:
  - Ở $35^\circ\text{C}$: SRT khuyến nghị $\ge 25\text{ ngày}$.
  - Ở $30^\circ\text{C}$: SRT khuyến nghị $\ge 30\text{ ngày}$.
  - Ở $25^\circ\text{C}$: SRT khuyến nghị $\ge 60\text{ ngày}$.
  - Ở $20^\circ\text{C}$: SRT khuyến nghị $\ge 100\text{ ngày}$.
  - Ở $15^\circ\text{C}$: SRT khuyến nghị $\ge 140\text{ ngày}$.

---

#### 8.2.2. Kiểm soát pH và Thế Oxy hóa - Khử (pH Control & Oxidation-Reduction Potential ORP)

##### 8.2.2.1. Dải pH Tối ưu cho Quần thể Kỵ khí ($6.8 - 7.4$)

###### 8.2.2.1.1. Tác động của pH lên Hoạt tính Enzyme Methanogen và Vi khuẩn Axit hóa
- **Dải pH tối ưu tuyệt đối của Methanogen:**
  $$6.8 \le \text{pH} \le 7.4 \quad (\text{tốt nhất } 7.0 - 7.2)$$
- **Sự lệch pha pH tối ưu giữa 2 nhóm vi sinh:**
  - Vi khuẩn lên men acidogenic: Hoạt động mạnh ở dải pH rộng ($5.0 - 6.5$).
  - Cổ khuẩn methanogen: Bị ức chế nghiêm trọng khi $\text{pH} < 6.5$; nếu $\text{pH} < 6.0$, hoạt tính tạo methane giảm $> 90\%$.
- Hiện tượng tự gia tốc axit hóa (acid runaway): Khi pH bắt đầu giảm, methanogen bị ức chế trong khi acidogen vẫn tiếp tục sinh VFA, dẫn đến pH tụt dốc nhanh chóng.

###### 8.2.2.1.2. Biện pháp Bổ sung Hóa chất Nâng kiềm (Alkalinity Chemicals: $\text{NaHCO}_3$, $\text{NaOH}$, $\text{Ca(OH)}_2$)
- **Natri Bicarbonate ($\text{NaHCO}_3$):**
  - Hóa chất lý tưởng nhất cho hệ thống kỵ khí: Cung cấp trực tiếp ion $\text{HCO}_3^-$ đệm mà không làm vọt pH cục bộ.
  - Phản ứng an toàn: $\text{NaHCO}_3 \rightarrow \text{Na}^+ + \text{HCO}_3^-$.
- **Natri Hydroxide ($\text{NaOH}$):**
  - Rẻ hơn nhưng đòi hỏi hệ thống châm định lượng chính xác; phản ứng gián tiếp với $\text{CO}_2$ hòa tan:
    $$\text{NaOH} + \text{CO}_2 \rightarrow \text{NaHCO}_3$$
  - Nguy cơ: Gây tăng pH cục bộ tại điểm châm làm chết tế bào methanogen.
- **Vôi tôi ($\text{Ca(OH)}_2$):**
  - Giá thành rẻ nhất; phản ứng tạo $\text{Ca(HCO}_3)_2$.
  - Nhược điểm: Tạo kết tủa Canxi cacbonat ($\text{CaCO}_3$) gây đóng cặn tắc nghẽn đường ống, làm nặng hạt bùn kỵ khí và tích tụ tro vô cơ trong bể.

##### 8.2.2.2. Thế Oxy hóa - Khử (ORP / Redox Potential)

###### 8.2.2.2.1. Ngưỡng ORP cho Methanogenesis ($E_h < -300\text{ mV}$ đến $-350\text{ mV}$)
- Methanogen là vi sinh vật kỵ khí bắt buộc nghiêm ngặt (strict anaerobes).
- Để quá trình sinh methane diễn ra liên tục, thế oxy hóa - khử danh định ($E_h$) trong vùng phản ứng phải đạt:
  $$E_h \le -300\text{ mV} \quad (\text{dải tối ưu } -330\text{ mV đến } -360\text{ mV})$$

###### 8.2.2.2.2. Tác động của sự xâm nhập Oxy và Nitrate
- **Oxy hòa tan ($\text{DO}$):**
  - Oxy làm tăng ORP lên vùng dương ($> 0\text{ mV}$), phá hủy các enzyme chứa kim loại chuyển tiếp của methanogen (như hydrogenase, methyl-coenzyme M reductase).
  - Tuy nhiên, trong hạt bùn UASB dày, lớp vi khuẩn kỵ khí tùy tiện ngoài vỏ tiêu thụ vết oxy xâm nhập, bảo vệ lõi methanogen bên trong.
- **Nitrate ($\text{NO}_3^-$):**
  - Nitrate đóng vai trò chất nhận electron ưu tiên hơn $\text{CO}_2$, làm tăng ORP lên khoảng $-100\text{ mV}$ đến $0\text{ mV}$.
  - Vi khuẩn khử nitrate (Denitrifiers) sẽ cạnh tranh cơ chất với methanogens và các chất trung gian như $\text{NO}_2^-$, $\text{NO}$ gây ức chế độc hại trực tiếp lên methanogen.

---

#### 8.2.3. Cân bằng Dinh dưỡng và Vi lượng (Nutrient & Micronutrient Requirements)

##### 8.2.3.1. Tỷ lệ Đa lượng COD : N : P

###### 8.2.3.1.1. Tỷ lệ kinh nghiệm COD : N : P = $250:5:1$ đến $350:5:1$
- Do hệ số sản lượng bùn kỵ khí rất thấp ($Y_H \approx 0.05 - 0.10\text{ g VSS/g COD}$, chỉ bằng $1/5$ so với bùn hiếu khí), nhu cầu dinh dưỡng đa lượng N và P thấp hơn đáng kể:
  - Ở tải trọng cao (tốc độ sinh trưởng nhanh): $\text{COD} : \text{N} : \text{P} \approx 250 : 5 : 1$.
  - Ở tải trọng thấp / SRT dài: $\text{COD} : \text{N} : \text{P} \approx 350 : 5 : 1$ đến $500 : 5 : 1$.

###### 8.2.3.1.2. Tỷ lệ dựa trên Hệ số Sản lượng $(\text{COD}/Y) : \text{N} : \text{P} : \text{S} = (50/Y) : 5 : 1 : 1$
- **Công thức lượng tế chuẩn xác:**
  $$\left( \frac{\text{COD}}{Y} \right) : \text{N} : \text{P} : \text{S} = \left( \frac{50}{Y} \right) : 5 : 1 : 1$$
- Với hệ số sản lượng điển hình $Y = 0.08\text{ g VSS/g COD}$:
  $$\frac{50}{0.08} = 625 \implies \text{COD} : \text{N} : \text{P} : \text{S} = 625 : 5 : 1 : 1 \quad (\text{hoặc } 125 : 1 : 0.2 : 0.2)$$
- Trong đó:
  - Hàm lượng Nitơ trong tế bào sinh khối: $f_N = 12.0\%\ \text{VSS}$ ($0.12\text{ g N/g VSS}$).
  - Hàm lượng Phospho trong tế bào sinh khối: $f_P = 2.4\%\ \text{VSS}$ ($0.024\text{ g P/g VSS}$).
  - Hàm lượng Lưu huỳnh cho cấu trúc protein tế bào: $f_S = 1.0 - 2.0\%\ \text{VSS}$.

##### 8.2.3.2. Vai trò của Vi chất Dinh dưỡng và Kim loại Vi lượng (Trace Elements)

###### 8.2.3.2.1. Nhu cầu Sắt ($\text{Fe}$), Nickel ($\text{Ni}$), Cobalt ($\text{Co}$), Molybdenum ($\text{Mo}$)
Các kim loại vết đóng vai trò trung tâm hoạt hóa trong các enzyme xúc tác quá trình sinh methane:
- **Sắt ($\text{Fe}$):** Nhu cầu cao nhất ($1 - 10\text{ mg/L}$); thành phần của cytochrome và protein chứa cụm $\text{Fe-S}$ (ferredoxin) vận chuyển electron.
- **Nickel ($\text{Ni}$):** Nồng độ yêu cầu $0.05 - 0.20\text{ mg/L}$; thành phần cấu tạo cốt lõi của Coenzyme $\text{F}_{430}$ trong enzyme Methyl-coenzyme M reductase.
- **Cobalt ($\text{Co}$):** Nồng độ yêu cầu $0.05 - 0.15\text{ mg/L}$; thành phần của Cobamide (Vitamin $\text{B}_{12}$ tương tự) tham gia chuyển nhóm methyl.
- **Molybdenum ($\text{Mo}$) & Tungsten ($\text{W}$):** Nồng độ yêu cầu $0.05 - 0.10\text{ mg/L}$; tham gia enzyme Formate dehydrogenase.
- **Kẽm ($\text{Zn}$), Mangan ($\text{Mn}$), Selenium ($\text{Se}$):** Cần thiết cho cấu trúc enzyme heterodisulfide reductase.

###### 8.2.3.2.2. Coenzyme $F_{420}$, Coenzyme M, Vitamin $B_{12}$ trong quá trình tạo Methane
- **Coenzyme $\text{F}_{420}$:** Coenzyme huỳnh quang đặc trưng của methanogen (phát huỳnh quang xanh lục lam dưới tia cực tím bước sóng $420\text{ nm}$), là chất mang electron hydro.
- **Coenzyme M (2-mercaptoethanesulfonate - HS-CoM):** Coenzyme nhỏ nhất, chất mang nhóm methyl cuối cùng trước khi bị khử thành $\text{CH}_4$.

---

#### 8.2.4. Các Tác nhân Ức chế và Ngưỡng Độc tính (Toxicity & Inhibition Thresholds)

##### 8.2.4.1. Ức chế bởi Amonia và Amoni tự do ($\text{NH}_3\text{-N} / \text{NH}_4^+$)

###### 8.2.4.1.1. Cân bằng phân ly $\text{NH}_3$ / $\text{NH}_4^+$ theo pH và Nhiệt độ
- Trong môi trường nước, amonia tồn tại ở 2 dạng cân bằng:
  $$\text{NH}_4^+ \rightleftharpoons \text{NH}_3\text{ (tự do)} + \text{H}^+ \quad (pK_a \approx 9.25 \text{ ở } 25^\circ\text{C}, \approx 8.95 \text{ ở } 35^\circ\text{C})$$
- Tỷ lệ Amonia tự do (Free Ammonia Nitrogen - FAN):
  $$\text{FAN} = \frac{\text{TAN}}{1 + 10^{(pK_a - \text{pH})}}$$
- FAN tăng mạnh khi pH tăng hoặc nhiệt độ tăng. FAN là phân tử không mang điện, có khả năng khuếch tán thụ động qua màng phospholipid của tế bào vi khuẩn, làm mất cân bằng gradient proton và ức chế enzyme nội bào.

###### 8.2.4.1.2. Ngưỡng độc tính Amonia tổng ($> 1,500\text{ mg/L}$) và Amonia tự do ($> 80 - 100\text{ mg/L}$)
- **Tổng Amonia Nitơ (TAN = $\text{NH}_4^+ + \text{NH}_3$):**
  - Dưới $200\text{ mg/L}$ TAN: Dinh dưỡng thiết yếu.
  - $200 - 1,000\text{ mg/L}$ TAN: Không có tác động tiêu cực.
  - $1,500 - 3,000\text{ mg/L}$ TAN: Bắt đầu ức chế methanogenesis (đặc biệt ở $\text{pH} > 7.4$).
  - Trên $3,000\text{ mg/L}$ TAN: Ức chế nặng đối với tất cả các nhóm methanogen chưa thích nghi.
- **Amonia tự do (FAN):**
  - Ngưỡng ức chế xuất hiện khi $\text{FAN} > 80 - 100\text{ mg/L}$.
  - Giải pháp vận hành: Khống chế pH nghiêm ngặt trong dải $6.8 - 7.1$ khi xử lý nước thải giàu đạm để giữ amonia ở dạng ion $\text{NH}_4^+$ ít độc.

##### 8.2.4.2. Ức chế bởi Hợp chất Lưu huỳnh và Sulfide ($\text{H}_2\text{S} / \text{S}^{2-}$)

###### 8.2.4.2.1. Cạnh tranh cơ chất giữa Vi khuẩn Khử Sulfate (SRB) và Methanogens
- Khi nước thải chứa sulfate ($\text{SO}_4^{2-}$), vi khuẩn khử sulfate (Sulfate-Reducing Bacteria - SRB) cạnh tranh electron với methanogen:
  - Cạnh tranh $\text{H}_2$: $\text{SO}_4^{2-} + 4\text{H}_2 + 2\text{H}^+ \rightarrow \text{H}_2\text{S} + 4\text{H}_2\text{O}$ ($\Delta G^{\circ'} = -152.2\text{ kJ/mol}$).
  - Cạnh tranh Acetate: $\text{CH}_3\text{COO}^- + \text{SO}_4^{2-} + \text{H}^+ \rightarrow 2\text{HCO}_3^- + \text{H}_2\text{S}$ ($\Delta G^{\circ'} = -63.0\text{ kJ/mol}$).
- SRB có ái lực cơ chất cao hơn ($K_s$ thấp hơn) và sinh năng lượng nhiều hơn methanogens, do đó SRB chiếm ưu thế, làm giảm sản lượng khí methane.
- Tỷ lệ $\text{COD}/\text{SO}_4^{2-}$ quyết định:
  - $\text{COD}/\text{SO}_4^{2-} > 10$: Methanogenesis chiếm ưu thế tuyệt đối ($> 95\%\ \text{COD}$ chuyển hóa thành $\text{CH}_4$).
  - $2 < \text{COD}/\text{SO}_4^{2-} < 10$: Có sự cạnh tranh song song; $\text{H}_2\text{S}$ sinh ra đáng kể.
  - $\text{COD}/\text{SO}_4^{2-} < 2$: SRB áp đảo; phần lớn electron chuyển sang khử sulfate, nguy cơ ngộ độc sulfide rất cao.

###### 8.2.4.2.2. Ngưỡng độc tính của Sulfide hòa tan ($> 200\text{ mg/L}$) và $\text{H}_2\text{S}$ tự do ($> 50\text{ mg/L}$)
- **Cân bằng hòa tan Sulfide:**
  $$\text{H}_2\text{S}\text{ (khí)} \rightleftharpoons \text{H}_2\text{S}\text{ (lỏng)} \rightleftharpoons \text{HS}^- + \text{H}^+ \rightleftharpoons \text{S}^{2-} + 2\text{H}^+ \quad (pK_{a1} \approx 7.0)$$
- Ở $\text{pH} \approx 7.0$, khoảng $50\%$ sulfide tồn tại dưới dạng phân tử $\text{H}_2\text{S}$ tự do hòa tan. $\text{H}_2\text{S}$ dễ dàng xuyên qua màng sinh chất và làm bất hoạt các enzyme chứa sắt.
- **Ngưỡng độc tính:**
  - Tổng sulfide hòa tan: Phải duy trì $< 200\text{ mg/L}$ (mục tiêu an toàn $< 100\text{ mg/L}$ sau pha loãng hoặc tuần hoàn).
  - Khí $\text{H}_2\text{S}$ hòa tan tự do: Ngưỡng ức chế $50 - 100\text{ mg/L}$.

##### 8.2.4.3. Ức chế bởi Kim loại Nặng và Cation Kim loại Nhẹ (Heavy Metals & Light Metal Cations)

###### 8.2.4.3.1. Kim loại nhẹ: $\text{Na}^+$, $\text{K}^+$, $\text{Ca}^{2+}$, $\text{Mg}^{2+}$
Cation kim loại nhẹ có đặc tính kích thích ở nồng độ thấp và ức chế ở nồng độ cao (hiện tượng lưỡng pha):
- **Natri ($\text{Na}^+$):**
  - Kích thích sinh trưởng: $100 - 200\text{ mg/L}$.
  - Ức chế vừa: $3,500 - 5,500\text{ mg/L}$.
  - Ức chế mạnh: $> 8,000\text{ mg/L}$.
- **Kali ($\text{K}^+$):**
  - Kích thích: $200 - 400\text{ mg/L}$.
  - Ức chế vừa: $2,500 - 4,500\text{ mg/L}$.
  - Ức chế mạnh: $> 12,000\text{ mg/L}$.
- **Canxi ($\text{Ca}^{2+}$):**
  - Kích thích tạo hạt bùn UASB: $100 - 200\text{ mg/L}$ (liên kết chéo mạng lưới EPS).
  - Ức chế / tạo cặn vôi: $> 2,500 - 4,000\text{ mg/L}$.
- **Hiện tượng đối kháng cation (Antagonism):** Sự hiện diện đồng thời của $\text{K}^+$ hoặc $\text{Ca}^{2+}$ ở tỷ lệ thích hợp có thể làm giảm độc tính của $\text{Na}^+$.

###### 8.2.4.3.2. Kim loại nặng: $\text{Cu}$, $\text{Zn}$, $\text{Ni}$, $\text{Pb}$, $\text{Cd}$, $\text{Cr}$ và cơ chế kết tủa với Sulfide
- Kim loại nặng tự do dạng ion hòa tan ($\text{Cu}^{2+}, \text{Zn}^{2+}, \text{Ni}^{2+}, \text{Cd}^{2+}, \text{Pb}^{2+}$) gây độc cực mạnh ở nồng độ chỉ vài $\text{mg/L}$ (thậm chí $< 1\text{ mg/L}$).
- **Cơ chế tự bảo vệ tự nhiên nhờ kết tủa Sulfide:**
  - Trong bể kỵ khí, lượng sulfide sinh ra ($\text{S}^{2-}$) phản ứng tức thời với kim loại nặng tạo thành kết tủa muối sulfide không tan có tích số tan cực nhỏ:
    $$\text{Me}^{2+} + \text{S}^{2-} \rightarrow \text{MeS} \downarrow \quad (\text{ví dụ } K_{sp}(\text{CuS}) = 6\times 10^{-36}, K_{sp}(\text{ZnS}) = 2\times 10^{-24})$$
  - Nhờ đó, nồng độ ion kim loại nặng tự do trong dung dịch giảm xuống mức gần như bằng không, loại bỏ hoàn toàn độc tính trừ khi hàm lượng kim loại nặng vượt quá lượng sulfide tương đương.

##### 8.2.4.4. Ức chế bởi Độ mặn và Ion Clorua ($\text{Cl}^-$)

###### 8.2.4.4.1. Áp suất thẩm thấu và ngưỡng nồng độ $\text{Cl}^- > 15,000\text{ mg/L}$
- Nước thải từ chế biến thủy hải sản, thuộc da, dưa muối chứa hàm lượng muối ăn ($\text{NaCl}$) rất cao.
- Nồng độ ion Clorua ($\text{Cl}^-$) vượt quá $15,000\text{ mg/L}$ ($15\text{ g/L}$) gây áp suất thẩm thấu lớn làm mất nước tế bào, gây ức chế nghiêm trọng đến vi sinh vật kỵ khí.

###### 8.2.4.4.2. Sự thích nghi của hạt bùn kỵ khí với môi trường mặn
- Nếu tăng dần nồng độ muối từ từ qua nhiều tháng, quần thể vi sinh vật kỵ khí có thể thích nghi thông qua việc tổng hợp các chất tương thích thẩm thấu (osmoprotectants như glycine betaine, trehalose), nâng ngưỡng chịu đựng lên đến $20,000 - 30,000\text{ mg/L Cl}^-$.

---

### 8.3. Sản lượng Methane Lý thuyết & Thu hồi Năng lượng Khí sinh học (Theoretical Methane Generation & Biogas Energy Recovery)

#### 8.3.1. Cơ sở Nhiệt động & Hóa học lượng tế về Sản lượng Methane

##### 8.3.1.1. Phương trình Buswell & Neave về Phân hủy Hợp chất Hữu cơ Tổng quát

###### 8.3.1.1.1. Dạng phương trình $C_n H_a O_b N_c S_d + \dots \rightarrow \dots$
Phương trình Buswell (1952) mô tả quá trình phân hủy kỵ khí hoàn toàn của một hợp chất hữu cơ có công thức hóa học tổng quát:
$$C_n H_a O_b N_c S_d + \left( n - \frac{a}{4} - \frac{b}{2} + \frac{3c}{4} + \frac{d}{2} \right) \text{H}_2\text{O} \rightarrow \left( \frac{n}{2} + \frac{a}{8} - \frac{b}{4} - \frac{3c}{8} - \frac{d}{4} \right) \text{CH}_4 + \left( \frac{n}{2} - \frac{a}{8} + \frac{b}{4} + \frac{3c}{8} + \frac{d}{4} \right) \text{CO}_2 + c\text{NH}_3 + d\text{H}_2\text{S}$$

###### 8.3.1.1.2. Ứng dụng tính toán thành phần khí sinh học lý thuyết cho Glucid, Protein, Lipid
- **Glucid / Carbohydrate (Glucose: $\text{C}_6\text{H}_{12}\text{O}_6$):**
  $$\text{C}_6\text{H}_{12}\text{O}_6 \rightarrow 3\text{CH}_4 + 3\text{CO}_2 \implies 50\%\ \text{CH}_4 : 50\%\ \text{CO}_2$$
- **Chất béo / Lipid (Glycerol trioleate: $\text{C}_{57}\text{H}_{104}\text{O}_6$):**
  $$\text{C}_{57}\text{H}_{104}\text{O}_6 + 28\text{H}_2\text{O} \rightarrow 40\text{CH}_4 + 17\text{CO}_2 \implies 70.2\%\ \text{CH}_4 : 29.8\%\ \text{CO}_2$$
- **Protein (Ví dụ tế bào vi khuẩn: $\text{C}_5\text{H}_7\text{O}_2\text{N}$):**
  $$\text{C}_5\text{H}_7\text{O}_2\text{N} + 2\text{H}_2\text{O} \rightarrow 2.5\text{CH}_4 + 2.5\text{CO}_2 + \text{NH}_3 \implies 50\%\ \text{CH}_4 : 50\%\ \text{CO}_2$$
*(Nhận xét: Chất béo sinh ra tỷ lệ methane cao nhất và thể tích biogas lớn nhất trên mỗi đơn vị khối lượng cơ chất).*

##### 8.3.1.2. Tương đương Khối lượng COD và Thể tích Methane Lý thuyết

###### 8.3.1.2.1. Chứng minh phản ứng oxy hóa metan: $\text{CH}_4 + 2\text{O}_2 \rightarrow \text{CO}_2 + 2\text{H}_2\text{O}$
- Trong phép đo COD, $1\text{ mol CH}_4$ cần $2\text{ mol O}_2$ để bị oxy hóa hoàn toàn thành $\text{CO}_2$ và $\text{H}_2\text{O}$:
  $$\text{CH}_4 + 2\text{O}_2 \rightarrow \text{CO}_2 + 2\text{H}_2\text{O}$$
- Khối lượng phân tử:
  - $1\text{ mol CH}_4 = 16.04\text{ g}$.
  - $2\text{ mol O}_2 = 2 \times 32.00\text{ g} = 64.00\text{ g COD}$.
- Do đó:
  $$1\text{ mol CH}_4 \equiv 64.0\text{ g COD} = 0.064\text{ kg COD}$$

###### 8.3.1.2.2. $1\text{ mol CH}_4$ tương đương $64\text{ g COD} \rightarrow 0.35\text{ m}^3\text{ CH}_4\text{/kg COD}$ ở STP ($0^\circ\text{C}, 1\text{ atm}$)
- Theo phương trình khí lý tưởng, ở điều kiện tiêu chuẩn (STP: $T = 0^\circ\text{C} = 273.15\text{ K}$, $P = 1.0\text{ atm}$):
  $$V_{mol,STP} = 22.414\text{ L/mol} = 0.022414\text{ m}^3/\text{mol}$$
- Thể tích methane sinh ra trên mỗi đơn vị khối lượng COD phân hủy:
  $$\text{Suất sinh methane lý thuyết tại STP} = \frac{0.022414\text{ m}^3\text{ CH}_4}{0.064\text{ kg COD}} = 0.3502\text{ m}^3\text{ CH}_4/\text{kg COD}_{\text{chuyển hóa}}$$
  **$\rightarrow$ Giá trị hằng số kỹ thuật chuẩn: $0.35\text{ m}^3\text{ CH}_4/\text{kg COD}_{\text{removed}}$ tại STP.**

###### 8.3.1.2.3. Quy đổi sang nhiệt độ vận hành thực tế: $0.38 - 0.40\text{ m}^3\text{ CH}_4\text{/kg COD}$ ở $25 - 35^\circ\text{C}$
- Quy đổi thể tích khí theo định luật Charles-Gay-Lussac:
  $$V_{CH_4,T} = V_{CH_4,STP} \times \left( \frac{273.15 + T}{273.15} \right)$$
- **Tại $25^\circ\text{C}$ ($298.15\text{ K}$):**
  $$V_{CH_4,25^\circ\text{C}} = 0.35 \times \left( \frac{298.15}{273.15} \right) = 0.35 \times 1.0915 = 0.382\text{ m}^3\text{ CH}_4/\text{kg COD}$$
- **Tại $35^\circ\text{C}$ ($308.15\text{ K}$):**
  $$V_{CH_4,35^\circ\text{C}} = 0.35 \times \left( \frac{308.15}{273.15} \right) = 0.35 \times 1.1281 = 0.395\text{ m}^3\text{ CH}_4/\text{kg COD} \approx 0.40\text{ m}^3/\text{kg COD}$$

---

#### 8.3.2. Thành phần và Thuộc tính Nhiệt lượng của Khí sinh học (Biogas Composition & Energy Potential)

##### 8.3.2.1. Thành phần Tỷ lệ Khí Biogas Điển hình

###### 8.3.2.1.1. Methane ($\text{CH}_4$): $60 - 70\%$ (điển hình $65\%$)
- Khí cháy mang năng lượng chính; không màu, không mùi, nhẹ hơn không khí ($\rho \approx 0.717\text{ kg/m}^3$ ở STP).

###### 8.3.2.1.2. Khí Cacbonic ($\text{CO}_2$): $30 - 40\%$ (điển hình $35\%$)
- Khí trơ không cháy; làm giảm nhiệt trị của biogas; nặng hơn không khí ($\rho \approx 1.98\text{ kg/m}^3$).

###### 8.3.2.1.3. Các khí vết: $\text{H}_2\text{S}$ ($0.1 - 2\%$), $\text{N}_2$, $\text{H}_2$, hơi nước bão hòa
- **Khí Hydro Sulfide ($\text{H}_2\text{S}$):** $500 - 10,000\text{ ppm}$ ($0.05 - 1.0\%$). Khí cực độc, có mùi trứng thối, khi cháy tạo $\text{SO}_2$ gây axit hóa và ăn mòn nghiêm trọng buồng đốt động cơ; bắt buộc phải qua thiết bị lọc $\text{H}_2\text{S}$ (tháp hấp thụ sinh học hoặc bể hấp phụ oxit sắt $\text{Fe}_2\text{O}_3$).
- **Hơi nước ($\text{H}_2\text{O}$):** Bão hòa ẩm ($100\%$ RH ở nhiệt độ bể); cần qua bẫy ngưng tụ nước (condensate trap) trước khi đưa vào máy phát điện.

##### 8.3.2.2. Nhiệt trị và Năng lượng Thu hồi

###### 8.3.2.2.1. Nhiệt trị thấp (LHV) của $\text{CH}_4$ nguyên chất: $35,800 - 38,846\text{ kJ/m}^3$
- Nhiệt trị thấp (Lower Heating Value - LHV) của khí methane tinh khiết tại điều kiện tiêu chuẩn:
  $$\text{LHV}_{CH_4} \approx 35,800 - 38,846\text{ kJ/m}^3 \approx 9.95 - 10.8\text{ kWh/m}^3\text{ CH}_4$$

###### 8.3.2.2.2. Nhiệt trị của Biogas ($65\%\ \text{CH}_4$): $\approx 23,000 - 25,000\text{ kJ/m}^3$
- Đối với khí sinh học thông thường chứa $65\%\ \text{CH}_4$:
  $$\text{LHV}_{biogas} = 0.65 \times 35,800\text{ kJ/m}^3 = 23,270\text{ kJ/m}^3\text{ biogas} \approx 6.46\text{ kWh/m}^3\text{ biogas}$$

###### 8.3.2.2.3. Công suất phát điện và gia nhiệt lò hơi từ Biogas
- **Năng lượng nhiệt sinh ra mỗi ngày:**
  $$E_{heat}\text{ (kJ/d)} = Q_{CH_4,STP} \times \text{LHV}_{CH_4} = Q_{CH_4,STP}\text{ (m}^3/\text{d)} \times 35,800\text{ kJ/m}^3$$
- **Công suất nhiệt liên tục tương đương:**
  $$P_{thermal}\text{ (kW)} = \frac{E_{heat}\text{ (kJ/d)}}{86,400\text{ s/d}}$$
- **Công suất phát điện (Hệ thống đồng phát CHP / Biogas Generator):**
  - Hiệu suất phát điện cơ học: $\eta_e \approx 33 - 40\%$.
  - Hiệu suất thu hồi nhiệt: $\eta_{th} \approx 45 - 50\%$.
  - Công suất điện đầu ra:
    $$P_{electrical}\text{ (kW)} = P_{thermal} \times \eta_e$$

---

### 8.4. Phân loại & Cấu tạo Các Mô hình Bể Xử lý Kỵ khí Tốc độ cao (High-Rate Anaerobic Reactor Configurations)

#### 8.4.1. Bể Xử lý Tiếp xúc Kỵ khí (Anaerobic Contact Process - Completely-Mixed with Recycle)

##### 8.4.1.1. Sơ đồ Công nghệ và Nguyên lý Hoạt động

###### 8.4.1.1.1. Bể phản ứng xáo trộn hoàn toàn (CSTR) với tải trọng OLR $= 2 - 5\text{ kg COD/m}^3\cdot\text{d}$
- Nước thải đầu vào được hòa trộn liên tục với bùn kỵ khí tuần hoàn bằng máy khuấy cơ học (impeller) hoặc bơm tuần hoàn cưỡng bức.
- Duy trì nồng độ sinh khối lơ lửng trong bể: $\text{MLVSS} = 4,000 - 8,000\text{ g/m}^3$ ($4 - 8\text{ g/L}$).
- Tải trọng hữu cơ thể tích vận hành ổn định: $\text{OLR} = 2.0 - 5.0\text{ kg COD/m}^3\cdot\text{d}$.

###### 8.4.1.1.2. Tách rời thời gian lưu bùn (SRT $= 15 - 30$ ngày) khỏi thời gian lưu nước (HRT $= 1.5 - 3$ ngày)
- Khác với bể phân hủy bùn kỵ khí CSTR thông thường ($\text{HRT} = \text{SRT}$), quy trình Anaerobic Contact bổ sung bể lắng thứ cấp và tuyến bùn tuần hoàn (Return Anaerobic Sludge - RAS).
- Hệ số cô đặc bùn giúp duy trì $\text{SRT} \ge 15 - 30\text{ ngày}$ trong khi $\text{HRT}$ chỉ cần $1.5 - 3.0\text{ ngày}$ ($36 - 72\text{ giờ}$), giảm thể tích xây dựng bể đi $5 - 10$ lần.

##### 8.4.1.2. Bộ khử khí Chân không (Vacuum Degasifier) và Bể Lắng Kỵ khí

###### 8.4.1.2.1. Hiện tượng bọt khí metan siêu bão hòa bám dính làm nổi bùn kỵ khí
- Hỗn hợp bùn nước sau khi rời bể kỵ khí bị bão hòa khí hòa tan ($\text{CH}_4$ và $\text{CO}_2$). Khi vào bể lắng trọng lực, phản ứng kỵ khí nội tại vẫn tiếp diễn, tạo ra các bọt khí vi mô bám vào bông bùn, làm giảm khối lượng riêng biểu kiến và khiến bùn bị nổi lên mặt nước (sludge flotation), gây mất bùn nghiêm trọng.

###### 8.4.1.2.2. Cấu tạo buồng khử khí chân không và bể lắng trọng lực với cào bùn trung tâm
- **Bộ khử khí chân không (Vacuum Degas Chamber):**
  - Đặt giữa bể kỵ khí và bể lắng thứ cấp.
  - Vận hành dưới áp suất chân không nhẹ (chân không khoảng $0.3 - 0.5\text{ atm}$, độ giảm áp $30 - 50\text{ kPa}$).
  - Cấu tạo gồm tháp đệm hoặc các tấm vách ngăn ziczac để phá vỡ các vi bọt khí entrained $\text{CH}_4/\text{CO}_2$ bám quanh bông bùn.
- **Bể lắng thứ cấp kỵ khí (Anaerobic Secondary Clarifier):**
  - Tải trọng tràn bề mặt thiết kế: $\text{OFR} = 15 - 24\text{ m}^3/(\text{m}^2\cdot\text{d})$ (thấp hơn bể lắng hiếu khí do bông bùn kỵ khí nhẹ hơn).
  - Đáy bể có độ dốc nón lớn hướng về hố thu trung tâm, trang bị dàn cào bùn đáy quay chậm để gom bùn nhanh chóng, hạn chế tối đa thời gian lưu bùn trong bể lắng nhằm tránh tái sinh khí.

---

#### 8.4.2. Bể Phản ứng Dòng chảy ngược qua Tầng bùn Kỵ khí (UASB - Upflow Anaerobic Sludge Blanket)

##### 8.4.2.1. Cấu trúc Hình học và Các Vùng Chức năng Trong Bể UASB

###### 8.4.2.1.1. Hệ thống Phân phối Nước thải Đầu vào đáy bể (Bottom Feed Manifold)
- Nước thải được bơm cấp từ đáy bể qua mạng lưới ống phân phối nhánh và các vòi phun hình nón ngược hướng xuống đáy (cách sàn bể $0.15 - 0.25\text{ m}$).
- Diện tích phục vụ của một đầu cấp nước (feed point distribution density):
  - Đối với bùn hạt đậm đặc: $1\text{ điểm cấp cho mỗi } 1.0 - 2.0\text{ m}^2$ diện tích sàn.
  - Đối với bùn bông/hạt hỗn hợp: $1\text{ điểm cấp cho mỗi } 2.0 - 4.0\text{ m}^2$ diện tích sàn.
- Mục đích: Đảm bảo phân bổ lưu lượng đều khắp tiết diện bể, ngăn ngừa hiện tượng dòng chảy tắt (short-circuiting) và hình thành các vùng chết thủy lực.

###### 8.4.2.1.2. Tầng bùn hạt đậm đặc đáy bể (Dense Granular Sludge Bed, MLVSS $35,000 - 40,000\text{ g/m}^3$)
- Chiếm khoảng $1.0 - 2.5\text{ m}$ chiều cao tính từ đáy bể.
- Nồng độ sinh khối cực cao: $\text{MLSS} = 50,000 - 100,000\text{ g/m}^3$, tương đương $\text{MLVSS} = 35,000 - 40,000\text{ g/m}^3$ ($35 - 40\text{ kg VSS/m}^3$).
- Tầng bùn gồm các hạt hình cầu hoặc bầu dục đường kính $1 - 4\text{ mm}$, nơi diễn ra phần lớn ($70 - 80\%$) quá trình chuyển hóa cơ chất hữu cơ và sinh khí metan.

###### 8.4.2.1.3. Tầng mền bùn lơ lửng (Fluidized Sludge Blanket, MLVSS $10,000 - 30,000\text{ g/m}^3$)
- Chiếm chiều cao khoảng $1.5 - 3.0\text{ m}$ phía trên tầng bùn hạt đáy.
- Nồng độ sinh khối: $\text{MLVSS} = 10,000 - 30,000\text{ g/m}^3$ ($10 - 30\text{ kg VSS/m}^3$).
- Trạng thái bùn: Các hạt bùn nhỏ hơn kết hợp với bông bùn lơ lửng trong dòng chất lỏng được xáo trộn tự nhiên bởi các dòng bọt khí metan và khí cacbonic bốc lên liên tục, tạo môi trường tiếp xúc cơ chất hoàn hảo mà không cần máy khuấy cơ học.

###### 8.4.2.1.4. Vùng nước trong (Clear Settling Zone)
- Nằm ở phần trên cùng của bể (bên ngoài chụp thu khí GLS).
- Chiều cao vùng nước trong: $H_{clear} \approx 0.5 - 1.2\text{ m}$.
- Vùng nước tĩnh không có bọt khí sục xáo, tạo điều kiện cho các hạt bùn sót lắng trở lại tầng mền bùn bên dưới.

##### 8.4.2.2. Bộ tách 3 Pha Khí - Lỏng - Rắn (Three-Phase GLS Separator)

###### 8.4.2.2.1. Tấm đổi hướng định hướng khí (Gas Deflector Baffles)
- Bố trí bên dưới các khe hở của chụp thu khí.
- Góc nghiêng: $45^\circ - 50^\circ$.
- Chức năng: Ngăn chặn bọt khí bốc thẳng lên khe hở vào vùng lắng; đổi hướng bọt khí đi thẳng vào lòng chụp thu khí (gas cap).

###### 8.4.2.2.2. Chụp thu khí hình nón/tam giác ngược (Gas Collection Canopy / Hood)
- Tiết diện hình tam giác úp ngược (canopy) hoặc hình chóp nón.
- Chiều cao kết cấu chụp: $H_{GLS} = 1.2 - 2.0\text{ m}$ (điển hình $1.5\text{ m}$).
- Tải trọng giải phóng khí trên diện tích mặt thoáng chụp thu:
  $$v_{gas} = \frac{Q_{biogas}}{A_{gas\_cap}} \le 1.0 - 3.0\text{ m}^3/(\text{m}^2\cdot\text{h})$$

###### 8.4.2.2.3. Vùng lắng trọng lực và góc nghiêng hồi bùn tự chảy ($45^\circ - 60^\circ$)
- Tấm vách nghiêng của chụp GLS đóng vai trò đáy dốc của vùng lắng.
- Góc nghiêng bắt buộc: $\alpha = 50^\circ - 60^\circ$ (tối thiểu $45^\circ$).
- Bùn tách khỏi bọt khí sẽ rơi xuống bề mặt nghiêng và tự động trượt trọng lực trở lại vùng phản ứng bên dưới mà không cần bơm hoàn lưu.

###### 8.4.2.2.4. Máng thu nước trong bề mặt và tấm chắn váng bọt
- Bố trí máng răng cưa (V-notch weir) thu nước đều khắp bề mặt trên đỉnh bể.
- Trang bị tấm chắn bọt (scum baffle) ngập sâu $0.15 - 0.20\text{ m}$ phía trước máng tràn để chặn váng nổi trôi ra theo dòng thải.

##### 8.4.2.3. Cơ chế Tạo Bùn Hạt Kỵ khí (Anaerobic Granular Sludge Mechanics)

###### 8.4.2.3.1. Quá trình tạo hạt 4 bước: Tiếp xúc ban đầu $\rightarrow$ Hấp phụ vật lý $\rightarrow$ Liên kết polyme ngoại bào (EPS) $\rightarrow$ Tăng trưởng tạo hạt bền vững
Sự hình thành hạt bùn kỵ khí là quá trình tự kết tập vi sinh vật không cần giá thể nhân tạo:
1. **Bước 1: Tiếp xúc và bám dính ban đầu (Initial Contact & Attachment):**
   - Các tế bào vi khuẩn va chạm ngẫu nhiên dưới tác động của dòng chất lỏng và bọt khí, tiếp xúc với các hạt nhân vô cơ vi mô (tinh thể canxi cacbonat, hạt đất sét hoặc mảnh vụn tế bào).
2. **Bước 2: Hấp phụ vật lý thuận nghịch (Reversible Adsorption):**
   - Lực liên kết tĩnh điện yếu, lực Van der Waals, và lực tương tác kỵ nước giữ các tế bào lại với nhau.
3. **Bước 3: Kết bám không thuận nghịch bằng Polyme ngoại bào (Irreversible Adhesion via EPS):**
   - Vi khuẩn tiết ra lượng lớn chất polyme ngoại bào (Extracellular Polymeric Substances - EPS) gồm polysaccharide, protein, axit nucleic.
   - Các cation đa hóa trị ($\text{Ca}^{2+}, \text{Mg}^{2+}, \text{Fe}^{2+}$) tạo cầu nối ion giữa các nhóm carboxylate tích điện âm của chuỗi EPS, biến liên kết lỏng lẻo thành cấu trúc gel sinh học bền vững.
4. **Bước 4: Nhân đôi tế bào và Thành thục Hạt bùn (Multiplication & Granule Maturation):**
   - Các vi sinh vật tiếp tục phân chia bên trong chất nền EPS. Do động lực khuếch tán cơ chất từ ngoài vào trong, các nhóm vi khuẩn tự sắp xếp thành cấu trúc phân lớp chức năng đồng tâm.

###### 8.4.2.3.2. Cấu trúc vi mô của hạt bùn UASB: Lớp vỏ ngoài (Acidogen), Lớp giữa (Acetogen/Syntroph), Lớp nhân trong (Methanogen)
- **Lớp vỏ ngoài ($0 - 100\ \mu\text{m}$):**
  - Tiếp xúc trực tiếp với nồng độ cơ chất hòa tan cao và lượng oxy hòa tan vết từ nước thải.
  - Chiếm ưu thế bởi vi khuẩn thủy phân và acidogenic sinh axit, tiêu thụ nhanh oxy và bẻ gãy chất hữu cơ phức tạp thành VFA.
- **Lớp chuyển tiếp ở giữa ($100 - 300\ \mu\text{m}$):**
  - Vùng kỵ khí sâu.
  - Quần thể cộng sinh dưỡng hỗ giữa vi khuẩn acetogenic (OHPA) và methanogens khử hydro; chuyển hóa propionate và butyrate thành acetate và $\text{H}_2$.
- **Lớp nhân trung tâm ($> 300\ \mu\text{m}$ đến tâm hạt):**
  - Chuyên biệt hóa cao bởi cổ khuẩn acetoclastic methanogens (*Methanosaeta* dạng sợi bện chặt làm khung đỡ cơ học cho toàn bộ hạt bùn) phân giải acetate thành khí $\text{CH}_4$ và $\text{CO}_2$.

###### 8.4.2.3.3. Đặc tính lắng tuyệt vời: Vận tốc lắng $v_{settling} = 20 - 60\text{ m/h}$, chỉ số SVI $< 20 - 30\text{ mL/g}$
- Khối lượng riêng của hạt bùn: $\rho_{granule} \approx 1.04 - 1.08\text{ g/cm}^3$.
- Kích thước hạt: $d = 1.0 - 4.0\text{ mm}$.
- Vận tốc lắng trọng lực cực lớn:
  $$v_{settling} = 20 - 60\text{ m/h} \quad (\text{gấp } 10 - 20 \text{ lần so với bùn hoạt tính hiếu khí flocs } 1.5 - 3.0\text{ m/h})$$
- Chỉ số thể tích bùn:
  $$\text{SVI} \le 15 - 30\text{ mL/g} \quad (\text{bùn lắng nhanh và nén cực đặc})$$

##### 8.4.2.4. Tiêu chí Thiết kế Thủy lực và Tải trọng UASB

###### 8.4.2.4.1. Vận tốc dòng dâng bề mặt ($v_{up} = 0.6 - 1.5\text{ m/h}$ theo loại nước thải)
- Vận tốc dòng dâng chất lỏng danh định ($v_{up} = Q / A$):
  - *Nước thải hòa tan hoàn toàn (Soluble COD $\approx 100\%$):* $v_{up} = 1.0 - 3.0\text{ m/h}$ (điển hình $1.5\text{ m/h}$).
  - *Nước thải hòa tan một phần (Partially soluble COD):* $v_{up} = 1.0 - 1.25\text{ m/h}$ (điển hình $1.0\text{ m/h}$).
  - *Nước thải sinh hoạt đô thị (Domestic wastewater):* $v_{up} = 0.8 - 1.0\text{ m/h}$ (điển hình $0.7\text{ m/h}$).
- Nếu $v_{up} > 1.5 - 2.0\text{ m/h}$ đối với nước thải có cặn, lực kéo thủy lực sẽ thắng trọng lực khiến hạt bùn bị cuốn trôi ra ngoài.

###### 8.4.2.4.2. Tải trọng thể tích hữu cơ (OLR $= 5 - 15\text{ kg COD/m}^3\cdot\text{d}$)
- Dải OLR thiết kế tiêu chuẩn cho UASB: $5.0 - 15.0\text{ kg COD/(m}^3\cdot\text{d)}$.
- Tải trọng tối đa cho phép phụ thuộc chặt chẽ vào nhiệt độ vận hành và độ hòa tan của COD:
  - Ở $15^\circ\text{C}$: $2.0 - 4.0\text{ kg COD/(m}^3\cdot\text{d)}$.
  - Ở $25^\circ\text{C}$: $6.0 - 10.0\text{ kg COD/(m}^3\cdot\text{d)}$.
  - Ở $35^\circ\text{C}$: $10.0 - 18.0\text{ kg COD/(m}^3\cdot\text{d)}$ (đối với nước thải tinh bột, bia, cồn có thể đạt $20\text{ kg COD/(m}^3\cdot\text{d)}$).

###### 8.4.2.4.3. Giới hạn thời gian lưu bùn theo nhiệt độ (SRT từ 25 d ở $35^\circ\text{C}$ đến 140 d ở $15^\circ\text{C}$)
- Thời gian lưu tế bào trung bình cần duy trì để đảm bảo sinh trưởng bùn hạt:
  - $35^\circ\text{C}$: $\text{SRT} \ge 25\text{ ngày}$.
  - $30^\circ\text{C}$: $\text{SRT} \ge 30\text{ ngày}$.
  - $25^\circ\text{C}$: $\text{SRT} \ge 60\text{ ngày}$.
  - $20^\circ\text{C}$: $\text{SRT} \ge 100\text{ ngày}$.
  - $15^\circ\text{C}$: $\text{SRT} \ge 140\text{ ngày}$.

###### 8.4.2.4.4. Chiều cao làm việc hiệu dụng ($H_{total} = 4 - 8\text{ m}$)
- Chiều cao tổng thể của bể UASB thường từ $4.5 - 8.0\text{ m}$ (điển hình $6.0\text{ m}$):
  $$H_{total} = H_{active} + H_{GLS} + H_{clear} + H_{freeboard}$$
  - $H_{active}$ (vùng bùn phản ứng): $3.5 - 5.0\text{ m}$.
  - $H_{GLS}$ (chiều cao bộ tách 3 pha): $1.2 - 1.8\text{ m}$.
  - $H_{clear}$ (vùng nước tĩnh): $0.5 - 1.0\text{ m}$.
  - $H_{freeboard}$ (chiều cao an toàn mặt thoáng): $0.3 - 0.5\text{ m}$.

---

#### 8.4.3. Các Biến thể UASB Thế hệ mới & Mô hình Kỵ khí Khác

##### 8.4.3.1. Bể Tầng bùn Hạt Mở rộng (EGSB - Expanded Granular Sludge Bed)

###### 8.4.3.1.1. Tỷ lệ chiều cao / đường kính lớn ($H/D > 4 - 6$), chiều cao $10 - 16\text{ m}$
- EGSB là bước phát triển vượt bậc của UASB, thiết kế theo dạng tháp đứng cao hình trụ tròn ($H = 10 - 16\text{ m}$), tỷ lệ $H/D$ từ $4:1$ đến $8:1$.

###### 8.4.3.1.2. Tuần hoàn dòng ra tạo vận tốc dâng cao ($v_{up} = 4 - 10\text{ m/h}$)
- Bằng cách bơm tuần hoàn một phần dòng nước sau xử lý trở lại đáy bể, vận tốc dâng thực tế trong EGSB được đẩy lên:
  $$v_{up} = 4.0 - 10.0\text{ m/h} \quad (\text{gấp } 4 - 8 \text{ lần UASB})$$
- Tầng bùn hạt ở đáy bị giãn nở (fluidized/expanded) từ $20 - 40\%$, xóa bỏ hiện tượng tạo kênh dẫn dòng (channeling) và tăng cường đối lưu tiếp xúc cơ chất.

###### 8.4.3.1.3. Áp dụng cho nước thải nồng độ thấp hoặc nhiệt độ thấp, tải trọng $15 - 25\text{ kg COD/m}^3\cdot\text{d}$
- Nhờ động học tiếp xúc cực tốt, EGSB xử lý hiệu quả nước thải nồng độ trung bình - thấp ($\text{COD} = 1,000 - 4,000\text{ mg/L}$) hoặc vận hành ở nhiệt độ môi trường thấp ($< 20^\circ\text{C}$), với tải trọng $\text{OLR} = 15 - 25\text{ kg COD/(m}^3\cdot\text{d)}$.

##### 8.4.3.2. Bể Tuần hoàn Nội bộ (IC - Internal Circulation Reactor)

###### 8.4.3.2.1. Thiết kế 2 tầng tách 3 pha (GLS 1 ở dưới và GLS 2 ở trên)
- Bể IC (phát triển bởi Paques) tương đương 2 tầng phản ứng UASB chồng lên nhau trong một tháp phản ứng duy nhất ($H = 16 - 24\text{ m}$):
  - Tầng dưới (First Stage / High-loaded zone): Chịu tải cực cao, sinh lượng khí biogas khổng lồ, thu bởi bộ tách GLS 1.
  - Tầng trên (Second Stage / Polishing zone): Chịu tải thấp, xử lý phần COD còn lại, thu khí bởi bộ tách GLS 2.

###### 8.4.3.2.2. Cơ chế nâng khí tự nhiên (Gas-lift) đẩy dòng nước và bùn lên đỉnh rồi hồi lưu tự trọng
- Lượng khí biogas lớn tạo ra ở tầng đáy tích tụ trong bộ thu GLS 1 tạo bọt khí nâng dòng hỗn hợp nước - bùn lên đỉnh tháp qua ống nâng khí trung tâm (riser pipe) mà **không cần bơm cơ học**.
- Tại bình tách khí trên đỉnh (gas-liquid separator dome), khí biogas thoát ra đường ống thu, còn hỗn hợp nước - bùn theo ống hồi lưu tự trọng (downcomer pipe) lao thẳng xuống đáy bể, tạo chu trình tuần hoàn nội bộ mạnh mẽ.

###### 8.4.3.2.3. Vận tốc dâng cực cao ($v_{up} = 10 - 25\text{ m/h}$) và OLR vượt trội ($20 - 35\text{ kg COD/m}^3\cdot\text{d}$)
- Vận tốc dòng dâng ở tầng đáy đạt $v_{up} = 10 - 25\text{ m/h}$.
- Khả năng chịu tải hữu cơ vượt trội:
  $$\text{OLR} = 20.0 - 35.0\text{ kg COD/(m}^3\cdot\text{d)} \quad (\text{tiết kiệm } 50 - 70\% \text{ diện tích mặt bằng so với UASB})$$

##### 8.4.3.3. Bể Lọc Kỵ khí (AF - Anaerobic Filter)

###### 8.4.3.3.1. Giá thể cố định đệm ngập nước (Dòng chảy hướng lên hoặc hướng xuống)
- Nước thải chảy qua một lớp vật liệu đệm ngập nước (đá cuội, ống gốm, giá thể nhựa tổ ong có diện tích bề mặt riêng $S_v = 100 - 300\text{ m}^2/\text{m}^3$).
- Sinh khối kỵ khí tồn tại dưới 2 dạng: Màng màng sinh học (biofilm) dính bám trên giá thể và bông bùn lắng đọng trong các khe hở rỗng của đệm.

###### 8.4.3.3.2. Khắc phục vấn đề hạt bùn khó hình thành nhưng dễ bị tắc nghẽn (Clogging)
- Phù hợp với nước thải hòa tan hoàn toàn, khó tạo hạt bùn UASB.
- Nhược điểm: Nếu nước thải đầu vào có nhiều cặn lơ lửng ($\text{TSS} > 200 - 500\text{ mg/L}$) hoặc bùn chết tích tụ nhiều, bể lọc kỵ khí sẽ bị tắc nghẽn (clogging), đòi hỏi phải sục rửa ngược (backwashing) phức tạp.

##### 8.4.3.4. Bể Phản ứng Xáo trộn Hoàn toàn Truyền thống (CSTR / Conventional Anaerobic Digester)

###### 8.4.3.4.1. Không có hệ thống giữ bùn, $\text{HRT} = \text{SRT} = 15 - 30$ ngày
- Không trang bị bể lắng hoặc cơ chế tuần hoàn tế bào; dòng ra mang theo toàn bộ sinh khối tương ứng với nồng độ trong bể.
- Để tránh bị rửa trôi methanogens, bắt buộc phải chọn:
  $$\text{HRT} = \text{SRT} \ge 15 - 30\text{ ngày ở } 35^\circ\text{C}$$

###### 8.4.3.4.2. Chuyên dụng phân hủy bùn cặn hữu cơ đặc hoặc nước thải cực giàu chất rắn lơ lửng
- Ứng dụng chính: Phân hủy bùn thải của trạm xử lý nước thải đô thị (bùn sơ cấp + bùn hoạt tính dư có $\text{TS} = 3 - 6\%$), phân chuồng trại chăn nuôi heo/bò, bã hèm rượu đậm đặc.

---

### 8.5. Cơ sở Động học & Hệ thống Công thức Thiết kế Kỹ thuật (Biokinetics & Engineering Design Equations)

#### 8.5.1. Động học Monod trong Xử lý Kỵ khí

##### 8.5.1.1. Thời gian Lưu bùn Tối thiểu ($\theta_c^{min}$)
Thời gian lưu tế bào giới hạn mà tại đó tốc độ sinh trưởng của vi sinh vật đúng bằng tốc độ rửa trôi ra khỏi bể; nếu $\text{SRT} \le \theta_c^{min}$, vi sinh vật sẽ bị rửa trôi hoàn toàn (washout):
$$\frac{1}{\theta_c^{min}} = \mu_m \cdot \frac{S}{K_s + S} - b_H \approx \mu_m - b_H \quad (\text{khi } S \gg K_s)$$
$$\theta_c^{min} = \frac{1}{\mu_m - b_H}$$
Trong đó:
- $\theta_c^{min}$: Thời gian lưu bùn tối thiểu (ngày, d).
- $\mu_m$: Tốc độ sinh trưởng riêng cực đại của methanogen ($d^{-1}$, ở $25^\circ\text{C} \approx 0.20\text{ d}^{-1}$; $35^\circ\text{C} \approx 0.35\text{ d}^{-1}$).
- $b_H$ (hoặc $k_d$): Hệ số phân hủy nội bào ($d^{-1}$, điển hình $0.03\text{ d}^{-1}$).
- $S$: Nồng độ cơ chất hòa tan trong bể (g COD/m³ hoặc mg/L).
- $K_s$: Hằng số nửa bão hòa Monod (g COD/m³ hoặc mg/L, điển hình $120\text{ mg/L}$).

##### 8.5.1.2. Thời gian Lưu bùn Thiết kế ($\text{SRT}_{design}$)
Để bảo đảm an toàn trước sự biến động lưu lượng, nhiệt độ và nồng độ cơ chất:
$$\text{SRT}_{design} = \theta_c = \text{SF} \cdot \theta_c^{min}$$
Trong đó:
- $\text{SF}$: Hệ số an toàn thiết kế (Safety Factor, không thứ nguyên, thường chọn $\text{SF} = 2.5 - 5.0$, chuẩn mực thiết kế chọn $\text{SF} = 3.0$).

##### 8.5.1.3. Nồng độ Cơ chất Hòa tan Dòng ra ($S$)
Ở trạng thái ổn định (steady-state), nồng độ cơ chất hòa tan trong dòng ra được xác định từ phương trình Monod kết hợp cân bằng sinh khối:
$$S = \frac{K_s \cdot [1 + b_H \cdot (\text{SRT})]}{\text{SRT} \cdot (\mu_m - b_H) - 1}$$
*(Lưu ý: Nồng độ $S$ chỉ phụ thuộc vào các hằng số động học của vi sinh vật và thời gian lưu bùn $\text{SRT}$, hoàn toàn không phụ thuộc vào nồng độ cơ chất đầu vào $S_0$).*

---

#### 8.5.2. Cân bằng Vật chất và Sản lượng Sinh khối Bùn

##### 8.5.2.1. Sản lượng Sinh khối Hoạt tính Vi sinh ($P_{X,bio}$)
Khối lượng tế bào vi sinh vật kỵ khí hoạt tính tổng hợp mới mỗi ngày:
$$P_{X,bio} = \frac{Q \cdot Y_H \cdot (\text{bCOD}_0 - S) \cdot 10^{-3}}{1 + b_H \cdot \text{SRT}}$$
Trong đó:
- $P_{X,bio}$: Tốc độ sinh khối hoạt tính sinh ra hàng ngày (kg VSS/d).
- $Q$: Lưu lượng nước thải thiết kế (m³/d).
- $Y_H$: Hệ số sản lượng sinh khối lý thuyết ($0.08\text{ g VSS/g COD}$).
- $\text{bCOD}_0$: Nồng độ COD có thể phân hủy sinh học trong nước thải đầu vào (g/m³ hoặc mg/L):
  $$\text{bCOD}_0 = S_{so} + f_{deg} \cdot S_{po}$$
- $S$: Nồng độ COD hòa tan còn lại trong dòng ra (g/m³).
- $10^{-3}$: Thừa số chuyển đổi từ gam sang kilôgam ($10^{-3}\text{ kg/g}$).

##### 8.5.2.2. Sản lượng Cặn tế bào Nội bào ($P_{X,d}$)
Khối lượng cặn mảnh vụn tế bào bất hoạt (cell debris) tích tụ từ quá trình tự phân hủy sinh khối:
$$P_{X,d} = f_d \cdot b_H \cdot (P_{X,bio} \cdot \text{SRT})$$
Trong đó:
- $f_d$: Phần cặn tế bào trơ không phân hủy được ($f_d = 0.10 - 0.15$, điển hình chọn $0.15$).

##### 8.5.2.3. Tích lũy Chất rắn Bay hơi Không phân hủy sinh học ($P_{X,nbVSS}$)
Khối lượng chất rắn lơ lửng bay hơi trơ không phân hủy sinh học từ nước thải đầu vào tích tụ lại trong bể:
$$P_{X,nbVSS} = Q \cdot \text{nbVSS}_{in} \cdot 10^{-3}$$
Trong đó:
- $\text{nbVSS}_{in}$: Nồng độ VSS không phân hủy sinh học trong nước thải cấp (g/m³):
  $$\text{nbVSS}_{in} = (1 - f_{deg}) \cdot \text{VSS}_0 = (1 - f_{deg}) \cdot \frac{S_{po}}{\text{COD/VSS}}$$

##### 8.5.2.4. Tổng Sản lượng Bùn Bay hơi Hàng ngày ($P_{X,VSS}$)
Tổng khối lượng bùn bay hơi ròng sinh ra trong hệ thống mỗi ngày:
$$P_{X,VSS} = P_{X,bio} + P_{X,d} + P_{X,nbVSS}$$

##### 8.5.2.5. Xả Bùn Dư và Lưu lượng Bùn Xả ($P_{X,w}, Q_w$)
- Khối lượng bùn mất mát tự nhiên theo nước thải ra khỏi bể:
  $$P_{X,e} = Q \cdot \text{VSS}_e \cdot 10^{-3}\text{ (kg VSS/d)}$$
- Khối lượng bùn dư cần chủ động xả bỏ định kỳ mỗi ngày:
  $$P_{X,w} = P_{X,VSS} - P_{X,e}\text{ (kg VSS/d)}$$
- Lưu lượng bùn xả thải ($Q_w$):
  $$Q_w = \frac{P_{X,w}}{X_w \cdot 10^{-3}}\text{ (m}^3/\text{d)}$$
  *(với $X_w$ là nồng độ VSS trong dòng bùn xả đáy, g VSS/m³).*

---

#### 8.5.3. Xác định Thể tích Bể và Thời gian Lưu Nước

##### 8.5.3.1. Tính thể tích Bể Xáo trộn Hoàn toàn có Tuần hoàn Bùn
- Tổng khối lượng sinh khối bùn cần duy trì trong bể:
  $$M_{VSS} = P_{X,VSS} \cdot \text{SRT}\text{ (kg VSS)}$$
- Thể tích chất lỏng hữu dụng của bể phản ứng kỵ khí:
  $$V = \frac{M_{VSS}}{X} = \frac{P_{X,VSS} \cdot \text{SRT}}{X \cdot 10^{-3}}\text{ (m}^3)$$
  Trong đó $X$ là nồng độ MLVSS duy trì trong bể ($4,000 - 8,000\text{ g/m}^3$).

##### 8.5.3.2. Tính thể tích Bể UASB dựa trên Tải trọng OLR Thiết kế
- Tổng tải trọng COD nạp vào bể hàng ngày:
  $$L_{COD} = Q \cdot S_0 \cdot 10^{-3}\text{ (kg COD/d)}$$
- Thể tích hoạt động hữu dụng của bể UASB:
  $$V = \frac{L_{COD}}{\text{OLR}_{design}} = \frac{Q \cdot S_0}{\text{OLR}_{design} \cdot 1000}\text{ (m}^3)$$
  Trong đó $\text{OLR}_{design}$ là tải trọng thể tích hữu cơ thiết kế ($\text{kg COD/(m}^3\cdot\text{d)}$).

##### 8.5.3.3. Thời gian Lưu Nước Thủy lực (HRT)
$$\text{HRT} = \frac{V}{Q}\text{ (ngày)} = \frac{V \cdot 24}{Q}\text{ (giờ)}$$

---

#### 8.5.4. Tính toán Khí sinh học & Sản lượng Methane Thực tế

##### 8.5.4.1. Khối lượng COD thực tế chuyển hóa thành Methane ($\text{COD}_{CH_4}$)
Nguyên lý bảo toàn COD: Tổng lượng COD bị loại bỏ trừ đi phần COD dùng để tổng hợp tế bào vi sinh vật mới (với hệ số chuyển đổi sinh học $1.42\text{ g COD/g VSS}$ tế bào vi khuẩn $\text{C}_5\text{H}_7\text{O}_2\text{N}$):
$$\Delta\text{COD}_{rem} = Q \cdot (S_0 - S) \cdot 10^{-3}\text{ (kg COD/d)}$$
$$\text{COD}_{bio} = 1.42 \cdot P_{X,bio}\text{ (kg COD/d)}$$
$$\text{COD}_{CH_4} = \Delta\text{COD}_{rem} - \text{COD}_{bio} = Q \cdot (S_0 - S) \cdot 10^{-3} - 1.42 \cdot P_{X,bio}$$

##### 8.5.4.2. Lưu lượng Methane ở Điều kiện Tiêu chuẩn ($Q_{CH_4,STP}$)
$$Q_{CH_4,STP} = 0.35 \cdot \text{COD}_{CH_4}\text{ (m}^3\text{ CH}_4\text{/d)}$$

##### 8.5.4.3. Hiệu chỉnh Thể tích Methane theo Nhiệt độ Vận hành
$$Q_{CH_4,T} = Q_{CH_4,STP} \cdot \left( \frac{273.15 + T}{273.15} \right)\text{ (m}^3/\text{d)}$$

##### 8.5.4.4. Tổng Lưu lượng Khí sinh học ($Q_{biogas}$)
$$Q_{biogas,STP} = \frac{Q_{CH_4,STP}}{\%_{CH_4}}\text{ (m}^3\text{ biogas/d)}$$
$$Q_{biogas,T} = \frac{Q_{CH_4,T}}{\%_{CH_4}}\text{ (m}^3\text{ biogas/d)}$$
*(với $\%_{CH_4}$ là phần thể tích methane, thường từ $0.60 - 0.70$, trung bình $0.65$).*

##### 8.5.4.5. Tính toán Tiềm năng Năng lượng Nhiệt và Điện
- Năng lượng nhiệt tiềm năng:
  $$E_{heat} = Q_{CH_4,STP} \times 35,800\text{ (kJ/d)}$$
- Công suất năng lượng liên tục:
  $$P = \frac{E_{heat}}{86,400}\text{ (kW)}$$

---

#### 8.5.5. Cân bằng Dinh dưỡng và Hóa chất Nâng độ Kiềm

##### 8.5.5.1. Nhu cầu Bổ sung Nitơ ($N_{req}, \Delta N$)
- Tổng lượng Nitơ yêu cầu cho vi sinh vật tổng hợp sinh khối:
  $$N_{req} = 0.12 \cdot P_{X,bio}\text{ (kg N/d)} \quad (\text{hoặc } 0.12 \cdot P_{X,VSS})$$
- Lượng Nitơ sẵn có trong nước thải cấp vào:
  $$N_{in} = Q \cdot N_{inf} \cdot 10^{-3}\text{ (kg N/d)}$$
- Lượng Nitơ cần bổ sung hàng ngày:
  $$\Delta N = \max(0, N_{req} - N_{in})\text{ (kg N/d)}$$

##### 8.5.5.2. Nhu cầu Bổ sung Phospho ($P_{req}, \Delta P$)
- Tổng lượng Phospho yêu cầu:
  $$P_{req} = 0.024 \cdot P_{X,bio}\text{ (kg P/d)}$$
- Lượng Phospho sẵn có:
  $$P_{in} = Q \cdot P_{inf} \cdot 10^{-3}\text{ (kg P/d)}$$
- Lượng Phospho cần châm thêm:
  $$\Delta P = \max(0, P_{req} - P_{in})\text{ (kg P/d)}$$

##### 8.5.5.3. Nhu cầu Bổ sung Lưu huỳnh theo Tỷ lệ UASB
- Dựa trên tỷ lệ stoichiometry $(\text{COD}/Y) : \text{N} : \text{P} : \text{S} = (50/Y) : 5 : 1 : 1$:
  $$S_{req} = \Delta\text{COD} \cdot \left( \frac{1}{50/Y} \right) = \Delta\text{COD} \cdot \left( \frac{Y}{50} \right)\text{ (kg S/d)}$$

##### 8.5.5.4. Tính toán Lượng Kiềm Bổ sung Bicarbonate Sodium ($\text{NaHCO}_3$)
- Độ kiềm mục tiêu: $\text{Alk}_{target} \approx 3,000\text{ g CaCO}_3\text{/m}^3$ (mg/L).
- Độ kiềm thiếu hụt:
  $$\Delta\text{Alk} = \max(0, \text{Alk}_{target} - \text{Alk}_{in})\text{ (g CaCO}_3\text{/m}^3)$$
- Khối lượng độ kiềm cần bổ sung tính theo $\text{CaCO}_3$:
  $$\text{Mass}_{CaCO_3} = Q \cdot \Delta\text{Alk} \cdot 10^{-3}\text{ (kg CaCO}_3\text{/d)}$$
- Quy đổi sang khối lượng Natri Bicarbonate ($\text{NaHCO}_3$, khối lượng đương lượng $84\text{ g/eq}$ so với $\text{CaCO}_3$ là $50\text{ g/eq}$):
  $$\text{Mass}_{NaHCO_3} = \text{Mass}_{CaCO_3} \cdot \left( \frac{84}{50} \right) = \text{Mass}_{CaCO_3} \cdot 1.68\text{ (kg NaHCO}_3\text{/d)}$$

---

#### 8.5.6. Kích thước Thủy lực Bể Lắng Thứ cấp & Bộ tách GLS

##### 8.5.6.1. Diện tích Bề mặt Bể lắng Thứ cấp ($A_{clarifier}$) & Đường kính ($D$)
- Diện tích mặt bằng lắng yêu cầu:
  $$A_{clarifier} = \frac{Q}{\text{OFR}}\text{ (m}^2)$$
  *(với $\text{OFR}$ là tải trọng tràn bề mặt, thường chọn $24\text{ m}^3/(\text{m}^2\cdot\text{d})$).*
- Đường kính bể lắng hình tròn:
  $$D = \sqrt{\frac{4 \cdot A_{clarifier}}{\pi}}\text{ (m)}$$

##### 8.5.6.2. Kiểm tra Vận tốc Dâng Bề mặt UASB ($v_{up}$)
$$v_{up} = \frac{Q}{24 \cdot A}\text{ (m/h)}$$
Trong đó $A$ là diện tích tiết diện ướt mặt bằng của bể UASB ($A = V / H_{active}$ hoặc $V / H_{total}$). Giá trị phải thỏa mãn $v_{up} \le 1.0 - 1.5\text{ m/h}$.

##### 8.5.6.3. Tính toán Kích thước Hình học Bộ tách 3 Pha GLS
- Tỷ lệ kích thước mặt bằng: Chiều dài $L$ và chiều rộng $W$ (chọn tỷ lệ $L/W = 2:1$):
  $$W = \sqrt{\frac{A}{L/W}} = \sqrt{\frac{A}{2}}, \quad L = 2 \cdot W$$
- Chiều cao tổng thể bể:
  $$H_{total} = H_{active} + H_{GLS} + H_{clear} = 4.0\text{ m} + 1.5\text{ m} + 0.5\text{ m} = 6.0\text{ m}$$

---

### 8.6. Bài tập Tính toán Thiết kế Chi tiết Từng Bước (Worked Engineering Examples)

#### 8.6.1. Bài toán Thiết kế 1: Bể Tiếp xúc Kỵ khí Xáo trộn Hoàn toàn (Completely-Mixed Anaerobic Contact Process)

##### 8.6.1.1. Dữ liệu Đầu vào & Yêu cầu Thiết kế ($Q = 500\text{ m}^3\text{/d}, S_0 = 6,000\text{ mg/L}$)
- **Lưu lượng dòng vào ($Q$):** $500.0\text{ m}^3/\text{d}$
- **COD tổng dòng vào ($S_0$):** $6,000.0\text{ g/m}^3$ (mg/L)
- **COD hòa tan dòng vào ($S_{so}$):** $4,000.0\text{ g/m}^3$
- **Tỷ số COD/VSS của chất rắn lơ lửng:** $1.80\text{ g COD/g VSS}$
- **Tỷ lệ phân hủy sinh học của VSS vào ($f_{deg}$):** $80\%\ (0.80)$
- **Nồng độ VSS dòng ra bể lắng ($VSS_e$):** $150.0\text{ g/m}^3$
- **Nồng độ MLVSS trong bể kỵ khí ($X$):** $6,000.0\text{ g/m}^3$ ($6.0\text{ kg/m}^3$)
- **Hệ số cặn tế bào trơ ($f_d$):** $0.15$
- **Thành phần biogas:** $65\%\ \text{CH}_4$, $35\%\ \text{CO}_2$
- **Hàm lượng dinh dưỡng vi sinh:** $12\%\ \text{N}$ ($f_N = 0.12$), $2.4\%\ \text{P}$ ($f_P = 0.024$)
- **Tải trọng tràn bề mặt bể lắng ($\text{OFR}$):** $24.0\text{ m}^3/(\text{m}^2\cdot\text{d})$
- **Hiệu suất khử COD mục tiêu:** $\ge 90.0\%$
- **Hệ số an toàn thời gian lưu bùn ($\text{SF}$):** $3.0$
- **Nồng độ Nitơ dòng vào ($N_{in}$):** $10.0\text{ g/m}^3$
- **Nồng độ Phospho dòng vào ($P_{in}$):** $20.0\text{ g/m}^3$
- **Độ kiềm dòng vào:** $500.0\text{ g CaCO}_3\text{/m}^3$
- **Nhiệt độ nước thải ($T$):** $25.0^\circ\text{C}$
- **Hằng số động học ở $25^\circ\text{C}$:**
  - $Y_H = 0.08\text{ g VSS/g COD}$
  - $b_H = 0.03\text{ d}^{-1}$
  - $K_s = 120.0\text{ g/m}^3$
  - $\mu_m = 0.20\text{ d}^{-1}$
  - Suất sinh methane tại STP: $0.35\text{ m}^3\text{ CH}_4\text{/kg COD}$

##### 8.6.1.2. Bước 1: Đặc trưng hóa COD Nước thải, Xác định $\text{SRT}_{min}$ và Chọn $\theta_c$
1. **Phân tách COD hạt:**
   $$S_{po} = S_0 - S_{so} = 6,000 - 4,000 = 2,000\text{ g/m}^3$$
2. **Tổng VSS dòng vào ($VSS_0$):**
   $$VSS_0 = \frac{S_{po}}{\text{COD/VSS}} = \frac{2,000}{1.80} = 1,111.11\text{ g/m}^3$$
3. **COD hạt có khả năng phân hủy sinh học ($bCOD_p$):**
   $$bCOD_p = 0.80 \times 2,000 = 1,600\text{ g/m}^3$$
4. **Tổng COD phân hủy sinh học đầu vào ($bCOD_0$):**
   $$bCOD_0 = S_{so} + bCOD_p = 4,000 + 1,600 = 5,600\text{ g/m}^3$$
5. **VSS trơ không phân hủy đầu vào ($nbVSS_{in}$):**
   $$nbVSS_{in} = (1 - 0.80) \times 1,111.11 = 222.22\text{ g/m}^3$$
6. **Thời gian lưu bùn tối thiểu ($\theta_c^{min}$):**
   $$\frac{1}{\theta_c^{min}} = \mu_m - b_H = 0.20 - 0.03 = 0.17\text{ d}^{-1} \implies \theta_c^{min} = \frac{1}{0.17} = 5.882\text{ ngày}$$
7. **Thời gian lưu bùn thiết kế ($\theta_c$):**
   $$\theta_c = \text{SF} \times \theta_c^{min} = 3.0 \times 5.882 = 17.65\text{ ngày}$$
   $\rightarrow$ Chọn thời gian lưu bùn thiết kế chuẩn hóa: **$\theta_c = \text{SRT} = 20.0\text{ ngày}$** (thỏa mãn dải khuyến nghị $15 - 30\text{ ngày}$).
8. **Kiểm tra COD hòa tan dòng ra ($S$) tại $\text{SRT} = 20.0\text{ d}$:**
   $$S = \frac{K_s \cdot [1 + b_H \cdot (\text{SRT})]}{\text{SRT} \cdot (\mu_m - b_H) - 1} = \frac{120 \times [1 + 0.03 \times 20]}{20 \times (0.20 - 0.03) - 1} = \frac{120 \times 1.60}{3.40 - 1} = \frac{192.0}{2.40} = 80.0\text{ g/m}^3\text{ (mg/L)}$$
   - Hiệu suất loại bỏ bCOD:
     $$E = \frac{5,600 - 80}{5,600} \times 100\% = 98.57\% > 90.0\%\quad \text{(Đạt tiêu chuẩn)}$$

##### 8.6.1.3. Bước 2: Tính toán Tổng Sản lượng Bùn Bay hơi Hàng ngày ($P_{X,VSS}$)
1. **Sinh khối hoạt tính tổng hợp mới hàng ngày ($P_{X,bio}$):**
   $$P_{X,bio} = \frac{Q \cdot Y_H \cdot (bCOD_0 - S) \cdot 10^{-3}}{1 + b_H \cdot \theta_c} = \frac{500 \times 0.08 \times (5,600 - 80) \times 10^{-3}}{1 + 0.03 \times 20} = \frac{40 \times 5.520}{1.60} = 138.00\text{ kg VSS/d}$$
2. **Cặn tế bào nội bào sinh ra ($P_{X,d}$):**
   $$P_{X,d} = f_d \cdot b_H \cdot (P_{X,bio} \cdot \theta_c) = 0.15 \times 0.03 \times (138.00 \times 20) = 0.0045 \times 2,760.0 = 12.42\text{ kg VSS/d}$$
3. **Chất rắn bay hơi không phân hủy tích tụ ($P_{X,nbVSS}$):**
   $$P_{X,nbVSS} = Q \cdot nbVSS_{in} \cdot 10^{-3} = 500 \times 222.22 \times 10^{-3} = 111.11\text{ kg VSS/d}$$
4. **Tổng khối lượng bùn bay hơi phát sinh ($P_{X,VSS}$):**
   $$P_{X,VSS} = 138.00 + 12.42 + 111.11 = 261.53\text{ kg VSS/d}$$

##### 8.6.1.4. Bước 3: Xác định Lượng Bùn Lưu giữ, Thể tích Bể ($V$) và Thời gian Lưu nước (HRT)
1. **Tổng lượng sinh khối bùn trong bể ($M_{VSS}$):**
   $$M_{VSS} = P_{X,VSS} \cdot \theta_c = 261.53\text{ kg/d} \times 20.0\text{ d} = 5,230.60\text{ kg VSS}$$
2. **Thể tích làm việc hữu dụng của bể kỵ khí ($V$):**
   $$V = \frac{M_{VSS}}{X \cdot 10^{-3}} = \frac{5,230.60\text{ kg VSS}}{6.00\text{ kg VSS/m}^3} = 871.77\text{ m}^3 \approx 872\text{ m}^3$$
3. **Thời gian lưu nước thủy lực ($\text{HRT}$):**
   $$\text{HRT} = \frac{V}{Q} = \frac{871.77\text{ m}^3}{500\text{ m}^3/\text{d}} = 1.744\text{ ngày} = 41.85\text{ giờ}$$

##### 8.6.1.5. Bước 4: Tính toán Sản lượng Khí Methane, Biogas và Tiềm năng Năng lượng
1. **Khối lượng bCOD bị phân hủy hàng ngày:**
   $$\Delta\text{COD}_{rem} = 500\text{ m}^3/\text{d} \times (5,600 - 80)\text{ g/m}^3 \times 10^{-3} = 2,760.00\text{ kg COD/d}$$
2. **Khối lượng COD chuyển hóa thành sinh khối tế bào:**
   $$\text{COD}_{bio} = 1.42 \times P_{X,bio} = 1.42 \times 138.00 = 195.96\text{ kg COD/d}$$
3. **Khối lượng COD chuyển thành khí methane:**
   $$\text{COD}_{CH_4} = \Delta\text{COD}_{rem} - \text{COD}_{bio} = 2,760.00 - 195.96 = 2,564.04\text{ kg COD/d}$$
4. **Lưu lượng methane sinh ra:**
   - Tại điều kiện tiêu chuẩn (STP, $0^\circ\text{C}, 1\text{ atm}$):
     $$Q_{CH_4,STP} = 0.35 \times 2,564.04 = 897.41\text{ m}^3\text{ CH}_4/\text{d}$$
   - Tại nhiệt độ thực tế $25^\circ\text{C}$ ($298.15\text{ K}$):
     $$Q_{CH_4,25^\circ\text{C}} = 897.41 \times \left( \frac{298.15}{273.15} \right) = 979.54\text{ m}^3\text{ CH}_4/\text{d}$$
5. **Tổng lưu lượng khí sinh học Biogas ($65\%\ \text{CH}_4$):**
   - Tại STP:
     $$Q_{biogas,STP} = \frac{897.41}{0.65} = 1,380.63\text{ m}^3/\text{d}$$
   - Tại $25^\circ\text{C}$:
     $$Q_{biogas,25^\circ\text{C}} = \frac{979.54}{0.65} = 1,506.98\text{ m}^3/\text{d}$$
6. **Tiềm năng năng lượng thu hồi:**
   - Năng lượng nhiệt phát sinh:
     $$E_{heat} = 897.41\text{ m}^3/\text{d} \times 35,800\text{ kJ/m}^3 = 32,127,278\text{ kJ/d} = 32.13\text{ GJ/d}$$
   - Công suất nhiệt tương đương:
     $$P = \frac{32,127,278\text{ kJ/d}}{86,400\text{ s/d}} = 371.84\text{ kW}$$

##### 8.6.1.6. Bước 5: Tính Lượng Bùn Xả Bỏ ($P_{X,w}$) và Cân bằng Bổ sung Dinh dưỡng (N, P)
1. **Lượng bùn mất mát theo dòng ra:**
   $$P_{X,e} = Q \cdot VSS_e \cdot 10^{-3} = 500 \times 150 \times 10^{-3} = 75.00\text{ kg VSS/d}$$
2. **Khối lượng bùn xả dư cần loại bỏ hàng ngày:**
   $$P_{X,w} = P_{X,VSS} - P_{X,e} = 261.53 - 75.00 = 186.53\text{ kg VSS/d}$$
3. **Cân bằng Nitơ:**
   - Nhu cầu Nitơ cho tổng hợp tế bào:
     $$N_{req} = 0.12 \times P_{X,VSS} = 0.12 \times 261.53 = 31.38\text{ kg N/d}$$
   - Lượng Nitơ sẵn có trong nước vào:
     $$N_{in} = 500 \times 10 \times 10^{-3} = 5.00\text{ kg N/d}$$
   - Lượng Nitơ thiếu hụt cần bổ sung:
     $$\Delta N = 31.38 - 5.00 = 26.38\text{ kg N/d}$$
4. **Cân bằng Phospho:**
   - Nhu cầu Phospho:
     $$P_{req} = 0.024 \times P_{X,VSS} = 0.024 \times 261.53 = 6.28\text{ kg P/d}$$
   - Lượng Phospho sẵn có:
     $$P_{in} = 500 \times 20 \times 10^{-3} = 10.00\text{ kg P/d}$$
   - Lượng Phospho cần bổ sung:
     $$\Delta P = 0.00\text{ kg P/d}\quad (\text{dư thừa } 10.00 - 6.28 = 3.72\text{ kg P/d})$$

##### 8.6.1.7. Bước 6: Kiểm tra Tải trọng Hữu cơ Thể tích (OLR)
$$\text{OLR} = \frac{Q \cdot S_0 \cdot 10^{-3}}{V} = \frac{500 \times 6,000 \times 10^{-3}}{871.77} = \frac{3,000.00\text{ kg COD/d}}{871.77\text{ m}^3} = 3.44\text{ kg COD/(m}^3\cdot\text{d)}$$
*(Nhận xét: Giá trị $3.44\text{ kg COD/(m}^3\cdot\text{d)}$ nằm hoàn hảo trong dải khuyến nghị $2.0 - 5.0\text{ kg COD/(m}^3\cdot\text{d)}$ đối với bể tiếp xúc kỵ khí).*

##### 8.6.1.8. Bước 7: Tính toán Kích thước Bể Lắng Thứ cấp Kỵ khí
1. **Diện tích bề mặt bể lắng tròn:**
   $$A_{clarifier} = \frac{Q}{\text{OFR}} = \frac{500.0\text{ m}^3/\text{d}}{24.0\text{ m}^3/(\text{m}^2\cdot\text{d})} = 20.83\text{ m}^2$$
2. **Đường kính bể lắng ($D$):**
   $$D = \sqrt{\frac{4 \cdot A_{clarifier}}{\pi}} = \sqrt{\frac{4 \times 20.83}{3.14159}} = \sqrt{26.526} = 5.15\text{ m} \approx 5.2\text{ m}$$

##### 8.6.1.9. Bước 8: Tính toán Nhu cầu Bổ sung Độ kiềm Đệm Hệ thống ($\text{NaHCO}_3$)
1. **Độ kiềm mục tiêu:** $\text{Alk}_{target} = 3,000\text{ g CaCO}_3\text{/m}^3$.
2. **Độ kiềm nước thải đầu vào:** $\text{Alk}_{in} = 500\text{ g CaCO}_3\text{/m}^3$.
3. **Độ kiềm thiếu hụt:** $\Delta\text{Alk} = 3,000 - 500 = 2,500\text{ g CaCO}_3\text{/m}^3$.
4. **Khối lượng $\text{CaCO}_3$ cần bổ sung:**
   $$\text{Mass}_{CaCO_3} = 500\text{ m}^3/\text{d} \times 2,500\text{ g/m}^3 \times 10^{-3} = 1,250.00\text{ kg CaCO}_3\text{/d}$$
5. **Khối lượng Natri Bicarbonate ($\text{NaHCO}_3$) thực tế cần châm:**
   $$\text{Mass}_{NaHCO_3} = 1,250.00 \times \left( \frac{84}{50} \right) = 2,100.00\text{ kg NaHCO}_3\text{/d}$$

##### 8.6.1.10. Bảng Tổng kết Thông số Kỹ thuật Thiết kế Hoàn chỉnh (EX-01)
| Thông số Kỹ thuật | Ký hiệu | Giá trị Tính toán | Đơn vị | Ghi chú Thiết kế |
| :--- | :--- | :--- | :--- | :--- |
| **Thời gian lưu bùn tối thiểu** | $\theta_c^{min}$ | $5.88$ | ngày | Giới hạn rửa trôi Monod |
| **Thời gian lưu bùn thiết kế** | $\theta_c$ (SRT) | $20.0$ | ngày | Hệ số an toàn $\text{SF} = 3.0$ |
| **Nồng độ COD hòa tan dòng ra** | $S$ | $80.0$ | $\text{g/m}^3$ | Hiệu suất loại bỏ $98.57\%$ |
| **Sinh khối hoạt tính sinh ra** | $P_{X,bio}$ | $138.00$ | kg VSS/d | Bùn vi sinh mới |
| **Tổng lượng bùn bay hơi phát sinh** | $P_{X,VSS}$ | $261.53$ | kg VSS/d | Bao gồm cặn và VSS trơ |
| **Lượng bùn duy trì trong bể** | $M_{VSS}$ | $5,230.60$ | kg VSS | Sinh khối hữu dụng |
| **Thể tích bể phản ứng kỵ khí** | $V$ | $871.77$ | $\text{m}^3$ | Làm tròn $\approx 872\text{ m}^3$ |
| **Thời gian lưu nước** | $\text{HRT}$ | $1.74$ ($41.9$) | ngày (giờ) | Đã tách rời khỏi SRT |
| **Lưu lượng sinh khí Methane (STP)** | $Q_{CH_4,STP}$ | $897.41$ | $\text{m}^3/\text{d}$ | Ở $0^\circ\text{C}, 1\text{ atm}$ |
| **Lưu lượng Methane ở $25^\circ\text{C}$** | $Q_{CH_4,25^\circ\text{C}}$ | $979.54$ | $\text{m}^3/\text{d}$ | Điều kiện thực tế |
| **Tổng lượng Biogas ($65\%\ \text{CH}_4$)** | $Q_{biogas,25^\circ\text{C}}$ | $1,506.98$ | $\text{m}^3/\text{d}$ | Khí sinh học thu hồi |
| **Công suất năng lượng tương đương** | $P$ | $371.84$ | kW | Tiềm năng nhiệt liên tục |
| **Lượng bùn dư cần xả thải** | $P_{X,w}$ | $186.53$ | kg VSS/d | Sau khi trừ bùn trôi theo dòng ra |
| **Lượng Nitơ cần bổ sung** | $\Delta N$ | $26.38$ | kg N/d | Bổ sung dạng Urea hoặc $\text{NH}_4\text{Cl}$ |
| **Lượng Phospho cần bổ sung** | $\Delta P$ | $0.00$ | kg P/d | Nước thải sẵn có dư $3.72\text{ kg/d}$ |
| **Tải trọng hữu cơ thể tích** | $\text{OLR}$ | $3.44$ | $\text{kg COD/(m}^3\cdot\text{d)}$ | Chuẩn dải $2.0 - 5.0$ |
| **Diện tích bể lắng thứ cấp** | $A_{clarifier}$ | $20.83$ | $\text{m}^2$ | Bể lắng bùn kỵ khí |
| **Đường kính bể lắng thứ cấp** | $D$ | $5.15$ | m | Chọn chuẩn $5.2\text{ m}$ |
| **Lượng hóa chất kiềm $\text{NaHCO}_3$** | $\text{Mass}_{NaHCO_3}$ | $2,100.00$ | kg/d | Chống chua hóa bể |

---

#### 8.6.2. Bài toán Thiết kế 2: Bể UASB Xử lý Nước thải Công nghiệp Nồng độ cao (UASB Industrial Design)

##### 8.6.2.1. Dữ liệu Đầu vào & Ràng buộc Hình học ($Q = 500\text{ m}^3\text{/d}, S_0 = 12,000\text{ mg/L}$)
- **Lưu lượng nước thải ($Q$):** $500.0\text{ m}^3/\text{d} = 20.833\text{ m}^3/\text{h}$
- **Nồng độ COD tổng đầu vào ($S_0$):** $12,000.0\text{ g/m}^3$ (mg/L)
- **Hàm lượng chất rắn lơ lửng ($TSS$):** $600.0\text{ g/m}^3$
- **Hàm lượng VSS không phân hủy ($nbVSS$):** $500.0\text{ g/m}^3$
- **Độ kiềm dòng vào:** $500.0\text{ g CaCO}_3\text{/m}^3$
- **Nhiệt độ nước thải ($T$):** $25.0^\circ\text{C}$
- **Tải trọng hữu cơ thể tích thiết kế ($\text{OLR}_{design}$):** $8.0\text{ kg COD/(m}^3\cdot\text{d)}$
- **Hiệu suất khử COD mục tiêu:** $90.0\%$
- **Nồng độ VSS dòng ra bể UASB ($VSS_e$):** $120.0\text{ g/m}^3$
- **Nồng độ MLVSS trung bình vùng bùn ($X$):** $30,000.0\text{ g/m}^3$ ($30.0\text{ kg/m}^3$)
- **Hệ số cặn tế bào ($f_d$):** $0.10$
- **Thành phần biogas:** $65\%\ \text{CH}_4$, $35\%\ \text{CO}_2$
- **Tổng chiều cao bể ($H_{total}$):** $6.0\text{ m}$
- **Chiều cao vùng nước tĩnh trên mặt bùn ($H_{clear}$):** $0.5\text{ m}$
- **Chiều cao bộ tách 3 pha GLS ($H_{separator}$):** $1.5\text{ m}$
- **Tỷ lệ mặt bằng Chiều dài / Chiều rộng ($L/W$):** $2.0$
- **SRT vận hành khuyến nghị ở $25^\circ\text{C}$:** $60.0\text{ ngày}$
- **Hằng số động học ở $25^\circ\text{C}$:**
  - $Y_H = 0.08\text{ g VSS/g COD}$
  - $b_H = 0.03\text{ d}^{-1}$
  - Suất sinh methane tại STP: $0.35\text{ m}^3\text{ CH}_4\text{/kg COD}$

##### 8.6.2.2. Bước 1: Xác định Thể tích Bể UASB từ OLR Thiết kế và Kiểm tra HRT
1. **Tổng tải lượng COD nạp hàng ngày:**
   $$L_{COD} = Q \cdot S_0 \cdot 10^{-3} = 500\text{ m}^3/\text{d} \times 12,000\text{ g/m}^3 \times 10^{-3} = 6,000.00\text{ kg COD/d}$$
2. **Thể tích làm việc yêu cầu của bể UASB ($V$):**
   $$V = \frac{L_{COD}}{\text{OLR}_{design}} = \frac{6,000.00\text{ kg COD/d}}{8.0\text{ kg COD/(m}^3\cdot\text{d)}} = 750.00\text{ m}^3$$
3. **Thời gian lưu nước thủy lực ($\text{HRT}$):**
   $$\text{HRT} = \frac{V}{Q} = \frac{750.00\text{ m}^3}{500\text{ m}^3/\text{d}} = 1.50\text{ ngày} = 36.00\text{ giờ}$$

##### 8.6.2.3. Bước 2: Xác định Diện tích Mặt bằng, Kích thước Rộng/Dài và Kiểm tra Vận tốc Dâng
1. **Diện tích mặt bằng bể ($A$):**
   $$A = \frac{V}{H_{total}} = \frac{750.00\text{ m}^3}{6.0\text{ m}} = 125.00\text{ m}^2$$
2. **Kích thước mặt bằng hình chữ nhật với $L/W = 2.0$ ($L = 2W$):**
   $$A = W \times L = W \times 2W = 2W^2 = 125.00\text{ m}^2$$
   $$W = \sqrt{\frac{125.00}{2}} = \sqrt{62.50} = 7.9057\text{ m} \approx 7.91\text{ m}$$
   $$L = 2 \times 7.9057\text{ m} = 15.8114\text{ m} \approx 15.81\text{ m}$$
3. **Kiểm tra vận tốc dòng dâng bề mặt ($v_{up}$):**
   - Lưu lượng dòng chảy theo giờ:
     $$Q_h = \frac{500\text{ m}^3/\text{d}}{24\text{ h/d}} = 20.833\text{ m}^3/\text{h}$$
   - Vận tốc dâng bề mặt:
     $$v_{up} = \frac{Q_h}{A} = \frac{20.833\text{ m}^3/\text{h}}{125.00\text{ m}^2} = 0.1667\text{ m/h} \approx 0.167\text{ m/h}$$
   *(Đánh giá: $v_{up} = 0.167\text{ m/h} \ll 1.0 - 1.25\text{ m/h}$, tuyệt đối an toàn, bảo đảm không bị cuốn trôi hạt bùn).*

##### 8.6.2.4. Bước 3: Phân vùng Chiều cao Vận hành, Vùng Phản ứng Hiệu dụng và Tổng Sinh khối
1. **Chiều cao vùng phản ứng sinh học hữu dụng ($H_{active}$):**
   $$H_{active} = H_{total} - H_{separator} - H_{clear} = 6.0\text{ m} - 1.5\text{ m} - 0.5\text{ m} = 4.0\text{ m}$$
2. **Thể tích vùng bùn hoạt tính hữu dụng ($V_{active}$):**
   $$V_{active} = A \times H_{active} = 125.00\text{ m}^2 \times 4.0\text{ m} = 500.00\text{ m}^3$$
3. **Tổng khối lượng sinh khối bùn hoạt tính lưu giữ ($M_{VSS}$):**
   $$M_{VSS} = V_{active} \times X \cdot 10^{-3} = 500.00\text{ m}^3 \times 30.00\text{ kg VSS/m}^3 = 15,000.00\text{ kg VSS}$$

##### 8.6.2.5. Bước 4: Tính toán Sản lượng Bùn Phát sinh, Lượng Bùn Xả Thải và Thời gian Lưu bùn Thực tế
1. **Khối lượng COD bị loại bỏ hàng ngày ($\Delta\text{COD}$):**
   $$\Delta\text{COD} = 500\text{ m}^3/\text{d} \times 12,000\text{ g/m}^3 \times 0.90 \times 10^{-3} = 5,400.00\text{ kg COD/d}$$
2. **Sinh khối hoạt tính tổng hợp mới hàng ngày (ở $\theta_c = 60.0\text{ d}$):**
   $$P_{X,bio} = \frac{Y_H \cdot \Delta\text{COD}}{1 + b_H \cdot \theta_c} = \frac{0.08 \times 5,400.00}{1 + 0.03 \times 60.0} = \frac{432.00}{1 + 1.80} = \frac{432.00}{2.80} = 154.29\text{ kg VSS/d}$$
3. **Cặn tế bào nội bào sinh ra ($P_{X,d}$):**
   $$P_{X,d} = f_d \cdot b_H \cdot (P_{X,bio} \cdot \theta_c) = 0.10 \times 0.03 \times (154.29 \times 60.0) = 0.003 \times 9,257.40 = 27.77\text{ kg VSS/d}$$
4. **VSS không phân hủy đầu vào tích lũy ($P_{X,nbVSS}$):**
   $$P_{X,nbVSS} = Q \cdot nbVSS \cdot 10^{-3} = 500 \times 500 \times 10^{-3} = 250.00\text{ kg VSS/d}$$
5. **Tổng sản lượng bùn bay hơi phát sinh ($P_{X,VSS}$):**
   $$P_{X,VSS} = 154.29 + 27.77 + 250.00 = 432.06\text{ kg VSS/d}$$
6. **Lượng bùn trôi theo dòng ra ($P_{X,e}$):**
   $$P_{X,e} = Q \cdot VSS_e \cdot 10^{-3} = 500 \times 120 \times 10^{-3} = 60.00\text{ kg VSS/d}$$
7. **Lượng bùn dư cần chủ động xả bỏ định kỳ ($P_{X,w}$):**
   $$P_{X,w} = P_{X,VSS} - P_{X,e} = 432.06 - 60.00 = 372.06\text{ kg VSS/d}$$
8. **Thời gian lưu tổng chất rắn thực tế trong bể ($\text{SRT}_{total}$):**
   $$\text{SRT}_{total} = \frac{M_{VSS}}{P_{X,VSS}} = \frac{15,000.00\text{ kg VSS}}{432.06\text{ kg VSS/d}} = 34.72\text{ ngày}$$
   *(Lưu ý: Thời gian lưu bùn riêng của sinh khối hoạt tính là $60.0\text{ ngày}$ nhờ cơ chế phân tầng lắng lọc).*

##### 8.6.2.6. Bước 5: Tính Sản lượng Khí Methane, Biogas và Tiềm năng Phát nhiệt/Công suất Điện
1. **Lượng COD chuyển hóa thành tế bào sinh khối:**
   $$\text{COD}_{bio} = 1.42 \times P_{X,bio} = 1.42 \times 154.29 = 219.10\text{ kg COD/d}$$
2. **Lượng COD chuyển hóa thành khí Methane:**
   $$\text{COD}_{CH_4} = \Delta\text{COD} - \text{COD}_{bio} = 5,400.00 - 219.10 = 5,180.90\text{ kg COD/d}$$
3. **Lưu lượng khí Methane thu hồi:**
   - Tại STP ($0^\circ\text{C}, 1\text{ atm}$):
     $$Q_{CH_4,STP} = 0.35 \times 5,180.90 = 1,813.32\text{ m}^3\text{ CH}_4/\text{d}$$
   - Tại nhiệt độ vận hành $25^\circ\text{C}$ ($298.15\text{ K}$):
     $$Q_{CH_4,25^\circ\text{C}} = 1,813.32 \times \left( \frac{298.15}{273.15} \right) = 1,979.24\text{ m}^3\text{ CH}_4/\text{d}$$
4. **Tổng lưu lượng Biogas ($65\%\ \text{CH}_4$):**
   - Tại STP:
     $$Q_{biogas,STP} = \frac{1,813.32}{0.65} = 2,789.72\text{ m}^3/\text{d}$$
   - Tại $25^\circ\text{C}$:
     $$Q_{biogas,25^\circ\text{C}} = \frac{1,979.24}{0.65} = 3,044.98\text{ m}^3/\text{d}$$
5. **Tiềm năng năng lượng thu hồi:**
   - Năng lượng nhiệt tiềm năng:
     $$E_{heat} = 1,813.32\text{ m}^3/\text{d} \times 35,800\text{ kJ/m}^3 = 64,916,856\text{ kJ/d} = 64.92\text{ GJ/d}$$
   - Công suất nhiệt liên tục tương đương:
     $$P = \frac{64,916,856\text{ kJ/d}}{86,400\text{ s/d}} = 751.35\text{ kW}$$

##### 8.6.2.7. Bước 6: Cân bằng Dinh dưỡng Toàn diện theo Tỷ lệ $(\text{COD}/Y):N:P:S$
1. **Tỷ lệ dinh dưỡng lượng tế chuẩn:**
   $$\frac{50}{Y_H} = \frac{50}{0.08} = 625 \implies \text{COD} : \text{N} : \text{P} : \text{S} = 625 : 5 : 1 : 1$$
2. **Khối lượng dinh dưỡng tối thiểu cần thiết cho $\Delta\text{COD} = 5,400.00\text{ kg/d}$:**
   - Nhu cầu Nitơ:
     $$N_{req} = 5,400.00 \times \left( \frac{5}{625} \right) = 43.20\text{ kg N/d}$$
   - Nhu cầu Phospho:
     $$P_{req} = 5,400.00 \times \left( \frac{1}{625} \right) = 8.64\text{ kg P/d}$$
   - Nhu cầu Lưu huỳnh:
     $$S_{req} = 5,400.00 \times \left( \frac{1}{625} \right) = 8.64\text{ kg S/d}$$
3. **Nồng độ tối thiểu yêu cầu trong nước thải nạp ($Q = 500\text{ m}^3\text{/d}$):**
   - Nồng độ Nitơ: $C_N = (43.20 \times 10^3) / 500 = 86.40\text{ mg/L}$
   - Nồng độ Phospho: $C_P = (8.64 \times 10^3) / 500 = 17.28\text{ mg/L}$
   - Nồng độ Lưu huỳnh: $C_S = (8.64 \times 10^3) / 500 = 17.28\text{ mg/L}$

##### 8.6.2.8. Bước 7: Kiểm tra Độc tính Ức chế và Lập Chiến lược Tuần hoàn / Pha loãng Theo Ma trận Quyết định
1. **Kiểm tra các ngưỡng ức chế độc tính kỹ thuật:**
   - Amonia: Kiểm tra tổng $\text{NH}_3\text{-N} < 1,500\text{ mg/L}$.
   - Độ mặn: Kiểm tra Clorua $\text{Cl}^- < 15,000\text{ mg/L}$.
   - Sulfide: Kiểm tra Sulfide hòa tan $\text{S}^{2-} < 200\text{ mg/L}$.
2. **Quy trình ra quyết định vận hành theo Ma trận Tải trọng & Sulfide (Slide 30):**
   - Tải trọng vận hành hiện tại: $\text{OLR} = 8.0\text{ kg COD/(m}^3\cdot\text{d)}$, nằm trong khung quy chuẩn **$5.0 - 20.0\text{ kg COD/(m}^3\cdot\text{d)}$**.
   - **Trường hợp A ($\text{S}^{2-} < 200\text{ mg/L}$):** Nước thải được nạp thẳng trực tiếp vào bể UASB mà không bắt buộc phải tuần hoàn dòng ra.
   - **Trường hợp B ($\text{S}^{2-} > 200\text{ mg/L}$):** Bắt buộc phải kích hoạt bơm tuần hoàn nước sau lắng trở lại hòa trộn với nước thải đầu vào cho đến khi nồng độ $\text{S}^{2-}$ hỗn hợp nạp vào đáy bể giảm xuống dưới ngưỡng an toàn $< 100\text{ mg/L}$.
   - Nếu tải trọng $\text{OLR} > 20.0\text{ kg COD/(m}^3\cdot\text{d)}$: Bắt buộc phải pha loãng nước thải cấp vào để chống quá tải hữu cơ và chua hóa bể.
3. **Độ kiềm bổ sung duy trì pH:**
   - Nước thải đầu vào có độ kiềm thấp ($500\text{ g CaCO}_3\text{/m}^3$), cần bổ sung $1,000 - 1,250\text{ kg CaCO}_3\text{/d}$ (tương đương châm $1,680 - 2,100\text{ kg NaHCO}_3\text{/d}$) hoặc tận dụng dòng tuần hoàn giàu kiềm bicarbonate để bảo đảm pH ổn định $6.8 - 7.4$.

##### 8.6.2.9. Bảng Tổng kết Thông số Kỹ thuật Thiết kế Bể UASB (EX-02)
| Thông số Thiết kế | Ký hiệu | Giá trị Kỹ thuật | Đơn vị | Ghi chú & Đánh giá |
| :--- | :--- | :--- | :--- | :--- |
| **Thể tích làm việc hữu dụng** | $V$ | $750.00$ | $\text{m}^3$ | Dựa trên OLR $= 8.0\text{ kg/(m}^3\cdot\text{d)}$ |
| **Thời gian lưu nước** | $\text{HRT}$ | $1.50$ ($36.0$) | ngày (giờ) | Đủ điều kiện tạo hạt bùn |
| **Diện tích mặt bằng bể** | $A$ | $125.00$ | $\text{m}^2$ | Mặt bằng tiết diện ngang |
| **Chiều rộng bể** | $W$ | $7.91$ | m | Tỷ lệ $L/W = 2.0$ |
| **Chiều dài bể** | $L$ | $15.81$ | m | Kích thước phủ bì bể |
| **Chiều cao tổng thể bể** | $H_{total}$ | $6.00$ | m | Gồm vùng phản ứng, GLS và nước tĩnh |
| **Chiều cao vùng phản ứng** | $H_{active}$ | $4.00$ | m | Vùng lưu giữ bùn đậm đặc |
| **Chiều cao bộ tách GLS** | $H_{separator}$ | $1.50$ | m | Chụp thu khí 3 pha |
| **Chiều cao vùng nước trong** | $H_{clear}$ | $0.50$ | m | Lắng thứ cấp nội tại |
| **Vận tốc dòng dâng bề mặt** | $v_{up}$ | $0.167$ | m/h | Rất an toàn ($\ll 1.0\text{ m/h}$) |
| **Tổng sinh khối bùn trong bể** | $M_{VSS}$ | $15,000.00$ | kg VSS | Ở MLVSS $= 30\text{ kg/m}^3$ |
| **Sản lượng sinh khối mới** | $P_{X,bio}$ | $154.29$ | kg VSS/d | Ở SRT $= 60\text{ ngày}$ |
| **Tổng lượng bùn bay hơi ròng** | $P_{X,VSS}$ | $432.06$ | kg VSS/d | Bùn sinh học + trơ |
| **Lượng bùn xả đáy định kỳ** | $P_{X,w}$ | $372.06$ | kg VSS/d | Xả qua các van thu bùn đa tầng |
| **Thời gian lưu bùn tổng** | $\text{SRT}_{total}$ | $34.72$ | ngày | SRT hoạt tính $\ge 60\text{ d}$ |
| **Lưu lượng Methane (STP)** | $Q_{CH_4,STP}$ | $1,813.32$ | $\text{m}^3/\text{d}$ | Tại $0^\circ\text{C}, 1\text{ atm}$ |
| **Lưu lượng Methane ở $25^\circ\text{C}$** | $Q_{CH_4,25^\circ\text{C}}$ | $1,979.24$ | $\text{m}^3/\text{d}$ | Điều kiện nhiệt độ thực tế |
| **Tổng lưu lượng Biogas ($65\%\ \text{CH}_4$)** | $Q_{biogas,25^\circ\text{C}}$ | $3,044.98$ | $\text{m}^3/\text{d}$ | Thu hồi làm nhiên liệu |
| **Công suất nhiệt tiềm năng** | $P$ | $751.35$ | kW | Công suất phát liên tục |
| **Nhu cầu Nitơ tối thiểu** | $N_{req}$ | $43.20$ | kg N/d | Tương đương $86.4\text{ mg/L}$ |
| **Nhu cầu Phospho tối thiểu** | $P_{req}$ | $8.64$ | kg P/d | Tương đương $17.3\text{ mg/L}$ |
| **Nhu cầu Lưu huỳnh tối thiểu** | $S_{req}$ | $8.64$ | kg S/d | Tương đương $17.3\text{ mg/L}$ |

---

#### 8.6.3. Bài toán Thiết kế Mở rộng: Thiết kế Hệ thống UASB Song song Công suất $3,000\text{ m}^3\text{/d}$ Nước thải Nhà máy Bia

##### 8.6.3.1. Đề bài & Dữ liệu Công nghệ Nhà máy Bia
- **Lưu lượng thiết kế:** $Q = 3,000.0\text{ m}^3/\text{d} = 125.0\text{ m}^3/\text{h}$
- **Nồng độ COD hòa tan đầu vào ($S_0$):** $5,000.0\text{ mg/L} = 5.0\text{ kg COD/m}^3$
- **Tổng tải lượng COD:** $M_{COD} = 3,000 \times 5.0 = 15,000.0\text{ kg COD/d}$
- **Tải trọng OLR lựa chọn:** $10.0\text{ kg COD/(m}^3\cdot\text{d)}$
- **Giới hạn vận tốc dâng cực đại:** $v_{up} \le 0.70\text{ m/h}$
- **Chiều cao bể dự kiến:** $H_{total} = 6.0\text{ m}$ (chiều sâu hiệu dụng $H_{eff} = 5.5\text{ m}$)

##### 8.6.3.2. Tính toán Thể tích Bể và Phân chia 2 Đơn nguyên Song song
1. **Thể tích làm việc yêu cầu:**
   $$V_{UASB} = \frac{M_{COD}}{\text{OLR}} = \frac{15,000.0\text{ kg COD/d}}{10.0\text{ kg/(m}^3\cdot\text{d)}} = 1,500.0\text{ m}^3$$
2. **Thời gian lưu nước:**
   $$\text{HRT} = \frac{1,500.0}{3,000.0} = 0.50\text{ ngày} = 12.0\text{ giờ}$$
3. **Diện tích mặt bằng bể tổng cộng:**
   $$A_{plan} = \frac{V_{UASB}}{H_{eff}} = \frac{1,500.0\text{ m}^3}{5.50\text{ m}} = 272.73\text{ m}^2$$
4. **Kiểm tra vận tốc dâng tổng thể:**
   $$v_{up} = \frac{125.0\text{ m}^3/\text{h}}{272.73\text{ m}^2} = 0.458\text{ m/h} \le 0.70\text{ m/h}\quad \text{(Thỏa mãn)}$$
5. **Phân chia 2 đơn nguyên (module) vận hành song song ($N = 2$ bể):**
   - Lưu lượng mỗi đơn nguyên: $Q_1 = 1,500.0\text{ m}^3/\text{d} = 62.5\text{ m}^3/\text{h}$
   - Diện tích mỗi bể: $A_1 = 272.73 / 2 = 136.36\text{ m}^2$
   - Chọn kích thước tiêu chuẩn:
     - Chiều rộng: $W = 9.00\text{ m}$
     - Chiều dài: $L = 15.20\text{ m}$
     - Diện tích thực tế mỗi bể: $A_{actual} = 9.00 \times 15.20 = 136.80\text{ m}^2$ ($273.60\text{ m}^2$ cho 2 bể)
     - Tổng thể tích thực tế 2 bể: $V_{actual} = 273.60 \times 6.00 = 1,641.6\text{ m}^3$
     - Tải trọng thực tế: $\text{OLR}_{actual} = 15,000 / 1,641.6 = 9.14\text{ kg COD/(m}^3\cdot\text{d)}$

##### 8.6.3.3. Thiết kế Mạng lưới Phân phối Nước vào Đáy bể và Mật độ Đầu phun (Nozzles)
- Tiêu chuẩn mật độ đầu phun cho bùn hạt: $1\text{ đầu phun per } 2.0\text{ m}^2$ diện tích sàn.
- Số lượng vòi phun cho mỗi đơn nguyên:
  $$N_{nozzles} = \frac{136.80\text{ m}^2}{2.0\text{ m}^2/\text{vòi}} = 68.4 \implies \text{Chọn } 70\text{ vòi phun/bể} \quad (140\text{ vòi cho 2 bể})$$
- Bố trí ống nhánh: Gồm 7 ống nhánh song song, mỗi ống gắn 10 vòi phun nón ngược hướng xuống đáy sàn, cách đáy $0.20\text{ m}$.
- Vận tốc dòng phụt tại miệng vòi: $v_{nozzle} \approx 1.5 - 2.0\text{ m/s}$ để tạo lực xoáy xáo trộn đều đáy bùn mà không phá vỡ hạt bùn kỵ khí.

##### 8.6.3.4. Thiết kế Kỹ thuật Bộ tách 3 Pha GLS và Tải trọng Thu khí Bề mặt
- **Góc nghiêng tấm thu bùn:** Chọn góc nghiêng $55^\circ$ để bùn tự trượt sạch hoàn toàn.
- **Tải trọng bề mặt chụp thu khí:** Kiểm tra tải thu khí:
  $$Q_{biogas} \approx 7,739\text{ m}^3/\text{d} \implies v_{gas} \approx 2.35\text{ m}^3/(\text{m}^2\cdot\text{h}) < 3.0\text{ m}^3/(\text{m}^2\cdot\text{h})\quad \text{(Đạt tiêu chuẩn)}$$

---

### 8.7. Hướng dẫn Vận hành, Giám sát Sự cố & Ma trận Quyết định (Operational Troubleshooting & Decision Matrix)

#### 8.7.1. Sự cố Nổi Bùn trong Bể Lắng Thứ cấp Kỵ khí

##### 8.7.1.1. Nguyên nhân: Khí hòa tan siêu bão hòa tạo bọt vi mô bám vào bông bùn
- Nước thải sau bể CSTR kỵ khí chứa lượng lớn bọt khí $\text{CH}_4$ và $\text{CO}_2$ siêu bão hòa. Khi vào bể lắng, vi sinh vật kỵ khí tiếp tục sinh khí làm các bọt khí vi mô dính chặt vào bông bùn, kéo bùn nổi lên mặt bể thành mảng lớn và trôi qua máng tràn.

##### 8.7.1.2. Biện pháp Khắc phục: Vận hành buồng khử khí chân không và kiểm soát cào bùn
- **Kiểm tra và hiệu chỉnh buồng khử khí chân không:** Đảm bảo duy trì áp suất âm từ $0.3 - 0.5\text{ atm}$ trong buồng degassing để hút sạch triệt để bọt khí bám dính trước khi dẫn sang bể lắng.
- **Tăng tốc độ tuần hoàn bùn (RAS):** Giảm thời gian lưu bùn trong bể lắng xuống dưới $1.5 - 2.0\text{ giờ}$ để ngăn phản ứng sinh khí phát triển trong đáy phễu lắng.
- **Vận hành hệ thống cào bùn:** Tối ưu hóa tốc độ quay của dàn cào bùn đáy (tránh quay quá nhanh làm tan vỡ bông bùn hoặc quá chậm gây lưu bùn).

---

#### 8.7.2. Sự cố Độc tính Sulfide và Cạnh tranh của Vi khuẩn Khử Sulfate (SRB)

##### 8.7.2.1. Cơ chế Ức chế Methanogenesis bởi $S^{2-}$ hòa tan và Khí $H_2S$
- Nước thải chứa nồng độ sulfate cao bị vi khuẩn SRB chuyển hóa thành dissolved sulfide ($\text{S}^{2-}, \text{HS}^-$) và $\text{H}_2\text{S}$ hòa tan. Nồng độ sulfide vượt ngưỡng $200\text{ mg/L}$ làm tê liệt enzyme của methanogens, làm giảm sản lượng khí metan và ăn mòn công trình.

##### 8.7.2.2. Ma trận Quyết định Tuần hoàn Dòng ra Kiểm soát Sulfide (Decision Matrix Slide 30)
| Tải trọng Hữu cơ Thể tích (OLR) | Nồng độ Sulfide hòa tan ($\text{S}^{2-}$) | Hành động Kỹ thuật Bắt buộc |
| :--- | :--- | :--- |
| **$< 5.0\text{ kg COD/(m}^3\cdot\text{d)}$** | Mọi nồng độ | Không cần tuần hoàn dòng ra; nạp trực tiếp nước thải thô. |
| **$5.0 - 20.0\text{ kg COD/(m}^3\cdot\text{d)}$** | $< 200\text{ mg/L}$ | Không cần tuần hoàn dòng ra; cấp nước thải thô trực tiếp. |
| **$5.0 - 20.0\text{ kg COD/(m}^3\cdot\text{d)}$** | $> 200\text{ mg/L}$ | **Bắt buộc tuần hoàn dòng ra:** Bật bơm tuần hoàn nước sau xử lý để pha loãng dòng vào cho đến khi nồng độ sulfide hỗn hợp $< 100\text{ mg/L}$; hoặc pha loãng nước thô để đưa tải trọng OLR $\le 5.0\text{ kg COD/(m}^3\cdot\text{d)}$. |
| **$> 20.0\text{ kg COD/(m}^3\cdot\text{d)}$** | Mọi nồng độ | **Bắt buộc pha loãng nước thải cấp:** Giảm tải nạp bằng cách pha loãng với nước sạch hoặc nước tuần hoàn để chống hiện tượng quá tải và chua hóa bể. |

---

#### 8.7.3. Sự cố Quá tải Hữu cơ và Chua hóa Bể Phản ứng (Reactor Acidification / Souring)

##### 8.7.3.1. Dấu hiệu Nhận biết: Tỷ số VFA/Alkalinity tăng vượt $0.4$, pH giảm dưới $6.5$
- **Giai đoạn 1 (Cảnh báo sớm):** Tỷ số Ripley ($\text{VFA/Alk}$) tăng từ $0.2 - 0.3$ lên $0.4 - 0.5$; nồng độ axit propionic tăng đột biến; hàm lượng $\text{CO}_2$ trong biogas tăng vọt từ $35\%$ lên $> 45 - 50\%$ do bicarbonate bị phân hủy giải phóng $\text{CO}_2$.
- **Giai đoạn 2 (Chua hóa hoàn toàn):** Tỷ số $\text{VFA/Alk} > 0.8$; pH giảm mạnh xuống $< 6.5$ rồi $< 6.0$; sản lượng khí methane sụt giảm gần như bằng không; bùn có mùi chua nồng.

##### 8.7.3.2. Biện pháp Khắc phục Khẩn cấp: Giảm tải nạp, pha loãng cưỡng bức và châm kiềm đệm
- **Bước 1: Cắt giảm tải nạp:** Lập tức giảm lưu lượng cấp nước thải thô vào từ $50 - 100\%$ (chỉ chạy tuần hoàn nước sau xử lý).
- **Bước 2: Châm hóa chất nâng kiềm đệm:** Bổ sung trực tiếp Natri Bicarbonate ($\text{NaHCO}_3$) vào dòng tuần hoàn cho đến khi đưa pH trở lại dải an toàn $7.0 - 7.2$ và độ kiềm đạt $\ge 3,000\text{ mg CaCO}_3\text{/L}$.
- **Bước 3: Phục hồi từ từ:** Sau khi tỷ số $\text{VFA/Alk}$ giảm xuống $< 0.3$, tăng dần tải nạp hữu cơ từng bước $10 - 20\%$ mỗi tuần.

---

#### 8.7.4. Sự cố Ức chế Amonia Tự do Trong Nước thải Đậm đặc Protein

##### 8.7.4.1. Cơ chế Thâm nhập Màng tế bào của Amonia Tự do
- Khi phân hủy nước thải giết mổ gia súc, chế biến thủy sản, quá trình deamination giải phóng lượng lớn ion amoni. Ở nhiệt độ cao hoặc pH kiềm ($> 7.5$), amonia tự do (FAN) tăng cao thâm nhập vào tế bào methanogen gây ức chế sinh trưởng.

##### 8.7.4.2. Giải pháp: Kiểm soát pH $< 7.2$, pha loãng hoặc tiền xử lý Tước Amonia (Stripping)
- **Điều chỉnh pH thấp:** Vận hành hệ thống ở ngưỡng pH cận dưới $6.8 - 7.1$ để dịch chuyển cân bằng $\text{NH}_3 \rightleftharpoons \text{NH}_4^+$ về dạng ion $\text{NH}_4^+$ ít độc.
- **Tiền xử lý:** Trang bị tháp Stripping tước amonia bằng không khí ở thượng nguồn hoặc pha loãng dòng thải đầu vào.

---

#### 8.7.5. Sự cố Trôi Bùn Hạt và Phá vỡ Tầng Mền Bùn UASB

##### 8.7.5.1. Nguyên nhân: Vận tốc dâng vượt ngưỡng ($v_{up} > 1.5 - 3.0\text{ m/h}$), kẹt tấm chắn khí
- Lưu lượng nước thải đột ngột tăng vọt (hydraulic peak surge) đẩy vận tốc dòng dâng $v_{up}$ vượt ngưỡng lắng của hạt bùn.
- Bọt khí metan bị kẹt trong chụp GLS do tắc đường ống thoát khí, khiến khí tích tụ tràn sang vùng lắng và đẩy tung hạt bùn qua máng tràn.
- Thiếu hụt vi chất dinh dưỡng ($\text{Ca}^{2+}, \text{Fe}, \text{Ni}, \text{Co}$) khiến mạng lưới liên kết EPS bị tan rã, hạt bùn bị phân rã (disintegration) thành bùn bông nhẹ.

##### 8.7.5.2. Biện pháp Khôi phục: Điều chỉnh thủy lực, bổ sung vi lượng thúc đẩy tạo hạt lại
- **Kiểm soát thủy lực:** Giảm lưu lượng bơm cấp vào, duy trì $v_{up} \le 1.0\text{ m/h}$; nếu có dao động lưu lượng lớn, phải sử dụng bể điều hòa (Equalization Tank) dung tích đủ lớn ở thượng nguồn.
- **Vệ sinh thông tắc chụp GLS:** Thông rửa đường ống dẫn khí biogas và xả rửa các tấm chắn định hướng khí.
- **Châm bổ sung ion Canxi ($\text{Ca}^{2+}$) và muối khoáng vi lượng:** Châm $\text{CaCl}_2$ ($100 - 200\text{ mg/L}$) cùng hỗn hợp vi lượng $\text{Fe}, \text{Ni}, \text{Co}$ để tái lập cầu nối EPS và kích thích vi khuẩn *Methanosaeta* tạo lại hạt bùn mới.
