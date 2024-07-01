from typing import List
from llama_index.core.types import BaseModel
import enum

questions = {}

class confidence_type(str, enum.Enum):
    """
    How confident are you in the answer?
    If you have a high degree of confidence, select “high.”
    If you don't have enough information in the context to answer the question, select “low.”
    """
    High = "high"
    Low = "low"

#NameCorp
class NameCorp(BaseModel):
    """Data model for Company"""
    val: str
    confidence: confidence_type

questions['NameCorp'] = {
        'description':"""The name of the 10-K filing company. If the 10-K filing 
company did not file bankruptcy, add the name of the principal filing
subsidiary in parentheses, followed by “only.” If more than one 10-K filing
company is administratively consolidated in the same bankruptcy case, add
the names of the additional 10-K filers in parentheses, not followed by
“only.” If the company has filed bankruptcy more than once, add the year of
this bankruptcy filing in parentheses. Remove apostrophes from names.
Access will tolerate apostrophes, but the WebBRD will not. If a company
name contains an apostrophe, the company’s date will not appear in View
data by company.""",
'output_class': NameCorp
}

#AssetsPetition
class AssetsPetition(BaseModel):
    """Data model for AssetsPetition, unit in millions of dollars"""
    val: float
    confidence: confidence_type

questions['AssetsPetition'] = {
        'description':"""Total assets of the debtors, as indicated on “Exhibit A” to
the petition, in millions of dollars. The SEC requires that companies file
Exhibit A if they remain public as of filing. If the Exhibit A amount listed
differs substantially from AssetsBefore, we investigate whether the amount
listed is for only the petitioning corporation or for the entire consolidated
group. If the amount is for the consolidate group, we use it. If the amount is
for only the petitioning corporation, we investigate whether the total
amounts listed on Exhibit A for all filers in the group indicate the aggregate
assets of the group. If they do, we use the total. If an amount is not available
from either source, we use the best amount available from (1) the first monthly 
operating report filed for the group in the bankruptcy case, (2) the
first 10-K or 10-Q filed with the SEC during the bankruptcy case, or (3) the
debtors’ schedules. For data entered prior to August 2004, we accepted
amounts from several sources. First, for cases filed in the 1980s, we
accepted the amount stated in on a list of bankruptcy cases maintained by
the SEC. When the SEC shows a different amount on a later list, we used
the later amount. Second, we accepted the assets at filing reported in
reputable publications. Third, in a few cases, we used data from the
schedules filed with the court. Most of the AssetsPetition data were
collected for both older and newer cases were collected beginning in August
2004. That month we adopted these new protocols: (1) We do not use
Exhibit A amounts that appear not to be consolidated. (2) We will use
amounts that appeared on Exhibit A, if available. (3) If an Exhibit A amount
is not available, we will use the next best source among the following –
schedules or monthly operating reports filed in the case; balance sheets filed
with the SEC during the case.""",
'output_class': AssetsPetition
}

#CeoFiling
class CeoFiling(BaseModel):
    """Data model for CeoFiling, the name of the CEO"""
    val: str
    confidence: confidence_type

questions['CeoFiling'] = {
        'description':"""The name of the debtor’s chief executive officer at filing. If no
person holds the chief executive officer title at filing, enter the name of the
highest officer, followed by a comma and the name of the office held. E.g.,
“Samuel Wilson, president.” If no one is CEO, but someone is acting CEO,
enter the name followed by “acting CEO”. A person is CEO during a period
when the person is co-CEO. If only one person qualifies as CEO on the
DateFiled, that is the one we use. If two qualify on the DateFiled, we use
the new one if he is on the petition or making a statement or doing
something as CEO by the moment of filing. If the new CEO is in office on
the DateFiled but there is no information regarding activity from either the
new or old CEO on the DateFiled, use the new CEO. """,
'output_class': CeoFiling
}

#CityFiled
class CityFiled(BaseModel):
    """Data model for CityFiled, the city in which the case was filed"""
    val: str
    confidence: confidence_type

questions['CityFiled'] = {
        'description':"""The city in which the case was filed. The city will always be a
city in which court meets and nearly always a city in which there is a clerk’s
office. If you have a district, but not a court city, run searches that combine
the name of the debtor with each of the court cities in the district to find
statements linking the case to a court city.""",
'output_class': CityFiled
}

