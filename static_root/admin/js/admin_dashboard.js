function ThisMonthSales(){
    thismonthsales = document.getElementById("thismonthsales")
    thismonthsales.style.display=""
    total_sales = document.getElementById("total_sales")
    total_sales.style.display="none"
    today_sales = document.getElementById("today_sales")
    today_sales.style.display="none"
}
function TotalSales(){
    total_sales = document.getElementById("total_sales")
    total_sales.style.display=""
    thismonthsales = document.getElementById("thismonthsales")
    thismonthsales.style.display="none"
    today_sales = document.getElementById("today_sales")
    today_sales.style.display="none"
}
function TodaySales(){
    today_sales = document.getElementById("today_sales")
    today_sales.style.display=""
    total_sales = document.getElementById("total_sales")
    total_sales.style.display="none"
    thismonthsales = document.getElementById("thismonthsales")
    thismonthsales.style.display="none"
}

function TotalRevenue(){
    totalrevenue = document.getElementById("totalrevenue")
    totalrevenue.style.display=""
    thismonthrevenue = document.getElementById("thismonthrevenue")
    thismonthrevenue.style.display="none"
    todayrevenue = document.getElementById("todayrevenue")
    todayrevenue.style.display="none"
}
function ThisMonthRevenue(){
    thismonthrevenue = document.getElementById("thismonthrevenue")
    thismonthrevenue.style.display=""
    totalrevenue = document.getElementById("totalrevenue")
    totalrevenue.style.display="none"
    todayrevenue = document.getElementById("todayrevenue")
    todayrevenue.style.display="none"
}
function TodayRevenue(){
    thismonthrevenue = document.getElementById("thismonthrevenue")
    thismonthrevenue.style.display="none"
    totalrevenue = document.getElementById("totalrevenue")
    totalrevenue.style.display="none"
    todayrevenue = document.getElementById("todayrevenue")
    todayrevenue.style.display=""
}

function TotalRating(){
    totalrating = document.getElementById("totalrating")
    totalrating.style.display=""
    thismonthrating = document.getElementById("thismonthrating")
    thismonthrating.style.display="none"
    todayrating = document.getElementById("todayrating")
    todayrating.style.display="none"
}
function ThisMonthRating(){
    totalrating = document.getElementById("totalrating")
    totalrating.style.display="none"
    thismonthrating = document.getElementById("thismonthrating")
    thismonthrating.style.display=""
    todayrating = document.getElementById("todayrating")
    todayrating.style.display="none"
}
function TodayRating(){
    totalrating = document.getElementById("totalrating")
    totalrating.style.display="none"
    thismonthrating = document.getElementById("thismonthrating")
    thismonthrating.style.display="none"
    todayrating = document.getElementById("todayrating")
    todayrating.style.display=""
}

window.onload = function(){ 
    document.getElementById("total_review_btn").addEventListener('click',function (){
        thismonthreview = document.getElementById("thismonthreview")
        today_review = document.getElementById("today_review")
        total_reviews = document.getElementById("total_reviews")
        thismonthreview.style.display = "none"
        today_review.style.display = "none"
        total_reviews.style.display = ""
    })
    document.getElementById("month_review_btn").addEventListener('click',function (){
        thismonthreview = document.getElementById("thismonthreview")
        today_review = document.getElementById("today_review")
        total_reviews = document.getElementById("total_reviews")
        thismonthreview.style.display = ""
        today_review.style.display = "none"
        total_reviews.style.display = "none"
    })
    document.getElementById("today_review_btn").addEventListener('click',function (){
        thismonthreview = document.getElementById("thismonthreview")
        today_review = document.getElementById("today_review")
        total_reviews = document.getElementById("total_reviews")
        thismonthreview.style.display = "none"
        today_review.style.display = ""
        total_reviews.style.display = "none"
    })
    document.getElementById("today_checkin_btn").addEventListener('click',function (){
        thismonthcheckin = document.getElementById("thismonthcheckin")
        today_checkin = document.getElementById("today_checkin")
        total_checkin = document.getElementById("total_checkin")
        thismonthcheckin.style.display = "none"
        today_checkin.style.display = ""
        total_checkin.style.display = "none"
    })
    document.getElementById("month_checkin_btn").addEventListener('click',function (){
        thismonthcheckin = document.getElementById("thismonthcheckin")
        today_checkin = document.getElementById("today_checkin")
        total_checkin = document.getElementById("total_checkin")
        thismonthcheckin.style.display = ""
        today_checkin.style.display = "none"
        total_checkin.style.display = "none"
    })
    document.getElementById("total_checkin_btn").addEventListener('click',function (){
        thismonthcheckin = document.getElementById("thismonthcheckin")
        today_checkin = document.getElementById("today_checkin")
        total_checkin = document.getElementById("total_checkin")
        thismonthcheckin.style.display = "none"
        today_checkin.style.display = "none"
        total_checkin.style.display = ""
    })
}