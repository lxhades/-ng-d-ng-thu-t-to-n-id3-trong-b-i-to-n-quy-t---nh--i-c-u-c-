import pandas as pd

df = pd.read_csv("test.csv")
def predict_play(WaterClarity, Outlook=None, Humidity=None,
                 Time=None, Temperature=None, Wind=None):


    if WaterClarity == "Trong" and Outlook == "Âm u" and Humidity == "Cao" and Time == "Tối":
        return "Không"


    if WaterClarity == "Trong" and Outlook == "Mát mẻ" and Humidity == "Cao":
        return "Không"


    if (WaterClarity == "Trong" and Outlook == "Mưa nhẹ"
        and Time == "Tối" and Temperature == "Lạnh"):
        return "Không"


    if WaterClarity == "Trong" and Outlook == "Mưa nhẹ" and Time == "Khác":
        return "Không"


    if WaterClarity == "Trong" and Outlook == "Mưa lớn":
        return "Không"


    if (WaterClarity == "Trong" and Outlook == "Nắng gắt"
        and Humidity == "Thấp" and Time == "Tối"):
        return "Không"

    if (WaterClarity == "Trong" and Outlook == "Nắng gắt"
        and Humidity == "Cao" and Wind != "Gió nhẹ"):
        return "Không"

    if WaterClarity == "Quá đục":
        return "Không"

    if (WaterClarity == "Hơi đục" and Wind == "Gió nhẹ"
        and Outlook == "Mưa lớn"):
        return "Không"

    if (WaterClarity == "Hơi đục" and Wind == "Không gió"
        and Temperature == "Nóng" and Humidity == "Cao"):
        return "Không"
    if WaterClarity == "Hơi đục" and Wind == "Gió mạnh":
        return "Không"
    return "Có"
correct = 0
for index, row in df.iterrows():
    predicted = predict_play(
        WaterClarity=row["WaterClarity"],
        Outlook=row["Outlook"],
        Humidity=row["Humidity"],
        Time=row["Time"],
        Temperature=row["Temperature"],
        Wind=row["Wind"]
    )
    actual = row["Play"]
    if predicted == actual:
        correct += 1

accuracy = correct / len(df)
print("Độ chính xác:", accuracy)