#ClaimsUnsec
class ClaimsUnsec(BaseModel):
    """Data model for ClaimsUnsec, the total amount, in millions of dollars, of non-priority"""
    val: float
    confidence: confidence_type

questions['ClaimsUnsec'] = {
        'description':"""
The total amount, in millions of dollars, of non-priority
unsecured claims, as indicated in the disclosure statement and compiled on
the Distribution Spreadsheet. If the disclosure statement information is
inadequate, we also consider the information on the schedules. Unsecured
claims include the claims of unsecured general creditors, unsecured senior
classes, unsecured junior classes, and the unsecured portions of secured
creditors’ claims if the unsecured portion is separately classified and
treated. Unsecured claims do not include claims entitled to priority under
Bankruptcy Code §507(a) (priority claims) or claims that are subordinated
under Bankruptcy Code 510(b) (sale-of-securities claims). Unsecured
claims do not include intercompany claim classes. We report an amount for
unsecured claims only if the disclosure statement provides the amount of
unsecured claims for all substantial unsecured classes. If the estimated
claims in a class are stated as a range, use the midpoint of the range. If the
estimated claims are stated as “less than” a stated amount, use the stated
amount. If the debtor states that claims are unlikely to be allowed, we
accept the debtor’s statement. If claims are disputed and the parties fix the 
amount of the claims by settlement, we use the settlement amount. If the
parties fix only the distribution by settlement and the information is
available to do so, we may impute the amount of the claims from the
settlement. For example, if the disputed unsecured claim is $10 million,
the settlement is for $1 million, and the other unsecured creditors are getting
50 cents on the dollar, we may infer that the parties agreed that the
unsecured claim was $2 million.
""",
'output_class': ClaimsUnsec
}

#CommCred

class CommCred_type(str, enum.Enum):
    """Possible Values for CommCred"""
    Yes = "Yes"
    No = "No"


class CommCred(BaseModel):
    """
    Yes and No Answer for CommCred
    """
    val: CommCred_type
    confidence: confidence_type


questions['CommCred'] = {
        'description':"""
Was an official committee appointed to represent the
unsecured creditors prior to case disposition? Yes/no. The best evidence is a
copy of the appointment. Committees appointed to represent particular
subgroups of creditors, such as a particular group of bondholders, are not
creditors’ committees. In some older cases, if the disclosure statement
indicates that no unsecured creditors’ committee had been appointed we
assumed that none was appointed prior to confirmation. In Refco Finance,
Inc., the creditors’ committee bifurcated. We recorded counsel for the
original committee and treated the second committee as an “additional
committee.” In Envirodyne Industries Inc., two official committees were
appointed to represent Trade Creditors and Bondholders. We considered
these to be subgroups and excluded them both. If the case was dismissed
before the order for relief, enter “no order for relief.” Other options are
“Chapter 7 at filing” and “case not disposed.”
""",
'output_class': CommCred
}

#CommCredAtty

class CommCredAtty(BaseModel):
    """
    Name of the law firm representing the unsecured creditors’ committee
    “none” if there is no evidence of an attorney hired to represent the committee.
    """
    val: str
    confidence: confidence_type


questions['CommCredAtty'] = {
        'description':"""
CommCredAttyCol, resolved to a single “lead” and
employing the most recent name for a firm that has changed its name. A
firm is lead if it is described as “counsel” or “attorney” while the competing
firm is described as “co-counsel.” When there is doubt about which firm is
lead, we examine the available fee information to determine which firm was
dominant early in the case. Ultimately, we make a judgment, using
hindsight, to determine which firm was probably lead at the time the representations
began. Enter “none” if there is no evidence of an attorney
hired to represent the committee.”
""",
'output_class': CommCredAtty
}

#CommEquity

class CommEquity_type(str, enum.Enum):
    """Possible Values for CommEquity"""
    Yes = "Yes"
    No = "No"
    Denied = "denied"
    Motion = "motion withdrawn"
    NoOrder = "no order for relief"
    Chapter7 = "Chapter 7 at filing"
    NotDisposed = "case not disposed"

class CommEquity(BaseModel):
    """
    Was an official committee appointed prior to confirmation to represent the common stock?
    """
    val: CommEquity_type
    confidence: confidence_type


