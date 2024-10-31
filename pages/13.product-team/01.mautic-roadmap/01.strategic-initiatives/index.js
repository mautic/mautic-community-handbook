const composerSupport = require('./initiatives/composerSupport');
const emailLandingPageBuilders = require('./initiatives/emailLandingPageBuilders');
const installationUpgradeExperience = require('./initiatives/installationUpgradeExperience');
const mauticMarketplace = require('./initiatives/mauticMarketplace');
const mauticNextGeneration = require('./initiatives/mauticNextGeneration');
const resourceManagement = require('./initiatives/resourceManagement');

const main = async () => {
  try {
    await composerSupport.execute();
    await emailLandingPageBuilders.execute();
    await installationUpgradeExperience.execute();
    await mauticMarketplace.execute();
    await mauticNextGeneration.execute();
    await resourceManagement.execute();
    
    console.log('All strategic initiatives executed successfully.');
  } catch (error) {
    console.error('Error executing initiatives:', error);
  }
};

main();
