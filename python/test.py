import ais_decoder

try:
    str = "!AIVDM,1,1,,A,13HOI:0P0000VOHLCnHQKwvL05Ip,0*23\n!AIVDM,1,1,,A,133sVfPP00PD>hRMDH@jNOvN20S8,0*7F\n!AIVDM,1,1,,B,100h00PP0@PHFV`Mg5gTH?vNPUIp,0*3B\n!AIVDM,1,1,,B,13eaJF0P00Qd388Eew6aagvH85Ip,0*45\n!AIVDM,1,1,,A,14eGrSPP00ncMJTO5C6aBwvP2D0?,0*7A\n!AIVDM,1,1,,A,15MrVH0000KH<:V:NtBLoqFP2H9:,0*2F\n!AIVDM,1,1,,A,15N9NLPP01IS<RFF7fLVmgvN00Rv,0*7F\n!AIVDM,1,1,,A,133w;`PP00PCqghMcqNqdOvPR5Ip,0*65\n!AIVDM,1,1,,B,35Mtp?0016J5ohD?ofRWSF2R0000,0*28\n!AIVDM,1,1,,A,133REv0P00P=K?TMDH6P0?vN289>,0*46\n!AIVDM,1,1,,B,139eb:PP00PIHDNMdd6@0?vN2D2s,0*43\n!AIVDM,1,1,,B,33aDqfhP00PD2OnMDdF@QOvN205A,0*13\n!AIVDM,1,1,,B,B43JRq00LhTWc5VejDI>wwWUoP06,0*29\n!AIVDM,1,1,,B,133hGvP0000CjLHMG0u==:VN05Ip,0*61\n!AIVDM,1,1,,A,13aEOK?P00PD2wVMdLDRhgvL289?,0*26\n!AIVDM,1,1,,B,16S`2cPP00a3UF6EKT@2:?vOr0S2,0*00\n!AIVDM,2,1,9,B,53nFBv01SJ<thHp6220H4heHTf2222222222221?50:454o<`9QSlUDp,0*09\n!AIVDM,2,2,9,B,888888888888880,2*2E\n!AIVDM,1,1,,A,13AwPr00000pFa0P7InJL5JP2<0I,0*79\n!AIVDM,1,1,,A,14eGKMhP00rkraHJPivPFwvL0<0<,0*23\n!AIVDM,1,1,,B,13P:`4hP00OwbPRMN8p7ggvN0<0h,0*69\n!AIVDM,1,1,,A,16:=?;0P00`SstvFnFbeGH6L088h,0*44\n!AIVDM,1,1,,A,16`l:v8P0W8Vw>fDVB0t8OvJ0H;9,0*0A\n!AIVDM,1,1,,A,169a:nP01g`hm4pB7:E0;@0L088i,0*5E\n!AIVDM,1,1,,A,169F<h0P1S8hsm0B:H9o4gvN2@8o,0*5E\n"
    ais_decoder.pushAisChunk(str, len(str))

    n = ais_decoder.numAisMessages()
    print("num messages = ", n)
    

    while True:
        if ais_decoder.numAisMessages() == 0:
            break
        
        msg = ais_decoder.popAisMessage().asdict()
        print(msg)


except RuntimeError as err:
    print("Runtime error. ", err)
except:
    print("Error.")
