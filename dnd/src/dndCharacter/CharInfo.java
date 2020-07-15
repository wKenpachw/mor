package dndCharacter;

public class CharInfo {
	public String name = "";
	public int init = 1;
	public int maxHP = 0;
	public int currentHP = 0;
	public String dopInfo = "";

	public CharInfo() {
		this.name = "new";
		this.init = 1;
	}

	public CharInfo(String name, int init, int maxHP, int currentHP, String dopInfo) {
		this.name = name;
		this.init = init;
		this.maxHP = maxHP;
		this.dopInfo = dopInfo;
	}
	
	public String getName() {
		return this.name;
	}
	
	public int getInit() {
		return this.init;
	}
	
	public int getMaxHP(){
		return this.maxHP;
	}
	
	public int getCurrentHP(){
		return this.currentHP;
	}
	
	public String getDopInfo() {
		return this.dopInfo;
	}
	
	public void setName(String name) {
		this.name = name;
	}
	
	public void setInit(int init) {
		this.init = init;
	}
	
	public void setMaxHP(int maxHP) {
		this.maxHP = maxHP;
	}
	
	public void setCurrenHP(int currentHP) {
		this.currentHP = currentHP;
	}
	
	public void setDopInfo(String dopInfo) {
		this.dopInfo = dopInfo;
	}
}