questions['CommEquity'] = {
        'description':"""
Was an official committee appointed prior to confirmation
to represent the common stock? “Yes,” “no,” “denied,” or “motion
withdrawn.” “Denied” means that the court entered an order denying the
request for a committee. “Motion withdrawn” means that all persons
requesting the committee withdrew their requests. In some older cases, if
the disclosure statement indicates that no equity committee had been
appointed we assumed that none was appointed prior to confirmation. If the
case was dismissed before the order for relief, enter “no order for relief.”
Other options are “Chapter 7 at filing” and “case not disposed.” 
""",
'output_class': CommEquity
}

#CommEquityAtty
class CommEquityAtty(BaseModel):
    """
    Name of the law firm 
    “none” if there is no evidence of an attorney hired
    """
    val: str
    confidence: confidence_type


questions['CommEquityAtty'] = {
        'description':"""
CommEquityAttyCol, resolved to a single “lead” and
employing the most recent name for a firm that has changed its name. A
firm is lead if it is described as Acounsel” or Aattorney” while the
competing firm is described as “co-counsel.” When there is doubt about
which firm is lead, we examine the available fee information to determine
which firm was dominant early in the case. Ultimately, we make a
judgment, using hindsight, to determine which firm was probably lead at the
time the representations began. Enter none” if there is no evidence of an
attorney hired to represent the committee” 
""",
'output_class': CommEquityAtty
}

#DateFiled
class DateFiled(BaseModel):
    """
    The month, day, and year the bankruptcy case was filed
    in the form of month/day/year
    """
    val: str
    confidence: confidence_type


questions['DateFiled'] = {
        'description':"""
The month, day, and year the bankruptcy case was filed. If the
consolidated case involved more than one filing, the date of the first filing.
Prior to Pacer, we may have collected DateFiled from BANKRUPTCY
YEARBOOK, BDS, 10-Ks, Moody's, reported opinions, searches of
newspapers. 
""",
'output_class': DateFiled
}

#DipAtty
class DipAtty(BaseModel):
    """
    The name identifies the lead counsel who represented the DIP in filing of the bankruptcy case.
    """
    val: str
    confidence: confidence_type


questions['DipAtty'] = {
        'description':"""
Debtor-in-possession (DIP) attorney resolved. This name
identifies the lead counsel who represented the DIP in filing of the
bankruptcy case. “Lead” means that this firm was not merely conflicts,
special, foreign, or local counsel. The “Res” suffix indicates that the field has
been compiled from several other fields. We collected the full names of the
law firms from different sources in other fields and then compiled this field
by using the best information available. We treat the Board of Directors
resolution at filing as determinative of lead status. But if that document
identified two firms as co-counsel without identifying one as lead counsel,
we resolved the issue from other sources. We resolved based on our
determination of which of the two firms was dominant in the case. We
considered a firm identified as "Delaware co-counsel" to be local counsel.
Firms that have changed their names over time are identified by their most
recent names. We simplified firm names by shortening them to no more
than two words and removing punctuation. Data are drawn from the
1980-86 LoPucki-Whitford study, 1997 LoPucki Survey, dockets, disclosure
statements and applications to employ. We used other sources when
director resolutions and applications to employ were not available. The
other sources included news stories. 
""",
'output_class': DipAtty
}

#Disposition
class Disposition_type(str, enum.Enum):
    """Disposition Values for Disposition"""
    chap7 = "Chapter 7 at filing."
    confirmed = "confirmed"
    converted = "converted"
    dismissed = "dismissed"
    pending = "pending"
    no_data = "no data"

class Disposition(BaseModel):
    """
    This field indicates the disposition of the bankruptcy cases.
    """
    val: Disposition_type
    confidence: confidence_type


questions['Disposition'] = {
        'description':"""
This field indicates the disposition of the bankruptcy cases.
Chapter 7 cases are “Chapter 7 at filing.” The primary dispositions of
Chapter 11 cases are “confirmed,” “dismissed,” or “converted.” Cases not
yet disposed of by one of those methods are “pending.” “no data” indicates
that the case is no longer pending, but we do not know the disposition. If
plans are confirmed for some, but not all, debtors, we record data for the
largest or most important debtors. If the plan is contingent on the entry of
two confirmation orders (one by the bankruptcy court, one by the district
court), the plan is confirmed only upon entry of the second.
""",
'output_class': Disposition
}

#DistFiled
class DistFiled(BaseModel):
    """
    The two letter abbreviation for the state in which the bankruptcy
    case was filed and, if the state is divided into districts, a space followed by
    the two letter abbreviation for the district. For example, “NY SD.”
    """
    val: str
    confidence: confidence_type


