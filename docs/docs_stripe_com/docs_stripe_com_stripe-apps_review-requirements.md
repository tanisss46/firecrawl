# Stripe App Marketplace review requirements

## Understand the process and requirements to get your app approved for listing in the Stripe App Marketplace.

Stripe reviews all apps and app updates submitted to the Stripe App Marketplace
to make sure they provide the best user experience in areas such as design,
reliability, security, and trust. Make sure your app fulfills these requirements
before submitting it for app review.

## App review principles

Three main principles guide the app review process:

- **Quality**: Users require high-quality and useful apps. This encompasses
elements of design, UX, performance, reliability, and so on.
- **Security**: All apps must meet Stripe’s standards for the security and
privacy of user data and comply with all applicable laws.
- **Trust**: App developers must adhere to a standard of trust that maintains
the integrity of our ecosystem. This extends to all communication, support, and
community behavior.

## The app review process

Here’s what you can expect when submitting your app for review:

- From the Stripe Dashboard, create or update your app listing. Then submit your
app and app listing for review. If your app requires an account or additional
data to function, you must submit a test plan and credentials that detail how to
test your app as part of the review process. For more information, see [example
test
credentials](https://docs.stripe.com/stripe-apps/review-requirements#test-plan-and-credentials)
or see [Submit app for
review](https://docs.stripe.com/stripe-apps/publish-app#submit-app-for-review)
for instructions on this step.
- A Stripe reviewer evaluates the app and listing against all relevant criteria.
This process might involve automated scans, live testing of the app, and human
review of all the information you provide.
- If the app and listing meet all app review requirements, we approve this
version of your app and listing, and you can make the app visible on the
marketplace at your convenience. You must explicitly publish your approved app
for it to be available on the marketplace. See [Publish your
app](https://docs.stripe.com/stripe-apps/publish-app#publish-app) for
instructions. However, if the app doesn’t meet all app review criteria, Stripe
will send you specific feedback on which criteria the app didn’t meet, and
provide you with guidance on ways to meet them.

Updates to apps and app listings go through the same process.

## App review requirements

To pass review, your app must pass the requirements in this section. Test it
end-to-end for bugs and edge cases before submitting it for review.

### Transparent and consistent pricing

You must clearly state your app pricing up front, without hidden costs or fees.
App pricing must also be consistent with off-marketplace prices.

Do Don’t- Price your service transparently and consistently with off-marketplace
prices.
- Offer useful free functionality for your users, if you so choose.
- Have pricing that is different from outside the Stripe App Marketplace.
- Advertise your service as free and then require users to pay for functionality
after they’ve installed the app.

### App developer standards

As an app developer, you must clearly represent yourself and your business
purpose. You can’t engage in any illegal or harmful activities online or
offline.

Do Don’t- Make sure you have a website that provides accurate information about
you, including contact information.
- Check if your business purpose is listed in Stripe’s [Prohibited and
Restricted Businesses](https://stripe.com/legal/restricted-businesses).
- Expect additional review if your business falls under the restricted business
category.
- Engage in any illegal or harmful behaviors.
- Misrepresent yourself or your purpose.

### App listing page

Your app listing helps businesses find your app and understand how it can help
them run their business. Make sure the content you add clearly describes your
app features and addresses potential questions, allowing businesses to quickly
evaluate if your app is right for them. See the [app listing
guidelines](https://docs.stripe.com/stripe-apps/listing-guidelines) for more
details.

**Spelling and grammar**

Your listing must use proper spelling and grammar. This includes being easy to
read and understand for your target audience.

Do Don’t- Proof for proper spelling and grammar.
- Proof that links point to appropriate URLs.
- Don’t submit with typos or grammatical errors.
- Don’t include links to expired or unrelated content.

**App name**

Do Don’t- Provide the name only. For example: HelpTable
- Use the same name in the app listing and in the app manifest.
- Don’t use “Stripe”, “app”, “RAK”, “Generator”, “API Key”, “Authenticator”,
“free” or “paid” in the app name. *For example: HelpTable app*
- Don’t submit a listing with a different name from the app manifest.

**Logo**

Do Don’t- Upload your own distinct logo. Make sure it’s high quality and square.
- Don’t use Stripe’s logo or name.
- Don’t use the logo or name of any other company without explicit permission or
in any way that would imply their endorsement of your app without their consent.
- Don’t provide images that are degraded in quality, stretched, or cropped in a
way that cuts off elements.

**Subtitle**

Do Don’t- Concisely summarize how your app works with Stripe. For example: View
and edit customer support history from your Stripe Dashboard
- Don’t use hyperbole, marketing jargon, keyword stuffing, or unprovable claims.
*For example: The world’s best support product.*

**Category**

Do Don’t- Select the category that applies to the primary functionality of your
app.
- Don’t select categories that don’t apply to your app, or only apply
tangentially.

**Description**

Do Don’t- Briefly describe what your company does, who your app is for, and the
value it delivers. An ideal description includes a quick intro to your service,
followed by a brief description of your Stripe app specifically. For example:
"HelpTable is a simple support management system designed for fast-moving
startups. After installing the HelpTable app, you’ll get easy access to any
customer’s support history within Stripe. This allows your agents to get a full
picture of customer’s experience with your products and services. Agents can
also view and manage support tickets, right within the Stripe Dashboard’
- Describe any limitations that your app might have.
- Don’t only talk about your company and omit app related functionality.

**Feature highlights**

Do Don’t- Spotlight 1-3 key features to help users quickly understand what your
app does.
- State the feature’s value using simple language in the feature title. For
example: Resolve tickets from Stripe
- Describe how the feature works and benefits the user in the feature
description.
- Make sure your feature images are high quality.
- Don’t highlight key features that aren’t available in your app.
- Don’t use real customer data in screenshots and images.
- Don’t provide images that are degraded in quality, stretched, skewed, or
cropped in a way that cuts off elements.

**Non-duplicate**

Each app can only appear in the Marketplace once (no duplicates, even under a
different name). Submit new versions of an app from the same account as the
previous version. Contact [Stripe
Support](https://support.stripe.com/contact/login) if this isn’t possible and
you need assistance.

Do Don’t- Check to be sure that neither you nor someone else have already
uploaded this application.
- Don’t submit the same app multiple times. This includes uploading the same
application under different names, in different categories, from different
accounts, and so on.

### UI extension for apps

If your app includes a UI extension, the app drawer is the main place where your
users see details about your app and take actions. Stripe users expect
consistency across their Stripe Dashboard, which includes engaging with your
app. Make sure that completing workflows through your app feels intuitive and
natural. See the app design guidelines for examples of apps we think work well
in the Stripe Dashboard.

**App installation**

If your app requires authentication, clearly direct the appropriate users to
authenticate after installation. Your app must also provide a clear way to
unauthenticate from within the Stripe Dashboard UI.

Do Don’t- Provide clear directions for user authentication. When a user installs
the app, provide a clear prompt or trigger to complete authentication in the app
drawer.
- Provide a clear path to unlink the Stripe account from the app platform from
either the settings page or the app drawer.
- Don’t guide admins to configure account-wide authentication in your app’s
settings.
- Don’t provide a prompt for per-user authentication from the app drawer if your
app authenticates users individually rather than account-wide.

**Information and actions**

Your app provides contextual information and actions, adding value to the user’s
workflow in Stripe.

Do Don’t- Provide relevant information and actions pertaining to the user’s
workflow within Stripe.
- Only provide deep links out to third-party services when it’s helpful to
reference a deeper workflow.
- Don’t use your App as a jumping off point to a third-party website, without
providing any tangible value to users within Stripe.

****

At any point in the app drawer, the user needs to know where they are, where
they can go, and how to go back or exit.

Do Don’t- Provide clear navigation components so the user can easily move
through your app.
- Make sure you don’t have dead-ends or looping. For example: don’t leave a user
in the middle of a workflow without a Cancel or Go back button if they need to
exit.
- Don’t exclude navigation, trap your user, or overload your navigation. *For
example: If a user is in the middle of a workflow and needs to exit, but you
don’t provide a Cancel or Go back button.*

**Buttons and links**

Make sure the user can immediately understand what each button or link does
without prior knowledge.

Do Don’t- Provide clear labels for buttons and links.
- Use the [external
icon](https://docs.stripe.com/stripe-apps/components/icon#icon-reference) to
indicate external links.
- Don’t link the word “here”—make sure to disclose the location.

**Notices and dialogs**

Only use notices and dialogs for critical or contextual information in your app.

Do Don’t- Provide notices when critical information requires a user’s attention.
- Provide confirmation dialogs for any costly or destructive actions that aren’t
easily reversible.
- Don’t show notices that are irrelevant or aim to upsell. These types of
messages might feel like spam and degrade the user’s preception of your app and
Stripe.
- Don’t allow the user to take any costly actions without clear confirmation.

**States**

The app needs to account for error states, loading states, and thoughtful
solutions for edge cases.

Do Don’t- Provide error states, loading states, and thoughtful solutions for
edge cases. For example: if a user is filling out a form in the app drawer,
notify them of any errors when they select Submit.
- Clearly highlight an error message and directly explain how to fix it, such as
“Select a country.”
- Don’t account for the happy path only.
- Don’t leave the user stranded or present error states that aren’t clear. *For
example: the user selects Next in a workflow, but nothing happens. The user has
hit an error, but it’s not clear how to correct it because there’s no
messaging.*

**UI error handling**

The app needs to gracefully handle errors and communicate clear and actionable
error messages to users. Monitor your app for problems.

Do Don’t- Use the provided components and patterns to display error
notifications to users.
- Make sure error messages clearly explain the issue, and provide the user with
an actionable next step.
- Monitor your app for errors so you know when your users are having problems.
- Display a vague “something went wrong” error message.
- Swallow errors silently with no message to the user.
- Catch an error and log it to the console without any indication to a
non-technical user.

### App settings

Users can navigate to your app settings within the Stripe Dashboard.

**Authentication Settings**

If your app requires authentication to a service other than Stripe, or stores
credentials on behalf of the app user, your app must provide a way to
reauthenticate or log out in your app’s settings.

Do Don’t- If your app requires authentication to your service or a third-party,
make sure you provide a way to both reauthenticate and deauthenticate.
- If your app authenticates with multiple services, make sure that each service
can deauthenticate and reauthenticate individually.
- Provide one clear way for users to save changes.
- Don’t omit the authentication setting if your app requires it.

**Labels and descriptions**

The app settings must include labels and descriptions that make it easier for
users to navigate and understand the app.

Do Don’t- Provide clear labels and descriptions for settings.
- Don’t label settings in a manner that makes it difficult for users to
understand.
- Don’t exclude descriptions for settings.

**Required and optional settings**

The app must clearly indicate which settings are required and which settings are
optional.

Do Don’t- Indicate which setting fields are required.
- Don’t leave required fields unmarked, causing users to not understand why the
app isn’t functioning properly.

**Settings save**

The app settings must provide one clear way to save changes.

Do Don’t- Provide one clear way for users to save changes.
- Don’t omit the a way to save changes.
- Don’t allow for multiple save patterns across the page.

**Change confirmations**

Follow app settings changes with a confirmation message after they’re saved.

Do Don’t- Provide a confirmation when settings changes are saved.
- Don’t omit confirmation messages.
- Don’t allow changes to happen without confirmation messages.

### Components

Use Stripe’s UI components for your app, specifically across the expandable app
drawer and your app settings page. This makes using your app feel like part of
the Stripe Dashboard.

Do Don’t- Build your app using the UI components.
- Use only the provided fonts, icons, form fields, and color schemes to keep
them consistent with the Dashboard.
- Don’t use stylized components from other design systems.
- Don’t customize or brand components.

**Visuals**

Use icons, images and illustrations to make it simpler for users to understand
the flows and features of your app.

Do Don’t- Use visuals (icons and illustrations) to support users in
understanding how to use the app or a specific feature.
- Use high quality visuals.
- Don’t use visuals that are purely decorative.
- Don’t use visuals that are degraded in quality.

**Drawer icon**

If your app has a UI component, it displays in the app drawer in the Stripe
Dashboard after a user installs it. Make sure that the app icon correctly
displays in that drawer by including a high quality app icon in your app
manifest.

Do Don’t- Include a high quality icon in your app manifest.
- Don’t omit the icon from your app manifest.
- Don’t add a low quality icon to your app manifest.

### App content

Provide clear and consistent content throughout the app. Clearly address users
with voice, tone, and grammar that’s consistent with the rest of the dashboard.

**Voice, tone, grammar, and style**

Do Don’t- Write simply. Lean into compact, specific language. For example: “Try
out the feature in your Dashboard.”
- Use active voice. For example, “Order a card reader.”
- Use simple verbs for calls to action (CTAs). For common actions where the
object is clear, you can include only the verb. For example: “Create
subscription”
- Use numerals for efficiency and space. For example: “You have 3 tickets to
review.”
- Don’t use corporate voice and jargon. *For example: “Utilize this programmed
software.”*
- Don’t use passive voice. For example: “Card readers are available to order.”
- Don’t include filler words like pronouns, adjectives, adverbs, or indefinite
articles (like “a,” “an,” or “the”). *For example: don’t write “Create a
subscription” or “Create your subscription” but rather “Create subscription.”*
- Don’t spell out numbers unless required to add emphasis. *For example: “there
are two ways to fix this problem.”*

**Sentence case**

Do Don’t- Use sentence case for all content, including headings and buttons. For
example: “Add bank account”. For example: “Create subscription”
- Use numerals for efficiency and space. For example: “You have 3 tickets to
review.”
- Don’t add capitalized words that aren’t proper nouns, acronyms or the first
word in a sentence. *For example: “Add Bank Account”.*

**Punctuation**

Do Don’t- Use periods in body text. This includes subheadings, descriptions,
legal text, and tooltips. The period goes inside quotation marks, not after
them.
- Use periods for titles or headings, or for clickable elements like menu labels
and buttons. *For example: Add a period after a “Learn more” link.*

**Date format**

Do Don’t- Format dates as follows: When abbreviating months, use the 3-letter
abbreviation and no period. For example, “Jan, Feb, Mar, Apr, May, Jun”. When
writing out the month name, day, and year, use a comma between the day and the
year. For example, “January 3, 2021” or “Jan 3, 2021”. When only writing the
month and year, don’t use a comma. For example, “January 2021” or “Jan 2021”.
- Don’t include periods after abbreviating a month.
- Don’t use ordinals (that is, 1st, 2nd, 3rd) for dates.

**Time format**

Do Don’t- Format time as follows: Use the 12-hour clock. Indicate ante meridian
(AM) and post meridian (PM) with all caps and a space after the last number. Use
two digits for minutes. For example,: “3:25 PM” or “10:00 AM”.
- Don’t use a 24-hour clock.
- Don’t omit AM and PM on a 12-hour clock.

### App functionality

Your app must be clear, useful, and reliable.

**Usefulness**

The Stripe App Marketplace is a business-to-business (B2B) ecosystem. Apps in
the marketplace must provide functionality that clearly enables or enhances a
Stripe user’s business activities.

Do Don’t- Provide an app that empowers users to conduct their business more
efficiently and effectively.
- Provide contextual information and actions. Make sure you’re adding value to
the user’s workflow in Stripe. Only provide deep links out to your service when
it might be helpful to reference a deeper workflow.
- Provide complementary, non-duplicative functionality. Your app should add new
and unique capabilities that are useful to users and augment their workflows on
Stripe.
- Don’t build consumer or social apps such as games, quizzes, and click bait.
- Don’t merely use your app as a jumping off point to your own service, without
providing any tangible value to your users within Stripe. Deep links should be
secondary to contextual information or actions.

**Accuracy of calculations and data visualization**

All calculations performed by your application must be accurate and trustworthy.
Any data or visualizations presented by your app should be accurate and
complete.

Do Don’t- Present users with valuable calculated data only where you have all
relevant information and data necessary to give a financially accurate result.
For example: Accurate balance totals with all relevant information and data.
- Don’t present users with unreliable information where you don’t have enough
information to correctly compute the result. *For example: Computing tax amounts
without proper tax classifications.*
- Don’t present users with inaccurate information because you don’t have all of
the data you need for an accurate calculation.

**Payment processing**

Unless approved by Stripe in writing, you must process payments triggered by
core functionalities of your app on Stripe.

Do Don’t- Use Stripe for any necessary payment processing in your app.
- Don’t use external payment processors in your app to bypass Stripe

#### Testing guidance and credentials

During app review, Stripe uses your test guidance and credentials to review your
app’s stability, component usage, and user experience. You must provide the
following:

- **Testing guidance**: Include several user scenarios or use cases that cover
all the key features of your app, including the onboarding process.
- **Testing credentials of test accounts**: Include one or more sets of testing
credentials that Stripe can use to install and use your app. If your test
accounts require specific data to use your app (such as a CSV file), you must
include it with the account. Make sure that the test links you provide for app
review connect to Stripe through the app installation, not through Connect
onboarding.

#### Caution

Stripe **does not** permit you to use real (non-test) accounts for the app
review process. If you need other ways to provide us access to a specific
account for testing purposes, contact [Stripe
Support](https://support.stripe.com/contact/login) for assistance.
Do Don’t- Provide the detailed steps required to test your app.
- Provide details about the expected behavior Stripe will see.
- Provide sample data as needed per test account.
- Provide test credentials of accounts that accurately represent your business.
- Provide test credentials for a paid account if any portion of your app
requires a paid account to test.
- Provide test credentials for the highest role-based access within your app.
For example: “admin”.
- Provide details about how different user roles in your system affect how
different elements render within the Stripe Dashboard UI. For example: “admin”
or “view only”.
- Provide detailed steps about how to connect your app with Stripe.
- For apps that require data sync, provide detailed steps for how to both sync
the necessary data and to confirm that the data is accurate.
- For apps that require live data (for example, transactions), provide detailed
steps for how to view this data.
- For apps that are region specific or have geographical restrictions, provide
details about which regions are supported, and test credentials for a Stripe
account with the latest version of your app installed.
- Disable multi-factor authentication or provide instructions for reviewers to
pass it.
- Don’t expect app reviewers to “figure it out.”

Example test credentials for an example app like Stripe with Google Sheets:

Test account nameUsernamePasswordGoogle
Sheets`teststripeapps@stripe.com``teststripeapps`Stripe`teststripeapps@stripe.com``teststripeapps`
Example user scenario for an example app like Stripe with Google Sheets:

User scenario Step by step instructionsSign in as a user- Install the app from
the Stripe App Marketplace.
- Open the app.
- Click the **Sign in** button.
- Enter the Google test credentials (provided for you below).
- Give the app access to your Google account.
- Return to the Stripe dashboard signed in to the app. You should be able to use
a service of Google Sheets in your app in the Dashboard.
Export data from Stripe to Google Sheets- Navigate to either the Payments or
Customers Dashboard page.
- Open the app in the Dashboard.
- Click the button in the app drawer to export data.
- Select a folder (optional).
- Save the data. The data should be available as a CSV in your Google Drive
account.

**No advertising**

Your app may not contain display or banner advertisements.

Do Don’t- Keep your app focused on the key value you’re providing to merchants.
- Include ads of any sort (your own or from a display advertising service).
- Include promises of future releases.

**Fully-functional and bug-free**

Your app must be complete, polished, and free from obvious bugs. This includes
broken links.

Do Don’t- Publish your app when it’s functionally complete.
- Perform end-to-end testing on your app under multiple scenarios.
- Fix any bugs you find before submitting your app for review.
- Make sure any links in your app point to valid URLs.
- Don’t leave in buttons that do nothing, half-finished views, and so on.
- Don’t attempt to publish the app with known bugs, crashes, and so on.
- Don’t include links to non-existent pages (404) or pages that produce error
messages.

**Permissions**

Your app manifest must include the minimum necessary set of permissions required
for your app to operate. Your app won’t be permitted to attempt any API call
that it hasn’t requested permissions for.

Do Don’t- Declare all necessary permissions for your app in your app’s manifest
file.
- Don’t request permissions that your app doesn’t actively use.
- Don’t attempt to make API calls that you haven’t requested permissions for.
(Not only will the calls fail, it provides a bad user experience.)

**Sandbox support**

Your app manifest must declare if your app supports being installed in a
sandbox. If you set this to false, your app won’t be installable in sandboxes.

Do Don’t- Declare if your app has sandbox support in your app’s manifest file.
- Don’t enable sandbox support unless you have validated it works as expected.

**Breaking changes**

Make sure that apps function seamlessly for users from version to version. Make
sure your app doesn’t cause breaking changes that require user intervention when
upgrading, because it can cause business disruptions. If any breaking changes
occur, you must clearly message them to users through app release notes and
other applicable channels.

Do Don’t- Evolve your app in a way that version upgrades can be automatic, with
no user intervention.
- Make sure new functionality degrades gracefully if not configured.
- Test your upgrade path from version-to-version so that you accurately reflect
the upgrade process for your users.
- Don’t add mandatory new settings that break your app until they’re configured.

### Privacy and security

**Data usage**

Your app may only leverage user data and APIs that are required for existing app
functionality that you clearly communicate to users. You may not resell or
publish any data obtained from Stripe users through your app.

Do Don’t- Request well-scoped permissions for the data your app needs to
function.
- Inform users about how you will use their data.
- Make sure that you use data consistently with your privacy policy.
- Don’t request permissions for data that you plan to use in the future.
- Don’t have “hidden” features or request permission for data that powers a
“hidden” feature in your app.
- Don’t collect data from users for a specific app feature and then use that
data for other purposes without disclosing that usage.
- Don’t compile and sell data sets containing data obtained through your app.

**Code readability**

Don’t submit UI extensions with obfuscated source code—this is a common way to
attempt to disguise malicious code. Minification is acceptable and recommended.

Do Don’t- Write your code in a straightforward manner.
- Minify your code during the build process.
- Don’t run your code through obfuscation tools during the build process.

**External endpoints**

If your app has a UI Extension, you must declare all external endpoints that the
UI Extension communicates with in your app manifest. Don’t allow your app to
communicate with any external endpoints not declared in the manifest.

Do Don’t- Declare all your external endpoints in the manifest file.
- Don’t attempt to make API calls or load resources from endpoints you haven’t
declared in the manifest file. (The request fails and we monitor apps for
similar activity.)

**Secrets**

You must properly store secret materials required by UI extensions using the
[Secret Store API](https://docs.stripe.com/api/secret_management). This includes
OAuth tokens, other credentials, and any app secrets required for operation of
your app’s UI Extension. Don’t use the Secret Store API for general data
storage.

Do Don’t- Store your users’ OAuth tokens in the Secret Store for secure
cross-browser persistent authentication with your service.
- Don’t use cookies, local storage, or Stripe metadata for storing sensitive
data.
- Don’t store non-secret data like user preferences using the Secret Store API.

### Performance and reliability

**API call success rates**

Your app must make consistently reliable and successful API calls. Stripe
monitors the API success rates for all installed apps.

**API call latency**

API calls made by your app need to have consistently low latency. Stripe
monitors the API call latency for all installed apps.

### Help and support

**Documentation**

You must provide reasonably complete documentation for your app, accessible from
the public internet.

Do Don’t- Write thorough documentation that helps users understand and be
successful with your app.
- Host your documentation on your website.
- Direct users to your documentation for help and support.
- Don’t link to a documentation page that says “coming soon.”
- Don’t link to a documentation page that fails to describe major portions of
the app’s functionality.

**Support**

You must provide clear and easily accessible support channels for users. At a
minimum, you must provide an email address for support inquiries and an
indication of the response time users should expect.

Do Don’t- Provide a support email address with an explicit SLA.
- Provide additional support channels such as chat, forums, and so on.
- Don’t provide a “black hole” email address for support.
- Don’t check support inquiries infrequently and take days or weeks to respond.

### Legal compliance

**Intellectual property**

Only include assets and works that you have permission to use. Don’t infringe on
the intellectual property rights of others.

Do Don’t- Use code, images, and other assets that you’ve created or have
obtained commercial licenses for.
- Don’t copy code from others without proper credit or permission.
- Don’t use open source code in a manner inconsistent with its license.
- Don’t use photos from the internet without permission.

**Data locality**

You’re responsible for complying with all data locality controls and any
applicable jurisdictional laws. Refer to the [Stripe Developer Terms of
Service](http://stripe.com/legal/app-developer-agreement) and [Stripe App
Marketplace Terms of Service](http://stripe.com/legal/app-marketplace-agreement)
for more information.

**Anti-spam**

Don’t send spam. Our anti-spam policy means you’re responsible for making sure
all communications with users are opt-in, relevant, and compliant with all
applicable email communications laws. You may not sell Stripe user contact
information to any third parties.

**Export controls and cryptographic functions**

Your app code must abide by all relevant export control laws. In particular,
your app must not contain any custom cryptographic functions. These are covered
under the [International Traffic in Arms
Regulations](https://www.ecfr.gov/cgi-bin/text-idx?SID=8870638858a2595a32dedceb661c482c&mc=true&tpl=/ecfrbrowse/Title22/22CIsubchapM.tpl)
(ITAR), and export of these functions outside of the United States can incur
serious penalties.

Do Don’t- Use built-in cryptographic functions from standard libraries.
- Use properly-vetted cryptographic functions from well-known open source
libraries.
- Don’t write your own novel cryptographic function and include it in your UI
Extension’s source code.

**Fraudulent activities**

Your app must not engage in or promote any sort of fraudulent activities.

**Restricted businesses and apps**

Apps that engage in activities that fall under Stripe’s [Prohibited and
Restricted
Businesses](https://stripe.com/legal/restricted-businesses#restricted-businesses)
and apps that offer services in licensed or regulated industries need to be
reviewed to determine whether Stripe can support your use case. If we determine
your app falls into one of these categories, we’ll notify you during app review
and work with you to complete the review process.

Do Don’t- Review [Prohibited and Restricted
Businesses](https://stripe.com/legal/restricted-businesses#restricted-businesses)
to determine whether it applies to your business or app.
- If Stripe considers your business or app a restricted business, or your app is
associated with an industry where licensing is required or your business is
regulated, contact [Stripe Support](https://support.stripe.com/contact/email) to
begin the enhanced review process.
- Ensure your business meets all regulatory requirements to operate in your
jurisdiction.
- Submit your app for review and work with Stripe to complete the review
process.
- Try to submit an app if your business operates in a regulated industry without
the necessary licenses or approvals.
- Submit an app with functionality related to a restricted business without
having the necessary licenses or approvals.
- Create a Stripe account to develop an app using information unrelated to your
business.

**Prohibited businesses**

Your company or you as a developer can’t engage in one or more types of business
that are prohibited by our [Terms of
Services](https://stripe.com/legal/restricted-businesses#restricted-businesses).

**Sanctioned countries**

Your company or you as a developer can’t be based in a country Stripe cannot
engage with due to [embargo or other
restrictions](https://support.stripe.com/questions/understanding-sanctions).

## See also

- [Publish your app](https://docs.stripe.com/stripe-apps/publish-app)
- [App listing
guidelines](https://docs.stripe.com/stripe-apps/listing-guidelines)

## Links

- [example test
credentials](https://docs.stripe.com/stripe-apps/review-requirements#test-plan-and-credentials)
- [Submit app for
review](https://docs.stripe.com/stripe-apps/publish-app#submit-app-for-review)
- [Publish your
app](https://docs.stripe.com/stripe-apps/publish-app#publish-app)
- [Prohibited and Restricted
Businesses](https://stripe.com/legal/restricted-businesses)
- [app listing
guidelines](https://docs.stripe.com/stripe-apps/listing-guidelines)
- [Stripe Support](https://support.stripe.com/contact/login)
- [external
icon](https://docs.stripe.com/stripe-apps/components/icon#icon-reference)
- [Secret Store API](https://docs.stripe.com/api/secret_management)
- [Stripe Developer Terms of
Service](http://stripe.com/legal/app-developer-agreement)
- [Stripe App Marketplace Terms of
Service](http://stripe.com/legal/app-marketplace-agreement)
- [International Traffic in Arms
Regulations](https://www.ecfr.gov/cgi-bin/text-idx?SID=8870638858a2595a32dedceb661c482c&mc=true&tpl=/ecfrbrowse/Title22/22CIsubchapM.tpl)
- [Prohibited and Restricted
Businesses](https://stripe.com/legal/restricted-businesses#restricted-businesses)
- [Stripe Support](https://support.stripe.com/contact/email)
- [embargo or other
restrictions](https://support.stripe.com/questions/understanding-sanctions)
- [Publish your app](https://docs.stripe.com/stripe-apps/publish-app)