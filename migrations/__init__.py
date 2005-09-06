from Products.CMFPlone import MigrationTool

def executeMigrations():
    import v1, v2, v2_1

def null(portal):
    """ This is a null migration, use it when nothing happens """
    pass

def registerMigrations():
    # so the basic concepts is you put a bunch of migrations is here

    MigrationTool.registerUpgradePath('1.0',
                                      '1.0.1',
                                      v1.final_one_zero_one.onezeroone)

    MigrationTool.registerUpgradePath('1.0.1',
                                      '1.0.2',
                                      v1.one01_one02.onezerotwo)

    MigrationTool.registerUpgradePath('1.0.2',
                                      '1.0.3',
                                      v1.one02_one03.onezerothree)

    MigrationTool.registerUpgradePath('1.0.3',
                                      '1.0.4',
                                      v1.one03_one04.onezerofour)

    MigrationTool.registerUpgradePath('1.0.4',
                                      '1.0.5',
                                      null)

    #Migrations to Plone 2.0 require a External Method.
    #We will rework the migration tool

    MigrationTool.registerUpgradePath('1.0.5',
                                      '2.0-beta2',
                                      v2.oneX_twoBeta2.oneX_twoBeta2)

    MigrationTool.registerUpgradePath('2.0-beta2',
                                      '2.0-beta3',
                                      v2.twoBeta2_twoBeta3.twoBeta2_twoBeta3)

    MigrationTool.registerUpgradePath('2.0-beta3',
                                      '2.0-rc2',
                                      null)

    MigrationTool.registerUpgradePath('2.0-rc2',
                                      '2.0-rc3',
                                      null)

    MigrationTool.registerUpgradePath('2.0-rc3',
                                      '2.0-rc4',
                                      v2.release_candidates.rc3_rc4)

    MigrationTool.registerUpgradePath('2.0-rc4',
                                      '2.0-rc5',
                                      v2.release_candidates.rc4_rc5)

    MigrationTool.registerUpgradePath('2.0-rc5',
                                      '2.0',
                                      v2.release_candidates.rc5_final)

    MigrationTool.registerUpgradePath('2.0',
                                      '2.0-rc6',
                                      v2.release_candidates.final_rc6)

    MigrationTool.registerUpgradePath('2.0-rc6',
                                      '2.0-final',
                                      v2.release_candidates.rc6_finalfinal)

    MigrationTool.registerUpgradePath('2.0-final',
                                      '2.0.1',
                                      v2.final_two01.twozeroone)

    MigrationTool.registerUpgradePath('2.0.1',
                                      '2.0.2',
                                      null)

    MigrationTool.registerUpgradePath('2.0.2',
                                      '2.0.3',
                                      null)

    MigrationTool.registerUpgradePath('2.0.3',
                                      '2.0.4',
                                      null)

    MigrationTool.registerUpgradePath('2.0.4',
                                      '2.0.5-rc1',
                                      null)

    MigrationTool.registerUpgradePath('2.0.5-rc1',
                                      '2.0.5-rc2',
                                      null)

    MigrationTool.registerUpgradePath('2.0.5-rc2',
                                      '2.0.5',
                                      v2.two04_two05.two04_two05)

    MigrationTool.registerUpgradePath('2.0.5',
                                      '2.1-alpha1',
                                      v2_1.alphas.two05_alpha1)

    MigrationTool.registerUpgradePath('2.1-alpha1',
                                      '2.1-alpha2',
                                      v2_1.alphas.alpha1_alpha2)

    MigrationTool.registerUpgradePath('2.1-alpha2',
                                      '2.1-beta1',
                                      v2_1.betas.alpha2_beta1)

    MigrationTool.registerUpgradePath('2.1-beta1',
                                      '2.1-beta2',
                                      v2_1.betas.beta1_beta2)

    MigrationTool.registerUpgradePath('2.1-beta2',
                                      '2.1-rc1',
                                      null)

    MigrationTool.registerUpgradePath('2.1-rc1',
                                      '2.1-rc2',
                                      v2_1.rcs.rc1_rc2)

    MigrationTool.registerUpgradePath('2.1-rc2',
                                      '2.1-rc3',
                                      v2_1.rcs.rc2_rc3)

    MigrationTool.registerUpgradePath('2.1-rc3',
                                      '2.1',
                                      v2_1.rcs.rc3_final)