questions['DistFiled'] = {
        'description':"""
The two letter abbreviation for the state in which the bankruptcy
case was filed and, if the state is divided into districts, a space followed by
the two letter abbreviation for the district. For example, “NY SD.”
""",
'output_class': DistFiled
}

#DistribEquity
class DistribEquity(BaseModel):
    """
    Dollar value, NOT in millions, as of the effective date of the plan, of the distributions to equity holders.
    """
    val: float
    confidence: confidence_type


questions['DistribEquity'] = {
        'description':"""
Dollar value, NOT in millions, as of the effective date of the
plan, of the distributions to equity holders. Equity holders include the
holders of common and preferred stock. They do not include the holders of
intercompany stock. If the estimated distribution includes warrants or
options to buy stock in the emerging company and the disclosure statement
provides no value for them, we count them as having no value. If the
estimated distribution is stated as a range, use the midpoint of the range. We
report an amount for distributions to equity only if the disclosure statement
reports amounts for all substantial equity classes. 
""",
'output_class': DistribEquity
}

#DistribUnsec
class DistribUnsec(BaseModel):
    """
    Dollar value, in millions, as of the effective date of the plan,
    of the distribution to all classes of unsecured claims combined, as indicated
    in the disclosure statement and compiled on the Distribution Spreadsheet.
    """
    val: float
    confidence: confidence_type


questions['DistribUnsec'] = {
        'description':"""
Dollar value, in millions, as of the effective date of the plan,
of the distribution to all classes of unsecured claims combined, as indicated
in the disclosure statement and compiled on the Distribution Spreadsheet.
Unsecured claims are defined in the protocol for ClaimsUnsec. If the
estimated distribution includes warrants or options to buy stock in the
emerging company and the disclosure statement provides no dollar value for
them, count them as having no value. If the estimated distribution is stated
as a range, use the midpoint of the range. If the estimated distribution is
stated as “less than” a stated amount, use the stated amount. If the estimated
distribution is a choice between a larger value and a smaller value, use the
larger value. If the estimated distribution is the choice between a cash
payment and payment in another medium, use the cash payment. We ignore
the proceeds of a litigation trust if the disclosure statement says it may be
zero and no other value is available. We report an amount for unsecured
claims only if the disclosure statement provides the amount of the
distribution for all substantial unsecured classes. 
""",
'output_class': DistribUnsec
}

#DistribUnsec
class Examiner_type(str, enum.Enum):
    """Possible Values for Examiner"""
    Yes = "Yes"
    No = "No"

class Examiner(BaseModel):
    """
    Enter “yes” if an examiner who was not a fee examiner was
    appointed under 11 USC §1104, “no” if one was not.
    """
    val: Examiner_type
    confidence: confidence_type


questions['Examiner'] = {
        'description':"""
Enter “yes” if an examiner who was not a fee examiner was
appointed under 11 USC §1104, “no” if one was not.. Fee examiners are
included in FeeReviewer, below. This field was seeded with data from
Jonathan Lipson, 2010.  
""",
'output_class': Examiner
}

#JudgeDisposition
class JudgeDisposition(BaseModel):
    """
    The full name of the bankruptcy judge who entered the 
    order disposing of the Chapter 11 case. 
    """
    val: str
    confidence: confidence_type


questions['JudgeDisposition'] = {
        'description':"""
The full name of the bankruptcy judge who entered the 
order disposing of the Chapter 11 case. That order will be an order
confirming a plan, dismissing the case, or converting the case to Chapter 7.
If a bankruptcy judge and a district judge entered parallel confirmation
orders, list only the bankruptcy judge. For example, in Owens Corning, a
bankruptcy judge and a district judge presided together over the
confirmation hearing and each signed a confirmation order. If a judge
signed orders both before and after disposition, we could not obtain a copy
of the disposition order, and we could not otherwise discover who signed
the disposition order, we assumed that the judge who signed the earlier and
later orders signed the disposition order. For Chapter 7 at filing cases,
indicate “Chapter 7 at filing.” For cases with “no data” on disposition but
which have been disposed of, JudgeDisposition is based on the best
available information. For pending cases, this field is blank.
""",
'output_class': JudgeDisposition
}

#JudgeFiling
class JudgeFiling(BaseModel):
    """
    The full name of the judge to whom the case was initially assigned.
    """
    val: str
    confidence: confidence_type


questions['JudgeFiling'] = {
        'description':"""
The full name of the judge to whom the case was initially
assigned. (This may not be the first judge who enters an order in the case,
the judge whose name is listed on the case summary, or the judge whose
initials later appear in the case number.) We ordinarily determine the judge
at filing solely from the docket and filed documents at the beginning of the
case. The first of the following is generally sufficient to determine the judge
at filing: (1) the docket recites that the case was assigned to the judge, (2)
the judge’s initials are part of the case number on a filed document, (3) the
judge is listed on the Case Summary on PACER. Merely holding a hearing
or signing an order is not itself sufficient but holding consecutive hearings
and signing consecutive orders on two separate occasions is presumptive
evidence of the judge at filing. If documents show the case was reassigned
from one judge to another, the judge from whom the case was reassigned is
the judge at filing even if that judge did not do anything in the case. In the
absence of information from any other source after thorough research and
any suggestion to the contrary, we have assumed that in cases prior to
PACER that a judge hearing the case as long as three months after filing
was the judge to whom the case was initially assigned. We have
discontinued making such assumptions for cases filed after November 30,
2003.
""",
'output_class': JudgeFiling
}

#LiabPetition
class LiabPetition(BaseModel):
    """
    Total liabilities of the debtors, as indicated in the source of our data for AssetsPetition.
    """
    val: float
    confidence: confidence_type


questions['LiabPetition'] = {
        'description':"""
Total liabilities of the debtors, as indicated in the source of
our data for AssetsPetition. In the event no amount is available from that
source, we will make a decision as to whether the next best source is
adequate and amend this protocol accordingly. 
""",
'output_class': LiabPetition
}

#Prepackaged
class Prepackaged_type(str, enum.Enum):
    """Possible Values for Prepackaged"""
    prenegotiated = "prenegotiated"
    agreement_in_principle = "agreement in principle"
    not_applicable= "not applicable"

class Prepackaged(BaseModel):
    """
    A case is prepackaged if the debtor drafted the plan,
submitted it to a vote of the impaired classes, and claimed to have obtained
the acceptances necessary for consensual confirmation before filing the
case.
    """
    val: Prepackaged_type
    confidence: confidence_type


questions['Prepackaged'] = {
        'description':"""
A case is prepackaged if the debtor drafted the plan,
submitted it to a vote of the impaired classes, and claimed to have obtained
the acceptances necessary for consensual confirmation before filing the
case. The claim must include that no class rejects the plan or the class that
rejects is minimal in dollar amount. (Cityscape did not qualify because the
preferred B shares rejected the plan – even though the debtor may have
claimed those shares were under water – because the class was not
minimal.) Prepackaged cases nearly always are filed solely to modify the
company's liability on an issue of junk bonds. If the debtor negotiates the
plan with at least one major creditor constituency or obtains the acceptance
of at least one, enter “prenegotiated” for this field — even if no vote was
taken on the plan. An example would be a plan to sell the debtor’s business,
which has been drafted and negotiated with a large secured creditor before
filing, but not with trade creditors. We accepted an “agreement in principle”
with 40% of the bondholders to a term sheet. We do not consider having a
contract to sell the business to be a prenegotiation unless the creditors have
agreed to the sale. As a result, 363 sales are rarely prenegotiated. The best
source for this field is the 8-K announcing the bankruptcy. That is ordinarily
the only source we check. If the debtor has an agreement, the debtor will
usually mention it in the 8-K. If the case was dismissed before the order for
relief or was Chapter 7 at filing, enter “not applicable”
""",
'output_class': Prepackaged
}

#Sale
class Sale_type(str, enum.Enum):
    """Possible Values for Sale"""
    Yes = "yes"
    No = "no"
    no_confirmation = "no confirmation"
    chapter7 = "Chapter 7 at filing"

class Sale(BaseModel):
    """
    “yes” if Sale363 is yes or SaleConf is yes. “no” if Sale363 is no and
    SaleConf is no. If no order for relief was filed, enter “no confirmation.”
    Chapter 7 cases are “Chapter 7 at filing.”
    """
    val: Sale_type
    confidence: confidence_type


questions['Sale'] = {
        'description':"""
“yes” if Sale363 is yes or SaleConf is yes. “no” if Sale363 is no and
SaleConf is no. If no order for relief was filed, enter “no confirmation.”
Chapter 7 cases are “Chapter 7 at filing.”
""",
'output_class': Sale
}

#Sale363
class Sale363_type(str, enum.Enum):
    """Possible Values for Sale363"""
    Yes = "yes"
    No = "no"
    not_classified = "not classified"
    chapter7 = "Chapter 7 at filing"
    pending = "pending"

class Sale363(BaseModel):
    """
    Was there a single or multiple 363 sale of all or substantially all of
the debtor’s assets? 
    """
    val: Sale363_type
    confidence: confidence_type


questions['Sale363'] = {
        'description':"""
Was there a single or multiple 363 sale of all or substantially all of
the debtor’s assets? Yes/No. To determine whether a sale was “all or
substantially all” of the company’s assets, we follow the characterization in
court documents; if they say it is “all or substantially all,” it is. If they do
not characterize the sale, we characterize it. Days Inn sold its franchise hotel
business for $250 million, keeping one or more hotels on its balance sheet at
$1.2 million. We characterized the $250 million sale as “all or substantially
all.” ICH sold assets of $310 million and retained assets of $10.5 million.
We characterized the sale as “all or substantially all.” A court order
authorizing an agent to sell all or substantially all of the assets is treated as a
363 sale. Example: Circuit City. If the case was dismissed before the order
for relief, enter “not classified.” Chapter 7 cases are “Chapter 7 at filing.”
Cases in which there has not yet been a 363 sale or a disposition are
“pending.” Enter “not classified” if the Emerge field is “not classified.”
""",
'output_class': Sale363
}

#SaleConf
class SaleConf_type(str, enum.Enum):
    """Possible Values for Sale363"""
    Yes = "yes"
    No = "no"
    no_confirmation = "no confirmation"
    no_data = "no data"

class SaleConf(BaseModel):
    """
    Did one or more entities buy the debtor’s assets or an interest in
the debtor’s business from the estate or emerging entity pursuant to the
confirmed plan?
    """
    val: SaleConf_type
    confidence: confidence_type


questions['SaleConf'] = {
        'description':"""
Did one or more entities buy the debtor’s assets or an interest in
the debtor’s business from the estate or emerging entity pursuant to the
confirmed plan? Yes, no, pending, no confirmation, or no data? A sale is
“pursuant” to the plan if the plan contemplates that it will take place. It counts
as a sale whether or not it ultimately occurs. A plan can be both a sale and a
reorganization. An all-stock merger is not a sale. No minimum purchase is
required to classify the case as a Sale. But the plan must specifically
contemplate the sale. Lenders who receive the company in satisfaction of
their debts are not buyers. Except as stated below, buying must be for value
not already invested. A creditor or equity holder that receives a distribution
on account of its claim or interest is not a buyer. But such a creditor or equity
holder that invests new cash, stock, or other value is a buyer to the extent of 
the new investment. A “rights offering” of stock in the emerging company is
ordinarily the sale of an interest; a rights offering of bonds is not. If the plan
authorizes sale to the highest bidder and the secured creditor is the highest
bidder, categorize the case as a sale. But if the plan surrenders the collateral
and the “buyer” doesn’t pay any money to the estate, categorize the case as
not a sale. Do not collect this variable for 363 sale cases. Plan modifications
that occur prior to plan consummation should be taken in to account. Plan
modifications that occur after plan consummation should not. 
""",
'output_class': SaleConf
}

#TortCause
class TortCause_type(str, enum.Enum):
    """Categories for this field are: products: bankruptcies caused
principally by product liability claims against the debtor or product recalls
by the debtor; fraud: bankruptcies caused principally by fraud claims
(include securities fraud claims) against the company. These cases often
began with financial difficulties from other causes, which were concealed
from the investors until they were severe enough to cause the bankruptcy;
pension: bankruptcies caused principally by pension claims against the
debtor, including underfunding claims by the Pension Benefit Guaranty
Corporation; environmental: bankruptcies caused principally by
environmental claims (other than products liability claims) against the
debtor patent: bankruptcies caused principally by patent infringement
claims against the debtor; other tort: bankruptcies caused principally by tort
claims against the debtor that do not fall into any of the categories above;
not tort: bankruptcies not caused principally by claims in any of the
categories above."""
    products = "products"
    fraud = "fraud"
    pension = "pension"
    environmental = "environmental"
    debtor_patent = "debtor patent"
    other_tort = "other tort"
    not_tort = "not tort"

class TortCause(BaseModel):
    """
    If tort debt caused the bankruptcy filing (in the sense that, had
the tort debt not existed, the case would not have been filed) list the type of
tort debt.
    """
    val: TortCause_type
    confidence: confidence_type


questions['TortCause'] = {
        'description':"""
If tort debt caused the bankruptcy filing (in the sense that, had
the tort debt not existed, the case would not have been filed) list the type of
tort debt. Categories for this field are: products: bankruptcies caused
principally by product liability claims against the debtor or product recalls
by the debtor; fraud: bankruptcies caused principally by fraud claims
(include securities fraud claims) against the company. These cases often
began with financial difficulties from other causes, which were concealed
from the investors until they were severe enough to cause the bankruptcy;
pension: bankruptcies caused principally by pension claims against the
debtor, including underfunding claims by the Pension Benefit Guaranty
Corporation; environmental: bankruptcies caused principally by
environmental claims (other than products liability claims) against the
debtor patent: bankruptcies caused principally by patent infringement
claims against the debtor; other tort: bankruptcies caused principally by tort
claims against the debtor that do not fall into any of the categories above;
not tort: bankruptcies not caused principally by claims in any of the
categories above.
""",
'output_class': TortCause
}

#Trustee
class Trustee_type(str, enum.Enum):
    """
    Possible Values for Trustee
    """
    Yes = "yes"
    No = "no"
    partial = "partial"
    no_hits = "No hits"
    denied = "Denied"

class Trustee(BaseModel):
    """
    Enter “yes” if an 11 USC §1104 trustee was appointed before
disposition, “no” if not, and “partial” if one was appointed for only some
debtor entities. Indenture trustees, liquidating trustees, and Chapter 7
trustees, are not 1104 trustees. “No hits” in this field means that we
searched a partial docket for the strings “Chapter 11 trustee” or “1104" and
“trustee” and the hits, if any, contain no suggestion that a chapter 11 trustee
was appointed. “Denied” means that the court entered an order denying the
request for a trustee.
    """
    val: Trustee_type
    confidence: confidence_type


questions['Trustee'] = {
        'description':"""
Enter “yes” if an 11 USC §1104 trustee was appointed before
disposition, “no” if not, and “partial” if one was appointed for only some
debtor entities. Indenture trustees, liquidating trustees, and Chapter 7
trustees, are not 1104 trustees. “No hits” in this field means that we
searched a partial docket for the strings “Chapter 11 trustee” or “1104" and
“trustee” and the hits, if any, contain no suggestion that a chapter 11 trustee
was appointed. “Denied” means that the court entered an order denying the
request for a trustee.
""",
'output_class': Trustee
}

#TurnFirm

class TurnFirm(BaseModel):
    """
The firm, if any, that provides the turnaround services. If the
turnaround manager’s services were not provided by a firm, indicate
“none”.
    """
    val: str
    confidence: confidence_type


questions['TurnFirm'] = {
        'description':"""
The firm, if any, that provides the turnaround services. If the
turnaround manager’s services were not provided by a firm, indicate
“none”. Use the name by which the firm is currently generally known,
whether or not it is the name used in the court file. If more than one firm
provided turnaround services, prefer firms that held one of the offices listed
in TurnOffice over firms that did not and between firms tied on the prior
criteria, prefer the first firm employed. The board resolution attached to the
petition is the determinative document.
""",
'output_class': TurnFirm
}

#Voluntary

class Voluntary_type(str, enum.Enum):
    """
    Possible Values for Voluntary
    """
    voluntary = "voluntary"
    involuntary = "involuntary"
    both = "both"

class Voluntary(BaseModel):
    """
A case is "voluntary" if it was filed by the debtor, "involuntary"
if it was filed by creditors. If some entities file voluntarily and others are
later brought in involuntarily, indicate “both.” 
    """
    val: Voluntary_type
    confidence: confidence_type


questions['Voluntary'] = {
        'description':"""
A case is "voluntary" if it was filed by the debtor, "involuntary"
if it was filed by creditors. If some entities file voluntarily and others are
later brought in involuntarily, indicate “both.” If the debtor and creditors
file roughly simultaneously, characterize the case by the first to file, even if
that case is dismissed in favor of the other. If the involuntary case is
transferred, so indicate in the Transferred field. If the voluntary and
involuntary cases are before the same judge and the times they are pending
overlap, characterize the case by the first to file, even if that case is
dismissed in favor of the other.
""",
'output_class': Voluntary
}
